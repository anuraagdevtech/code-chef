[&larr; 59. Minimum number of coins](MINCOINS.md) &middot; [Index](../../README.md) &middot; [82. Single-use Attack &rarr;](SINGLEUSE.md)

# 66. A or B

> CodeChef problem code [`AORB`](https://www.codechef.com/problems/AORB) &middot; difficulty **728** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Scheduling order and the exchange argument |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

There are two problems in a contest.
- Problem `A` is worth $500$ points at the start of the contest.
- Problem `B` is worth $1000$ points at the start of the contest.

Once the contest starts, after each minute:
- Maximum points of Problem `A` reduce by $2$ points .
- Maximum points of Problem `B` reduce by $4$ points.

It is known that Chef requires $X$ minutes to solve Problem `A` correctly and $Y$ minutes to solve Problem `B` correctly.

Find the **maximum** number of points Chef can score if he optimally decides the order of attempting both the problems.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers $X$ and $Y$ - the time required to solve problems $A$ and $B$ in minutes respectively.

**Output**

For each test case, output in a single line, the **maximum** number of points Chef can score if he optimally decides the order of attempting both the problems.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X, Y \leq 100$

## Sample

**Sample input**

```
4
10 20
8 40
15 15
20 10
```

**Sample output**

```
1360
1292
1380
1400
```

<details><summary>Explanation</summary>

**Test Case $1$:** If Chef attempts in the order $A \rightarrow B$ then he submits Problem `A` after $10$ minutes and Problem `B` after $30$ minutes.
Thus, he gets $500 - 10 \cdot 2 = 480$ points for problem `A` and $1000 - 30 \cdot 4 = 880$ points for problem `B`. Thus, total $480+880=1360$ points for both the problems.

If Chef attempts in the order $B \rightarrow A$ then he submits Problem `B` after $20$ minutes and Problem `A` after $30$ minutes.
Thus, he gets $1000 - 20 \cdot 4 = 920$ points for Problem `B` and $500 - 30 \cdot 2 = 440$ points for Problem `A`. Thus total $920+440=1360$ points for both the problems.

So, in both cases Chef gets $1360$ points in total.

**Test Case $2$:** If Chef attempts in the order $A \rightarrow B$ then he submits Problem `A` after $8$ minutes and Problem `B` after $48$ minutes.
Thus, he gets $500 - 8 \cdot 2 = 484$ points for problem `A` and $1000 - 48 \cdot 4 = 808$ points for problem `B`. Thus, total $484+808=1292$ points for both the problems.

If Chef attempts in the order $B \rightarrow A$ then he submits Problem `B` after $40$ minutes and Problem `A` after $48$ minutes.
Thus, he gets $1000 - 40 \cdot 4 = 840$ points for Problem `B` and $500 - 48 \cdot 2 = 404$ points for Problem `A`. Thus total $840+404=1244$ points for both the problems.

So, Chef will attempt in the order $A \rightarrow B$ and thus obtain $1292$ points.

**Test Case $3$:** If Chef attempts in the order $A \rightarrow B$ then he submits Problem `A` after $15$ minutes and Problem `B` after $30$ minutes.
Thus, he gets $500 - 15 \cdot 2 = 470$ points for problem `A` and $1000 - 30 \cdot 4 = 880$ points for problem `B`. Thus, total $470+880=1350$ points for both the problems.

If Chef attempts in the order $B \rightarrow A$ then he submits Problem `B` after $15$ minutes and Problem `A` after $30$ minutes.
Thus, he gets $1000 - 15 \cdot 4 = 940$ points for Problem `B` and $500 - 30 \cdot 2 = 440$ points for Problem `A`. Thus total $940+440=1380$ points for both the problems.

So, Chef will attempt in the order $B \rightarrow A$ and thus obtain $1380$ points.

**Test Case $4$:** If Chef attempts in the order $A \rightarrow B$ then he submits Problem `A` after $20$ minutes and Problem `B` after $30$ minutes.
Thus, he gets $500 - 20 \cdot 2 = 460$ points for problem `A` and $1000 - 30 \cdot 4 = 880$ points for problem `B`. Thus, total $460+880=1340$ points for both the problems.

If Chef attempts in the order $B \rightarrow A$ then he submits Problem `B` after $10$ minutes and Problem `A` after $30$ minutes.
Thus, he gets $1000 - 10 \cdot 4 = 960$ points for Problem `B` and $500 - 30 \cdot 2 = 440$ points for Problem `A`. Thus total $960+440=1400$ points for both the problems.

So, Chef will attempt in the order $B \rightarrow A$ and thus obtain $1400$ points.

</details>

## Approach

Chef solves both problems, so the only decision is the **order**. Points decay with wall-clock time from the start of the contest, and whichever problem is attempted second absorbs the first one's solving time as extra delay.

Solving `A` first, `A` is submitted at minute $X$ and `B` at minute $X + Y$:

$$(500 - 2X) + \bigl(1000 - 4(X+Y)\bigr) = 1500 - 6X - 4Y$$

Solving `B` first, `B` lands at $Y$ and `A` at $X + Y$:

$$(1000 - 4Y) + \bigl(500 - 2(X+Y)\bigr) = 1500 - 2X - 6Y$$

The answer is the larger of the two.

Comparing them shows the structure. `A` first wins when $-6X - 4Y > -2X - 6Y$, that is when $2Y > 4X$, or $Y > 2X$. So Chef should start with `A` exactly when `B` takes more than twice as long — the quick problem goes first, but weighted by decay rate, not by raw time.

This is the classic **exchange argument**: with two jobs, swapping adjacent ones and comparing totals reveals the ordering rule, which here is to sort by $\frac{\text{solve time}}{\text{decay rate}}$. The same reasoning generalises to $n$ jobs and underlies scheduling results such as Smith's rule.

Sample case 3 makes the point concretely: with $X = Y = 15$ the times are identical, yet order still matters — doing `B` first scores $1380$ against $1350$, because delaying the faster-decaying problem is the costlier mistake. With only two orderings available, evaluating both is simplest and avoids re-deriving the inequality.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        a_first = (500 - 2 * x) + (1000 - 4 * (x + y))
        b_first = (1000 - 4 * y) + (500 - 2 * (x + y))
        # Whichever problem goes second pays the other's solving time.
        out.append(str(max(a_first, b_first)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The two orders tie** ($X = 10$, $Y = 20$: both give $1360$). The sample's first row, so taking either is fine but the maximum must still be computed.
- **Equal solving times, unequal decay** ($X = Y = 15$): B-first scores $1380$ against A-first's $1350$. Which order wins is decided by the *decay rates*, not by which problem is quicker — B loses $4$ points a minute and so should be submitted early. A rule like "solve the faster one first" gets this row wrong.
- **Scores never go negative** at these bounds: with $X + Y \leq 200$ the worst cases are $1000 - 4 \times 200 = 200$ and $500 - 2 \times 200 = 100$, both positive, so no clamping is needed.
- Only two orders exist, so evaluating both and taking the larger is exact — there is no greedy rule to justify.

## Dry run

| $X$ | $Y$ | A first | B first | output |
|---:|---:|---:|---:|---|
| 10 | 20 | $480 + 880 = 1360$ | $920 + 440 = 1360$ | `1360` |
| 8 | 40 | $484 + 808 = 1292$ | $840 + 404 = 1244$ | `1292` |
| 15 | 15 | $470 + 880 = 1350$ | $940 + 440 = 1380$ | `1380` |
| 20 | 10 | $460 + 880 = 1340$ | $960 + 440 = 1400$ | `1400` |

In each pair the problem solved second pays for the first one's time; rows 3 and 4 both favour B first.

---

Same problem in rating order (#73 of 486): [../../by-rating/073-AORB.md](../../by-rating/073-AORB.md)
