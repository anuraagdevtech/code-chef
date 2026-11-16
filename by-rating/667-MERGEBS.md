[&larr; 666. Chefs Favourite Function](666-CHEFFFUNC.md) &middot; [Index](README.md) &middot; [668. Red Green Grids &rarr;](668-REDGREEN.md)

# 667. Merging Binary Strings

> [`MERGEBS`](https://www.codechef.com/problems/MERGEBS) &middot; difficulty **2318** &middot; time limit **1.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Merge DP where appending a zero costs the ones already placed |
| **CodeChef tags** | `dynamic-programming` |
| **Complexity class** | Quadratic $O(n^2)$ |
| **Time** | $O(N^2)$ per test case |
| **Space** | $O(N)$ |

## Question

You have two binary strings $A$ and $B$, both of length $N$. You have to merge both the binary strings to form a new binary string $C$ of length $2 \cdot N$. The relative order of characters in the original binary strings $A$ and $B$ should not change in the binary string $C$.

For example, if $A = {\color{blue}01011}$ and $B = {\color{red}10100}$, one possible way to merge them to form $C$ is: $C = {\color{blue}0}{\color{red}1}{\color{red}0}{\color{blue}1}{\color{red}1}{\color{blue}0}{\color{blue}1}{\color{blue}1}{\color{red}0}{\color{red}0}$.

**Minimize** the number of inversions in the merged binary string $C$.

As a reminder, a pair of indices $(i, j)$ is an inversion for binary string $C$ if and only if $1 \leq i \lt j \leq |C|$, $C_i = 1$ and $C_j = 0$.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$ — the length of the binary strings $A$ and $B$.
- The second line of each test case contains the binary string $A$.
- The third line of each test case contains the binary string $B$.

**Output**

For each test case, output a single line containing the **minimum** number of inversions in the merged binary string $C$.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000$
- It is guaranteed that the sum of $N$ over all test cases does not exceed $2000$.
- $|A| = |B| = N$
- $A$ and $B$ are binary strings, i.e, contain only $0$ and $1$.

## Sample

**Sample input**

```
3
4
1010
0101
5
10010
11001
5
00001
11110
```

**Sample output**

```
6
12
4
```

<details><summary>Explanation</summary>

**Test Case $1$:** $A = {\color{blue}1010}$ and $B = {\color{red}0101}$. One optimal $C$ is ${\color{red}0}{\color{blue}1}{\color{blue}0}{\color{red}1}{\color{red}0}{\color{blue}1}{\color{blue}0}{\color{red}1}$. The $6$ inversions in this $C$ are $\{(2, 3), (2, 5), (2, 7), (4, 5), (4, 7), (6, 7)\}$.

**Test Case $2$:** $A = {\color{blue}10010}$ and $B = {\color{red}11001}$. One optimal $C$ is ${\color{blue}1}{\color{blue}0}{\color{blue}0}{\color{red}1}{\color{red}1}{\color{red}0}{\color{red}0}{\color{blue}1}{\color{blue}0}{\color{red}1}$.

**Test Case $3$:** $A = {\color{blue}00001}$ and $B = {\color{red}11110}$. One optimal $C$ is ${\color{blue}0}{\color{blue}0}{\color{blue}0}{\color{blue}0}{\color{red}1}{\color{red}1}{\color{red}1}{\color{red}1}{\color{red}0}{\color{blue}1}$.

</details>

## Approach

An inversion is a `1` placed before a `0`. Build the merged string left to right; the state is how many characters have been taken from each string, $(i, j)$. The number of ones already placed is then known - ones among the first $i$ characters of $A$ plus ones among the first $j$ of $B$ - regardless of the order in which they were merged.

Appending a `1` creates no new inversion. Appending a `0` creates one inversion with every `1` already placed. So

$$\text{cost}(i, j) = \min\bigl(\text{cost}(i-1, j) + w_A,\; \text{cost}(i, j-1) + w_B\bigr),$$

where $w_A$ is the number of ones in the state $(i, j)$ if $A_i$ is `0` (else 0), and similarly for $w_B$; the appended character is a zero, so counting ones "including" it changes nothing. A prefix count of ones in $B$ and a running count for $A$ give the weights in $O(1)$. Only one row of the table is kept.

## Solution

```python
import sys


def solve(tokens):
    n = int(next(tokens))
    first = next(tokens)
    second = next(tokens)
    second_ones = [0]
    for char in second:
        second_ones.append(second_ones[-1] + (char == 49))
    cost = [0] * (n + 1)
    for j in range(1, n + 1):
        cost[j] = cost[j - 1] + (second_ones[j - 1] if second[j - 1] == 48 else 0)
    first_ones = 0
    for char_a in first:
        first_ones += char_a == 49
        cost[0] += first_ones if char_a == 48 else 0
        for j, char_b in enumerate(second, 1):
            cost[j] = min(cost[j] + (first_ones + second_ones[j] if char_a == 48 else 0), cost[j - 1] + (first_ones + second_ones[j - 1] if char_b == 48 else 0))
    return str(cost[n])


if __name__ == "__main__":
    tokens = iter(sys.stdin.buffer.read().split())
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- Inversions inside $A$ and inside $B$ are unavoidable and are included automatically.
- If one string is all zeros it should simply go first, which the DP finds.
- The answer can reach about $N^2$.
- The first row and the first column are the costs of taking characters from one string only.

## Dry run

`A = 00001`, `B = 11110`.

Take the four zeros of $A$ first: no ones are placed yet, cost 0. The final `0` of $B$ has to come after the four ones of $B$, so it costs at least 4; placing the `1` of $A$ after it avoids a fifth inversion.

Merged string `0000 1111 0 1`: answer 4.

---

Same problem grouped by topic: [../docs/dynamic-programming/MERGEBS.md](../docs/dynamic-programming/MERGEBS.md)
