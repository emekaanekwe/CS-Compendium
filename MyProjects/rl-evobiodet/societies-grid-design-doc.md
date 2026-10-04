---
title: "Geographic Determinants of Political Consolidation — Design Document"
project: societies-grid
doc-type: technical-design-document
version: 0.1.0
status: draft
author: Emeka
created: 2026-10-03
updated: 2026-10-03
tags: [simulation, multi-agent, evolutionary-biology, design-doc, portfolio]
---

# Geographic Determinants of Political Consolidation

> [!ABSTRACT] One-line summary
> An agent-based simulation testbed that measures whether geographic initial conditions alone are sufficient, and necessary, to generate the political consolidation patterns observed in the ecological evolution of human societies using matched synthetic continents as a controlled counterfactual.

**Contents**
[Context](#1-context) · [Objectives](#2-objectives) · [Validation ladder](#3-validation-ladder) · [Scope](#4-scope) · [Requirements](#5-requirements) · [Constraints](#6-constraints) · [Assumptions](#7-assumptions) · [Input data](#8-input-data) · [Desiderata](#9-desiderata) · [Metrics](#10-metrics) · [Experiments](#11-experiment-register) · [Milestones](#12-milestones-and-acceptance-criteria) · [Risks](#13-risk-register) · [Open questions](#14-open-questions) · [Glossary](#15-glossary) · [References](#16-references)

---

## 1. Context

### 1.1 Problem statement

Theories of state formation are difficult to test because history ran once, with every causal variable confounded. Diamond's ecological-evolutionary thesis holds that differences in the trajectories of human societies are driven primarily by geographic and biogeographic endowment — domesticable species availability, continental axis orientation governing the diffusion of crops and technology, landmass area, and disease environments arising from animal domestication — rather than by intrinsic differences between peoples.

It is quite obvious that there does not exist a intellectually-satisfying theory of state formation. However, with our current improvements in simulation and learning agents, we can move the compass a little bit by addressing confounding causal variables using Jarred Diamond's Ecological-Evolutionary Thesis (EET). The thesis can be paraphrased as follows: 

EET holds that differences in the trajectories of human state societies are driven primarily by their geographic and biogeographic endowment of domesticable species availability, geographical position in relation to neighboring state societies, the potentiality of diffusion of resources, rather than by intrinsic differences in racial, cultural, or ideological demographics.

The thesis makes claims about *rates* and *probabilities* across continents, but Earth supplies roughly six continents, so observational data has almost no statistical power to discriminate it from alternatives. A simulation can supply the missing control group: synthetic continents matched on every dimension except the one under test.

### 1.2 What this project is

A reproducible computational testbed, built in stages, in which political consolidation emerges from local interaction on a spatial grid under geographic constraint. The headline experiment manipulates continental axis orientation while holding area, cell count, and resource endowment fixed.

### 1.3 What this project is not

> [!WARNING] Epistemic boundary
> No simulation can demonstrate that this is how states *actually* formed. Many distinct micro-rule sets produce the same macro-pattern, so pattern matching does not identify mechanism. Every claim made by this project is a claim about the **model**, except where [EXP-05](#exp-05) is run, which is a scored prediction about data. This constraint is binding on all documentation, commit messages, and the final writeup.

---

## 2. Objectives

| ID | Objective | Success criterion |
|---|---|---|
| **O-1** | Establish a spatial-game baseline that produces non-trivial structure without learning | Stage 0 reproduces the qualitative cluster formation reported by Nowak & May (1992) |
| **O-2** | Show geography alone is *sufficient* to generate political consolidation | Consolidation metrics rise above a null model with uniform terrain, p < 0.01 over ≥ 200 seeds |
| **O-3** | Show the geographic mechanism is *necessary within the model* | No setting of remaining parameters recovers the pattern once the mechanism is ablated |
| **O-4** | Demonstrate a matched counterfactual on axis orientation | East–west continents consolidate earlier and larger than matched north–south, with effect size and CI reported |
| **O-5** | Compare learning dynamics against evolutionary dynamics | Macro-metrics from the RL layer and the selection layer compared on identical maps; agreement or divergence characterised |
| **O-6** | Produce a portfolio-grade artefact | Public repo, reproducible from seed, documented, with preregistered predictions timestamped before results |

> [!NOTE] Objective ordering
> O-1 through O-4 are the scientific spine. O-5 is the distinguishing contribution — the learning-versus-selection comparison is a sharper question than either mechanism alone and is where this differs from existing work. O-6 is a constraint on how the others are delivered, not a separate workstream.

---

## 3. Validation ladder

Each level is logically stronger than the one below it. The milestone plan assigns levels to stages so that claim strength is always traceable to an experiment that was actually run.

| Level | Claim form | Method | Milestone |
|---|---|---|---|
| **V0** | Mechanism *can* produce pattern | Single demonstrative run | M1 |
| **V1** | Pattern is robust | Sweep over nuisance parameters: topology, update order, payoff scale, N | M2 |
| **V2** | Mechanism is necessary within model | Ablation; exhaustive sweep of remaining parameters fails to recover pattern | M3 |
| **V3** | Threshold is analytic, not merely observed | Mean-field or branching-process treatment of stripped-down variant; closed-form threshold | M4 |
| **V4** | Causal isolation of one variable | Matched counterfactual with control continent | M5 |
| **V5** | Prediction about the world | Calibrate on region A, predict held-out region B, score against preregistration | M7 (stretch) |

> [!IMPORTANT] Preregistration rule
> For V4 and V5, the predicted direction and effect size are committed to the repository with a timestamp **before** the experiment is run. A prediction written after seeing results is a fitted result, not a tested one, and must be labelled as such.

---

## 4. Scope

### 4.1 In scope

- Headless simulation core: grid, terrain, agents, interaction games, traversal cost
- Four interchangeable agent decision modules (fixed strategy, imitation, evolutionary, RL)
- Synthetic continent generation with matching constraints
- Experiment runner, parameter sweeps, seeded reproducibility
- Metrics computation and persistence
- Minimal interactive UI for the player-facing "game" aspect

### 4.2 Out of scope (v1)

- Real-world geographic calibration (deferred to M7)
- Deep RL beyond a single standard algorithm
- Multi-agent credit assignment research
- Agent birth/death changing the agent count at runtime (see [C-08](#6-constraints))
- Networked or multiplayer play
- 3D rendering, art assets, sound

---

## 5. Requirements

### 5.1 Functional

| ID | Priority | Requirement |
|---|---|---|
| **FR-01** | Must | Represent a world as a 2D grid of cells, each with a terrain type and a resource endowment |
| **FR-02** | Must | Support exactly one landmass-adjacency relation and one traversal-cost function between landmasses |
| **FR-03** | Must | Assign a 2×2 payoff matrix to each terrain type from a named game family (PD, Stag Hunt, Hawk–Dove, Harmony) |
| **FR-04** | Must | Resolve pairwise interactions between agents controlling adjacent cells using the terrain's payoff matrix |
| **FR-05** | Must | Transfer cell ownership between agents according to a documented conquest rule |
| **FR-06** | Must | Expose agent decision-making behind a single interface so modules are swappable without touching the core |
| **FR-07** | Must | Generate synthetic continents parameterised by axis orientation, area, cell count, and endowment distribution |
| **FR-08** | Must | Enforce matching constraints between a treatment continent and its control, and fail loudly if unmet |
| **FR-09** | Must | Propagate a "technology" scalar between adjacent cells with anisotropic cost (cheap along latitude, expensive across) |
| **FR-10** | Must | Compute and persist all metrics in [§10](#10-metrics) at a configurable sampling interval |
| **FR-11** | Must | Run a full experiment from a single config file plus a seed, with no other input |
| **FR-12** | Must | Support ablation of any named mechanism via a config flag, including the anisotropy in FR-09 |
| **FR-13** | Should | Provide an imitation-dynamics module (copy best-performing neighbour) |
| **FR-14** | Should | Provide an evolutionary module with mutation and differential reproduction |
| **FR-15** | Should | Provide an RL module with a single learning algorithm shared by all agents |
| **FR-16** | Should | Vary agent objectives by reward function, not by algorithm (see [C-09](#6-constraints)) |
| **FR-17** | Should | Expose an interactive mode where a human alters terrain or traversal cost mid-run |
| **FR-18** | Could | Render the grid as an animation for a completed run |
| **FR-19** | Could | Load real geography from raster input |
| **FR-20** | Won't (v1) | Support agents entering or leaving the population at runtime |

### 5.2 Non-functional

| ID | Priority | Requirement |
|---|---|---|
| **NFR-01** | Must | Identical seed + identical config ⇒ bit-identical metric output, on any supported platform |
| **NFR-02** | Must | Simulation core imports only `numpy` from the standard scientific stack; no plotting, no I/O, no UI |
| **NFR-03** | Must | A single run of the default configuration completes in < 10 s on a laptop CPU |
| **NFR-04** | Must | A full parameter sweep completes within one overnight window (≈ 10 h) on one machine, single-threaded |
| **NFR-05** | Must | Peak memory for the default configuration stays under 500 MB |
| **NFR-06** | Should | Every mechanism in the core has a unit test asserting a hand-computable outcome |
| **NFR-07** | Should | Runs are resumable from a checkpoint, so an interrupted sweep is not lost |
| **NFR-08** | Should | Metric output is a tidy long-format table, one row per (run, timestep, metric) |
| **NFR-09** | Could | Sweeps parallelise across cores without changing results |

---

## 6. Constraints

> [!CAUTION] Hard constraints
> These are not negotiable without revising this document and bumping its version.

| ID | Type | Constraint | Rationale |
|---|---|---|---|
| **C-01** | Platform | Must run on Windows PC *and* Android | Stated working environment; mobile is where much of the thinking time happens |
| **C-02** | Platform | No compiled extensions requiring an Android NDK toolchain | Rules out Numba, Cython, custom C extensions |
| **C-03** | Dependency | `numpy` first; `scipy` and `matplotlib` permitted; no deep-learning framework before M6 | Keeps the mobile path viable and the core auditable |
| **C-04** | Resource | Single developer, part-time, alongside Monash coursework | Sets milestone granularity; each milestone must be completable in isolation |
| **C-05** | Compute | CPU only; no GPU, no cluster | Caps grid size and agent count; forces design for sweep efficiency over per-run fidelity |
| **C-06** | Reproducibility | All stochasticity flows from explicitly seeded generators passed down the call stack | Global RNG state makes multi-run reproducibility impossible to guarantee |
| **C-07** | Epistemic | No claim may exceed the validation level actually achieved | See [§3](#3-validation-ladder) |
| **C-08** | Design | Agent count is fixed for the lifetime of a run; conquest transfers territory, never deletes an agent | Variable agent counts break most multi-agent tooling and complicate every metric |
| **C-09** | Design | One learning algorithm across all agents in any given run; agent diversity comes from reward functions | Mixing algorithms confounds "which strategy won" with "which optimiser won" |
| **C-10** | Scientific | Terrain-to-game mapping must be declared in config before a run, never tuned post hoc to produce a result | Post-hoc tuning converts an experiment into a demonstration |

---

## 7. Assumptions

| ID | Assumption | Risk if false |
|---|---|---|
| **A-01** | Pairwise local interaction is an adequate abstraction of inter-polity contact | Macro-patterns may require coalition or multi-party dynamics; Stage 2 would under-produce consolidation |
| **A-02** | A 2×2 payoff matrix captures enough of the strategic structure of conquest and trade | Richer action spaces may be needed; mitigated by keeping the matrix pluggable |
| **A-03** | Technology diffusion can be modelled as a scalar propagating across cells | Diamond's mechanism involves package effects (crops *and* animals *and* writing); a scalar may wash out the axis effect |
| **A-04** | Consolidation reaches a stable or quasi-stable regime within the simulated horizon | Metrics sampled before equilibrium are not comparable across conditions; requires a stationarity check |
| **A-05** | Matching on area, cell count, and endowment distribution is sufficient to isolate axis orientation | Hidden confounds in the generator; mitigated by [FR-08](#51-functional) failing loudly and by generator unit tests |

---

## 8. Input data

> [!TIP] Zero data dependency through M6
> Stages 0 through 4 require **no external data**. All terrain is procedurally generated. This is a deliberate design advantage: the headline experiment needs synthetic continents precisely *because* real ones are confounded. Data acquisition is a stretch goal, not a blocker.

### 8.1 Required (none)

No external input data is required to satisfy O-1 through O-5.

### 8.2 Optional — stretch calibration (M7 only)

| Source | Use | Format | Licence note |
|---|---|---|---|
| Natural Earth | Coastlines, landmass polygons for real-geography mode | Vector / raster | Public domain |
| ETOPO (NOAA) | Elevation and bathymetry to derive terrain classes and traversal cost | Gridded raster | Open |
| Diamond's domesticable large-mammal tally | Per-continent endowment parameter | Small published table, hand-entered | Verify against the primary source before use |
| D-PLACE / Ethnographic Atlas | Societal trait data for comparison against model outputs | Tabular | Check per-dataset terms |
| Seshat Global History Databank | Polity-scale time series for V5 scoring | Tabular | Check access terms; registration may be required |

> [!WARNING] Verify before relying
> Every figure in the table above should be checked against its primary source at the time of use. Do not hard-code a number taken from secondary description.

---

## 9. Desiderata

Quality attributes, in priority order. Where two conflict, the higher-ranked wins.

1. **Reproducibility over everything.** A result that cannot be regenerated from a seed is not a result. This outranks performance, elegance, and convenience.
2. **Mechanism separated from presentation.** The core computes; it does not plot, print, or render. Anything else can be rebuilt; a core entangled with its UI cannot be trusted or reused.
3. **Falsifiability by construction.** Every mechanism has an off switch. If a mechanism cannot be ablated, its contribution cannot be measured, and [V2](#3-validation-ladder) is unreachable.
4. **Parameters externalised.** No magic numbers in source. Every quantity that could plausibly be swept lives in config, because the ones you hard-code are the ones you will want to sweep.
5. **Instrumented by default.** Metrics are computed during the run, not reconstructed afterwards from saved states.
6. **Incremental verifiability.** Each stage ships with an acceptance test that passes before the next stage begins. No stage depends on an unvalidated stage below it.
7. **Swappability at the decision boundary.** Fixed-strategy, imitation, evolutionary, and RL modules satisfy one interface. This is what makes [O-5](#2-objectives) a controlled comparison rather than two unrelated programs.
8. **Readability over micro-optimisation.** Vectorise where it is free; do not obfuscate the mechanism to save milliseconds. The code is part of the argument.
9. **Scalability designed in, not bolted on.** Grid size, agent count, and sweep breadth are parameters from day one, even while they are small.

---

## 10. Metrics

> [!IMPORTANT] Defined before coding
> These definitions are fixed now. Choosing metrics after seeing output is how a simulation becomes an aquarium.

| ID | Metric | Definition | Interprets |
|---|---|---|---|
| **M-01** | Polity count | Number of agents controlling ≥ 1 cell | Consolidation (falls as empires absorb rivals) |
| **M-02** | Largest-polity share | Cells held by the largest agent ÷ total land cells | Hegemony |
| **M-03** | Territorial Gini | Gini coefficient over per-agent cell counts | Inequality of political power |
| **M-04** | Cooperation rate | Fraction of resolved interactions ending in mutual cooperation | Behavioural regime |
| **M-05** | Turnover / half-life | Timesteps for half of cells to change controlling agent | Stability versus churn |
| **M-06** | Time-to-consolidation | First timestep at which M-02 exceeds a declared threshold; censored if never | Rate — the variable Diamond's thesis speaks to |
| **M-07** | Spatial autocorrelation | Moran's I over the strategy or ownership field | Cluster formation versus homogeneity |
| **M-08** | Technology frontier | Mean and max of the technology scalar, by latitude band | Direct test of the anisotropic-diffusion mechanism |

Sampling interval and the M-06 threshold are config values, declared per experiment.

---

## 11. Experiment register

Each experiment names the objective it serves and the validation level it reaches.

| ID | Name | Manipulates | Holds fixed | Serves | Level |
|---|---|---|---|---|---|
| **EXP-01** | Baseline pattern formation | Nothing | Uniform terrain | O-1 | V0 |
| **EXP-02** | Nuisance robustness | Topology, update order, payoff scale, N | Terrain, mechanism | O-1 | V1 |
| **EXP-03** | Circumscription sweep | Traversal cost, 0 → prohibitive | Terrain, agents | O-2 | V1 |
| **EXP-04** | Anisotropy ablation | Diffusion anisotropy on/off, then full sweep of remaining parameters | Map, seeds | O-3 | V2 |
| <a id="exp-05"></a>**EXP-05** | **Axis orientation** | Continental axis: east–west vs north–south | Area, cell count, endowment distribution, seed family | O-4 | V4 |
| **EXP-06** | Learning vs selection | Decision module: evolutionary vs RL | Map, seeds, reward structure | O-5 | V1 |
| **EXP-07** | Analytic threshold | — (derivation, checked against simulation) | Stripped-down variant | O-3 | V3 |
| **EXP-08** | Held-out region | Calibrate region A, predict region B | Preregistered prediction | — | V5 |

> [!NOTE] Prediction for EXP-05, to be timestamped before running
> East–west continents will reach the M-06 threshold **earlier** and attain a **higher** terminal M-02 than matched north–south continents. Direction is predicted; magnitude is not. A null result is publishable within this project and must be reported.
>
> Secondary prediction for EXP-03: the response of M-02 to traversal cost is **non-monotonic** — low cost permits escape and prevents absorption, prohibitive cost prevents contact entirely, and consolidation peaks at intermediate cost.

---

## 12. Milestones and acceptance criteria

| ID | Stage | Deliverable | Acceptance criterion | Level |
|---|---|---|---|---|
| **M1** | Stage 0 | Grid, fixed strategies, imitation dynamics, no learning | EXP-01 produces stable spatial clusters; result reproduces from seed | V0 |
| **M2** | Stage 0+ | Metrics module, experiment runner, config system | EXP-02 runs unattended; all metrics in §10 emitted as tidy output | V1 |
| **M3** | Stage 1 | Terrain game family, traversal cost, ablation flags | EXP-03 and EXP-04 complete; non-monotonic prediction tested | V2 |
| **M4** | Stage 1+ | Analytic treatment of stripped-down variant | Closed-form threshold derived and matched against EXP-07 within tolerance | V3 |
| **M5** | Stage 2 | Continent generator with matching constraints; evolutionary module | EXP-05 run with ≥ 200 matched pairs; effect size and CI reported | V4 |
| **M6** | Stage 3 | RL module behind the same interface | EXP-06 complete; learning and selection outcomes compared on identical maps | V1 |
| **M7** | Stretch | Real-geography loader; held-out prediction | EXP-08 scored against preregistration | V5 |

> [!TIP] Stop-and-ship points
> M3 is a complete, defensible project on its own. M5 is the strongest version most of the value is in. M6 is the differentiator. M7 is optional and should not be started until M5 is written up.

---

## 13. Risk register

| ID | Risk | L | I | Mitigation |
|---|---|---|---|---|
| **R-01** | Multi-agent RL fails to converge; non-stationary environment prevents stable policies | High | High | RL deferred to M6; project is already defensible at M3/M5 without it. Compare against the evolutionary module rather than depending on RL alone |
| **R-02** | Axis effect is swamped by generator noise; no detectable difference | Medium | High | Power analysis before M5; increase matched pairs; verify the diffusion mechanism in isolation via M-08 first |
| **R-03** | Environmental-determinism critique applied to the project | High | Medium | Address explicitly in the writeup; report distributions of outcomes rather than single trajectories; frame geography as setting rates, not outcomes |
| **R-04** | Scope creep from game-like features displacing scientific work | High | Medium | UI is Could-priority throughout; no UI work before M3 acceptance |
| **R-05** | Hidden confound in the continent generator invalidates EXP-05 | Medium | High | FR-08 hard-fails on unmet matching constraints; generator unit tests assert matched statistics |
| **R-06** | Sweeps exceed the overnight compute budget | Medium | Medium | Profile at M2; cap grid size; checkpointing per NFR-07; parallelise per NFR-09 |
| **R-07** | Android environment proves too limited for comfortable iteration | Medium | Low | Core is pure numpy and headless; phone used for reading and config edits, PC for sweeps |
| **R-08** | Post-hoc tuning of terrain-to-game mapping to produce a desired result | Medium | High | C-10; mapping committed to version control before each experiment run |

*L = likelihood, I = impact.*

---

## 14. Open questions

- [ ] What exactly is the conquest rule? Payoff-proportional, threshold-based, or stochastic in payoff difference? Affects every consolidation metric and must be fixed before M1.
- [ ] Does the technology scalar feed back into payoffs, or only into diffusion? Feedback makes the axis effect compounding; its absence may make the effect too weak to detect.
- [ ] Is the continent generator noise-based (Perlin/Simplex) or constructive? Constructive makes matching far easier to guarantee.
- [ ] What counts as "one polity" for M-01 when territory is non-contiguous?
- [ ] Should traversal cost be a fixed parameter or an agent-accumulated resource? The latter is closer to the sailing analogy but adds a state dimension.
- [ ] Which RL algorithm for M6, given C-02 and C-03? Tabular Q-learning may suffice and avoids the framework dependency entirely.
- [ ] What is the stationarity test for A-04?

---

## 15. Glossary

| Term | Meaning in this project |
|---|---|
| **Agent** | A persistent decision-making entity controlling zero or more cells; a "country" |
| **Polity** | An agent currently controlling ≥ 1 cell |
| **Cell** | One grid square, with a terrain type, resource endowment, technology scalar, and controlling agent |
| **Landmass** | A maximal set of cells connected without crossing water |
| **Traversal cost** | Penalty incurred when interacting or expanding across a landmass boundary |
| **Game family** | The set of 2×2 payoff matrices assignable to terrain types |
| **Ablation** | Disabling a named mechanism via config to measure its contribution |
| **Matched pair** | Two generated continents identical in every controlled statistic except the manipulated variable |
| **Consolidation** | Decrease in polity count with concurrent increase in largest-polity share |

---

## 16. References

Primary theoretical sources, to be read before the milestone that depends on them.

| Work | Relevance | Needed by |
|---|---|---|
| Diamond, *Guns, Germs, and Steel* (1997) | Core thesis; axis orientation, domesticable species, area effects | M5 |
| Blaut, critique of environmental determinism | The strongest objection; must be engaged, not ignored | Writeup |
| Nowak & May, *Nature* 359 (1992) | Direct ancestor of Stage 0; spatial prisoner's dilemma, cluster formation | M1 |
| Turchin et al., *PNAS* (2013) | Grid simulation of Old World polity formation; closest prior art and the V5 benchmark | M5, M7 |
| Carneiro, *Science* (1970) | Circumscription; the local transition mechanism complementing Diamond's initial conditions | M3 |
| Epstein & Axtell, *Growing Artificial Societies* (1996) | Methodological standard for generative social science; the sufficiency framing | M2 |

> [!NOTE] Reading posture
> Diamond supplies initial conditions and continental rates; Carneiro supplies the local absorption mechanism. They operate at different scales and are complementary rather than rival, regardless of how they are usually contrasted.

---

## Revision history

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-10-03 | Initial draft — objectives, constraints, data, desiderata |
