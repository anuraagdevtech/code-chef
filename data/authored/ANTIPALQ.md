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
