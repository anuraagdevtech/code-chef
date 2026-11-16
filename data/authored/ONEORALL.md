---
topic: Game Theory
subtopic: Parity of the total, plus the parity of the minimum when N is even
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
**$N$ odd.** A type-1 move removes 1 stone and a type-2 move removes $N$ stones, an odd number. Every move flips the parity of the total, the game ends at total 0, and so the number of moves has the parity of the initial total: the first player wins exactly when the total is odd.

**$N$ even.** Now a type-2 move keeps the parity of the total but flips the parity of the minimum. Claim: the losing positions are exactly those where both the total and the minimum are even.

- From such a position every move leaves the set: a type-1 move makes the total odd; a type-2 move (possible only if the minimum is at least 2) keeps the total even but makes the minimum odd.
- From any other position there is a move into the set. If the minimum is odd and the total even, take one from every pile. If the total is odd and the minimum is even, take one stone from a pile that is larger than the minimum - one exists, since $N$ equal even piles would have an even total. If both are odd, take one stone from a minimum pile, making both even.

The terminal position (all piles empty) has total 0 and minimum 0 and is losing, consistent with the claim. So for even $N$ Chef wins unless the total and the minimum are both even.

## Edge cases

- $N = 1$: the two move types coincide and Chef wins exactly when the pile is odd.
- All piles equal to 1 with even $N$: one type-2 move wins immediately.
- Only two parities are needed; the actual sizes are irrelevant.
- The total can reach $10^{14}$.

## Dry run

- `[1, 1, 1, 1]`: $N$ even, minimum 1 is odd - CHEF (he removes one from every pile).
- `[1, 2, 3]`: $N$ odd, total 6 is even - CHEFINA.
- `[15]`: $N$ odd, total 15 is odd - CHEF.
