# 164. Programming Languages

> [`PROGLANG`](https://www.codechef.com/problems/PROGLANG) &middot; difficulty **1001** &middot; time limit **0.5s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Sets |
| **Technique** | Subset containment |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef is a software developer, so he has to switch between different languages sometimes. Each programming language has some features, which are represented by integers here.

Currently, Chef has to use a language with two given features $A$ and $B$. He has two options --- switching to a language with two features $A_1$ and $B_1$, or to a language with two features $A_2$ and $B_2$. All four features of these two languages are pairwise distinct.

Tell Chef whether he can use the first language, the second language or neither of these languages (if no single language has all the required features).

**Input**

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains six space-separated integers $A, B, A_1, B_1, A_2, B_2$.

**Output**

For each test case, print a single line containing the integer $1$ if Chef should switch to the first language, or $2$ if Chef should switch to the second language, or $0$ if Chef cannot switch to either language.

## Constraints

- $1 \leq T \leq 288$
- $1 \leq A, B, A_1, B_1, A_2, B_2 \leq 4$
- $A, B$ are distinct
- $A_1, B_1, A_2, B_2$ are pairwise distinct

**Subtasks**

**Subtask #1 (100 points):** original constraints

## Sample

**Sample input**

```
3
1 2 2 1 3 4
3 4 2 1 4 3
1 2 1 3 2 4
```

**Sample output**

```
1
2
0
```

<details><summary>Explanation</summary>

**Example case 1:** The first language has the required features --- features $1$ and $2$.

**Example case 2:** The second language has the required features --- features $3$ and $4$.

**Example case 3:** Neither language has both features $1$ and $2$.

</details>

## Approach

Chef needs a language providing **both** features $A$ and $B$. Each candidate language offers exactly two features, so the test is whether the required pair is contained in the offered pair:

$$\{A, B\} \subseteq \{A_1, B_1\} \quad\text{or}\quad \{A, B\} \subseteq \{A_2, B_2\}$$

Since both sides have exactly two distinct elements, containment here is the same as set equality — but writing it as `<=` (subset) states the requirement directly and would still be right if a language offered more features.

Using sets removes the ordering question entirely, which is the main trap. The features may be listed in either order, so a positional comparison of $A$ against $A_1$ and $B$ against $B_1$ fails. Sample case 1 is built on that: the required $\{1, 2\}$ is offered as $A_1 = 2, B_1 = 1$ — the same pair, reversed — and the answer is $1$.

The first language is checked first, which matters only if both qualified; the constraint that $A_1, B_1, A_2, B_2$ are **pairwise distinct** means the two languages share no feature at all, so at most one can ever match and the order is immaterial.

Sample case 3 is the zero case: $\{1,2\}$ is split across the two languages, each holding one required feature, so neither suffices and the answer is $0$. That pairwise-distinct guarantee is precisely what makes such a split possible.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, a1, b1, a2, b2 = map(int, data[1 + 6 * i:7 + 6 * i])
        need = {a, b}
        # Features may be listed in either order, so compare as sets.
        if need <= {a1, b1}:
            out.append("1")
        elif need <= {a2, b2}:
            out.append("2")
        else:
            out.append("0")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Features may be listed in either order**: the first row offers $\{2, 1\}$ against a need of $\{1, 2\}$, so the comparison must be on sets rather than positions.
- **Neither language works** (the third row): the answer is $0$.
- **The two languages share no feature.** Since $A_1, B_1, A_2, B_2$ are pairwise distinct, their feature sets are disjoint, so at most one language can supply both needs — which is why checking the first and then the second with an `elif` cannot mask a valid answer.
- **$A \neq B$ is guaranteed**, so the requirement always has exactly two distinct features.

## Dry run

| needed | language 1 | language 2 | subset of 1? | subset of 2? | output |
|---|---|---|:---:|:---:|---|
| $\{1,2\}$ | $\{2,1\}$ | $\{3,4\}$ | yes | — | `1` |
| $\{3,4\}$ | $\{2,1\}$ | $\{4,3\}$ | no | yes | `2` |
| $\{1,2\}$ | $\{1,3\}$ | $\{2,4\}$ | no | no | `0` |

Row 3 has each needed feature available, but split across the two languages.

---

Same problem grouped by topic: [../docs/sets/PROGLANG.md](../docs/sets/PROGLANG.md)
