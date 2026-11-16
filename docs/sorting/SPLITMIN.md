[&larr; 687. Chef and Ants](ANTSCHEF.md) &middot; [Index](../../README.md) &middot; [733. Chef Up &rarr;](CHEF7UP.md)

# 711. Two Piles

> CodeChef problem code [`SPLITMIN`](https://www.codechef.com/problems/SPLITMIN) &middot; difficulty **2347** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | The larger maximum is at least the largest of the pair minima; pair it with its nearest lower value |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

You are given $N$ pairs of integers. The $i$-th pair is $(A_i, B_i)$.
You also have two piles with you, both initially empty.

You will perform the following process:
- For each $i$ from $1$ to $N$, choose **exactly one** of $A_i$ or $B_i$.
- Then, add the chosen integer to one of your two piles.

At the end of the process, both piles **must be non-empty** (i.e, you should have added at least one integer to both).

The *value* of a pile is defined to be its maximum element.
If you make your choices optimally, find the **minimum possible difference** between the *values* of the piles.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$ — the number of pairs.
    - The next $N$ lines describe the pairs. The $i$-th of these lines contains two space-separated integers $A_i$ and $B_i$ — the elements of the $i$-th pair.

**Output**

For each test case, output on a new line the minimum possible difference between the values of the piles.

## Constraints

- $1 \leq T \leq 10^4$
- $2 \leq N \leq 2\cdot 10^5$
- $1 \leq A_i, B_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
3
2
1 6
4 9
2
1 9
4 6
4
10 10
23 55
21 80
105 91
```

**Sample output**

```
2
3
11
```

<details><summary>Explanation</summary>

**Test case $1$:** The pairs are $(1, 6)$ and $(4, 9)$.
Choose $6$ from the first pair, and $4$ from the second pair, and place them on different piles.
The maximums are $6$ and $4$, and the difference between them is $|6-4| = 2$.
Achieving a smaller difference is not possible.

**Test case $2$:** The pairs are $(1, 9)$ and $(4, 6)$.
Choose $1$ from the first pair and $4$ from the second pair and place them on different piles, for a difference of $3$.

**Test case $3$:** One optimal solution is:
- From the first pair, place $10$ on pile $1$.
- From the second pair, place $55$ on pile $2$.
- From the third pair, place $80$ on pile $2$.
- From the fourth pair, place $91$ on pile $1$.

The difference between the maximums of the piles is $|80 - 91| = 11$. This is the smallest possible difference.

</details>

## Approach

Let $L = \max_i \min(A_i, B_i)$. Whatever is chosen, the pair attaining $L$ contributes a value of at least $L$, so the larger of the two pile maxima is at least $L$.

Conversely, take any value $X \ge L$ from some pair and any value $Y \le X$ from a *different* pair. They can be made the two maxima: put $Y$ alone in one pile, and put $X$ together with the smaller element of every other pair - each at most $L \le X$ - in the other. The difference is $X - Y$.

So the answer is the minimum of $X - Y$ over values $X \ge L$ and $Y \le X$ belonging to different pairs. Sort all $2N$ values tagged with their pair index; for each $X \ge L$ the best partner is the closest earlier value in sorted order with a different tag, and since a pair has only two values at most one earlier entry is skipped.

## Solution (Python)

```python
import sys


def solve(tokens):
    n = next(tokens)
    tagged = []
    floor_value = 0
    for i in range(n):
        a, b = (next(tokens), next(tokens))
        tagged.extend(((a, i), (b, i)))
        floor_value = max(floor_value, min(a, b))
    tagged.sort()
    best = 10 ** 30
    for j, (value, i) in enumerate(tagged):
        if value < floor_value:
            continue
        k = j - 1
        while k >= 0 and tagged[k][1] == i:
            k -= 1
        if k >= 0:
            best = min(best, value - tagged[k][0])
    return str(best)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Both piles must be non-empty, which the construction guarantees ($Y$ is alone in its pile).
- The two maxima may be equal, giving 0.
- $X$ and $Y$ must come from different pairs - both elements of one pair cannot be chosen.
- With $N = 2$ the answer is simply the best of the four cross differences.

## Dry run

Pairs `(1, 9)` and `(4, 6)`: $L = \max(1, 4) = 4$.

Sorted values with owners: `1(a) 4(b) 6(b) 9(a)`.

- $X = 4$: previous value of another pair is 1, difference 3.
- $X = 6$: skip 4 (same pair), take 1, difference 5.
- $X = 9$: previous is 6 from the other pair, difference 3.

Answer 3.

> CodeChef tags: `Algorithms`

---

Same problem in rating order (#676 of 735): [../../by-rating/676-SPLITMIN.md](../../by-rating/676-SPLITMIN.md)
