# 1507 &middot; Reduce to One

> CodeChef problem code [`REDONE`](https://www.codechef.com/problems/REDONE) &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topics used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | A telescoping product in disguise |
| **CodeChef tags** | `Advanced Algorithms`, `Algorithms`, `Pre processing`, `Observation` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case after an $O(N)$ precomputation |
| **Space** | $O(N)$ |

Same write-up grouped by topic: [../docs/number-theory/REDONE.md](../docs/number-theory/REDONE.md)

## Question

You have become good friends with Chef. Right now, Chef is busy in the kitchen, so he asked you to solve a problem for him.

Consider a list of integers $L$. Initially, $L$ contains the integers $1$ through $N$, each of them exactly once (but it may contain multiple copies of some integers later). The order of elements in $L$ is not important. You should perform the following operation $N-1$ times:
- Choose two elements of the list, let's denote them by $X$ and $Y$. These two elements may be equal.
- Erase the chosen elements from $L$.
- Append the number $X + Y + X \cdot Y$ to $L$.

At the end, $L$ contains exactly one integer. Find the maximum possible value of this integer. Since the answer may be large, compute it modulo $1,000,000,007$ ($10^9+7$).

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$.

### Output
For each test case, print a single line containing one integer ― the maximum possible value of the final number in the list modulo $10^9+7$.

### Constraints
- $1 \le T \le 100,000$
- $1 \le N \le 1,000,000$

### Subtasks
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
