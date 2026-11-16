[&larr; 552. Byteknights and Byteknaves](552-BYTEISLE.md) &middot; [Index](README.md) &middot; [554. Appy Loves One &rarr;](554-HMAPPY1.md)

# 553. Chef and Strings

> [`STRQ`](https://www.codechef.com/problems/STRQ) &middot; difficulty **1930** &middot; time limit **2s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Prefix counts of ordered character pairs, corrected for starts before L |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(16 \cdot N + Q)$ |
| **Space** | $O(N + Q)$ |

## Question

Chef likes strings a lot but moreover he likes good strings. Chef calls a string **str** a good string if **str** starts and ends at different characters. For eg : strings such as **abab** , **baccba** , **abc** are all good strings whereas strings like **aba**, **baab** , **baacaab** are not good at all .

Today, Chef has a special string **P** consisting of lower case letters **"c"** , **"h"** , **"e"** and **"f"** only. Chef wants to make some queries about his string **P**.

Each of chef's query has the following form **a b L R**. For a given query, Chef wants to count the number of good strings which starts at letter **a** and ends at letter **b** such that starting index **S_i** and ending index **E_i** of a chosen substring satisfies **L <= S_i < E_i <= R**.

**NOTE**

Two substrings **P_1** and **P_2** are considered to be different if either **S_1 != S_2** or **E_1 != E_2** where **S_1,E_1** and **S_2,E_2** are the starting and ending index of string **P_1** and string **P_2** respectively.

Chef is not able to accomplish this task efficiently. Can you help him ?

**Input**

First line of the input contains a string **P** denoting the chef's special string. Next line of the input contains a single integer **Q** denoting the number of chef's queries. Next **Q** lines of the input contains **four** space separated parameters where the first **two** parameters are characters denoting **a** and **b** respectively and rest **two** are integers denoting **L** and **R** respectively.

**Output**

For each chef's query, print the required answer.

**Constraints**

- **1 <= |P| <= 10^6**

- **1 <= Q <= 10^6**

- **1 <= L <= R <= |P|**

- **P,a,b** belongs to the set of lower case letters **[c,h,e,f] and a != b**.

- **All test files are strictly according to constraints.**

**Subtasks**

-  Subtask #1: **1<=|P|,Q<=10^4 : 27 pts**

-  Subtask #2: **1<=|P|,Q<=10^5 : 25 pts**

-  Subtask #3: **1<=|P|,Q<=10^6 : 48 pts**

**Warning**

Large test data set, Prefer to use faster input/output methods .

## Constraints

- 1 <= |P| <= 10^6
- 1 <= Q <= 10^6
- 1 <= L <= R <= |P|
- P,a,b belongs to the set of lower case letters [c,h,e,f] and a != b.
- All test files are strictly according to constraints.

## Sample

**Sample input**

```
checfcheff
5
c h 1 10
c f 1 10
e c 1 10
c f 1 5
c f 6 10
```

**Sample output**

```
4
8
2
2
2
```

<details><summary>Explanation</summary>

- Q1 : good strings are **ch** , **checfch** , **cfch** , **ch**

- Q2 : good strings are **checf** , **checfchef** , **checfcheff** , **cf** , **cfchef** , **cfcheff** , **chef** , **cheff**

</details>

## Approach

For a query $(a, b, L, R)$ with $a \ne b$ we need the pairs of positions $L \le s < e \le R$ with $P_s = a$ and $P_e = b$.

For a fixed character pair let `prefix[i]` be the number of such pairs with $e \le i$ and no lower bound on $s$; it grows by the number of $a$'s seen so far every time a $b$ is read. Then `prefix[R] - prefix[L-1]` counts pairs with $e \in [L, R]$ but still allows $s < L$. Those unwanted pairs are exactly (an $a$ before $L$) times (a $b$ inside $[L, R]$), so

$$\text{answer} = \text{prefix}[R] - \text{prefix}[L-1] - \text{cntA}[L-1] \cdot (\text{cntB}[R] - \text{cntB}[L-1]).$$

There are at most 12 useful pairs. Queries are grouped by pair and each pair's prefix array is built once, so memory stays linear even with a million queries.

## Solution

```python
import sys
from array import array


def main() -> None:
    read = sys.stdin.buffer.readline
    text = read().strip()
    q = int(read())
    by_pair = {}
    for i in range(q):
        a, b, l, r = read().split()
        by_pair.setdefault((a[0], b[0]), array('I')).extend((i, int(l) - 1, int(r)))
    chars = sorted(set(text))
    counts = {c: array('I', [0]) for c in chars}
    for ch in text:
        for c in chars:
            counts[c].append(counts[c][-1] + (c == ch))
    answers = array('Q', [0]) * q
    for (a, b), group in by_pair.items():
        if a not in counts or b not in counts:
            continue
        prefix = array('Q', [0])
        count_a = counts[a]
        count_b = counts[b]
        total = 0
        for i, ch in enumerate(text):
            if ch == b:
                total += count_a[i]
            prefix.append(total)
        for j in range(0, len(group), 3):
            i, l, r = group[j:j + 3]
            answers[i] = prefix[r] - prefix[l] - count_a[l] * (count_b[r] - count_b[l])
    for start in range(0, q, 8192):
        sys.stdout.write('\n'.join(map(str, answers[start:start + 8192])) + '\n')


if __name__ == "__main__":
    main()
```

## Edge cases

- The statement guarantees $a \ne b$; a character that never occurs in the string gives 0.
- Counts reach about $N^2 / 4$, beyond 32 bits - 64-bit arrays are used.
- Output is written in chunks to keep the peak memory bounded.
- $L$ is converted to a 0-based prefix index once, when the query is read.

## Dry run

`P = checfcheff`, query `c h 1 10`.

`c` occurs at positions 1, 4, 6 and `h` at 2, 7. Reading the string, the `h` at 2 has one `c` before it and the `h` at 7 has three, so `prefix[10] = 4`. With $L = 1$ nothing lies before the range, so the correction is 0.

Answer 4: `ch`, `checfch`, `cfch`, `ch`.

---

Same problem grouped by topic: [../docs/prefix-sums/STRQ.md](../docs/prefix-sums/STRQ.md)
