[&larr; 654. Wishcraft](MAJIK.md) &middot; [Index](../../README.md) &middot; [664. Chef Goes Shopping &rarr;](CHEFSHOPPING.md)

# 658. Maximising Vacations

> CodeChef problem code [`MAXVAC`](https://www.codechef.com/problems/MAXVAC) &middot; difficulty **2147** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Vacations per run of holidays, plus the best gain from bridging one workday |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

You are given Chef's calendar for the next $N$ days, defined as a binary string $S$ of length $N$ where $S_i = 0$ means that Chef has a holiday on the $i^{th}$ day from now, and $S_i = 1$ means that Chef has to work on that day.

Chef wants to plan his vacations. For each vacation, Chef needs $X$ consecutive holidays in his calendar. Obviously, he can only go on one vacation at a time.

Chef can take at most one extra holiday. That is, he can flip at most one digit in $S$ from $1$ to $0$. If he does this optimally, what is the **maximum** number of vacations that he can go on?

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $X$.
- The second line of each test case contains a binary string $S$ of length $N$ — Chef's schedule.

**Output**

For each test case, output on a new line the answer — the maximum number of vacations Chef can take if he takes at most one more extra holiday.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 2 \cdot 10^5$
- $1 \leq X \leq N$
- The sum of $N$ across all test cases does not exceed $2 \cdot 10^5$

## Sample

**Sample input**

```
3
7 2
0010001
4 3
1010
5 2
00100
```

**Sample output**

```
3
1
2
```

<details><summary>Explanation</summary>

**Test Case $1$:** Chef can flip the $3^{rd}$ digit to make his calendar $0000001$. This allows him to take $3$ vacations in the first $6$ days.

**Test Case $2$:** Chef can flip the $3^{rd}$ digit to make his calendar $1000$. This allows him to take one vacation using the last $3$ days.

**Test Case $3$:** Regardless of whether Chef flips the $3^{rd}$ digit or not, he can take at most $2$ vacations.

</details>

## Approach

A maximal run of $\ell$ consecutive holidays allows $\lfloor \ell / X \rfloor$ vacations, and runs are independent. Without any change the answer is the sum of that over all runs.

Turning one workday into a holiday merges the run on its left, the day itself and the run on its right into one run of length $\ell_1 + \ell_2 + 1$ (either side may be empty). The gain is

$$\Bigl\lfloor \frac{\ell_1 + \ell_2 + 1}{X} \Bigr\rfloor - \Bigl\lfloor \frac{\ell_1}{X} \Bigr\rfloor - \Bigl\lfloor \frac{\ell_2}{X} \Bigr\rfloor,$$

and no other run is affected. Splitting the string at every `1` lists the runs in order, including empty ones between adjacent workdays, so consecutive entries of that list are exactly the pairs separated by one workday. Add the best gain, or 0 if no flip helps.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        need = int(next(tokens))
        calendar = next(tokens).decode()
        runs = [len(v) for v in calendar.split('1')]
        base = sum((v // need for v in runs))
        gain = max([0] + [(runs[i] + runs[i + 1] + 1) // need - runs[i] // need - runs[i + 1] // need for i in range(len(runs) - 1)])
        out.append(str(base + gain))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- No workday at all: there is nothing to flip.
- Adjacent workdays give empty runs, which the split keeps as zeros.
- $X = 1$: every holiday is a vacation and a flip always adds one (if a workday exists).
- The flip is optional.

## Dry run

`S = 0010001`, `X = 2`.

Runs: `2, 3, 0` (the last one is the empty run after the final `1`). Base: $1 + 1 + 0 = 2$.

- flip the first workday: $\lfloor 6/2 \rfloor - 1 - 1 = 1$
- flip the last one: $\lfloor 4/2 \rfloor - 1 - 0 = 1$

Answer $2 + 1 = 3$.

---

Same problem in rating order (#618 of 735): [../../by-rating/618-MAXVAC.md](../../by-rating/618-MAXVAC.md)
