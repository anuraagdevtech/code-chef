[&larr; 494. Rectangles Counting](RECTCNT.md) &middot; [Index](../../README.md) &middot; [693. ABC-Strings &rarr;](ABCSTR.md)

# 519. IS IT DSU HARD!!

> CodeChef problem code [`CFMAR04`](https://www.codechef.com/problems/CFMAR04) &middot; difficulty **unrated** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Hashing |
| **Technique** | Use letter-frequency tuples as anagram signatures |
| **Time** | $O(\sum |S_i|+26N)$ overall |
| **Space** | $O(26N)$ in the worst case |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

You might hear about  Disjoint Set Union,[click here](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) for more info. Question is, You are given a list of $N$ words (strings containing only lower case English alphabet). Let's say two words are equivalent if one word can be obtained by rearranging the letters of another word. Your task is, form sets equivalent words and print the size of the $largest$ set.

**Input:**
- First-line will contain $N$, the number of words.
- The next $N$ line contains a string.

**Output:**
Output the size of the $largest$ subset of equivalent words.

**Constraints**
- $1 \leq N \leq 10^5$
- $1 \leq |S| \leq 10^5$
- $$
\begin{equation}
\sum_{i=1}^{N}|S|
\leq 10^6 \end{equation}
$$

## Constraints

- $1 \leq N \leq 10^5$
- $1 \leq |S| \leq 10^5$
- $
\begin{equation}
\sum_{i=1}^{N}|S| \leq 10^6
\end{equation}
$

## Sample

**Sample input**

```
4
aaa
aba
aab
aca
```

**Sample output**

```
2
```

## Approach

Two words can be rearranged into each other exactly when all 26 letter frequencies agree. Count words by this frequency tuple and output the largest bucket. This directly models the equivalence classes without constructing pairwise edges or a DSU.

## Solution (Python)

```python
import sys
from collections import Counter


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    n = int(next(tokens))
    counts = Counter()
    for _ in range(n):
        frequency = [0]*26
        for c in next(tokens):
            frequency[c-97] += 1
        counts[tuple(frequency)] += 1
    print(max(counts.values()))

if __name__ == '__main__':
    main()
```

## Complexity

- **Time:** $O(\sum |S_i|+26N)$ overall
- **Space:** $O(26N)$ in the worst case
- Auxiliary space excludes the buffered input and output.

## Edge cases

- There is one test case with a leading word count.
- Repeated identical words belong to the same class.
- Letter order is irrelevant, but multiplicity is essential.

## Dry run

The signatures of `aba` and `aab` are both two `a`s and one `b`; they form the largest sample bucket, of size two.

---

Same problem in rating order (#720 of 735): [../../by-rating/720-CFMAR04.md](../../by-rating/720-CFMAR04.md)
