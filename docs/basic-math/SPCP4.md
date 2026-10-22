[&larr; 144. Car Range](CARRANGE.md) &middot; [Index](../../README.md) &middot; [154. Keplers Law &rarr;](KEPLERSLAW.md)

# 145.  Am I Lucky!

> CodeChef problem code [`SPCP4`](https://www.codechef.com/problems/SPCP4) &middot; difficulty **941** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Remainders paired off |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

A school has organized a field trip for a class of $N$ students, of which $X$ students are boys, and the remaining students are girls.
Everyone is excited to go trekking, and must form groups of size exactly $K$ to do so. However, boys will only form groups among themselves, and girls will only form groups among themselves.
Both boys and girls will form *as many* groups as possible.

The remaining students can either dance around a bonfire, or just read books.
Dancing around the bonfire requires a pair of one girl and one boy, while reading is done alone.

Reading is much more boring than dancing, so students will try to avoid it.
What's the minimum number of students who will be engaged in reading?

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The only line of each test case contains three space-separated integers $N$, $X$ and $K$ — the total number of students, the number of boys and the number of students in each trekking group.

**Output**

* For each test case, output on a new line the  the minimum number of students engaged in reading.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N, K \leq 10^9$
- $1 \leq X \leq N$

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
3
12 4 3
15 10 5
8 8 3
```

**Sample output**

```
1
0
2
```

<details><summary>Explanation</summary>

**Test case $1$:** There are $4$ boys and $8$ girls. The boys will form $1$ group of $3$ members and the girls will form $2$ groups of $3$ members each.
Of the remaining $1$ boy and $2$ girls, one boy and one girl will pair up to dance around the bonfire, while the remaining girl will read books.

**Test case $2$:** There are $10$ boys and $5$ girls. The boys will form $2$ groups of $5$ members each, and the girls will form one group containing $5$ members. So, there is no one left for reading in this case.

**Test case $3$:** There are $8$ boys and $0$ girls. The boys will form $2$ groups of $3$ members each; now, the remaining $2$ boys will have to read books as there is no partner to pair up for dancing.

</details>

## Approach

There are $X$ boys and $N - X$ girls. Each gender forms as many full groups of $K$ as possible, so the students left over are the remainders:

$$r_b = X \bmod K, \qquad r_g = (N - X) \bmod K$$

Those leftovers can dance, but only in mixed pairs — one boy with one girl. So $\min(r_b, r_g)$ pairs form, consuming $2\min(r_b, r_g)$ students, and the rest must read:

$$r_b + r_g - 2\min(r_b, r_g) = |r_b - r_g|$$

The absolute difference is the whole answer, and it says something clean: dancing cancels the leftovers against each other, and only the **imbalance** is stranded.

Note that the group-forming is not a choice — the statement says both genders form as many groups as possible — so there is no optimisation deciding whether to leave more students out for dancing. If it were a choice, holding back students to form more dancing pairs could sometimes beat this, and the problem would be considerably harder.

Sample case 3 is the one-sided case: $8$ boys and no girls leave $r_b = 2$ and $r_g = 0$, so both leftover boys read. Sample case 2 divides evenly on both sides, leaving nobody. Sample case 1 has $r_b = 1$ and $r_g = 2$, so one pair dances and a single girl reads.

With $N$ and $K$ up to $10^9$ only the closed form is viable, but the arithmetic is trivial.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x, k = map(int, data[1 + 3 * i:4 + 3 * i])
        boys_left, girls_left = x % k, (n - x) % k
        # Dancing pairs cancel leftovers off; only the imbalance reads.
        out.append(str(abs(boys_left - girls_left)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Both remainders zero** (the second row, $15\,10\,5$): nothing is left over on either side, so $0$.
- **Everyone on one side** (the third row, where $X = N$): the other group is empty, so its remainder is $0$ and the answer is the first remainder alone.
- **The remainders cancel rather than add.** Leftover members of the two groups pair off with each other, so only the imbalance shows — taking the sum instead of the absolute difference would report $3$ on the first row instead of $1$.
- **$K = 1$**: every remainder is $0$, so the answer is always $0$.

## Dry run

The three values are $N$, then $X$, then $K$.

| $N$ | $X$ | $K$ | $X \bmod K$ | $(N{-}X) \bmod K$ | difference | output |
|---:|---:|---:|---:|---:|---:|---|
| 12 | 4 | 3 | 1 | 2 | 1 | `1` |
| 15 | 10 | 5 | 0 | 0 | 0 | `0` |
| 8 | 8 | 3 | 2 | 0 | 2 | `2` |

Row 3 has an empty second group.

---

Same problem in rating order (#150 of 486): [../../by-rating/150-SPCP4.md](../../by-rating/150-SPCP4.md)
