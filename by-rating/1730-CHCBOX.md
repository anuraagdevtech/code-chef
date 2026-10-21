# 1730 &middot; Box of Chocolates

> CodeChef problem code [`CHCBOX`](https://www.codechef.com/problems/CHCBOX) &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Fitting a window into the gaps between maxima |
| **CodeChef tags** | `Algorithms`, `Constructive`, `Simple Algos`, `ad-hoc`, `Cyclic Rotation` |
| **CodeChef top tag** | `Ad Hoc` |
| **CodeChef category** | easy |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

Same write-up grouped by topic: [../docs/arrays/CHCBOX.md](../docs/arrays/CHCBOX.md)

## Question

Chef just got a box of chocolates as his birthday gift. The box contains $N$ chocolates in a row (numbered $1$ through $N$), where $N$ is even. For each valid $i$, the $i$-th chocolate has a *sweetness value* $W_i$.

Chef wants to eat all the chocolates in the first half of the box and leave all chocolates in the second half uneaten. Since he does not like chocolates that are too sweet, he will be unhappy if at least one of the chocolates he eats has the maximum sweetness among all the chocolates in the box.

A right cyclic shift by $k$ chocolates ($0 \le k \lt N$) consists of moving the last $k$ chocolates in the row to the beginning in the same order and moving each of the remaining $N-k$ chocolates $k$ places to the right. Before eating the first half of the chocolates, Chef wants to perform some right cyclic shift in such a way that he will not be unhappy after eating them. Find the number of ways to do this, i.e. the number of valid integers $k$ such that if Chef performs the right cyclic shift by $k$ chocolates and then eats the first half of the chocolates in the box, he does not become unhappy.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $W_1, W_2, \ldots, W_N$.

### Output
For each test case, print a single line containing one integer ― the number of shifts for which Chef does not become unhappy.

### Constraints
- $1 \le T \le 5$
- $1 \le N \le 10^5$
- $N$ is even
- $1 \le W_i \le 10^5$ for each valid $i$

## Constraints

- $1 \le T \le 5$
- $1 \le N \le 10^5$
- $N$ is even
- $1 \le W_i \le 10^5$ for each valid $i$

## Sample

**Sample input**

```
2
6
1 1 2 1 1 1
6
1 1 2 1 1 2
```

**Sample output**

```
3
0
```

<details><summary>Explanation</summary>

**Example case 1:** The three valid right shifts and the contents of the box for these shifts are:
- shift by $k = 1$: $(1, 1, 1, 2, 1, 1)$
- shift by $k = 2$: $(1, 1, 1, 1, 2, 1)$
- shift by $k = 3$: $(1, 1, 1, 1, 1, 2)$

</details>

## Approach

A right shift by $k$ moves the chocolate originally at index $i$ to position $i + k$, so the half Chef eats — positions $1 \ldots N/2$ — is the **cyclic block of $N/2$ original chocolates** starting at index $(N-k) \bmod N$. As $k$ runs over $0 \ldots N-1$ that start runs over every index exactly once, so the question becomes:

> how many cyclic windows of length $N/2$ contain no chocolate of maximum sweetness?

The maxima cut the circle into gaps of consecutive non-maximal chocolates. A window avoiding every maximum must sit inside one gap, and a gap of length $g$ holds

$$\max\bigl(0,\ g - N/2 + 1\bigr)$$

such windows. Summing over the gaps gives the answer, in one pass after locating the maxima.

Thinking in terms of gaps rather than shifts is what removes the $O(N^2)$ "check each shift" loop, and it makes the structure obvious: with two or more maxima well spread around the circle, no gap can reach half the length and the answer is $0$.

The samples are exactly that contrast. $[1,1,2,1,1,1]$ has a single maximum, leaving one gap of length $5$, so $5 - 3 + 1 = 3$ shifts work. $[1,1,2,1,1,2]$ has two maxima three apart, splitting the circle into gaps of length $2$ and $2$, both shorter than the required $3$ — so Chef cannot avoid the sweetest chocolate however he shifts.

Note that if every chocolate ties for the maximum there are no gaps at all, and the answer is $0$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        w = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        peak = max(w)
        spots = [i for i, v in enumerate(w) if v == peak]
        half = n // 2
        # Each cyclic gap between consecutive maxima holds g - half + 1 windows.
        total = 0
        for j, p in enumerate(spots):
            nxt = spots[(j + 1) % len(spots)]
            gap = (nxt - p - 1) % n if len(spots) > 1 else n - 1
            total += max(0, gap - half + 1)
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
