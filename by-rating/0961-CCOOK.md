# 961 &middot; Chef and Cook-Off

> CodeChef problem code [`CCOOK`](https://www.codechef.com/problems/CCOOK) &middot; time limit **0.5s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Sum of flags mapped to a label |
| **CodeChef tags** | `Special`, `Basic Programming Concepts`, `Case work`, `Conditional Statements` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per contestant |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/arrays/CCOOK.md](../docs/arrays/CCOOK.md)

## Question

Chef has obtained the results of a past Cook-Off. He wants to estimate the skill level of each contestant. The contestants can be classified [with high probability](https://en.wikipedia.org/wiki/With_high_probability) (w.h.p.) based on the number of solved problems:

- A contestant that solved exactly 0 problems is a beginner.

- A contestant that solved exactly 1 problem is a junior developer.

- A contestant that solved exactly 2 problems is a middle developer.

- A contestant that solved exactly 3 problems is a senior developer.

- A contestant that solved exactly 4 problems is a hacker.

- A contestant that solved all five problems is <a href = "https://www.quora.com/What-are-all-the-Jeff-Dean-facts">Jeff Dean</a>.

Please help Chef to identify the programming level of each participant.

**Input**

- The first line of the input contains a single integer **N** denoting the number of competitors.

- **N** lines follow. The **i**-th of these lines contains five space-separated integers **A_i, 1, A_i, 2, A_i, 3, A_i, 4, A_i, 5**. The **j**-th of these integers (1 ≤ **j** ≤ 5) is 1 if the **i**-th contestant solved the **j**-th problem and 0 otherwise.

**Output**

For each participant, print a single line containing one string denoting Chef's classification of that contestant — one of the strings <tt>"Beginner"</tt>, <tt>"Junior Developer"</tt>, <tt>"Middle Developer"</tt>, <tt>"Senior Developer"</tt>, <tt>"Hacker"</tt>, <tt>"Jeff Dean"</tt> (without quotes).

**Constraints**

- 1 ≤ **N** ≤ 5000

- 0 ≤ **A_i, j** ≤ 1 for each valid **i**, **j**

## Constraints

- 1 ≤ N ≤ 5000
- 0 ≤ A_i, j ≤ 1 for each valid i, j

## Sample

**Sample input**

```
7
0 0 0 0 0
0 1 0 1 0
0 0 1 0 0
1 1 1 1 1
0 1 1 1 0
0 1 1 1 1
1 1 1 1 0
```

**Sample output**

```
Beginner
Middle Developer
Junior Developer
Jeff Dean
Senior Developer
Hacker
Hacker
```

<details><summary>Explanation</summary>

The first contestant has no solved problems, therefore he is a beginner. The second contestant solved 2 problems (the second and fourth problem), therefore he has the skills of a middle developer. The third contestant solved 1 problem, therefore he's at the expected level of a junior developer. The fourth contestant solved 5 problems — we can guess it was Jeff Dean. The fifth contestant solved 3 problems, so he is a senior developer. And the last two contestants should be hackers because they solved exactly 4 problems each.

</details>

## Approach

Each contestant's row is five $0/1$ flags, so the number of problems solved is simply their **sum**. The classification then depends only on that count, which makes a lookup table the natural structure:

$$0 \to \texttt{Beginner},\ 1 \to \texttt{Junior Developer},\ \ldots,\ 5 \to \texttt{Jeff Dean}$$

Indexing a six-element tuple by the sum replaces a six-branch `if`/`elif` ladder with a single expression, and makes it obvious that every count from $0$ to $5$ is covered.

The labels must be reproduced exactly, including the internal spaces in `Junior Developer` and `Jeff Dean`. These are the sort of strings where a typo costs a wrong answer with no hint why.

Note the input shape: there is **no $T$**. The first line is $N$, the number of contestants, and each of the next $N$ lines holds five flags. Every contestant produces one output line.

The samples sweep all six categories, and the last two rows are worth comparing: `0 1 1 1 1` and `1 1 1 1 0` both sum to $4$ and both print `Hacker`, confirming that *which* problems were solved is irrelevant — only how many.

With $N$ up to $5000$ and five values each, reading the whole stream at once and emitting one joined write keeps this comfortably fast.

## Solution (Python)

```python
import sys

LEVELS = ("Beginner", "Junior Developer", "Middle Developer",
          "Senior Developer", "Hacker", "Jeff Dean")


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])          # no test-case count: this is the contestant count
    out = []
    for i in range(n):
        solved = sum(map(int, data[1 + 5 * i:6 + 5 * i]))
        out.append(LEVELS[solved])
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per contestant
- **Space:** $O(1)$
