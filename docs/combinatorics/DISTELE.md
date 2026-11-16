[&larr; 484. Bear and AB](ABREPEAT.md) &middot; [Index](../../README.md) &middot; [582. Barcelona Gameplay Tactics &rarr;](FCBARCA.md)

# 492. Distinct Elements

> CodeChef problem code [`DISTELE`](https://www.codechef.com/problems/DISTELE) &middot; difficulty **1762** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Independent choice from each frequency class |
| **Time** | $O(N)$ per test case |
| **Space** | $O(U)$ for $U$ distinct values |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You are given an array $A$ containing $N$ integers. A [subsequence](https://en.wikipedia.org/wiki/Subsequence) of this array is called *good* if all the elements of this subsequence are distinct.

Find the number of *good* non-empty subsequences of $A$. This number can be large, so report it modulo $10^9 + 7$.

Note that two subsequences are considered different if they differ in the indices chosen. For example, in the array $[1, 1]$ there are 3 different non-empty subsequences: $[1]$ (the first element), $[1]$ (the second element) and $[1, 1]$. Out of these three subsequences, the first two are good and the third is not.

**Input**

- The first line contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$, denoting the number of elements in $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

**Output**

For each test case, print a single line containing one integer — the number of good subsequences modulo $10^9 + 7$

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^6$
- The sum of $N$ over all test cases does not exceed $10^6$.

## Sample

**Sample input**

```
2
2
1 1
2
1 2
```

**Sample output**

```
2
3
```

<details><summary>Explanation</summary>

- **Test Case $1$**: Explained in the problem statement.

- **Test Case $2$**: There are 3 non-empty subsequences: $[1]$, $[2]$ and $[1, 2]$. All three subsequences are good.

</details>

## Approach

For a value occurring $f$ times, a good subsequence either skips it or selects exactly one of its $f$ positions. That gives $f+1$ choices. Choices for different values are independent, and their selected indices define exactly one subsequence in original order.

Multiply all $f+1$ values modulo $10^9+7$, then subtract the empty subsequence.

## Solution (Python)

```python
import sys
from collections import Counter


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        freq = Counter(int(next(tokens)) for _ in range(n))
        answer = 1
        for f in freq.values():
            answer = answer * (f+1) % 1000000007
        out.append(str((answer-1) % 1000000007))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(U)$ for $U$ distinct values
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Repeated values represent distinct index choices.
- An all-equal array has exactly $N$ good nonempty subsequences.
- Subtract one modulo the modulus.

## Dry run

For `[1,1]`, the frequency is two, giving `(2+1)-1=2`. For `[1,2]`, `(1+1)(1+1)-1=3`.

> CodeChef tags: `Data Structures`, `Arrays`, `Mathematics`, `Algorithms`

---

Same problem in rating order (#491 of 735): [../../by-rating/491-DISTELE.md](../../by-rating/491-DISTELE.md)
