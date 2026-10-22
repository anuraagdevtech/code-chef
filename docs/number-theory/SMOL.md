[&larr; 152. Joining Date](JOINING.md) &middot; [Index](../../README.md) &middot; [170. Maximum Length Even Subarray &rarr;](MXEVNSUB.md)

# 166. Smallest Possible Whole Number

> CodeChef problem code [`SMOL`](https://www.codechef.com/problems/SMOL) &middot; difficulty **1306** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Modulo, with a zero-divisor guard |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

You are given two integers $N$ and $K$. You may perform the following operation any number of times (including zero): change $N$ to $N-K$, i.e. subtract $K$ from $N$. Find the smallest non-negative integer value of $N$ you can obtain this way.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $N$ and $K$.

**Output**
For each test case, print a single line containing one integer — the smallest value you can get.

**Constraints**
- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^9$
- $0 \leq K \leq 10^9$

**Subtasks**
**Subtask #1 (100 points):** original constraints

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^9$
- $0 \leq K \leq 10^9$

## Sample

**Sample input**

```
3
5 2
4 4
2 5
```

**Sample output**

```
1
0
2
```

<details><summary>Explanation</summary>

**Example case 1:**
- First, we change $N = 5$ to $N - K = 5 - 2 = 3$.
- Then, we have $N = 3$ and we change it to $N - K = 3 - 2 = 1$.

Since $1 \lt K$, the process stops here and the smallest value is $1$.

**Example case 2:** We change $N = 4$ to $N - K = 4 - 4 = 0$. Since $0 \lt K$, the process stops here and the smallest value is $0$.

**Example case 3:** Since $2 \lt K$ initially, we should not perform any operations and the smallest value is $2$.

</details>

## Approach

Repeatedly subtracting $K$ from $N$ while staying non-negative lands on exactly the remainder:

$$N \bmod K$$

That is what the modulo operator *means* — the smallest non-negative value reachable by subtracting multiples of $K$. Looping the subtractions would be correct but hopeless at $N$ up to $10^9$ with $K = 1$; the modulo is $O(1)$.

The case that makes this more than a one-liner is **$K = 0$**, which the constraints explicitly allow. Subtracting zero changes nothing, so the answer is $N$ itself — and `n % 0` raises `ZeroDivisionError` in Python (and is undefined behaviour in C). So the guard is not defensive padding; without it the program crashes on valid input.

The samples do not include $K = 0$, which is exactly why it is worth reading the constraints rather than trusting the examples. A solution tested only against the three given cases passes locally and fails on submission.

Sample case 3 covers the other easily-missed case: $K > N$, where no subtraction is possible at all and the answer is $N$ unchanged. The modulo handles that without a branch, since $2 \bmod 5 = 2$.

Sample case 2 is the exact-division case, reaching $0$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # k = 0 is allowed by the constraints and would crash the modulo.
        out.append(str(n if k == 0 else n % k))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **$K = 0$ is permitted by the constraints** and would raise `ZeroDivisionError`. With a step of zero no subtraction changes anything, so the answer is $N$ itself — this guard is the whole problem.
- **$K > N$** (the third row, $N = 2$ with $K = 5$): no subtraction is possible without going negative, and `n % k` already returns $N$, so no extra branch is needed.
- **$K$ divides $N$** (the second row): the result is $0$, the smallest whole number reachable.
- **$N$ is at least $1$**, so a $0$ answer only ever arises from exact divisibility.
- **$T$ up to $10^5$** with constant work per case; the input is read in one buffered call.

## Dry run

| $N$ | $K$ | path | output |
|---:|---:|---|---:|
| 5 | 2 | $5 \to 3 \to 1$ | `1` |
| 4 | 4 | $4 \to 0$ | `0` |
| 2 | 5 | cannot subtract | `2` |

A fourth, unsampled case: $N = 7$, $K = 0$ stays at `7` instead of crashing.

---

Same problem in rating order (#204 of 486): [../../by-rating/204-SMOL.md](../../by-rating/204-SMOL.md)
