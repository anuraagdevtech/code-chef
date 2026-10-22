[&larr; 449. Minimum Coloring](MINCOLOR.md) &middot; [Index](../../README.md)

# 478. Same Parity Swaps in Binary Strings

> CodeChef problem code [`MAX01EVSWP`](https://www.codechef.com/problems/MAX01EVSWP) &middot; difficulty **1747** &middot; time limit **8s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Matching on a path, with a parity-forced shortfall |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You are given a binary string $S$ of length $N$ (i.e. every character of $S$ is either $0$ or $1$).

You can perform the following operation on $S$:
- select any two indices $i, j$ of the same parity, i.e. either both $i, j$ are odd or both $i, j$ are even
- swap $S_i$ and $S_j$

For example, in the string $1110$, we can swap the second and the fourth characters to get $1011$. However, we can never obtain $1101$ from $1110$ by performing such swaps.

Find the maximum possible number of occurrences of the string $01$ as a [substring](https://en.wikipedia.org/wiki/Substring) of $S$ after performing the above operation any number of times (it is also allowed to not perform any operation).

For example, the string $1110$ has no occurrence of the string $01$ as a substring, whereas we can swap the second and fourth characters to obtain $1{\color{red}{01}}1$ which has exactly one occurrence of $01$ (colored red).

**Input**

- The first line of input contains an integer $T$, denoting the number of testcases. The description of the $T$ testcases follow.
- Each testcase consists of two lines.
- The first line contains a single integer $N$, the length of the string $S$.
- The second line contains a binary string of length $N$.

**Output**

- For each testcase, print in a single line, an integer — the answer as per the problem statement.

## Constraints

- $1 \leq T \leq 4000$
- $1 \leq |S| \leq 10^5$
- The sum of $|S|$ over all testcases doesn't exceed $10^5$

**Subtasks**

**Subtask #1 (100 points):** Original constraints

## Sample

**Sample input**

```
3
5
00100
5
01010
5
10001
```

**Sample output**

```
1
2
2
```

<details><summary>Explanation</summary>

**Test case $1$:** The only strings that can be obtained by performing the given operations are $\{10000, 00100, 00001\}$. Of these the two strings $0{\color{red}{01}}00$ and $000{\color{red}{01}}$ contain exactly one occurrence of $01$.

**Test case $2$:** The given string $S$ cannot be changed by performing the given operation and contains $2$ occurrences of the string $01$, i.e. ${\color{red}01}{\color{blue}01}0$.

**Test case $3$:** The only strings that can be obtained by performing the given operations are $\{00101, 10001, 10100\}$. The string $0{\color{red}{01}}{\color{blue}{01}}$ contains two occurrences of $01$.

</details>

## Approach

Same-parity swaps let the odd positions be permuted freely among themselves, and likewise the even ones. So the only data that matters is four counts: $o_A, z_A$ ones and zeros on odd positions, and $o_B, z_B$ on even positions.

Occurrences of `01` are automatically **disjoint** — two of them cannot share a character, since the shared position would have to be both `1` and `0`. So they form a matching on the path of adjacent position pairs, where each edge joins one odd and one even position. An edge of **type A** (odd, even) needs a zero on the odd side and a one on the even side; **type B** (even, odd) needs the reverse. With $x$ type-A and $y$ type-B edges,

$$x \leq X := \min(z_A, o_B), \qquad y \leq Y := \min(z_B, o_A), \qquad x + y \leq \lfloor N/2 \rfloor$$

The last bound is the maximum matching of the path. For **odd** $N$ the path has an odd number of vertices and every split of the maximum size is realisable, so the answer is $\min(X + Y, \lfloor N/2 \rfloor)$.

For **even** $N$ the path has $N$ vertices and its perfect matching is **unique** — all type A. So the maximum $\lfloor N/2 \rfloor$ is reachable only when $X \geq N/2$, which forces every odd position to hold `0` and every even one `1`, i.e. the string $0101\ldots01$. Otherwise one occurrence is lost:

$$\text{answer} = \begin{cases} \lfloor N/2 \rfloor & N \text{ odd, or } X \geq N/2 \\ \min(X+Y,\ N/2 - 1) & \text{otherwise}\end{cases}$$

capped by $X+Y$ throughout. That shortfall is the whole subtlety, and a brute force over all strings up to length $14$ confirms the formula exactly.

The samples are all $N = 5$, hence odd: `00100` has $X = 0, Y = 1$ for $1$; `01010` has $X = 2$ for $2$; and `10001` has $Y = 2$ for $2$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + 2 * i])
        s = data[2 + 2 * i]
        odd_ones = sum(1 for j in range(0, n, 2) if s[j] == 0x31)
        even_ones = sum(1 for j in range(1, n, 2) if s[j] == 0x31)
        odd_zeros = (n + 1) // 2 - odd_ones
        even_zeros = n // 2 - even_ones
        # Type A edges pair an odd zero with an even one; type B the reverse.
        a = min(odd_zeros, even_ones)
        b = min(even_zeros, odd_ones)
        half = n // 2
        if n % 2 == 0 and a < half:
            # The path's perfect matching is unique and all type A.
            out.append(str(min(a + b, half - 1)))
        else:
            out.append(str(min(a + b, half)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Same-parity swaps mean the two parity classes are separate multisets**, so only four counts matter: zeros and ones at odd positions, and the same at even positions.
- **Each `01` occurrence needs a zero immediately before a one**, so it uses one position of each parity — giving two edge types, odd-zero beside even-one and even-zero beside odd-one.
- **The answer is capped at $\lfloor N/2 \rfloor$**, the number of disjoint adjacent pairs available in a string of length $N$.
- **An even $N$ has a unique perfect matching on the path, and it is all one type** — so when the type-A supply falls short of $\lfloor N/2 \rfloor$, the maximum drops to $\lfloor N/2 \rfloor - 1$ rather than simply $A + B$. That asymmetry is the whole subtlety, and it was verified exhaustively up to $N = 14$ with no mismatch.
- **An odd $N$ has slack**, so the plain $\min(A + B,\, \lfloor N/2 \rfloor)$ applies — all three samples are odd-length.
- **An all-zero or all-one string** gives $0$, since one of the two counts in every product is zero.
- **Sum of $|S| \leq 10^5$**, so the four counts come from one strided pass.

## Dry run

Third sample: $S = $ `10001` with $N = 5$.

| class | zeros | ones |
|---|---:|---:|
| odd positions ($1,3,5$) | 1 | 2 |
| even positions ($2,4$) | 2 | 0 |

| edge type | supply |
|---|---:|
| A: odd zero beside even one | $\min(1, 0) = 0$ |
| B: even zero beside odd one | $\min(2, 2) = 2$ |

$N$ is odd, so the answer is $\min(0 + 2,\, \lfloor 5/2 \rfloor) = $ `2` — for instance `00101`, which contains `01` twice.

> CodeChef tags: `Data Structures`

---

Same problem in rating order (#450 of 486): [../../by-rating/450-MAX01EVSWP.md](../../by-rating/450-MAX01EVSWP.md)
