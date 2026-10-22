[&larr; 307. Minimum Number of Pizzas](MINPIZZAS.md) &middot; [Index](../../README.md) &middot; [332. Modular Equation &rarr;](MODEQ.md)

# 308. Alternating Work Days

> CodeChef problem code [`ALTER`](https://www.codechef.com/problems/ALTER) &middot; difficulty **1486** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Divisibility plus an alternation constraint |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

Alice and Bob are two friends. Initially, the skill levels of them are zero. They work on alternative days, i.e one of Alice and Bob works on the odd-numbered days$(1, 3, 5, \dots)$ and the other works on the even-numbered days $(2, 4, 6, \dots)$. The skill levels of Alice and Bob increase by $A, B$ respectively on the days they work.

Determine if it is possible that the skill levels of Alice and Bob become exactly $P, Q$ respectively on some day.

**Input**

- The first line contains an integer $T$, denoting the number of test cases. The $T$ test cases then follow:
- The first and only line of each test case contains four space-separated integers $A, B, P, Q$.

**Output**

For each test case, print `YES` if it is possible that the skill levels of Alice and Bob become exactly $P, Q$ on some day, otherwise print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq A, B, P, Q \leq 10^9$

**Subtasks**

- **Subtask 1 (100 points):** Original constraints

## Sample

**Sample input**

```
4
1 2 1 2
1 2 3 2
4 3 4 6
3 5 9 25
```

**Sample output**

```
YES
NO 
YES
NO
```

<details><summary>Explanation</summary>

**Test Case $1$:** Alice works on the first day and gains skill level $1$. Bob works on the second day and gains skill level $2$.

**Test Case $2$:** There is no possible way that the skill levels of Alice and Bob become $3$ and $2$ respectively.

 **Test Case $3$:** Bob works on the first and third day and Alice works on the second day. Hence after the third day, the skill levels of Alice and Bob become $1\cdot4 = 4$ and $2 \cdot 3 = 6$ respectively.

</details>

## Approach

Alice gains $A$ on each of her work days and Bob gains $B$ on each of his, so reaching exactly $P$ and $Q$ requires

$$a = \frac{P}{A}, \qquad b = \frac{Q}{B}$$

to both be **whole numbers** — otherwise the targets are simply unreachable.

But divisibility alone is not enough, and this is where the problem has its teeth. Because they work on **alternating** days, after $d$ days one of them has worked $\lceil d/2 \rceil$ times and the other $\lfloor d/2 \rfloor$. So the two work counts can never differ by more than one:

$$|a - b| \leq 1$$

That covers all three legal shapes — equal counts after an even number of days, or one ahead after an odd number — and it does not matter which of them takes the odd days, since both orderings are allowed.

Sample case 2 shows divisibility passing while the alternation fails: $P = 3$ with $A = 1$ needs three Alice-days, but $Q = 2$ with $B = 2$ needs only one Bob-day, and a gap of $2$ is impossible. Sample case 4 is the same failure with a gap of $2$ between three and five.

Sample case 3 is the off-by-one case that must be **accepted**: $a = 1$ and $b = 2$ differ by exactly one, which happens naturally after three days with Bob starting.

A strict equality check would reject it, and a check omitting the gap entirely would accept cases 2 and 4 — both halves are load-bearing.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, p, q = map(int, data[1 + 4 * i:5 + 4 * i])
        if p % a or q % b:
            out.append("NO")
            continue
        # They alternate, so the two work counts differ by at most one.
        out.append("YES" if abs(p // a - q // b) <= 1 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Divisibility first**: each person's total must be an exact multiple of their per-day gain, so $P \bmod A$ and $Q \bmod B$ must both be zero. The fourth row passes this and still fails.
- **Alternation bounds the day counts.** They work on alternate days, so the two counts can differ by at most one — $|P/A - Q/B| \leq 1$. The second row needs $3$ days from Alice and $1$ from Bob, which no alternating schedule produces.
- **A difference of exactly one is fine** (the third row: one day for Alice, two for Bob), since whoever starts gets the extra day.
- **Equal counts are fine too** (the first row), corresponding to an even total number of days.
- **$P, Q \geq 1$**, so both day counts are at least one and the degenerate "nobody works" case cannot arise.
- **Which of them takes the odd days is not fixed**, which is exactly why the bound is on the absolute difference rather than on a signed one.

## Dry run

| $A$ | $B$ | $P$ | $Q$ | Alice's days | Bob's days | difference | output |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 2 | 1 | 2 | 1 | 1 | 0 | `YES` |
| 1 | 2 | 3 | 2 | 3 | 1 | **2** | `NO` |
| 4 | 3 | 4 | 6 | 1 | 2 | 1 | `YES` |
| 3 | 5 | 9 | 25 | 3 | 5 | **2** | `NO` |

---

Same problem in rating order (#284 of 486): [../../by-rating/284-ALTER.md](../../by-rating/284-ALTER.md)
