[&larr; 008. Chef And Operators](008-CHOPRT.md) &middot; [Index](README.md) &middot; [010. Second Largest &rarr;](010-FLOW017.md)

# 009. Decrement OR Increment

> [`DECINC`](https://www.codechef.com/problems/DECINC) &middot; difficulty **520** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Single divisibility branch |
| **CodeChef tags** | `Basic Programming Concepts`, `Conditional Statements` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ |
| **Space** | $O(1)$ |

## Question

Write a program to obtain a number $N$ and increment its value by 1 if the number is divisible by 4 $otherwise$ decrement its value by 1.

**Input**

First line will contain a number $N$.

**Output**

Output a single line, the new value of the number.

## Constraints

- $0 \leq N \leq 1000$

## Sample

**Sample input**

```
5
```

**Sample output**

```
4
```

<details><summary>Explanation</summary>

Since 5 is not divisible by 4 hence, its value is decreased by 1.

</details>

## Approach

One number in, one number out: if $N$ is divisible by $4$ print $N + 1$, otherwise print $N - 1$.

$$\text{answer} = \begin{cases} N + 1 & N \equiv 0 \pmod 4 \\ N - 1 & \text{otherwise} \end{cases}$$

The sample is the "otherwise" branch — $5$ is not a multiple of $4$, so the answer is $4$.

Two details are worth pinning down. First, there is **no $T$** here: the input is a single number, not a count followed by test cases. Reading a test-case count would consume $N$ itself and then wait for input that never arrives.

Second, $N = 0$ is inside the constraints, and $0$ *is* divisible by $4$ — the branch taken is the increment, giving $1$. It is tempting to treat zero as a special case, but `0 % 4 == 0` is true and the general rule already handles it. The only input that could produce a negative answer would be an $N$ below $1$ that is not a multiple of $4$, which the constraints exclude.

## Solution

```python
import sys


def main() -> None:
    # Single value, no test-case count on the first line.
    n = int(sys.stdin.buffer.read().split()[0])
    print(n + 1 if n % 4 == 0 else n - 1)


main()
```

## Edge cases

- **$N = 0$**: $0$ is divisible by $4$, so the answer is $0 + 1 = 1$. Taking the other branch would print $-1$, which is why the divisibility test has to come first.
- **$N = 4$** (smallest positive multiple of four): $5$.
- **$N = 1$**: not a multiple of four, so $0$ — the result may legitimately be zero.
- **$N = 1000$** (the bound, and a multiple of four): $1001$.
- **Input shape**: a single integer with *no* leading test-case count, unlike almost every other problem here — reading a count first would consume the value itself.

## Dry run

Input is the single value $N = 5$.

| step | value |
|---|---|
| $N$ | $5$ |
| $N \bmod 4$ | $1$ |
| branch | not divisible, so $N - 1$ |
| output | `4` |

---

Same problem grouped by topic: [../docs/conditionals-case-work/DECINC.md](../docs/conditionals-case-work/DECINC.md)
