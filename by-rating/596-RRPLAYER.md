[&larr; 595. Parity Permutation](595-PARPER.md) &middot; [Index](README.md) &middot; [597. Angry Cyborg &rarr;](597-AGCY.md)

# 596. Player

> [`RRPLAYER`](https://www.codechef.com/problems/RRPLAYER) &middot; difficulty **2067** &middot; time limit **1s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Probability |
| **Technique** | Coupon collector - a sum of geometric waiting times |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(\max N + T)$ |
| **Space** | $O(\max N)$ |

## Question

Petr, Nikita G. and Nikita are the most influential music critics in Saint-Petersburg. They have recently downloaded their favorite band's new album and going to listen to it. Nikita claims that the songs of entire album should be listened strictly in the same order as they are given, because there is the secret message from the author in the songs' order. Petr, being chaotic, does not think so, hence he loves listening to songs in a random order. Petr is pretty good in convincing other people, so after a two-hours discussion Nikita accepted listening in random order(the discussion's duration was like three times longer thatn the album's one). In this context random order means following: There are **N** songs in the album. In the very beginning random song is chosen(here and further "random song" means that every song has equal probability to be chosen). After some song is over the next one is chosen randomly and independently of what have been played before.

Nikita G., being the only one who is not going to drop out from the university, wonders, what is the expected number of songs guys have to listen to until every song is played at least once.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first and only line of each test case contains a single integer **N** denoting the number of songs in the album.

**Output**

For each test case, output a single line containing the expected number of songs the guys will listen to. Your answer will be considered as correct if it has an absolute or relative error less than **10^−1**. More formally if the expected output is **A** and your output is **B**, your output will be considered as correct if and only if
**|A − B| ≤ 10^−1 * max{|A|, |B|, 1}**.

**Constraints**

**1** ≤ **T** ≤ ** 100 **
**1** ≤ **N** ≤ ** 3000 **

## Constraints

- 1 ≤ T ≤  100
- 1 ≤ N ≤  3000

## Sample

**Sample input**

```
3
1
2
3
```

**Sample output**

```
1.0
3.0
5.5
```

<details><summary>Explanation</summary>

**Example case 2** After playing the first song there is **1/2** chance to finish the album each time new song is played. So the expected number of songs is **2/2 + 3/4 + 4/8... = 3**

</details>

## Approach

This is the coupon collector problem. Once $k$ distinct songs have been heard, each new play is an unheard song with probability $(N - k) / N$, so the expected number of plays until the next new song is $N / (N - k)$.

By linearity of expectation the total is

$$\sum_{k=0}^{N-1} \frac{N}{N-k} = N \cdot H_N,$$

with $H_N$ the $N$-th harmonic number. Precompute the harmonic numbers up to the largest query.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    queries = [next(tokens) for _ in range(next(tokens))]
    harmonic = [0.0] * (max(queries, default=0) + 1)
    for i in range(1, len(harmonic)):
        harmonic[i] = harmonic[i - 1] + 1 / i
    print('\n'.join(('%.10f' % (n * harmonic[n]) for n in queries)))


if __name__ == "__main__":
    main()
```

## Edge cases

- $N = 1$: the first song finishes the album, answer 1.
- The first play is always new - the $k = 0$ term is exactly 1.
- Floating-point harmonic sums are accurate far beyond the required tolerance for the given limits.
- All queries share one prefix table.

## Dry run

`N = 3`: waiting times $3/3 + 3/2 + 3/1 = 1 + 1.5 + 3 = 5.5$.

`N = 2`: $2/2 + 2/1 = 3$.

---

Same problem grouped by topic: [../docs/probability/RRPLAYER.md](../docs/probability/RRPLAYER.md)
