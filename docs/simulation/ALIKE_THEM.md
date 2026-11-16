[&larr; 627. Alternative Sufferings](ALTSUFF.md) &middot; [Index](../../README.md) &middot; [735. College Admissions &rarr;](ADMIT.md)

# 688. Make Them Alike

> CodeChef problem code [`ALIKE_THEM`](https://www.codechef.com/problems/ALIKE_THEM) &middot; difficulty **2245** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Simulation |
| **Technique** | Track which original position every final value comes from |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

You are given a permutation $P$ of length $N$, an array $A$ of size $N$, and an integer $M$.

Initially, $0 \le A_i \le M$. Consider an array $A'$ obtained from $A$ by replacing all **zeros** in $A$ with **positive** integers **less than or equal to** $M$.

The array $A'$ will then be transformed as follows, in $N$ steps:
- In the $i^{th}$ step, we set $A'_i = A'_{P_i}$.

The initial array $A'$ is said to be *beautiful*, if, after the transformation of $N$ steps, all elements of array $A'$ are **equal**.

Find the number of such *beautiful* arrays $A'$ which can be formed by changing the zeros in array $A$ to any value $\leq M$. Since this number can be huge, print this number modulo $10^9+7$.

Note that a permutation of length $N$ contains of all elements from $1$ to $N$ exactly once.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$, the size of the array and the maximum value it can have.
    - The second line of each test case consists of $N$ space-separated integers $P_1, P_2, \ldots, P_N$, the permutation $P$.
    - The third line of each test case consists of $N$ space-separated integers $A_1, A_2, \ldots, A_N$, the initial array $A$.

**Output**

For each test case, output on a new line, the number of such *beautiful* arrays $A'$ which can be formed by changing the zeros in array $A$ to any value $\leq M$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $1 \leq M \leq 10^9$
- $0 \leq A_i \leq M$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

## Sample

**Sample input**

```
3
4 3
2 1 4 3
0 2 0 2
3 2
3 1 2
0 0 0
8 54
8 1 2 4 3 6 7 5
0 0 0 0 0 0 0 0
```

**Sample output**

```
9
8
459165024
```

<details><summary>Explanation</summary>

**Test case $1$:** The given permutation is $[2,1,4,3]$. One of the possible beautiful arrays is: $A' = [1,2,3,2]$. This is obtained by replacing the first $0$ with $1$ and the second $0$ with $3$ in the array $A$.
For the transformation:
- In the first step, $A'_1$ is replaced with $A'_{P_1} = A'_2$, that is $2$. The array becomes $[2,2,3,2]$.
- In the second step, $A'_2$ is replaced with $A'_{P_2} = A'_1$, that is $2$. The array becomes $[2,2,3,2]$.
- In the third step, $A'_3$ is replaced with $A'_{P_3} = A'_4$, that is $2$. The array becomes $[2,2,2,2]$.
- In the fourth step, $A'_4$ is replaced with $A'_{P_4} = A'_3$, that is $2$. The array becomes $[2,2,2,2]$.

Thus, after the transformation, all elements of the array are equal. The other beautiful arrays for this test case are: $[1,2,1,2], [1,2,2,2], [2,2,1,2], [2,2,2,2], [2,2,3,2], [3,2,1,2], [3,2,2,2], [3,2,3,2]$.

There are $9$ beautiful arrays in total.

</details>

## Approach

The transformation only copies values, so every final entry is a copy of some original entry. Simulate the $N$ steps on indices instead of values: start with `source[i] = i` and, in step $i$, set `source[i] = source[P_i]`, reading the current (possibly already overwritten) value. At the end `source[i]` names the original position whose value ends up at $i$.

The final array is constant exactly when all original positions that occur as a source hold the same value. Call these the surviving positions; all other positions are overwritten before they are ever read by a survivor and are completely free.

- If the surviving positions contain two different non-zero values, the answer is 0.
- Otherwise the zeros among the survivors are all forced to the common value: if some survivor is non-zero that value is fixed, else it can be chosen in $M$ ways.
- Every zero at a non-surviving position contributes an independent factor $M$.

The answer is $M^{\text{free zeros} + [\text{no fixed survivor}]}$ modulo $10^9 + 7$.

## Solution (Python)

```python
import sys


def solve(tokens):
    n, limit = (next(tokens), next(tokens))
    perm = [next(tokens) - 1 for _ in range(n)]
    values = [next(tokens) for _ in range(n)]
    source = list(range(n))
    for i in range(n):
        source[i] = source[perm[i]]
    used = set(source)
    fixed = {values[i] for i in used if values[i]}
    free = sum((values[i] == 0 for i in range(n) if i not in used))
    return str(0 if len(fixed) > 1 else pow(limit, free + (not fixed), 1000000007))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Steps are sequential: step $i$ may read a position that an earlier step already changed.
- Non-zero entries at non-surviving positions impose nothing.
- A fixed point $P_i = i$ simply keeps its own value in that step.
- $M$ is up to $10^9$, so the power is computed modularly.

## Dry run

`P = [3, 1, 2]`, `A = [0, 0, 0]`, `M = 2`.

Sources: step 1 copies from position 3: `[3, 2, 3]`; step 2 copies from position 1, which now holds source 3: `[3, 3, 3]`; step 3 copies from position 2: `[3, 3, 3]`.

Only position 3 survives and it is a zero: $M$ choices for it. Positions 1 and 2 are free zeros: $M^2$.

Answer $2^3 = 8$.

> CodeChef tags: `Data Structures`, `Graphs`

---

Same problem in rating order (#650 of 735): [../../by-rating/650-ALIKE_THEM.md](../../by-rating/650-ALIKE_THEM.md)
