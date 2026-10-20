# 237. Maximum Angriness

> CodeChef problem code [`MAXAGRY`](https://www.codechef.com/problems/MAXAGRY) &middot; difficulty **1432** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Maximising inversions with limited swaps |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Alice and Bob were playing a game yet again but this time, Bob already lost the game. Now he wants to take revenge.

Bob saw a jigsaw puzzle which was solved by Alice and decided to jumble the puzzle pieces again. There are $N$ puzzle pieces in a line numbered from $1$ to $N$ in increasing order and he has $K$ minutes before Alice catches him.
Bob can **swap any two pieces** of the puzzle. Each swap takes $1$ minute, and so Bob can make **at most** $K$ swaps.

Let $A_i$ denote the piece in the $i$-th position after Bob finishes making his swaps.

Alice's *angriness* is defined to be the number of pairs $(i, j)$ such that $1 \leq i \lt j \leq N$ and $A_i \gt A_j$.

Bob would like to make Alice as angry as possible, so he asks for your help: if he performs his swaps optimally, what is the **maximum *angriness*** he can achieve?

**Input**

- The first line of input contains an integer $T$, denoting the number of test cases.
- The first and only line of each test case contains two space-separated integers $N$ and $K$: the number of pieces and the number of swaps Bob can make.

**Output**

- For each test case, output on a new line a single integer: Alice's maximum possible angriness.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^{9}$
- $1 \leq K \leq 10^{9}$

## Sample

**Sample input**

```
4
7 3
1 4
8 2
5 3
```

**Sample output**

```
21
0
22
10
```

<details><summary>Explanation</summary>

**Test case $1$:** $N = 7$, so the pieces are initially arranged as $[1, 2, 3, 4, 5, 6, 7]$. Bob can make $K = 3$ swaps. One optimal way of swapping is as follows:
- First, swap $2$ and $6$. Now the pieces are $[1, 6, 3, 4, 5, 2, 7]$
- Next, swap $1$ and $7$. Now the pieces are $[7, 6, 3, 4, 5, 2, 1]$
- Finally, swap $3$ and $5$. Now the pieces are $[7, 6, 5, 4, 3, 2, 1]$

The angriness of this sequence is $21$, which is the maximum possible.

**Test case $2$:** $N = 1$, so no swaps can be made. The answer is always $0$.

</details>

## Approach

The pieces start sorted, so there are no inversions. The absolute maximum is the fully reversed order with $\binom{N}{2}$ inversions, and reversing takes $\lfloor N/2 \rfloor$ swaps — each one exchanging a symmetric pair $(i,\ N+1-i)$.

With only $K$ swaps, use $k = \min(K, \lfloor N/2 \rfloor)$ of them, and spend each on the **outermost remaining pair**, since the wider the swap the more inversions it creates. Exchanging positions $i$ and $N+1-i$ in an otherwise sorted array creates

$$2\,(N - 2i + 1) - 1$$

inversions: the two moved values now invert against each of the $N - 2i$ elements between them, twice over, plus the pair itself.

Summing over $i = 1 \ldots k$ collapses to a closed form:

$$k\,(2N + 1) - 2k(k+1)$$

which is essential — with $N$ and $K$ up to $10^9$ and $T$ up to $10^5$, no loop over swaps is affordable.

The clamp at $\lfloor N/2 \rfloor$ matters. Extra swaps beyond a full reversal cannot help, since $\binom{N}{2}$ is the ceiling. Sample case 1, $N = 7$ with $K = 3$, uses exactly $\lfloor 7/2 \rfloor = 3$ swaps and reaches the maximum $21$. Sample case 4 has $K = 3$ but only $\lfloor 5/2 \rfloor = 2$ useful swaps, giving $10$ rather than the full $\binom{5}{2} = 10$ — which happens to coincide, since two swaps already reverse a five-element array.

Sample case 2 is the degenerate one: a single piece admits no swaps at all, so the answer is $0$ despite $K = 4$.

The result reaches roughly $5 \times 10^{17}$, so this needs **64-bit arithmetic** outside Python.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Swaps beyond a full reversal cannot add anything.
        k = min(k, n // 2)
        # Sum over i of 2(n - 2i + 1) - 1, in closed form.
        out.append(str(k * (2 * n + 1) - 2 * k * (k + 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Algorithms`
