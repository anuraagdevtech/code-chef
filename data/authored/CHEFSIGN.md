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
