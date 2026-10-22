---
topic: Prefix Sums
subtopic: Reducing a rotation condition to one count
time: $O(N + Q)$ per test case
space: $O(N)$
---
Unwinding the definition collapses it completely. For the rotation by $r$, the anti-palindrome condition compares positions $a$ and $b$ with

$$a + b \equiv M - 1 - 2r \pmod M$$

As $r$ runs over all rotations and $M$ is even, $M-1-2r$ runs over **every odd residue** mod $M$. So $B$ is beautiful exactly when $B_a \neq B_b$ for every pair with $a + b$ odd — that is, whenever the index parities differ. Equivalently: the values at even positions and the values at odd positions must form **disjoint sets**.

(For odd $M$ the middle index pairs with itself, so no array qualifies: the answer is `No`.)

Since the values are only $1, 2, 3$, each value must go entirely to the even side or entirely to the odd side, and each side has $M/2 $ slots. So we need a sub-collection of the three value-classes whose total count is exactly $M/2$ — and because the three counts sum to $M$, every such choice amounts to **one value class holding exactly half the subarray**:

$$\text{Yes} \iff M \text{ even and } c_v = M/2 \text{ for some } v \in \{1,2,3\}$$

Three prefix-count arrays make each query $O(1)$.

The samples exercise each failure. $[2,3,1,3]$ has $c_3 = 2 = M/2$, so `Yes` — e.g. $3\,1\,3\,2$. $[2,3,1]$ is odd-length, so `No`. $[2,2]$ is even but $c_2 = 2 \neq 1$, so `No` — with both elements equal, opposite entries must collide. And $[1,2,3,2,2,2]$ has counts $1, 4, 1$ against $M/2 = 3$, so `No` despite being even and having three distinct values.

## Edge cases

- **The query asks whether the subarray can be *rearranged* to be beautiful**, not whether it already is — so only the multiset matters, and the sample's fourth query answers `Yes` for $[2,2,3,1]$ even though that exact order fails.
- **Over all rotations, every pair of opposite-parity positions gets compared.** A rotation by $s$ compares the pairs summing to $2s - 1 \pmod M$, and as $s$ varies those sums cover every odd residue — so beautiful means the odd-indexed and even-indexed values are disjoint sets.
- **An odd length is hopeless**, because the middle element would have to differ from itself.
- **With only three values, one parity class must be monochromatic.** Two disjoint non-empty value sets drawn from $\{1,2,3\}$ cannot both hold two values, so one class is a single value $v$ filling all $M/2$ of its slots — giving $\mathrm{count}(v) = M/2$ exactly.
- **That makes the test "even length and some value appears exactly $M/2$ times"**, which is both necessary and sufficient — verified exhaustively against brute force over all multisets up to size $8$.
- **$[2,2]$ fails** despite its even length: the only value has count $2 \neq 1$, so no rearrangement works.
- **Three prefix arrays suffice**, one per value, making each query $O(1)$.

## Dry run

First sample's fourth query: $B = [2, 2, 3, 1]$, so $M = 4$ and $M/2 = 2$.

| value | count in range | equals $2$? |
|---:|---:|:---:|
| 1 | 1 | no |
| 2 | **2** | **yes** |
| 3 | 1 | no |

Output `Yes`. A witnessing arrangement is $[3, 2, 1, 2]$: the even positions both hold $2$ and the odd positions hold $3$ and $1$, so the two parity classes share no value.
