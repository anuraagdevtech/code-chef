[&larr; 619. Love Squares Hate Cubes](619-SQRTCBRT.md) &middot; [Index](README.md) &middot; [621. SUM OR &rarr;](621-AWESUM_OR.md)

# 620. Lexicographically Largest 

> [`LEXILARGEST`](https://www.codechef.com/problems/LEXILARGEST) &middot; difficulty **2151** &middot; time limit **2s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Largest multiplier coprime to the ratio of consecutive prefix gcds |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log M)$ per test case plus the short downward searches |
| **Space** | $O(N)$ |

## Question

You are given a positive integer $M$ and an array $A \ (1\leq A_i \leq M)$ consisting of $N$ positive integers.

Find the **lexicographically largest** array $B$ such that:
- $|B|=N$;
- $1 \leq B_i \leq M$ for all $1 \leq i \leq N$;
- $A_i = \gcd(B_1, B_2, \ldots, B_i)$, where $\gcd$ denotes the [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor).

Note that the input $A$ guarantees that $B$ always exists.
For two arrays $X$ and $Y$, both of size $N$, the array $X$ is said to be lexicographically larger than array $Y$, if, in the first position where $X$ and $Y$ differ, $X_i \gt Y_i$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space separated integers $N$ and $M$ — the  length of array $A$ and upper bound on array elements.
    - The next line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ representing the array $A$.

**Output**

For each test case, output on a new line, the lexicographically largest array $B$, satisfying the given conditions.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^4$
- $1 \leq M \leq 10^9$
- $1 \leq A_i \leq M$
- The sum of $N$ over all test cases won't exceed $5 \cdot 10^4$.

## Sample

**Sample input**

```
4
1 1
1
2 2
2 1
4 3
2 2 2 2
4 5
2 2 2 2
```

**Sample output**

```
1
2 1
2 2 2 2
2 4 4 4
```

<details><summary>Explanation</summary>

**Test case $1$:** The only possible array is $B = [1]$ which satisfies the given conditions.

**Test case $2$:** The only possible array is $B = [2, 1]$ which satisfies the given conditions.
Here $A_1 = B_1 = 2$, and $A_2 = \gcd(B_1, B_2) = 1$.

**Test case $4$:** The lexicographically largest valid array is $B = [2, 4, 4, 4]$. Some other arrays that are valid include $[2, 2, 2, 2], [2, 2, 4, 2], [2, 2, 4, 4]$.

</details>

## Approach

$B_1 = A_1$ is forced. For $i \ge 2$, $A_i$ must divide $B_i$, so write $B_i = A_i \cdot t$. The condition $\gcd(A_{i-1}, B_i) = A_i$ then becomes

$$\gcd\Bigl(\frac{A_{i-1}}{A_i},\; t\Bigr) = 1.$$

The prefix gcds are given, so the choice of $B_i$ does not influence any later position; each position can be maximised on its own, which also gives the lexicographically largest array. Start from the largest possible multiplier $t = \lfloor M / A_i \rfloor$ and decrease it until it is coprime to the ratio $A_{i-1} / A_i$.

The search is short: $t = 1$ always works, and coprime values are dense - consecutive integers are coprime to each other, so the gaps between admissible $t$ stay small in practice.

## Solution

```python
import sys
from math import gcd


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        m = next(tokens)
        prefix_gcd = [next(tokens) for _ in range(n)]
        result = [prefix_gcd[0]]
        for i in range(1, n):
            ratio = prefix_gcd[i - 1] // prefix_gcd[i]
            multiplier = m // prefix_gcd[i]
            while gcd(multiplier, ratio) != 1:
                multiplier -= 1
            result.append(prefix_gcd[i] * multiplier)
        out.append(' '.join(map(str, result)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- $A_i = A_{i-1}$: the ratio is 1 and the largest multiple of $A_i$ not exceeding $M$ is taken.
- The first element has no freedom at all.
- $t = 1$ (i.e. $B_i = A_i$) is always valid, so the loop terminates.
- The input guarantees $A_i$ divides $A_{i-1}$.

## Dry run

`M = 5, A = [2, 2, 2, 2]`.

$B_1 = 2$. For the other positions the ratio is $2/2 = 1$ and the largest multiplier is $\lfloor 5/2 \rfloor = 2$, coprime to 1, so $B_i = 4$.

Output `2 4 4 4`. With `M = 2, A = [2, 1]`: ratio 2, multiplier starts at 2 (not coprime) and drops to 1, giving `2 1`.

---

Same problem grouped by topic: [../docs/number-theory/LEXILARGEST.md](../docs/number-theory/LEXILARGEST.md)
