# 26. Good Program

> CodeChef problem code [`NIBBLE`](https://www.codechef.com/problems/NIBBLE) &middot; difficulty **593** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Divisibility test |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

In computing, the collection of **four bits** is called a **nibble**.

Chef defines a program as:
- **Good**, if it takes exactly $X$ nibbles of memory, where $X$ is a positive integer.
- **Not Good**, otherwise.

Given a program which takes $N$ **bits** of memory, determine whether it is **Good** or **Not Good**.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- The first and only line of each test case contains a single integer $N$, the number of bits taken by the program.

**Output**

For each test case, output $\texttt{Good}$ or $\texttt{Not Good}$ in a single line.
You may print each character of $\texttt{Good}$ or $\texttt{Not Good}$ in uppercase or lowercase (for example, $\texttt{GoOd}$, $\texttt{GOOD}$, $\texttt{good}$ will be considered identical).

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000$

**Subtasks**

**Subtask #1 (100 points):** original constraints

## Sample

**Sample input**

```
4
8
17
52
3
```

**Sample output**

```
Good
Not Good
Good
Not Good
```

<details><summary>Explanation</summary>

**Test case 1:** The program requires $8$ bits of memory. This is equivalent to $\frac{8}{4} = 2$ nibbles. Since $2$ is an integer, this program is good.

**Test case 2:** The program requires $17$ bits of memory. This is equivalent to $\frac{17}{4} = 4.25$ nibbles. Since $4.25$ is not an integer, this program is not good.

**Test case 3:** The program requires $52$ bits of memory. This is equivalent to $\frac{52}{4} = 13$ nibbles. Since $13$ is an integer, this program is good.

**Test case 4:** The program requires $3$ bits of memory. This is equivalent to $\frac{3}{4} = 0.75$ nibbles. Since $0.75$ is not an integer, this program is not good.

</details>

## Approach

A nibble is $4$ bits, and a program is *Good* when its size is exactly $X$ nibbles for a positive integer $X$. A program of $N$ bits occupies $N/4$ nibbles, so $N$ must divide evenly by $4$:

$$N \equiv 0 \pmod 4$$

which is the single expression `n % 4 == 0`.

The clause "where $X$ is a **positive** integer" formally rules out $X = 0$, so $N = 0$ would be *Not Good*. The constraints guarantee $N \geq 1$, so this never arises and no extra guard is needed — but it is worth noticing the requirement rather than assuming divisibility alone is the whole condition, because the same wording in a problem allowing $N = 0$ would change the answer.

Since $4$ is a power of two there is a bitwise equivalent, `n & 3 == 0`, which tests that the low two bits are clear. It is the same test and no faster in Python, but it is the idiom to recognise when reading C-style code: `n % 2^k == 0` is `n & (2^k - 1) == 0`.

Checking the samples: $8 = 2 \times 4$ and $52 = 13 \times 4$ are Good, while $17$ and $3$ leave remainders of $1$ and $3$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # A nibble is 4 bits, so the size must divide evenly by 4.
        out.append("Good" if n % 4 == 0 else "Not Good")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Mathematics`, `Modular Arithmetic`, `Basic Math`
