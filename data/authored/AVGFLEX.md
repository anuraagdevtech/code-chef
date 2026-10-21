---
topic: Arrays
subtopic: Counting against a global threshold
time: $O(N^2)$ per test case at these bounds, or $O(N \log N)$ sorted
space: $O(1)$
---
Student $i$ boasts when the number scoring $\leq A_i$ exceeds the number scoring $> A_i$. Those two groups partition the class, so if $c_i$ is the count of scores $\leq A_i$ then the other group has $N - c_i$, and the condition becomes

$$c_i > N - c_i \quad\Longleftrightarrow\quad 2c_i > N$$

In words: a student boasts exactly when they are at or above the **median** — more precisely, when strictly more than half the class scores no higher than they do.

The complement trick is the useful part: one count plus the total replaces two counts, the same move used for the even/odd and contest-code problems.

Note that $c_i$ counts the student themselves, since $A_i \leq A_i$. Sample case 1, with three identical scores, has $c_i = 3$ for everyone, and $6 > 3$ makes all three boast — ties count in your favour, which is what the `<=` encodes. Using a strict `<` would give $c_i = 0$ and nobody boasting.

Sample case 3 is the same effect with duplicates: the three students scoring $30$ each see $c_i = 4$, comfortably clearing the bar, while the lone $1$ does not.

With $N \leq 100$ the direct $O(N^2)$ double loop is perfectly fine and reads closest to the statement. Sorting once and using binary search would give $O(N \log N)$, which is the shape to reach for if $N$ grew.

## Edge cases

- **The condition is a strict majority including yourself.** With $c$ students scoring at most $A_i$, the rest number $n - c$, so boasting means $c > n - c$, i.e. $2c > n$. This is a median test, *not* a comparison against the average — on $2, 1, 3$ the mean is $2$ and the median rule happens to agree, but the two rules diverge on skewed inputs.
- **Equal scores all boast or none do.** The third row has three $30$s, each seeing $c = 4$ out of $4$, so all three boast; ties are counted in the "less than or equal" side by definition.
- **All scores identical** (the first row): every student sees $c = n$, so everyone boasts.
- **An even $N$ makes the threshold strict.** With $n = 4$, $c = 2$ gives $4 > 4$, which is false — exactly half is not a majority.
- **$A_i$ may be $0$**, which is an ordinary score.
- **$N \leq 100$** makes the quadratic double count affordable; sorting once would give $O(N \log N)$ if the bounds were larger.

## Dry run

Second sample: scores $2, 1, 3$, so $n = 3$.

| student | score | $c$ = count $\leq$ score | $n - c$ | $c > n - c$? |
|---:|---:|---:|---:|:---:|
| 1 | 2 | 2 | 1 | yes |
| 2 | 1 | 1 | 2 | no |
| 3 | 3 | 3 | 0 | yes |

Output `2`.
