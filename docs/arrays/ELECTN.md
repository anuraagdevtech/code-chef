# 28. Elections in Chefland

> CodeChef problem code [`ELECTN`](https://www.codechef.com/problems/ELECTN) &middot; difficulty **604** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Counting with a predicate |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Election season has started in Chefland and the election commission wants to know the count of eligible voters.

There are $N$ people in Chefland where the age of the $i^{th}$ person in $A_i$.
Given that a person needs to be **at least** $X$ years old to vote, find the number of eligible voters.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $X$ — the number of people in Chefland, and the minimum age required for a person to vote in Chefland.
    - The next line contains $N$ space-separated integers, where the $i^{th}$ integer denotes the age of the $i^{th}$ person.

**Output**

For each test case, output on a new line, the number of eligible voters in Chefland.

## Constraints

- $1 \leq T \leq 200$
- $1 \leq N \leq 100$
- $1 \leq A_i, X \leq 100$

## Sample

**Sample input**

```
4
4 3
5 3 1 2
3 2
1 3 4
4 2
2 1 2 4
5 6
1 2 3 4 5
```

**Sample output**

```
2
2
3
0
```

<details><summary>Explanation</summary>

**Test case $1$:** The minimum age to vote in Chefland is $3$ years. There are $2$ people with age greater than equal to $3$ and thus, there are $2$ eligible voters.

**Test case $2$:** The minimum age to vote in Chefland is $2$ years. There are $2$ people with age greater than equal to $2$ and thus, there are $2$ eligible voters.

**Test case $3$:** The minimum age to vote in Chefland is $2$ years. There are $3$ people with age greater than equal to $2$ and thus, there are $3$ eligible voters.

**Test case $4$:** The minimum age to vote in Chefland is $6$ years. There are no people with age greater than equal to $6$ and thus, there are no eligible voters.

</details>

## Approach

A person votes when their age is **at least** $X$, so the answer is the number of array entries satisfying $A_i \geq X$ — one linear scan with a counter, no sorting and no auxiliary storage.

In Python, `sum(1 for a in ages if a >= x)` expresses it directly; summing the boolean generator counts the matches. The structure is identical to the to-do-list problem, with only the comparison direction and the threshold changed, which is the point of seeing both: "count the elements passing a test" is a single reusable shape.

The wording "at least $X$" makes the comparison inclusive, so someone aged exactly $X$ *can* vote. Sample case 3 leans on this — with $X = 2$ and ages $2, 1, 2, 4$, the two people aged exactly $2$ both count, giving $3$. Using a strict `>` would wrongly return $1$.

The answer can legitimately be zero, as in case 4 where nobody reaches the voting age of $6$, so there is no need to special-case an empty result.

Each test case spans two lines and $N$ varies between cases, so a cursor into the flat token stream is the tidiest way to walk the input.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, x = int(data[pos]), int(data[pos + 1])
        ages = data[pos + 2:pos + 2 + n]
        pos += 2 + n
        # "At least X" is inclusive, so age == x still votes.
        out.append(str(sum(1 for a in ages if int(a) >= x)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **An age exactly $X$ votes**, since the rule is "at least $X$". The sample's third case has $X = 2$ with two voters aged exactly $2$, and both count — an off-by-one gives $1$ instead of $3$.
- **Nobody eligible**: the last sample case sets $X = 6$ above every age, so the answer is $0$.
- **Everybody eligible** when $X$ is at or below the minimum age.
- **$N = 1$**: a single citizen, counted or not.
- Only the tally is needed, so the ages never have to be stored or sorted.

## Dry run

| $X$ | ages | aged $\geq X$ | output |
|---:|---|---|---:|
| 3 | $5, 3, 1, 2$ | $5, 3$ | `2` |
| 2 | $1, 3, 4$ | $3, 4$ | `2` |
| 2 | $2, 1, 2, 4$ | $2, 2, 4$ | `3` |
| 6 | $1, 2, 3, 4, 5$ | none | `0` |

Row 3 is the inclusive boundary: both twos vote.

> CodeChef tags: `Basic Programming Concepts`

---

Same problem in rating order (#35 of 486): [../../by-rating/035-ELECTN.md](../../by-rating/035-ELECTN.md)
