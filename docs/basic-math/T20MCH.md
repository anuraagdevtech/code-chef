[&larr; 76. Small Factorial](FLOW018.md) &middot; [Index](../../README.md) &middot; [81. Reach fast &rarr;](REACHFAST.md)

# 78. Possible Victory

> CodeChef problem code [`T20MCH`](https://www.codechef.com/problems/T20MCH) &middot; difficulty **769** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Best-case bound |
| **Time** | $O(1)$ |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Chef is playing in a T20 cricket match. In a match, Team A plays for 20 overs. In a single over, the team gets to play 6 times, and in each of these 6 tries, they can score a maximum of 6 runs. After Team A's 20 overs are finished, Team B similarly plays for 20 overs and tries to get a higher total score than the first team. The team with the higher total score at the end wins the match.

Chef is in Team B. Team A has already played their 20 overs, and have gotten a score of $R$. Chef's Team B has started playing, and have already scored $C$ runs in the first $O$ overs. In the remaining $20 - O$ overs, find whether it is possible for Chef's Team B to get a score high enough to win the game. That is, can their final score be strictly larger than $R$?

**Input**

- There is a single line of input, with three integers, $R, O, C$.

**Output**

Output in a single line, the answer, which should be "YES" if it's possible for Chef's Team B  to win the match and "NO" if not.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

## Constraints

- $0 \leq C \leq R \leq 720$
- $1 \leq O \leq 19$
- $0 \leq C \leq 36 * O$

## Sample

**Sample 1 input**

```
719 18 648
```

**Sample 1 output**

```
YES
```

<details><summary>Explanation</summary>

In the remaining $20-O = 2$ overs, Team B gets to play $2*6 = 12$ times, and in each try, they can get a maximum of 6 score. Which means that the maximum score that they can acheieve in these 2 overs is $12*6 = 72$. Thus, the maximum total score that Team B can achieve is $C+72 = 720$. $720$ is strictly more than Team A's score of $719$, and hence Chef's Team B can win this match.

</details>

**Sample 2 input**

```
720 18 648
```

**Sample 2 output**

```
NO
```

<details><summary>Explanation</summary>

Similar to the previous explanation, the maximum total score that Team B can achieve is $720$, which isn't strictly greater than Team A's $720$.Hence Chef's Team B can't win this match.

</details>

## Approach

The question is whether Team B *can* win, not whether it is likely, so the right move is to compute their **maximum possible** final score and compare it against the target.

An over consists of $6$ balls scoring at most $6$ runs each, so an over yields at most $36$ runs. Team B has $20 - O$ overs left, so the best they can finish on is

$$C + 36(20 - O)$$

They win if that strictly exceeds $R$, since the problem requires a higher score and a tie is not a win.

Framing it as an upper bound is what makes this a one-liner rather than a search. Any question of the form "is it possible to reach a target" becomes "is the optimum at least the target" — there is nothing to simulate once the best case is in hand.

The sample is deliberately tight: $648 + 36 \times 2 = 720$ against $R = 719$, a margin of exactly one run. Using a per-over maximum of $30$, or forgetting that $20 - O$ overs remain rather than $O$, flips the answer.

Two details to note. There is **no $T$** here — a single line of three integers is the whole input. And the input order is $R, O, C$: target, overs bowled, then runs scored, which is not the order the prose introduces them in.

## Solution (Python)

```python
import sys


def main() -> None:
    # Single test case; input order is R, O, C.
    r, o, c = map(int, sys.stdin.buffer.read().split()[:3])
    # Best case: 6 balls x 6 runs = 36 per over, for the overs that remain.
    best = c + 36 * (20 - o)
    print("YES" if best > r else "NO")


main()
```

## Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

## Edge cases

- **The best case exactly ties the target**: the two sample runs differ by a single run, $719$ and $720$, against a best possible $720$. A tie is not a win, so the comparison must be **strict** — this pair exists to catch `>=`.
- **One over left** ($O = 19$): the best case adds only $36$.
- **A T20 has $20$ overs**, so the overs remaining are $20 - O$; using $O$ itself inverts the whole calculation.
- **$36$ per over** is $6$ balls at $6$ runs each, the theoretical ceiling — the constraint $C \leq 36 \cdot O$ confirms the same rate applies to what has already been scored.
- **Input order is $R$, $O$, $C$**, with no test-case count.

## Dry run

Sample 1: $R = 719$, $O = 18$, $C = 648$.

| step | value |
|---|---|
| overs left | $20 - 18 = 2$ |
| best possible extra | $2 \times 36 = 72$ |
| best final score | $648 + 72 = 720$ |
| $720 > 719$? | yes |
| output | `YES` |

Sample 2 is identical but with $R = 720$: now $720 > 720$ fails, so `NO`.

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#84 of 486): [../../by-rating/084-T20MCH.md](../../by-rating/084-T20MCH.md)
