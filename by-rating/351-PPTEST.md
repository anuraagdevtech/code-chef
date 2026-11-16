[&larr; 350. Odd Sum](350-ODDSUM.md) &middot; [Index](README.md) &middot; [352. Chef And Adjacent Sums &rarr;](352-CHFADJSUM.md)

# 351. Polo the Penguin and the Test

> [`PPTEST`](https://www.codechef.com/problems/PPTEST) &middot; difficulty **1603** &middot; time limit **1s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | 0-1 knapsack with total test value |
| **Complexity class** | Product of two sizes $O(n m)$ |
| **Time** | $O(NW)$ per test case |
| **Space** | $O(W)$ |

## Question

** Read problems statements in Russian [here](https://www.codechef.com/download/translated/COOK39/russian/PPTEST.pdf)**

Polo, the Penguin, has a lot of tests tomorrow at the university.

He knows that there are **N** different questions that will be on the tests. For each question **i** (**i = 1..N**), he knows **C[i]** - the number of tests that will contain this question, **P[i]** - the number of points that he will get for correctly answering this question on each of tests and **T[i]** - the amount of time (in minutes) that he needs to spend to learn this question.

Unfortunately, the amount of free time that Polo has is limited to **W** minutes. Help him to find the maximal possible total number of points he can get for all tests if he studies for no more than **W** minutes.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows. The first line of each test case contains the pair of integers **N** and **W**, separated by a space. The following **N** lines contain three space-separated integers **C[i]**, **P[i]** and **T[i]** (**i = 1..N**).

**Output**

For each test case, output a single line containing the answer to the corresponding test case.

**Constraints**

- **1** ≤ **T** ≤ **100**

- **1** ≤ **N** ≤ **100**

- **1** ≤ **C[i], P[i], T[i]** ≤ **100**

- **1** ≤ **W** ≤ **100**

## Constraints

- 1 ≤ T ≤ 100
- 1 ≤ N ≤ 100
- 1 ≤ C[i], P[i], T[i] ≤ 100
- 1 ≤ W ≤ 100

## Sample

**Sample input**

```
1
3 7
1 2 3
2 3 5
3 3 3
```

**Sample output**

```
11
```

<details><summary>Explanation</summary>

**Example case 1.** The best choice is to learn the first and the third questions and get **1*2 + 3*3 = 11** points.

</details>

## Approach

Learning question $i$ once earns $C_iP_i$ points across all tests and consumes $T_i$ minutes. This is a 0-1 knapsack item. For every question, update time capacities in descending order, ensuring the question cannot be learned more than once. The capacity-$W$ entry stores the best score achievable within the available time.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,budget = int(next(tokens)),int(next(tokens))
        dp = [0]*(budget+1)
        for _ in range(n):
            count,points,time = (int(next(tokens)) for _ in range(3))
            value = count*points
            for capacity in range(budget,time-1,-1):
                dp[capacity] = max(dp[capacity],dp[capacity-time]+value)
        out.append(str(dp[budget]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- Multiply test count by points per test.
- Skipping every question is allowed.
- Descending capacity updates prevent reusing one question.

## Dry run

The first and third sample questions use six minutes and earn `1*2+3*3=11` points, better than studying only the second question.

---

Same problem grouped by topic: [../docs/dynamic-programming/PPTEST.md](../docs/dynamic-programming/PPTEST.md)
