[&larr; 164. Programming Languages](PROGLANG.md) &middot; [Index](../../README.md) &middot; [182. Nobel Prize &rarr;](NOBEL.md)

# 177. ICPC Balloons

> CodeChef problem code [`BALLOON`](https://www.codechef.com/problems/BALLOON) &middot; difficulty **1205** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Sets |
| **Technique** | Smallest prefix covering a required set |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

Chef is participating in an ICPC regional contest, in which there is a total of $N$ problems (numbered $1$ through $N$) with varying difficulties. For each valid $i$, the $i$-th easiest problem is problem $A_i$.

After a team solves a problem, a balloon with a colour representing that problem is tied next to their desk. Chef is fond of colours in **VIBGYOR**, which are representative of the problems with numbers $1$ through $7$. The remaining problems have their own representative colours too.

Find the minimum number of problems which Chef's team needs to solve in order to get all the balloons for problems $1$ through $7$ (and possibly some other balloons too) tied next to their desk, if you know that Chef's team knows the difficulties of all problems and solves the problems in increasing order of difficulty.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

**Output**
For each test case, print a single line containing one integer ― the minimum number of problems Chef's team needs to solve.

**Constraints**
- $1 \leq T \leq 10,500$
- $7 \leq N \leq 15$
- $1 \leq A_i \leq N$ for each valid $i$
- $A_1, A_2, \ldots, A_N$ are pairwise distinct

## Constraints

- $1 \leq T \leq 10,500$
- $7 \leq N \leq 15$
- $1 \leq A_i \leq N$ for each valid $i$
- $A_1, A_2, \ldots, A_N$ are pairwise distinct

## Sample

**Sample input**

```
3
7
1 2 3 4 5 7 6
8
8 7 6 5 4 3 2 1
9
7 4 3 5 6 1 8 2 9
```

**Sample output**

```
7
8
8
```

<details><summary>Explanation</summary>

**Example case 1:** Since there are a total of $7$ problems, Chef's team will have to solve all of them.

**Example case 2:** Problems $1$ through $7$ appear among the first $8$ problems.

**Example case 3:** Problems $1$ through $7$ again appear among the first $8$ problems.

</details>

## Approach

The team solves problems in increasing order of difficulty, and $A$ already lists the problems in that order — $A_1$ is the easiest. So the problems solved after $m$ attempts are exactly $A_1, \ldots, A_m$, a **prefix** of the array.

The balloons wanted are those for problems $1$ through $7$, so the answer is the length of the shortest prefix containing all seven:

$$\min \{\, m : \{1,\ldots,7\} \subseteq \{A_1, \ldots, A_m\} \,\}$$

Scanning left to right and tracking how many of the seven have appeared gives this in one pass, stopping as soon as the count reaches $7$.

The ordering is the point. The team cannot cherry-pick the seven problems it wants — it must work through the difficulty order, picking up unwanted balloons along the way. So the answer is governed by the **latest position** among problems $1$ to $7$, not by the number of them.

Sample case 2 shows this starkly: the problems arrive in descending order, so problem $1$ is last at position $8$, and the team must solve all $8$ problems to collect $7$ balloons. Sample case 1 is the lucky case where the seven arrive first, giving exactly $7$ — which is also the minimum possible answer, since seven balloons need at least seven solves.

Sample case 3 needs $8$: problem $2$ does not appear until position $8$, even though problem $8$ was picked up at position $7$ as a side effect.

The constraint $N \geq 7$ with distinct values in $[1, N]$ guarantees all seven are present, so the scan always terminates.

## Solution (Python)

```python
import sys

NEEDED = frozenset(range(1, 8))     # the VIBGYOR balloons, problems 1..7


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        # Problems are solved in the given order, so the answer is the
        # position at which the last of 1..7 finally shows up.
        seen = set()
        answer = n
        for idx, v in enumerate(a, 1):
            x = int(v)
            if x in NEEDED:
                seen.add(x)
                if len(seen) == 7:
                    answer = idx
                    break
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Problems numbered above $7$ are irrelevant and must not advance the count.** The second and third rows both contain an $8$, and the third also a $9$; counting them as progress gives the wrong index.
- **The answer can be $N$** (the first row, where the last of the seven arrives on the final problem).
- **All of $1, \dots, 7$ are guaranteed present**, because $N \geq 7$ and the $A_i$ are distinct values in $[1, N]$ — so the loop always finds the seventh and the fallback `answer = n` is a formality.
- **Duplicates are impossible**, so each needed problem is counted exactly once and the set never re-adds.
- **$T$ up to $10{,}500$** with $N \leq 15$: the work is dominated by reading input, so the scan should break as soon as the seventh is seen.

## Dry run

Third sample: $7, 4, 3, 5, 6, 1, 8, 2, 9$.

| position | problem | needed? | distinct needed seen |
|---:|---:|:---:|---:|
| 1 | 7 | yes | 1 |
| 2 | 4 | yes | 2 |
| 3 | 3 | yes | 3 |
| 4 | 5 | yes | 4 |
| 5 | 6 | yes | 5 |
| 6 | 1 | yes | 6 |
| 7 | 8 | **no** | 6 |
| 8 | 2 | yes | **7** |

Output `8`. Problem $8$ at position $7$ contributes nothing.

---

Same problem in rating order (#180 of 486): [../../by-rating/180-BALLOON.md](../../by-rating/180-BALLOON.md)
