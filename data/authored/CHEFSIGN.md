---
topic: Strings
subtopic: Run lengths scanned from both directions
time: $O(|s|)$ per test case
space: $O(|s|)$
---
Each of the $N+1$ slots needs a value large enough to satisfy the chain of `<` signs reaching it from the left and the chain of `>` signs reaching it from the right. Both are computed by a linear sweep.

**Left pass.** $L_0 = 1$, and for each $i$:
- $s_{i-1} =$ `<` → $L_i = L_{i-1} + 1$ (must exceed the previous value)
- $s_{i-1} =$ `=` → $L_i = L_{i-1}$ (must equal it)
- $s_{i-1} =$ `>` → $L_i = 1$ (free to restart at the minimum)

**Right pass** is the mirror image, with `>` driving the increase.

A slot must satisfy both constraints at once, so its value is $\max(L_i, R_i)$, and the answer is the largest such value over all slots.

Taking the maximum is what couples the two passes. A slot sitting at the bottom of a `>` run *and* the start of a `<` run is pinned by whichever run is longer — neither pass alone sees that.

The `=` case is the one most easily mishandled: it propagates the running value **unchanged** rather than resetting it, so a long `<<=<` chain keeps climbing across the equals sign. Sample case 4, `<=<`, gives left values $1, 2, 2, 3$ and answer $3$ — the `=` holds the value flat but does not break the chain, so the final `<` still has to climb past it.

Sample case 3, `<=>`, peaks at $2$ because the `<` and `>` runs each have length one and the `=` merely ties the two middle slots together.

Sample case 1, `<<<`, is a pure ascent needing $1,2,3,4$.

## Edge cases

- **`=` propagates rather than resetting.** Two slots joined by `=` must hold the same number, so the run length carries across — which is why the third row (`<=>`) needs only $2$ and not $3$.
- **Each slot is constrained from both sides at once**, so the answer is the maximum over slots of $\max(\text{left}, \text{right})$: a slot ending a long `<` chain and starting a long `>` chain must satisfy whichever is larger.
- **The two sweeps are not symmetric in what they count**: the forward pass grows on `<` and the backward pass on `>`, each tracking the chain that forces a *larger* value at that slot.
- **A single direction gives the worst case.** `<<<` forces $1 < 2 < 3 < 4$, so $P = 4$ — the maximum possible for its length.
- **Alternating signs stay cheap**: `<><` needs only $2$, since each slot's constraints are short.
- **There are $N+1$ slots for $N$ signs**, so both arrays have length $N+1$ and the final maximum runs over all of them.
- **Sum of $|s| \leq 10^6$**: two linear passes on bytes, comparing against the literal codes for `<`, `=` and `>`.

## Dry run

The string `<=<`, with four slots.

| slot | left chain (forced by `<` before it) | right chain (forced by `>` after it) | needed |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 2 | 1 | 2 |
| 3 | 2 (carried over the `=`) | 1 | 2 |
| 4 | 3 | 1 | **3** |

Output `3`, realised by $1 < 2 = 2 < 3$.
