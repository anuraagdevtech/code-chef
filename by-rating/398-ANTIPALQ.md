[&larr; 397. Chef and Water Car](397-CHEFCAR.md) &middot; [Index](README.md) &middot; [399. Boxes &rarr;](399-BOX95.md)

# 398. Anti-Palindrome Queries

> [`ANTIPALQ`](https://www.codechef.com/problems/ANTIPALQ) &middot; difficulty **1688** &middot; time limit **1.5s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Reducing a rotation condition to one count |
| **CodeChef tags** | `prefix-sum` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N + Q)$ per test case |
| **Space** | $O(N)$ |

## Question

An array $B$ of length $M$ is called an *anti-palindrome* if **no** pair of its opposite elements are equal.
That is, $B_i \neq B_{M+1-i}$ should hold for *every* index $1 \leq i \leq M$.
For example, $[1, 2]$ and $[1, 2, 3, 2]$ are anti-palindromes, but $[1, 2, 3]$ and $[1, 2, 3, 1]$ are not ($i = 2$ is violated in the first case, $i = 1$ in the second).

We say the array $B$ is *beautiful* if **every** cyclic rotation$^\dagger$ of $B$ is an anti-palindrome.

You are given an array $A$ of length $N$, which contains only the integers $1, 2, $ and $3$.
Answer $Q$ queries on this array:
- Given $L$ and $R$, let $B = [A_L, A_{L+1}, \ldots, A_R]$ denote the subarray of $A$ from index $L$ to index $R$.
Is it possible to rearrange the elements of $B$ to make it beautiful?

$^\dagger$ A cyclic rotation of an array is obtained by repeatedly removing its last element and placing it at the beginning.
For example, the cyclic rotations of $A = [1, 2, 2, 3]$ are:
$[1, 2, 2, 3], [3, 1, 2, 2], [2, 3, 1, 2], [2, 2, 3, 1]$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $Q$ — the length of the array and the number of queries.
    - The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
    - The next $Q$ lines describe the queries. The $i$-th line contains two space-separated integers $L$ and $R$, the parameters of the $i$-th query.

**Output**

For each query, output on a new line the answer: `"Yes"` if it's possible to rearrange the subarray to make it beautiful, and `"No"` otherwise (without quotes).

Each character of the output may be printed in either uppercase or lowercase, i.e, the strings `NO`, `nO`, `No`, and `no` will all be treated as equivalent.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N, Q \leq 2\cdot 10^5$
- $1 \leq A_i \leq 3$
- $1 \leq L \leq R \leq N$
- The sum of $N$ and the sum of $Q$ over all test cases both won't exceed $2\cdot 10^5$.

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
2
5 4
2 2 3 1 3
2 5
2 4
1 2
1 4
6 4
1 2 3 2 2 2
1 6
4 4
4 5
1 4
```

**Sample output**

```
Yes
No
No
Yes
No
No
No
Yes
```

<details><summary>Explanation</summary>

**Test case $1$:** There are four queries, with their results as follows:
1. The first query asks for $[2, 3, 1, 3]$. This is already beautiful, and doesn't require rearrangement.
This can be verified by looking at every cyclic shift of it, namely:
$[2, 3, 1, 3], [3, 2, 3, 1], [1, 3, 2, 3], [3, 1, 3, 2]$.
2. The second query asks for $[2, 3, 1]$. It can be verified that no rearrangement of this is beautiful.
3. The third query asks for $[2, 2]$. This is the only rearrangement possible, and it isn't beautiful since it isn't an anti-palindrome.
4. The fourth query asks for $[2, 2, 3, 1]$.
This is not beautiful since its third cyclic shift $[2, 3, 1, 2]$ isn't an anti-palindrome.
However, it can be rearranged to form $[3, 2, 1, 2]$, which is beautiful.

</details>

## Approach

Unwinding the definition collapses it completely. For the rotation by $r$, the anti-palindrome condition compares positions $a$ and $b$ with

$$a + b \equiv M - 1 - 2r \pmod M$$

As $r$ runs over all rotations and $M$ is even, $M-1-2r$ runs over **every odd residue** mod $M$. So $B$ is beautiful exactly when $B_a \neq B_b$ for every pair with $a + b$ odd — that is, whenever the index parities differ. Equivalently: the values at even positions and the values at odd positions must form **disjoint sets**.

(For odd $M$ the middle index pairs with itself, so no array qualifies: the answer is `No`.)

Since the values are only $1, 2, 3$, each value must go entirely to the even side or entirely to the odd side, and each side has $M/2 $ slots. So we need a sub-collection of the three value-classes whose total count is exactly $M/2$ — and because the three counts sum to $M$, every such choice amounts to **one value class holding exactly half the subarray**:

$$\text{Yes} \iff M \text{ even and } c_v = M/2 \text{ for some } v \in \{1,2,3\}$$

Three prefix-count arrays make each query $O(1)$.

The samples exercise each failure. $[2,3,1,3]$ has $c_3 = 2 = M/2$, so `Yes` — e.g. $3\,1\,3\,2$. $[2,3,1]$ is odd-length, so `No`. $[2,2]$ is even but $c_2 = 2 \neq 1$, so `No` — with both elements equal, opposite entries must collide. And $[1,2,3,2,2,2]$ has counts $1, 4, 1$ against $M/2 = 3$, so `No` despite being even and having three distinct values.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, q = int(data[pos]), int(data[pos + 1])
        pos += 2
        pre = [[0] * (n + 1) for _ in range(3)]
        for i in range(n):
            v = int(data[pos + i]) - 1
            for k in range(3):
                pre[k][i + 1] = pre[k][i] + (k == v)
        pos += n
        for _ in range(q):
            l, r = int(data[pos]), int(data[pos + 1])
            pos += 2
            m = r - l + 1
            # Even length, and one value must fill exactly one parity class.
            ok = m % 2 == 0 and any(
                pre[k][r] - pre[k][l - 1] == m // 2 for k in range(3))
            out.append("Yes" if ok else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

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

---

Same problem grouped by topic: [../docs/prefix-sums/ANTIPALQ.md](../docs/prefix-sums/ANTIPALQ.md)
