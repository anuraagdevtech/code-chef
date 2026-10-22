[&larr; 195. Password](PASSWD.md) &middot; [Index](../../README.md) &middot; [216. Even Splits &rarr;](EVENSPLIT.md)

# 205. Lucky Four

> CodeChef problem code [`LUCKFOUR`](https://www.codechef.com/problems/LUCKFOUR) &middot; difficulty **775** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Counting a digit |
| **Time** | $O(d)$ per number |
| **Space** | $O(1)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

You are given a list of **T** integers, for each of them you have to calculate the number of occurrences of the digit **4** in the decimal representation.

**Input**

The first line of input consists of a single integer **T**, denoting the number of integers in the list.

Then, there are **T** lines, each of them contain a single integer from the list.

**Output**

Output **T** lines. Each of these lines should contain the number of occurrences of the digit **4** in the respective integer from the list.

**Constraints**

- **1** ≤ **T** ≤ **10^5**

- (Subtask 1): **0** ≤ Numbers from the list  ≤ **9** - 33 points.

- (Subtask 2): **0** ≤ Numbers from the list  ≤ **10^9** - 67 points.

## Constraints

- 1 ≤ T ≤ 10^5
- (Subtask 1): 0 ≤ Numbers from the list  ≤ 9 - 33 points.
- (Subtask 2): 0 ≤ Numbers from the list  ≤ 10^9 - 67 points.

## Sample

**Sample input**

```
5
447474
228
6664
40
81
```

**Sample output**

```
4
0
1
1
0
```

<details><summary>Explanation</summary>

There are four 4s in the **447474**, no 4s in **228**, one 4s in **6664**

</details>

## Approach

Count how many times the digit `4` appears in each number. Treating the input as **text** makes this a single call to `str.count`, with no arithmetic at all:

```python
s.count("4")
```

The arithmetic alternative peels digits with `n % 10` and `n //= 10`, incrementing when the digit is $4$. It is equally correct, but needs a guard for $n = 0$ — a `while n > 0` loop never executes and reports $0$ fours, which is right here only by luck, since $0$ genuinely contains no `4`. The constraints do admit $0$, so it is worth noticing.

Reading digits as characters sidesteps that entirely and is faster in Python, since `count` runs in C. With $T$ up to $10^5$, the per-call overhead is what dominates, so bulk-reading the whole input and emitting one joined write matters more than the counting itself.

The sample covers the shapes that matter: a number of all-fours-and-sevens (`447474` → $4$), one with no fours (`228` → $0$), one where `4` sits at the end (`6664` → $1$), and one where it leads (`40` → $1$). Position is irrelevant — every occurrence counts.

Note the problem asks only about the digit $4$, not about "lucky numbers" in the usual CodeChef sense of numbers built from $4$s and $7$s.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    # Counting on the text avoids a digit loop and its n = 0 edge case.
    out = [str(data[1 + i].count(b"4")) for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(d)$ per number
- **Space:** $O(1)$

## Edge cases

- **The number $0$**: the text is `0`, so the count is $0$. Reading the token as text sidesteps the digit-loop special case, where `while n: n //= 10` never executes.
- **All digits are fours** ($444$): the count is $3$.
- **The number $4$ itself**: $1$.
- **No fours at all** ($228$, $81$): $0$.
- **Largest input** ($10^9$): ten digits, so the per-number work stays tiny.
- $T$ reaches $10^5$, so the input must be read in one block rather than line by line.

## Dry run

| number | digits | fours | output |
|---:|---|---:|---|
| 447474 | `4 4 7 4 7 4` | 4 | `4` |
| 228 | `2 2 8` | 0 | `0` |
| 6664 | `6 6 6 4` | 1 | `1` |
| 40 | `4 0` | 1 | `1` |
| 81 | `8 1` | 0 | `0` |

---

Same problem in rating order (#85 of 486): [../../by-rating/085-LUCKFOUR.md](../../by-rating/085-LUCKFOUR.md)
