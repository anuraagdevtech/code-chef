[&larr; 585. Trip](TRIP.md) &middot; [Index](../../README.md) &middot; [587. Girl Friend and String Gift &rarr;](CHGLSTGT.md)

# 586. String Merging

> CodeChef problem code [`STRMRG`](https://www.codechef.com/problems/STRMRG) &middot; difficulty **1965** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Run compression and a bit-parallel longest common subsequence |
| **Time** | $O(N+M+AB/w)$ word operations per test case for compressed lengths $A,B$ |
| **Space** | $O(B/w)$ machine words for a fixed alphabet |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

For a string **S**, let's define a function **F**(**S**) as the minimum number of blocks consisting of consecutive identical characters in **S**. In other words, **F**(**S**) is equal to 1 plus the number of valid indices **i** such that **S_i** ≠ **S_i+1**.

You are given two strings **A** and **B** with lengths **N** and **M** respectively. You should merge these two strings into one string **C** with length **N+M**. Specifically, each character of **C** should come either from **A** or **B**; all characters from **A** should be in the same relative order in **C** as in **A** and all characters from **B** should be in the same relative order in **C** as in **B**.

Compute the minimum possible value of **F**(**C**).

**Input**

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains two space-separated integers **N** and **M**.

- The second line contains a single string **A** with length **N**.

- The third line contains a single string **B** with length **M**.

**Output**

For each test case, print a single line containing one integer — the minimum possible value of **F**(**C**).

**Constraints**

- 1 ≤ **T** ≤ 100

- 1 ≤ **N**, **M** ≤ 5,000

- 1 ≤ sum of **N** in all test cases ≤ 5,000

- 1 ≤ sum of **M** in all test cases ≤ 5,000

- strings **A**, **B** consist only of lowercase English letters

**Subtasks**

**Subtask 1 (10 points):** 1 ≤ **T**, **N**, **M** ≤ 10

**Subtask 2 (20 points):** the characters of **A** and **B** are sorted in non-decreasing order

**Subtask 3 (70 points):** original constraints

## Constraints

- 1 ≤ T ≤ 100
- 1 ≤ N, M ≤ 5,000
- 1 ≤ sum of N in all test cases ≤ 5,000
- 1 ≤ sum of M in all test cases ≤ 5,000
- strings A, B consist only of lowercase English letters

## Sample

**Sample input**

```
1
4 4
abab
baba
```

**Sample output**

```
5
```

<details><summary>Explanation</summary>

**Example case 1:** One possible way to choose the string **C** to get the desired answer is "abbaabba".

</details>

## Approach

Replace each maximal run in both strings by its character. Any merged output's run labels must contain both compressed strings as subsequences. Conversely, a shortest common supersequence of these run labels can be expanded into a valid merge of the original runs. Thus the answer is the shortest common supersequence length, $A+B-LCS$.

Compute the LCS length with a bit-parallel row representation. Build a position bitmask for each character of the second string. A row bit marks where the LCS value rises across that row. For a new character, let `x = row | positions[character]`; the update `x & ~(x - ((row << 1) | 1))` implements the ordinary LCS row transitions through bitwise subtraction and borrow propagation. The number of set row bits is the final LCS length.

## Solution (Python)

```python
import sys
from itertools import groupby


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m = int(next(tokens)),int(next(tokens))
        a = bytes(c for c,_ in groupby(next(tokens)))
        b = bytes(c for c,_ in groupby(next(tokens)))
        if len(a) < len(b):
            a,b = b,a
        positions = {}
        for i,c in enumerate(b):
            positions[c] = positions.get(c,0)|(1 << i)
        row = 0
        for c in a:
            x = row|positions.get(c,0)
            row = x&~(x-((row << 1)|1))
        out.append(str(len(a)+len(b)-row.bit_count()))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N+M+AB/w)$ word operations per test case for compressed lengths $A,B$
- **Space:** $O(B/w)$ machine words for a fixed alphabet
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Compress runs before the LCS calculation.
- Relative order within each original string must be preserved.
- Identical compressed strings need only their own number of runs.
- Python integer operations work over many LCS columns at once.

## Dry run

For `abab` and `baba`, both already have four runs. Their LCS length is three, so the minimum merged run count is `4+4-3=5`.

---

Same problem in rating order (#560 of 735): [../../by-rating/560-STRMRG.md](../../by-rating/560-STRMRG.md)
