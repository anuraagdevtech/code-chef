# 1308 &middot; Maximise the Subsequence Sum

> CodeChef problem code [`SIGNFLIP`](https://www.codechef.com/problems/SIGNFLIP) &middot; time limit **2.5s** &middot; Level up from 1* to 2* (Level 2)

## Topics used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Flip the largest magnitudes first |
| **CodeChef category** | main |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

Same write-up grouped by topic: [../docs/greedy/SIGNFLIP.md](../docs/greedy/SIGNFLIP.md)

## Question

Chef has an array $A$ containing $N$ integers. The integers of the array can be positive, negative, or even zero.

Chef allows you to choose at most $K$ elements of the array and multiply them by $-1$.

Find the **maximum** sum of a subsequence you can obtain if you choose the elements of the subsequence optimally.

**Note**: A sequence $a$ is a *subsequence* of a sequence $b$ if $a$ can be obtained from $b$ by deletion of several (possibly, zero or all) elements. For example, $[3,1]$ is a subsequence of $[3,2,1]$ and $[4,3,1]$, but not a subsequence of $[1,3,3,7]$ and $[3,10,4]$. Note that empty sequence is also a subsequence.

**Input**

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N, K$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2,..., A_N$

**Output**

For each test case, print a single line containing one integer - the maximum sum of a subsequence you can obtain.

## Constraints

- $1 \leq T \leq 15$
- $1 \leq N \leq 10^5$
- $0 \leq K \leq N$
- $-10^4 \leq A_i \leq 10^4$
- Sum of $N$ over all test cases does not exceed $10^6$

## Sample

**Sample input**

```
3
6 2
6 -10 -1 0 -4 2
5 0
-1 -1 -1 -1 -1
3 3
1 2 3
```

**Sample output**

```
22
0
6
```

<details><summary>Explanation</summary>

**Test case $1$:** It is optimal to multiply $-10, -4$ with $-1$ and then take the subsequence $[6, 10, 4, 2]$.

**Test case $2$:** It is optimal to choose empty subsequence with a sum equal to $0$.

**Test case $3$:** We can take subsequence $[1, 2, 3]$. Here, we do not multiply $-1$ with any element.

</details>

## Approach

Two freedoms compose here, and separating them makes the problem easy.

**The subsequence may drop anything.** So after the flips are decided, the best subsequence is simply "every positive element" — negatives and zeros are excluded at no cost. The empty subsequence is allowed, so the answer is never negative.

**The flips should target the most negative elements.** Turning $-v$ into $+v$ swings the achievable sum by $v$, since the element goes from excluded to contributing $v$. So each flip is worth the *magnitude* of the negative it fixes, and the greedy is to spend the $K$ flips on the largest magnitudes.

Flipping a positive is never useful — it would only remove it from the subsequence — and flipping fewer than $K$ times is allowed, so there is no obligation to use them all.

Putting it together: sum the positives, then add the magnitudes of the $K$ most negative values (or all of them, if fewer than $K$ negatives exist).

Sample case 1: positives give $6 + 2 = 8$; the two most negative are $-10$ and $-4$, adding $14$, for $22$. Note $-1$ is left unflipped — the flips go to the biggest magnitudes, not the first negatives encountered.

Sample case 2 has $K = 0$ and all negatives, so nothing can be fixed and the empty subsequence gives $0$ — not $-5$. Sample case 3 has no negatives at all, so the three available flips go unused and the answer is the full sum $6$.

Sorting ascending puts the most negative values first, making the $K$ flips a prefix. With the sum of $N$ reaching $10^6$, the sort is the dominant cost and bulk input reading matters.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        a = sorted(int(v) for v in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        total = sum(v for v in a if v > 0)
        # Ascending order puts the most negative first; flipping one is worth
        # its magnitude. Flipping a positive would never help.
        for i in range(min(k, n)):
            if a[i] >= 0:
                break
            total += -a[i]
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$
