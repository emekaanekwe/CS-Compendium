"""
Societies Grid -- proto, steps 1-3.

Scope of this file: two agents, a 4x4 grid, movement. No obstacle (step 4), no
game (step 5). Both are stubbed at the exact seam where they will attach, so
adding them is a replacement rather than a restructure.

DECISIONS MADE HERE (each is one line to reverse)
-------------------------------------------------
1. SIMULTANEOUS movement. Both agents choose from the same world state, then
   both resolutions are applied. Sequential turn order would make the model
   asymmetric -- the second mover would see the first's new position -- and the
   game-theoretic framing assumes simultaneity.

2. WALLS, not wrap-around. Moving off the edge is refused and the agent holds
   position. A torus removes boundary effects, which is conventional in spatial
   game theory, but boundaries are exactly what circumscription is about, so
   they stay. Topology is a nuisance parameter to sweep later.

3. BLOCKED, not clamped. An illegal move is refused outright, not silently
   turned into a different legal move. Clamping would quietly convert "walk into
   the wall" into "slide along it", which changes the effective action space
   without saying so.

4. POLICY BEHIND AN INTERFACE from the start. Even random walk goes through
   Policy.choose(). Swapping in fixed strategies, imitation or RL later must not
   require touching the world.

INVARIANT: every source of randomness comes from an explicitly passed rng.
No module-level np.random anywhere, ever. This is painful to retrofit.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# --- actions ---------------------------------------------------------------

STAY, UP, DOWN, LEFT, RIGHT = range(5)
ACTIONS = (STAY, UP, DOWN, LEFT, RIGHT)
ACTION_NAMES = {STAY: "stay", UP: "up", DOWN: "down", LEFT: "left", RIGHT: "right"}

# (row, col) deltas. Row 0 is the top.
DELTA = {
    STAY:  np.array([0, 0]),
    UP:    np.array([-1, 0]),
    DOWN:  np.array([1, 0]),
    LEFT:  np.array([0, -1]),
    RIGHT: np.array([0, 1]),
}


# --- world -----------------------------------------------------------------

@dataclass
class World:
    """Grid state. Holds no policy and no history -- those live outside."""

    size: int
    positions: np.ndarray          # (n_agents, 2) int, row-col
    blocked: np.ndarray            # (size, size) bool -- all False until step 4
    t: int = 0

    @property
    def n_agents(self) -> int:
        return len(self.positions)

    def in_bounds(self, rc) -> bool:
        return bool((0 <= rc[0] < self.size) and (0 <= rc[1] < self.size))

    def passable(self, rc) -> bool:
        return not bool(self.blocked[rc[0], rc[1]])


def make_world(size: int, starts) -> World:
    return World(
        size=size,
        positions=np.array(starts, dtype=int),
        blocked=np.zeros((size, size), dtype=bool),
    )


# --- policies --------------------------------------------------------------

class Policy:
    """The one seam every decision module must satisfy.

    Fixed strategy, imitation, evolutionary and RL modules all implement this.
    `choose` may read the world but must never mutate it.
    """

    name = "abstract"

    def choose(self, world: World, agent_id: int, rng: np.random.Generator) -> int:
        raise NotImplementedError


class RandomWalk(Policy):
    name = "random"

    def choose(self, world, agent_id, rng):
        return int(rng.integers(len(ACTIONS)))


# --- encounters ------------------------------------------------------------

def find_encounters(current: np.ndarray, target: np.ndarray):
    """Agent pairs that meet this step.

    TWO distinct cases, and missing the second is the classic gridworld bug:

      same-cell: both agents target the same square.
      swap:      A and B are adjacent and move through each other. They never
                 share a square, so naive same-cell detection misses it entirely
                 and the two simply trade places as if nothing happened.

    O(n^2), which is honest at n=2 and must be replaced by a cell-hash before
    the agent count grows.
    """
    pairs = []
    n = len(current)
    for i in range(n):
        for j in range(i + 1, n):
            same = np.array_equal(target[i], target[j])
            swap = (np.array_equal(target[i], current[j])
                    and np.array_equal(target[j], current[i]))
            if same or swap:
                pairs.append((i, j, "same-cell" if same else "swap"))
    return pairs


def hold_both(world, i, j, kind, target, rng):
    """PLACEHOLDER resolution -- step 5 replaces this with the game.

    Both agents are returned to where they started. This is deliberately a
    non-answer: who ends up holding a contested cell is the conquest rule, which
    is still an open question in the design doc and is the single decision that
    every consolidation metric depends on. Making it a named, swappable function
    keeps that choice visible instead of burying it in the step loop.
    """
    target[i] = world.positions[i]
    target[j] = world.positions[j]
    return {"event": "encounter", "kind": kind, "agents": (i, j),
            "resolution": "both held"}


# --- step ------------------------------------------------------------------

def step(world: World, policies, rng: np.random.Generator, resolve=hold_both):
    """Advance one timestep. Returns (actions, events)."""
    current = world.positions
    target = current.copy()
    events = []

    # 1. everyone chooses from the SAME pre-move state
    actions = [policies[i].choose(world, i, rng) for i in range(world.n_agents)]

    # 2. legality, independently per agent
    for i, a in enumerate(actions):
        candidate = current[i] + DELTA[a]
        if not world.in_bounds(candidate):
            events.append({"event": "refused", "agent": i, "reason": "edge"})
            continue
        if not world.passable(candidate):
            events.append({"event": "refused", "agent": i, "reason": "obstacle"})
            continue
        target[i] = candidate

    # 3. interaction between agents
    for i, j, kind in find_encounters(current, target):
        events.append(resolve(world, i, j, kind, target, rng))

    world.positions = target
    world.t += 1
    return actions, events


# --- rendering (outside the core; for eyeballing only) ---------------------

def render(world: World, labels="AB") -> str:
    glyphs = [["." for _ in range(world.size)] for _ in range(world.size)]
    for r in range(world.size):
        for c in range(world.size):
            if world.blocked[r, c]:
                glyphs[r][c] = "#"
    for i, (r, c) in enumerate(world.positions):
        glyphs[r][c] = labels[i] if glyphs[r][c] == "." else "*"
    return "\n".join(" ".join(row) for row in glyphs)


# --- demo ------------------------------------------------------------------

def run(seed: int, n_steps: int, verbose: bool = True):
    rng = np.random.default_rng(seed)
    world = make_world(4, starts=[(0, 0), (3, 3)])
    policies = [RandomWalk(), RandomWalk()]
    trace = [world.positions.copy()]

    for _ in range(n_steps):
        actions, events = step(world, policies, rng)
        trace.append(world.positions.copy())
        if verbose:
            names = " ".join(f"{lbl}:{ACTION_NAMES[a]:<5}"
                             for lbl, a in zip("AB", actions))
            note = ""
            for e in events:
                if e["event"] == "encounter":
                    note = f"   <- {e['kind']} encounter, {e['resolution']}"
                elif e["event"] == "refused":
                    note += f"   ({'AB'[e['agent']]} refused: {e['reason']})"
            print(f"\nt={world.t:<3} {names}{note}")
            print(render(world))

    return np.array(trace)


def check_determinism():
    """NFR-01 in miniature. Worth having from the first file, not the fiftieth."""
    a = run(seed=7, n_steps=40, verbose=False)
    b = run(seed=7, n_steps=40, verbose=False)
    c = run(seed=8, n_steps=40, verbose=False)
    assert np.array_equal(a, b), "same seed produced different trajectories"
    assert not np.array_equal(a, c), "different seeds produced identical trajectories"
    print("determinism: same seed identical, different seed divergent -- OK")


def check_swap_detected():
    """The bug this guards against is silent, so the test is not optional."""
    world = make_world(4, starts=[(1, 1), (1, 2)])
    current = world.positions
    target = np.array([[1, 2], [1, 1]])          # A and B pass through each other
    found = find_encounters(current, target)
    assert found and found[0][2] == "swap", f"swap not detected: {found}"
    print("swap detection: pass-through caught -- OK")


if __name__ == "__main__":
    check_determinism()
    check_swap_detected()
    print("\n--- 10 steps, seed 3 ---")
    run(seed=3, n_steps=10)
