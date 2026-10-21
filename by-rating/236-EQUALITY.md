# 236. Equality

> [`EQUALITY`](https://www.codechef.com/problems/EQUALITY) &middot; difficulty **1419** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Solving a symmetric linear system by summing |
| **CodeChef tags** | `Mathematics`, `Basic Math` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

<meta charset="utf8" />

An *equation* is an equality containing one or more variables. Solving the equation consists of determining which values of the variables make the equality true. In this situation, variables are also known as unknowns and the values which satisfy the equality are known as solutions. An equation differs from an identity in that an equation is not necessarily true for all possible values of the variable.

There are many types of equations, and they are found in all areas of mathematics. For instance, a linear equation is an algebraic equation in which each term is either a constant or the product of a constant and (the first power of) a single variable.

In this problem we'll consider quite a special kind of systems of linear equations. To be more specific, you are given a system of **N** linear equations of the following form:

	- **x_2** + **x_3** + ... + **x_N - 1** + **x_N** = **a_1**

	- **x_1** + **x_3** + ... + **x_N - 1** + **x_N** = **a_2**

	- ...

	- **x_1** + **x_2** + ... + **x_N - 2** + **x_N** = **a_N - 1**

	- **x_1** + **x_2** + ... + **x_N - 2** + **x_N - 1** = **a_N**

In other words, **i**'th equation of the system consists of the sum of all the variable **x_1**, ..., **x_N** except **x_i** to the left of the equality sign and the constant **a_i** to the right of the equality sign.

One can easily prove, that a system of linear equations as described above always have exactly one solution in case **N** is greater than one. Your task is to find the solution of the system(such a sequence **x_1**, **x_2**, ..., **x_N**, that turns each of the equations into equality). It's guaranteed, that the solution of the system is a sequence consisting only of integers from the range [1, 10^8].

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of the test case description contains one integer **N** denoting the number of equations in the system.

The second line contains **N** integers **a_1**, **a_2**, ..., **a_N** denoting the constants defining a system of linear equations, that you are asked to solve.

**Output**

For each test case, output a single line containing **N** integers: a sequence **x_1**, **x_2**, ..., **x_N**, which is the solution of the system.

**Constraints**

- 1 ≤ **T** ≤ 25000

- 2 ≤ **N** ≤ 50000

- 1 ≤ **a_i** ≤ 5 × 10^12

- 1 ≤ **x_i** ≤ 10^8

- The sum of all **N** in the input is not greater than 50000

## Constraints

- 1 ≤ T ≤ 25000
- 2 ≤ N ≤ 50000
- 1 ≤ a_i ≤ 5 × 10^12
- 1 ≤ x_i ≤ 10^8
- The sum of all N in the input is not greater than 50000

## Sample

**Sample input**

```
2
3
9 6 5
4
13 11 10 8
```

**Sample output**

```
1 4 5 
1 3 4 6
```

<details><summary>Explanation</summary>

In the first test case, we can simply replace the variables with the values from the correct output to make sure, that all the conditions are satisfied:

		- **x_2** + **x_3** = 4 + 5 = 9 = **a_1**

		- **x_1** + **x_3** = 1 + 5 = 6 = **a_2**

		- **x_1** + **x_2** = 1 + 4 = 5 = **a_3**

	In the second test case, we can repeat the same process to make sure, that all the conditions are satisfied:

		- **x_2** + **x_3** + **x_4** = 3 + 4 + 6 = 13 = **a_1**

		- **x_1** + **x_3** + **x_4** = 1 + 4 + 6 = 11 = **a_2**

		- **x_1** + **x_2** + **x_4** = 1 + 3 + 6 = 10 = **a_3**

		- **x_1** + **x_2** + **x_3** = 1 + 3 + 4 = 8 = **a_4**

</details>

## Approach

Each equation omits exactly one variable, so writing $S = x_1 + \cdots + x_N$ the $i$-th equation is simply

$$S - x_i = a_i \quad\Longrightarrow\quad x_i = S - a_i$$

The only unknown left is $S$. Summing all $N$ equations counts every variable exactly $N-1$ times:

$$\sum_i a_i = \sum_i (S - x_i) = NS - S = (N-1)S
\quad\Longrightarrow\quad
S = \frac{\sum_i a_i}{N-1}$$

So one pass to total the $a_i$, one division, then $x_i = S - a_i$ for each. No Gaussian elimination, which on an $N \times N$ system would be $O(N^3)$ and hopeless at $N = 50{,}000$.

Exploiting the **symmetry** — every equation has the same shape — is what collapses the system. The statement's remark that a unique solution always exists for $N > 1$ is explained by the same algebra: the division by $N - 1$ is well defined precisely when $N \geq 2$.

Checking the first sample: $a = [9,6,5]$ sums to $20$, so $S = 20/2 = 10$ and $x = [1, 4, 5]$. Indeed $4+5 = 9$, $1+5 = 6$, $1+4 = 5$.

Two practical notes. The $a_i$ reach $5 \times 10^{12}$ and there may be $50{,}000$ of them, so the total needs **64-bit** arithmetic outside Python. And the division is guaranteed exact, so integer division is right — using floating point would lose precision at this magnitude.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        # Summing all equations counts each variable n - 1 times.
        total = sum(a) // (n - 1)
        out.append(" ".join(str(total - v) for v in a))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/basic-math/EQUALITY.md](../docs/basic-math/EQUALITY.md)
