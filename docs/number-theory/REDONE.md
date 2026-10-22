# 274. Reduce to One

> CodeChef problem code [`REDONE`](https://www.codechef.com/problems/REDONE) &middot; difficulty **1507** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | A telescoping product in disguise |
| **Time** | $O(1)$ per test case after an $O(N)$ precomputation |
| **Space** | $O(N)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

You have become good friends with Chef. Right now, Chef is busy in the kitchen, so he asked you to solve a problem for him.

Consider a list of integers $L$. Initially, $L$ contains the integers $1$ through $N$, each of them exactly once (but it may contain multiple copies of some integers later). The order of elements in $L$ is not important. You should perform the following operation $N-1$ times:
- Choose two elements of the list, let's denote them by $X$ and $Y$. These two elements may be equal.
- Erase the chosen elements from $L$.
- Append the number $X + Y + X \cdot Y$ to $L$.

At the end, $L$ contains exactly one integer. Find the maximum possible value of this integer. Since the answer may be large, compute it modulo $1,000,000,007$ ($10^9+7$).

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$.

**Output**
For each test case, print a single line containing one integer ― the maximum possible value of the final number in the list modulo $10^9+7$.

**Constraints**
- $1 \le T \le 100,000$
- $1 \le N \le 1,000,000$

**Subtasks**
**Subtask #1 (20 points):** $1 \le T, N \le 25$

**Subtask #2 (80 points):** original constraints

## Constraints

- $1 \le T \le 100,000$
- $1 \le N \le 1,000,000$

## Sample

**Sample input**

```
3
1
2
4
```

**Sample output**

```
1
5
119
```

<details><summary>Explanation</summary>

**Example case 1:** $L=[1]$

**Example case 2:** $L=[1,2] \rightarrow [1 + 2 + 1 \cdot 2] $

**Example case 3:** $L=[\textbf{1},2,3,\textbf{4}] \rightarrow [\textbf{2},3,\textbf{9}] \rightarrow [3,29] \rightarrow [119] $. The chosen elements in each step are in bold.

</details>

## Approach

The combining rule factorises:

$$X + Y + XY = (1+X)(1+Y) - 1$$

So if we track $1 + v$ instead of $v$ for every element, the operation becomes plain **multiplication**. Replacing two values multiplies their shifted forms together, and the shifted form of the result is the product.

After all $N-1$ operations, one value remains, and its shifted form is the product of every original shifted value:

$$1 + \text{result} = \prod_{i=1}^{N} (1 + i) = 2 \cdot 3 \cdots (N+1) = (N+1)!$$

so the answer is $(N+1)! - 1$.

Notice what this says: the result is **independent of the order of operations**, because multiplication is commutative and associative. The problem asks for the maximum, but every sequence of choices gives the same value — there is nothing to optimise, which is the real surprise.

Checking the samples: $N = 1$ gives $2! - 1 = 1$; $N = 2$ gives $3! - 1 = 5$; $N = 4$ gives $5! - 1 = 119$.

With $T$ up to $10^5$ and $N$ up to $10^6$, factorials modulo $10^9+7$ are precomputed once in a single $O(N)$ pass, making each query a lookup. Computing a factorial per query would be $10^{11}$ operations.

One subtlety of working modulo a prime: the $-1$ must be taken **after** the modular reduction, and the result kept non-negative — `(fact[n + 1] - 1) % MOD` handles that.

## Solution (Python)

```python
import sys

MOD = 10 ** 9 + 7
LIMIT = 10 ** 6 + 2


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    # (1 + x)(1 + y) = 1 + (x + y + xy), so the whole list telescopes to (n+1)!
    fact = [1] * LIMIT
    for i in range(1, LIMIT):
        fact[i] = fact[i - 1] * i % MOD
    out = [str((fact[int(data[1 + i]) + 1] - 1) % MOD) for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case after an $O(N)$ precomputation
- **Space:** $O(N)$

## Edge cases

- **The operation is a disguised product.** $X + Y + XY = (1+X)(1+Y) - 1$, so the quantity $\prod (1 + L_i)$ is invariant across every move — the order of choices cannot matter.
- **The invariant starts at $(N+1)!$**, since $\prod_{i=1}^{N} (1 + i) = 2 \cdot 3 \cdots (N+1)$, and ends at $1 + V$ for the single survivor. Hence $V = (N+1)! - 1$.
- **$N = 1$** performs zero operations and leaves the list as $[1]$, which the formula gives as $2! - 1 = 1$.
- **The factorials must be precomputed modularly.** With $T$ up to $10^5$ and $N$ up to $10^6$, each query is a table lookup; computing a factorial per query would be far too slow.
- **The subtraction needs a final `% MOD`.** The reduced factorial can be $0$, in which case $0 - 1$ is negative, and the modulo brings it back into range.
- **The table runs to $10^6 + 1$**, one past the maximum $N$, because the answer uses $(N+1)!$.

## Dry run

| $N$ | list | invariant $\prod(1 + L_i)$ | survivor $V$ |
|---:|---|---:|---:|
| 1 | $[1]$ | $2 = 2!$ | `1` |
| 2 | $[1, 2]$ | $2 \cdot 3 = 3!$ | `5` |
| 4 | $[1,2,3,4]$ | $2 \cdot 3 \cdot 4 \cdot 5 = 5!$ | `119` |

For $N = 2$: $1 + 2 + 1 \cdot 2 = 5$, and $1 + 5 = 6 = 3!$ ✓

> CodeChef tags: `Advanced Algorithms`, `Algorithms`

---

Same problem in rating order (#301 of 486): [../../by-rating/301-REDONE.md](../../by-rating/301-REDONE.md)
