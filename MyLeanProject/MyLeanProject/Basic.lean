-- ============ Introduction to Lean 4 ============
-- Lean 4 is a functional language and proof assistant.
-- Types can represent both data and mathematical propositions.

def hello := "world"

-- ------------ Definitions ------------
def add (a b : Nat) : Nat := a + b

-- ------------ Functions (anonymous) ------------
def inc : Nat → Nat := fun x => x + 1
def double (n : Nat) : Nat := n + n

-- ------------ Basic types ------------
-- Nat (naturals), Int, Bool, String, List α, α → β

-- ------------ Pattern matching ------------
def isZero : Nat → Bool
  | 0 => true
  | _ => false

-- ------------ A simple proof ------------
-- The type "n + 0 = n" is a proposition; the proof goes after :=
theorem add_zero_right (n : Nat) : n + 0 = n := by
  exact Nat.add_zero n

-- ------------ Using #check and #eval ------------
-- In the infoview: #check add        -- type of add
--                 #eval add 2 3     -- evaluates to 5
