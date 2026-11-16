---
topic: Dynamic Programming
subtopic: Balanced partition by subset-sum bitset, then a simulated hand-out order
time: $O(N \cdot S / w)$ per test case, $S$ the sum of the values
space: $O(N \cdot S / w)$ machine words - one bitset per prefix for reconstruction
complexity_note: Auxiliary space excludes the buffered input and output.
---
Whatever the order, just before the last coin he receives Chefu holds at most as much as Chefa. The best he can do is therefore to be as close to level as possible on all coins but one and then receive the largest coin last.

Set the largest coin aside and split the other coins into two parts whose sums are as close as possible: a subset-sum bitset over them gives the largest reachable sum not exceeding half of their total, and keeping the bitset after every coin lets us walk backwards and recover which coins form that part. Chefu is given the smaller part, Chefa the other.

To turn the split into an order, simulate Chef's rule: whenever Chefu is not ahead, hand out the next coin from his pile, otherwise the next one from Chefa's pile. The reserved coin sits at the bottom of Chefu's pile, so he takes it at the moment his own part is exhausted and he is still not ahead. He ends with (total + largest - minimum difference) / 2. Any order achieving the maximum is accepted.

## Edge cases

- A single coin: the order is just `1` and Chefu takes it because of the tie rule.
- Several coins share the maximum value: reserving any one of them is equally good.
- Ties go to Chefu, so the simulation uses `chefu <= chefa`.
- The output is a permutation of indices, not the values.

## Dry run

Coins `[3, 1, 2]`. Reserve the 3. The other coins `{1, 2}` total 3, so the target is 1: Chefu's part is `{1}`, Chefa's is `{2}`.

Simulation: level at 0, so Chefu takes value 1 (coin 2). He is ahead, so Chefa takes value 2 (coin 3). Now 1 against 2, so Chefu takes the reserved 3 (coin 1).

Order `2 3 1`; Chefu ends with 4 out of 6.
