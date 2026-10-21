# 134. Problem

> [`PR0BLEM`](https://www.codechef.com/problems/PR0BLEM) &middot; difficulty **908** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Parity invariant |
| **CodeChef tags** | `Mathematics`, `Basic Math` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

*One less problem without ya \
I got one less problem without ya*

Alice and Bob are competing in a challenge. Initially Alice has $N$ problems and Bob has $M$ problems.

- Each time Alice solves a problem, Bob receives **one more** problem to solve.
- Each time Bob solves a problem, Alice receives **three more** problems to solve.

Find whether it is possible that both of them have the **same** number of problems left if they can solve the problems in any arbitrary manner.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case contains two space-separated integers $N$ and $M$ — the initial number of problems of Alice and Bob respectively.

**Output**

For each test case, output on a new line, `YES`, it is possible that both of them have the **same** number of problems left if they can solve the problems in any arbitrary manner and `NO` otherwise.

Each character of the output may be printed in either uppercase or lowercase. That is, the strings `NO`, `no`, `nO`, and `No` will be treated as equivalent.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N, M \leq 100$

## Sample

**Sample input**

```
4
4 2
1 5
2 3
2 2
```

**Sample output**

```
YES
YES
NO
YES
```

<details><summary>Explanation</summary>

**Test case $1$:** Initially Alice has $4$ problems while Bob has $2$ problems.
Alice can solve a problem first. Thus, Alice now has $4-1 = 3$ problems left and Bob has $2 + 1 = 3$ problems left.

Thus, both of them can have same number of problems left.

**Test case $2$:** Initially Alice has $1$ problem while Bob has $5$ problems.
Bob can solve a problem first. Thus, Bob now has $5-1 = 4$ problems left and Alice has $1 + 3 = 4$ problems left.

Thus, both of them can have same number of problems left.

**Test case $3$:** It can be proven that they cannot have the same number of problems left.

**Test case $4$:** Both of them have the same number of problems initially.

</details>

## Approach

Let $a$ be the number of problems Alice solves and $b$ the number Bob solves. Tracking both counts:

$$\text{Alice} = N - a + 3b, \qquad \text{Bob} = M + a - b$$

Setting them equal and rearranging:

$$N - M = 2a - 4b = 2(a - 2b)$$

The right side is always **even**, so the two can only level up when $N - M$ is even — that is, when $N$ and $M$ share a parity. Conversely, whenever the difference is even a suitable $(a, b)$ exists, so the condition is exactly

$$N \equiv M \pmod 2$$

Looking for what the operations preserve is again the fastest route. Each of Alice's solves changes the difference $N - M$ by $-2$, and each of Bob's changes it by $+4$; both are even, so the **parity of the difference is invariant**. Starting from an odd difference, no sequence of moves can ever reach zero.

Sample case 3 is the odd case: $N = 2$, $M = 3$ differ by $1$, so `NO`. The others all have even differences, including case 4 where they are already equal and no moves are needed.

Note the problem never requires the counts to stay non-negative, nor that the problems actually be solvable — "in any arbitrary manner" licenses treating $a$ and $b$ as free non-negative integers. That generality is what makes the parity condition sufficient as well as necessary.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Every move changes n - m by an even amount, so its parity is fixed.
        out.append("YES" if (n - m) % 2 == 0 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **$N = M$**: the difference is $0$, which is even, so `YES`.
- **$N < M$** (the second row, $1$ and $5$): the difference is negative. Python's `%` returns a non-negative remainder so the parity test still works, but a language where the modulo follows the sign of the dividend needs care — `-1 % 2` can be `-1` there, and comparing it against $0$ then fails.
- **Both odd or both even** → `YES`; **mixed parity** → `NO`.
- Every move changes $N - M$ by an even amount, so its parity is invariant — which is why the answer depends on nothing else and no simulation is needed.

## Dry run

| $N$ | $M$ | $N - M$ | even? | output |
|---:|---:|---:|:---:|---|
| 4 | 2 | 2 | yes | `YES` |
| 1 | 5 | $-4$ | yes | `YES` |
| 2 | 3 | $-1$ | no | `NO` |
| 2 | 2 | 0 | yes | `YES` |

Row 2 is the negative-difference case.

---

Same problem grouped by topic: [../docs/number-theory/PR0BLEM.md](../docs/number-theory/PR0BLEM.md)
