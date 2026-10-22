[&larr; 314. Count Distinct Values](CNTDIST.md) &middot; [Index](../../README.md) &middot; [386. Good Pairs &rarr;](GOODPAIRS.md)

# 337. Version Control System

> CodeChef problem code [`VCS`](https://www.codechef.com/problems/VCS) &middot; difficulty **1217** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Sets |
| **Technique** | Intersection and complement of a union |
| **Time** | $O(M + K)$ per test case |
| **Space** | $O(M + K)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

<meta charset="utf8" />

	A *version control system*(VCS) is a repository of files, often the files for the source code of computer programs, with monitored access. Every change made to the source is tracked, along with who made the change, why they made it, and references to problems fixed, or enhancements introduced, by the change.

	Version control systems are essential for any form of distributed, collaborative development. Whether it is the history of a wiki page or large software development project, the ability to track each change as it was made, and to reverse changes when necessary can make all the difference between a well managed and controlled process and an uncontrolled ‘first come, first served’ system. It can also serve as a mechanism for due diligence for software projects.

	In this problem we'll consider a simplified model of a development project. Let's suppose, that there are **N** source files in the project. All the source files are distinct and numbered from 1 to **N**.

	A VCS, that is used for maintaining the project, contains two sequences of source files. The first sequence contains the source files, that are ignored by the VCS. If a source file is not in the first sequence, then it's considered to be unignored. The second sequence contains the source files, that are tracked by the VCS. If a source file is not in the second sequence, then it's considered to be untracked. A source file can either be or not be in any of these two sequences.

	Your task is to calculate two values: the number of source files of the project, that are both tracked and ignored, and the number of source files of the project, that are both untracked and unignored.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of the test case description contains three integers **N**, **M** and **K** denoting the number of source files in the project, the number of ignored source files and the number of tracked source files.

The second line contains **M** distinct integers denoting the sequence **A** of ignored source files. The sequence is strictly increasing.

The third line contains **K** distinct integers denoting the sequence **B** of tracked source files. The sequence is strictly increasing.

**Output**

For each test case, output a single line containing two integers: the number of the source files, that are both tracked and ignored, and the number of the source files, that are both untracked and unignored.

**Constraints**

- 1 ≤ **T** ≤ 100

- 1 ≤ **M**, **K** ≤ **N** ≤ 100

- 1 ≤ **A_1** < **A_2** < ... < **A_M** ≤ **N**

- 1 ≤ **B_1** < **B_2** < ... < **B_K** ≤ **N**

## Constraints

- 1 ≤ T ≤ 100
- 1 ≤ M, K ≤ N ≤ 100
- 1 ≤ A_1 < A_2 < ... < A_M ≤ N
- 1 ≤ B_1 < B_2 < ... < B_K ≤ N

## Sample

**Sample input**

```
2
7 4 6
1 4 6 7
1 2 3 4 6 7
4 2 2
1 4
3 4
```

**Sample output**

```
4 1
1 1
```

<details><summary>Explanation</summary>

In the first test case, the source files {1, 4, 6, 7} are both tracked and ignored, the source file {5} is both untracked and unignored.

	In the second test case, the source file {4} is both tracked and ignored, the source file {2} is both untracked and unignored.

</details>

## Approach

The two sequences are given as **membership lists**, so both questions are set operations once they are loaded into sets. Let $I$ be the ignored files and $T$ the tracked ones.

"Tracked **and** ignored" is the intersection:

$$|T \cap I|$$

"Untracked **and** unignored" means in neither list, which is the complement of the union:

$$N - |T \cup I|$$

The second one is where a careless solution goes wrong: counting $(N - M) + (N - K)$ double-counts, and subtracting $M + K$ from $N$ ignores the overlap. Taking the union first handles it correctly, because a file in both lists must be discounted only once.

Note the two counts are not complementary — the files that are tracked-but-unignored and ignored-but-untracked belong to neither answer. In the first sample $N = 7$ with $I = \{1,4,6,7\}$ and $T = \{1,2,3,4,6,7\}$: the intersection is all of $I$, giving $4$, and the union has size $6$, leaving exactly one file (number $5$) in neither, giving $1$.

Since the input guarantees both sequences are strictly increasing, there are no duplicates to worry about, and the raw tokens can be used as set elements directly without parsing them to integers.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m, k = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        pos += 3
        ignored = set(data[pos:pos + m])
        pos += m
        tracked = set(data[pos:pos + k])
        pos += k
        # Neither list means outside the union -- subtracting M + K would
        # double-count the files that appear in both.
        out.append(f"{len(ignored & tracked)} {n - len(ignored | tracked)}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(M + K)$ per test case
- **Space:** $O(M + K)$

## Edge cases

- **Files in both lists must not be double-counted.** In the second row $M = K = 2$ and $N = 4$, so $N - M - K$ gives $0$, but file $4$ appears in both lists and the true answer is $1$. The union, not the sum, is what must be subtracted.
- **A file can be in neither list**: file $5$ in the first row and files $1$ and $2$ in the second.
- **A file can be in both**, which is what the first number counts — the first row has all four ignored files also tracked.
- **Both lists are strictly increasing**, so neither contains an internal duplicate and the sets can be built straight from the tokens.
- Comparing the raw byte tokens is safe here because the input has no leading zeros, so each number has exactly one spelling.

## Dry run

Second sample: $N = 4$, ignored $\{1, 4\}$, tracked $\{3, 4\}$.

| file | ignored? | tracked? | counted as |
|---:|:---:|:---:|---|
| 1 | yes | no | — |
| 2 | no | no | **untracked and not ignored** |
| 3 | no | yes | — |
| 4 | yes | yes | **both** |

Output `1 1`. Note $N - M - K = 0$ would be wrong, because file $4$ is subtracted twice.

---

Same problem in rating order (#183 of 486): [../../by-rating/183-VCS.md](../../by-rating/183-VCS.md)
