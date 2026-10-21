# 167. Devu and friendship testing

> [`CFRTEST`](https://www.codechef.com/problems/CFRTEST) &middot; difficulty **1061** &middot; time limit **1.5s** &middot; Level up from 1* to 2* (Level 2)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Sets |
| **Technique** | Distinct values as a capacity bound |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(n)$ per test case |
| **Space** | $O(n)$ |

## Question

Devu has **n** weird friends. Its his birthday today, so they thought that this is the best occasion for testing their friendship with him. They put up conditions before Devu that they will break the friendship unless he gives them a grand party on their chosen day. Formally, **i**^th friend will break his friendship if he does not receive a grand party on **d_i**^th day.

Devu despite being as rich as Gatsby, is quite frugal and can give at most one grand party daily. Also, he wants to invite only one person in a party. So he just wonders what is the maximum number of friendships he can save. Please help Devu in this tough task !!

**Input**

- The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

- First line will contain a single integer denoting **n**.
- Second line will contain **n** space separated integers where **i**^th integer corresponds to the day **d_i**^th as given in the problem.

**Output**

Print a single line corresponding to the answer of the problem.

**Constraints**

- **1** ≤ **T** ≤ **10^4**

- **1** ≤ **n** ** ≤ 50**

- **1** ≤ **d_i** **≤ 100**

## Constraints

- 1 ≤ T ≤ 10^4
- 1 ≤ n  ≤ 50
- 1 ≤ d_i ≤ 100

## Sample

**Sample input**

```
2
2
3 2
2
1 1
```

**Sample output**

```
2
1
```

<details><summary>Explanation</summary>

**Example case 1.** Devu can give party to second friend on day 2 and first friend on day 3, so he can save both his friendships.

**Example case 2.** Both the friends want a party on day 1, and as the Devu can not afford more than one party a day, so he can save only one of the friendships, so answer is 1.

</details>

## Approach

Devu can host one party per day, with one guest each. Friend $i$ is satisfied only by a party on day $d_i$. So two friends demanding the **same** day are in direct conflict — only one of them can be saved.

Conversely, friends demanding different days never conflict, since each day hosts its own party. So the maximum number of friendships saved is exactly the number of **distinct** days requested:

$$\bigl|\{d_1, \ldots, d_n\}\bigr|$$

The bound holds in both directions: at most one friend per day can be satisfied, and choosing exactly one friend from each distinct day achieves it. There is nothing to optimise beyond counting.

What makes this easy is that the days are **fixed demands**, not a schedule to arrange. Each friend accepts precisely one day, so there is no matching problem — had friends accepted ranges of days, this would become bipartite matching and be far harder.

Sample case 1 has days $\{3, 2\}$, two distinct, so both friendships survive. Sample case 2 has both friends demanding day $1$, so only one can be saved.

A Python `set` gives the count in one pass. With $d_i \leq 100$ a boolean array of size $101$ would be marginally faster, which matters a little at $T = 10^4$, but $n \leq 50$ keeps the total work small either way.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        # One party per day, so friends sharing a day compete for it.
        days = set(data[pos + 1:pos + 1 + n])
        pos += 1 + n
        out.append(str(len(days)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/sets/CFRTEST.md](../docs/sets/CFRTEST.md)
