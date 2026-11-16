[&larr; 633. Maximum And Or](MAXANDOR.md) &middot; [Index](../../README.md) &middot; [671. Chef Is Just Throwing Random Words &rarr;](SSO.md)

# 645. Double Burgers

> CodeChef problem code [`BURGER`](https://www.codechef.com/problems/BURGER) &middot; difficulty **2072** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Each streak is a power of two minus one - search the number of streaks |
| **Time** | $O(\log^2 (Y / X))$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

You have taken an eating challenge from Chef and now you have to eat exactly $Y$ burgers. You will eat in the following way:

- In the first minute you will eat exactly $X$ burgers and every minute after that you will eat exactly twice the number of burgers you ate in the previous minute.
- Since you can get tired of eating, Chef also allows you take a break from eating for exactly $1$ minute.
- When you start eating again after taking a break, your eating streak resets, i.e. in the first minute after the break you will eat exactly $X$ burgers and every minute after that you will eat exactly double the burgers you ate on the previous minute.

Let $a_1, a_2, ..., a_k$ be the lengths of your eating streaks in minutes. Chef requires that all $a_i$ are pairwise distinct.

Find the minimum number of minutes you need to eat exactly $Y$ burgers or determine it is impossible to do so.

**Input**
- The first line contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $X$ and $Y$.

**Output**
For each test case, print a single line containing one integer — the minimum number of minutes you need to eat exactly $Y$ burgers, or $−1$ if it is impossible.

**Constraints**
- $1\leq T\leq 10^5$
- $1\leq X,Y\leq 10^{18}$

## Constraints

- $1\leq T\leq 10^5$
- $1\leq X,Y\leq 10^{18}$

## Sample

**Sample input**

```
2
1 7
1 4
```

**Sample output**

```
3
4
```

## Approach

A streak of $a$ minutes eats $X (1 + 2 + \dots + 2^{a-1}) = X (2^a - 1)$ burgers, so $Y$ must be a multiple of $X$; let $Z = Y / X$. With $k$ streaks of lengths $a_1, \dots, a_k$, which have to be pairwise distinct,

$$Z = \sum_{i} (2^{a_i} - 1) \iff Z + k = \sum_i 2^{a_i}.$$

The right-hand side is a number whose binary representation has exactly $k$ ones, none of them at bit 0 (every streak lasts at least a minute). So for each $k$ from 1 to 60 check whether $Z + k$ is even and has popcount $k$. If it does, the streak lengths are the positions of its set bits and the time is their sum plus $k - 1$ minutes of breaks.

The weights $2^a - 1$ are super-increasing - each exceeds the sum of all smaller ones - so a number has at most one representation as a sum of distinct weights. The first $k$ that works is therefore the only one, and its time is the answer; if none works the answer is $-1$.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        first = next(tokens)
        target = next(tokens)
        answer = -1
        if target % first == 0:
            units = target // first
            for streaks in range(1, 61):
                shifted = units + streaks
                if shifted % 2 == 0 and shifted.bit_count() == streaks:
                    answer = sum((i for i in range(1, shifted.bit_length()) if shifted >> i & 1)) + streaks - 1
                    break
        out.append(str(answer))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(\log^2 (Y / X))$ per test case
- **Space:** $O(1)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $Y$ not divisible by $X$: impossible.
- $Z + k$ odd would need a streak of length 0.
- The breaks cost $k - 1$ minutes, not $k$.
- Trying up to 60 streaks covers every input that fits in 64 bits.

## Dry run

`X = 1, Y = 4`, so $Z = 4$.

- $k = 1$: $Z + 1 = 5$ is odd - no.
- $k = 2$: $Z + 2 = 6 = 110_2$, even with two set bits at positions 1 and 2 - yes.

Streaks of 1 and 2 minutes eat $1 + 3 = 4$ burgers; time $1 + 2 + 1 = 4$.

> CodeChef tags: `Mathematics`, `Number Theory`, `Bit Manipulation`, `Sequences and Progression`, `Exponentiation`, `Algorithms`, `Constructive`

---

Same problem in rating order (#598 of 735): [../../by-rating/598-BURGER.md](../../by-rating/598-BURGER.md)
