[&larr; 407. Chef and Interesting Subsequences ](CHEFINSQ.md) &middot; [Index](../../README.md) &middot; [441. OR Tuples &rarr;](ORTUPLES.md)

# 416. The Vowel Matrix

> CodeChef problem code [`VOWMTRX`](https://www.codechef.com/problems/VOWMTRX) &middot; difficulty **1694** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Independent cut choices between vowel blocks |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Welcome to The Mega City!

Neo finds himself in a high-stakes situation. He has a string $S$ of length $N$ and his task is to crack the string using the *vowel matrix*.
The vowel matrix is a unique cryptographic scheme where the string is sliced into multiple pieces, such that, each piece contains **exactly** $K$ vowels.

Determine the number of ways you can slice the string $S$ using *vowel matrix* scheme. Since the number can be huge, print it modulo $10^9+7$.

Note:
- The characters `a`, `e`, `i`, `o`, and `u` are considered vowels in lowercase english alphabets.
- It is **guaranteed** that $S$ contains at least one vowel and the number of vowels in $S$ is a multiple of $K$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $K$, the length of string and the number of vowels required in each piece of string.
    - The second line contains the string $S$, consisting of lowercase english letters.

**Output**

For each test case, output on a single line, the number of ways you can slice the string $S$ using *vowel matrix* scheme. Since the number can be huge, print it modulo $10^9+7$.

## Constraints

- $1 \leq T \leq 10^{4}$
- $1 \leq N \leq 10^{6}$
- $1 \leq K \leq N$
- The sum of $N$ over all test cases won't exceed $10^{6}$.
- It is guaranteed that the number of vowels in $S$ is a multiple of $K$.

## Sample

**Sample input**

```
2 
3 1
neo
10 2
babylonian
```

**Sample output**

```
1
2
```

<details><summary>Explanation</summary>

**Test case $1$:** There is only one possible way to slice the string such that all pieces have $1$ vowel each:
- `ne` $|$ `o`.

**Test case $2$:** There are two possible ways to slice the string such that all pieces have $2$ vowels each:
- `babylo` $|$ `nian`
- `babylon` $|$ `ian`

</details>

## Approach

Every piece holds exactly $K$ vowels, so with $m$ vowels in total there are exactly $m/K$ pieces and the cuts are **forced in position relative to the vowels**: the $j$-th cut must fall after vowel $jK$ and before vowel $jK+1$, for $j = 1, \ldots, m/K - 1$.

What is *not* forced is where among the consonants in between. If those two vowels sit at indices $v_{jK}$ and $v_{jK+1}$, the cut may go in any of the gaps strictly after the first and up to the second, giving $v_{jK+1} - v_{jK}$ placements. The cuts are independent — each lies in its own stretch — so the count multiplies:

$$\text{answer} = \prod_{j=1}^{m/K - 1} \bigl(v_{jK+1} - v_{jK}\bigr) \pmod{10^9+7}$$

Note there are $m/K - 1$ factors, not $m/K$: the final piece ends at the string's end, which is not a choice. Leading and trailing consonants likewise contribute nothing, since they must attach to the first and last piece.

The guarantee that $K$ divides $m$ is what makes the product well defined; otherwise the answer would be $0$.

For `neo` with $K = 1$ the two vowels are adjacent (indices $1$ and $2$), so the single cut has one placement: the answer is $1$. For `babylonian` with $K = 2$ the cut must separate the second vowel `o` (index $5$) from the third, `i` (index $7$), and the consonant `n` between them gives two placements — `babylon|ian` and `babylo|nian` — so the answer is $2$.

## Solution (Python)

```python
import sys

MOD = 1_000_000_007
VOWELS = frozenset(b"aeiou")


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        k = int(data[2 + 3 * i])
        s = data[3 + 3 * i]
        spots = [j for j, c in enumerate(s) if c in VOWELS]
        ways = 1
        # One cut per vowel block boundary; it may sit anywhere between them.
        for j in range(k, len(spots), k):
            ways = ways * (spots[j] - spots[j - 1]) % MOD
        out.append(str(ways))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **Only the cut positions between consecutive vowel blocks are free.** A piece must hold exactly $K$ vowels, so the cut after the $j$-th block may sit anywhere strictly between the $jK$-th vowel and the $(jK+1)$-th — giving as many choices as the index gap between them.
- **The choices are independent**, so the answer is the product of those gaps.
- **Consonants between two vowels widen the gap**, and consonants at the very ends contribute nothing — they are glued to the first or last piece whatever happens.
- **One block means no cuts**, so the answer is $1$ — the first sample row, where $K = 1$ and the two vowels sit adjacent, also gives a gap of $1$.
- **The vowel count is guaranteed to be a multiple of $K$**, so the blocks divide evenly and no leftover case arises.
- **The loop starts at $j = K$ and steps by $K$**, which visits exactly the block boundaries and skips the final block (there is no cut after the last piece).
- **Sum of $N \leq 10^6$**, so the vowel positions are collected in one pass and the product is taken modulo $10^9+7$.

## Dry run

Second sample: $S = $ `babylonian` with $K = 2$. Vowels sit at indices $1$ (`a`), $5$ (`o`), $7$ (`i`), $8$ (`a`).

| block | vowels | boundary |
|---:|---|---|
| 1 | indices $1, 5$ | cut after vowel 2 |
| 2 | indices $7, 8$ | — (last block) |

The single cut may fall anywhere between index $5$ and index $7$, which is $7 - 5 = 2$ positions. Output `2`.

---

Same problem in rating order (#404 of 486): [../../by-rating/404-VOWMTRX.md](../../by-rating/404-VOWMTRX.md)
