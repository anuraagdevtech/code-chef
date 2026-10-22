[&larr; 96. The Preparations](SUPCHEF.md) &middot; [Index](../../README.md) &middot; [100. Mileage matters &rarr;](MILEAGE.md)

# 98. Best of N Sets

> CodeChef problem code [`BESTOFTENNIS`](https://www.codechef.com/problems/BESTOFTENNIS) &middot; difficulty **830** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Inverting a stopping condition |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Sonu and Titu are playing a tennis match. They are playing a "best of $N$ sets" match ($N$ is always odd). That means that they will play at most $N$ sets, and the person who has won most sets wins the match. But they are smart, and if they notice at any point that one of them has no chance of winning the match, they will stop the match right then, without playing out all the $N$ sets needlessly.

For example, suppose $N = 11$. And at some point, Sonu has won 5 sets, and Titu has won 4 sets. Sonu is leading now, but it is possible that Titu wins the two remaining sets and wins the whole match. So they will not stop right now.

But suppose Sonu wins the next set as well, and so now the score is $(6, 4)$. Now, even though there is one set remaining, there is no chance of Titu winning the whole match, since at best, even if he wins the next set, the score will become $(6, 5)$, and Sonu still wins. So, they will stop at a score of $(6, 4)$ and declare Sonu as the winner.

As another example, if $N=15$, and the score is currently $(8, 2)$, then they'll stop right now, since there is no way for Titu to win the match. Even if Titu wins all the $5$ remaining sets, Titu cannot win the match.

---

You are watching the match, and you see that the match has ended with a score of $(X, Y)$. That is, Sonu has won $X$ sets, and Titu has won $Y$ sets. But you don't know what $N$ is. Can you find out $N$ from just knowing the final score?

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing two space-separated integers $X$ and $Y$ where $X$ is the number of sets won by Sonu and $Y$ is the number of sets won by Titu.

**Output**

- For each test case, output on a new line the value of $N$.
- Note that you should only output an odd integer.

## Constraints

- $1 \leq T \leq 10000$
- $1 \leq X \leq 100$
- $1 \leq Y \leq 100$
- $X ≠ Y$, since they would never stop when they have won the same number of sets.

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
4
2 5
8 10
99 1
4 8
```

**Sample output**

```
9
19
197
15
```

<details><summary>Explanation</summary>

**Testcase 1:** Sonu has won 2 sets and Titu has won 5. They have played 7 sets and Titu has been decided to be the winner.

Suppose $N = 11$, then 4 more sets are remaining and if Sonu wins them all, Sonu's score ($2 + 4 = 6$) will become greater than Titu's score of $5$. So at this point, they could not have stopped playing, and so $N$ cannot be $11$ or more.

But suppose $N = 9$, then 2 more sets are remaining and even if Sonu wins them all, he still cannot win, since $2 + 2 = 4$ is still $< 5$. So it makes sense that they stopped right now.

$N$ can't be lower than $9$, since they would have stopped the match sooner.

So, the answer is $N = 9$.

**Testcase 2:** Sonu has won 8 sets and Titu has won 10. They have played 18 sets and Titu has been decided to be the winner.

Suppose $N = 21$, then 3 more sets are remaining and if Sonu wins them all, Sonu's score ($8 + 3 = 11$) will become greater than Titu's score of $10$. So at this point, they could not have stopped playing, and so $N$ cannot be $21$ or more.

But suppose $N = 19$, then 1 more set is remaining and even if Sonu wins that set, he still cannot win, since $8 + 1 = 9$ is still $< 10$. So it makes sense that they stopped right now.

$N$ can't be lower than $19$, since they have played $18$ sets.

So, the answer is $N = 19$.

**Testcase 3:** Sonu has won 99 sets and Titu has won 1. They have played 100 sets and Sonu has been decided to be the winner.

Suppose $N = 199$, then 99 more sets are remaining and if Titu wins them all, Titu's score ($1 + 99 = 100$) will become greater than Titu's score of $99$. So at this point, they could not have stopped playing, and so $N$ cannot be $199$ or more.

But suppose $N = 197$, then 97 more sets are remaining and even if Titu wins that set, he still cannot win, since $1 + 97 = 98$ is still $< 9$. So it makes sense that they stopped right now.

$N$ can't be lower than $197$, since they would have stopped the match sooner.

So, the answer is $N = 197$.

**Testcase 4:** Sonu has won 4 sets and Titu has won 8. They have played 12 sets and Titu has been decided to be the winner.

Suppose $N = 17$, then 5 more sets are remaining and if Sonu wins them all, Sonu's score ($4 + 5 = 9$) will become greater than Titu's score of $8$. So at this point, they could not have stopped playing, and so $N$ cannot be $17$ or more.

But suppose $N = 15$, then 3 more sets are remaining and even if Sonu wins them all, he still cannot win, since $4 + 3 = 7$ is still $< 8$. So it makes sense that they stopped right now.

$N$ can't be lower than $15$, since they would have stopped the match sooner.

So, the answer is $N = 15$.

</details>

## Approach

In a best-of-$N$ match with $N$ odd, the winner needs $\frac{N+1}{2}$ sets — a strict majority. The players stop the instant the outcome is decided, which is exactly the moment the winner reaches that number. So at the final score, the winner has **precisely** $\frac{N+1}{2}$ sets, never more.

Inverting that gives $N$ directly from the larger of the two scores:

$$W = \max(X, Y) \quad\Longrightarrow\quad N = 2W - 1$$

The loser's score plays no part at all. That is the counter-intuitive bit, and it is worth seeing why: the match ends when the winner clinches, so the winner's tally pins down the required majority and hence $N$, whatever the loser happened to accumulate along the way. Sample cases 1 and 4 share nothing except $\max = 5$ and $\max = 8$ respectively, and the answers $9$ and $15$ follow from those alone.

Sample case 3 is the extreme: $(99, 1)$ gives $N = 197$, a best-of-197 match that was stopped as soon as Sonu reached $99$ — long before $197$ sets could be played.

The result is automatically odd, since $2W - 1$ is odd for any integer $W$, which satisfies the problem's requirement without a check. The guarantee $X \neq Y$ means there is always a unique winner and no ambiguity about which score to take.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # They stop the moment the winner clinches, so the winner's score is
        # exactly the majority (n + 1) // 2. The loser's score is irrelevant.
        out.append(str(2 * max(x, y) - 1))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The loser's score is irrelevant.** They stop the instant the winner clinches, so the winner holds exactly the majority $\frac{N+1}{2}$ and $N = 2\max(X,Y) - 1$ regardless of the other score — the sample's $(2,5)$ and $(4,8)$ both depend on only the larger number.
- **A one-set match** ($\max = 1$): $N = 1$.
- **$X \neq Y$ is guaranteed**, so there is always a clear winner and the maximum is unambiguous.
- **Largest input** ($\max = 100$): $N = 199$.
- The answer is always odd, which is what "best of $N$" requires — an even $N$ could end level.

## Dry run

| $X$ | $Y$ | winner's sets | $N = 2\max - 1$ | output |
|---:|---:|---:|---:|---|
| 2 | 5 | 5 | 9 | `9` |
| 8 | 10 | 10 | 19 | `19` |
| 99 | 1 | 99 | 197 | `197` |
| 4 | 8 | 8 | 15 | `15` |

In row 1, winning $5$ of a best-of-$9$ clinches it, which is why the loser's $2$ never enters.

---

Same problem in rating order (#101 of 486): [../../by-rating/101-BESTOFTENNIS.md](../../by-rating/101-BESTOFTENNIS.md)
