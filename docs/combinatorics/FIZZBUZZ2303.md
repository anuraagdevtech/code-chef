[Index](../../README.md) &middot; [122. Farmers League &rarr;](LEAGUE.md)

# 71. Chef Fantasy 11

> CodeChef problem code [`FIZZBUZZ2303`](https://www.codechef.com/problems/FIZZBUZZ2303) &middot; difficulty **739** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Ordered pairs (permutations) |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

All of Chef's friends are playing fantasy cricket based upon the ODI World Cup, and Chef would like to join them.

For a certain cricket match, Chef has decided upon his team of $11$ players. However, he hasn't yet decided who should be the captain and who should be the vice-captain.

He's narrowed his decision down to $N$ players out of the $11$, from which he'll choose one to be the captain and one to be the vice captain.
How many different choices does he have?

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and the only line of each testcase contains a single integer $N$, the number of players Chef is considering.

**Output**

For each test case, output on a new line the number of possible choices of captain and vice-captain.

## Constraints

- $1 \leq T \leq 10$
- $2 \leq N \leq 11$

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
2
2
3
```

**Sample output**

```
2
6
```

<details><summary>Explanation</summary>

**Test case $1$:** With $N = 2$, there are only two possibilities: one of the players must be selected as the captain, and the other will become the vice-captain.

**Test case $2$:** It can be shown that there are $6$ possibilities in total for captain/vice-captain choices.

</details>

## Approach

Chef picks a captain and a vice-captain from $N$ players. The two roles are **distinct**, so choosing Alice as captain and Bob as vice-captain is a different outcome from the reverse — the order matters.

There are $N$ ways to fill the captaincy and, with that player used up, $N - 1$ remaining for vice-captain:

$$N \cdot (N-1)$$

This is the permutation count $P(N, 2) = \frac{N!}{(N-2)!}$, not the combination count $\binom{N}{2} = \frac{N(N-1)}{2}$. Halving is the classic error here, and the sample pins it down: $N = 3$ gives $6$, not $3$. The division by $2$ in $\binom{N}{2}$ exists precisely to discard orderings, which is the wrong thing to do when the two slots mean different jobs.

The rule of thumb: ask whether swapping the two chosen items changes the answer. If it does, count permutations; if it does not, count combinations.

The team size of $11$ is scenery — only $N$, the shortlist, enters the formula. The constraint $N \geq 2$ guarantees at least one valid choice, so no empty case arises.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Captain and vice-captain are different roles, so order matters.
        out.append(str(n * (n - 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Smallest squad** ($N = 2$): two arrangements — either player can captain while the other is vice-captain.
- **Order matters.** Captain and vice-captain are different roles, so the count is the ordered pair $N(N-1)$ and *not* the combination $\binom{N}{2} = N(N-1)/2$. Using the combination halves every answer.
- **One player cannot hold both roles**, which is why the second factor is $N - 1$ rather than $N$.
- **Largest input** ($N = 11$): $110$ arrangements.

## Dry run

| $N$ | captain choices | vice-captain choices | total $N(N-1)$ | output |
|---:|---:|---:|---:|---|
| 2 | 2 | 1 | 2 | `2` |
| 3 | 3 | 2 | 6 | `6` |

For $N = 3$ the six orderings are $(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)$ — the pairs $(1,2)$ and $(2,1)$ counting separately is exactly what makes this a permutation count.

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#78 of 486): [../../by-rating/078-FIZZBUZZ2303.md](../../by-rating/078-FIZZBUZZ2303.md)
