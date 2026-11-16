[&larr; 680. Mahesh and his lost array](ANUMLA.md) &middot; [Index](../../README.md) &middot; [694. Saving a gift of love &rarr;](ASHIGIFT.md)

# 690. Maximize 1s

> CodeChef problem code [`MAX1S`](https://www.codechef.com/problems/MAX1S) &middot; difficulty **2255** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Positional weights and a maximum-sum segment of flip gains |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

You are given a binary string $S$. You are allowed to perform the following operation **at most once**:
- Pick some [substring](https://en.wikipedia.org/wiki/Substring) of $S$
- Flip all the values in this substring, i.e, convert $0$ to $1$ and vice versa

For example, if $S = 1\underline{00101}011$, you can pick the underlined substring and flip it to obtain $S = 1\underline{11010}011$.

For the substring of $S$ consisting of all the positions from $L$ to $R$, we define a function $f(L, R)$ to be the number of $1$'s in this substring. For example, if $S = 100101011$, then $f(2, 5) = 1$ and $f(4, 9) = 4$ (the respective substrings are $0010$ and $101011$).

If you perform the given operation optimally, find the **maximum** possible value of
$$
\sum_{L=1}^N \sum_{R=L}^N f(L, R)
$$
that can be obtained. Note that the substring flip operation can be performed **at most once**.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of single line of input, containing a binary string $S$.

**Output**

For each test case, output on a new line the maximum possible value of $\sum_{L=1}^N \sum_{R=L}^N f(L, R)$ that can be obtained.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq |S| \leq 3\cdot 10^5$
- The sum of $|S|$ over all test cases won't exceed $3\cdot 10^5$.

## Sample

**Sample input**

```
3
111
000
00100
```

**Sample output**

```
10
10
26
```

<details><summary>Explanation</summary>

**Test case $1$:** There is no need to apply the operation since everything is already a $1$. The answer is thus the sum of:
- $f(1, 1) = 1$
- $f(1, 2) = 2$
- $f(1, 3) = 3$
- $f(2, 2) = 1$
- $f(2, 3) = 2$
- $f(3, 3) = 1$

which is $10$.

**Test case $2$:** Flip the entire string to obtain $111$, whose answer has been computed above.

**Test case $3$:** Flip the entire string to obtain $11011$. The sum of $f(L, R)$ across all substrings is now $26$, which is the maximum possible.

</details>

## Approach

Swap the order of summation: position $i$ lies in $i \cdot (N - i + 1)$ substrings, so a `1` there contributes exactly that weight $w_i$ to the total, and the sum is $\sum_{S_i = 1} w_i$.

Flipping a substring changes each position in it independently: a `0` gains $+w_i$, a `1` loses $w_i$. The best single flip is therefore the contiguous segment with the largest total of these signed gains - Kadane's algorithm - and since the operation is optional the gain is at least 0.

The answer is the current total plus the best gain.

## Solution (Python)

```python
import sys


def solve(tokens):
    bits = next(tokens)
    n = len(bits)
    total = best = running = 0
    for i, char in enumerate(bits, 1):
        weight = i * (n - i + 1)
        if char == 49:
            total += weight
            weight = -weight
        running = max(0, running + weight)
        best = max(best, running)
    return str(total + best)


if __name__ == "__main__":
    tokens = iter(sys.stdin.buffer.read().split())
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- All ones: no flip, the answer is $\sum w_i = N(N+1)(N+2)/6$.
- All zeros: flip everything, same answer.
- The best segment may include a few ones if the zeros around them outweigh them.
- Totals grow like $N^3$ and need big integers.

## Dry run

`S = 00100`, weights `5 8 9 8 5`.

Current total: 9 (the single one). Gains: `+5 +8 -9 +8 +5`. The best segment is the whole string, with gain 17.

Answer $9 + 17 = 26$ (the string becomes `11011`).

> CodeChef tags: `Data Structures`, `Algorithms`, `Greedy`

---

Same problem in rating order (#652 of 735): [../../by-rating/652-MAX1S.md](../../by-rating/652-MAX1S.md)
