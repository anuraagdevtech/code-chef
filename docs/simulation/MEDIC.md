[&larr; 235. Full Barrier Alchemist](PIPSQUIK.md) &middot; [Index](../../README.md) &middot; [334. Sudhanva and Books &rarr;](SUDBOOKS.md)

# 278. When to take medicine

> CodeChef problem code [`MEDIC`](https://www.codechef.com/problems/MEDIC) &middot; difficulty **1522** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Simulation |
| **Technique** | Where a parity rule breaks at month boundaries |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

You visit a doctor on a date given in the format $yyyy:mm:dd$. Your doctor suggests you to take pills every alternate day starting from that day. You being a forgetful person are pretty sure won’t be able to remember the last day you took the medicine and would end up in taking  the medicines on wrong days.

So you come up with the idea of taking medicine on the dates whose day is odd or even depending on whether $dd$ is odd or even. Calculate the number of pills you took on right time before messing up for the first time.

**Note:**
Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100; the centurial years that are exactly divisible by 400 are still leap years. For example, the year 1900 is not a leap year; the year 2000 is a leap year.

**Input:**
- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, in the format $yyyy:mm:dd$

**Output:**
For each testcase, output in a single line the required answer.

**Constraints**
- $ 1 \leq T \leq 1000 $
- $ 1900 \leq yyyy \leq 2038 $
- $yyyy:mm:dd$ is a valid date

## Constraints

- $ 1 \leq T \leq 1000 $
- $ 1900 \leq yyyy \leq 2038 $
- $yyyy:mm:dd$ is a valid date

## Sample

**Sample input**

```
1
2019:03:31
```

**Sample output**

```
1
```

<details><summary>Explanation</summary>

You can take pill on the right day only on 31st March. Next you will take it on 1st April which is not on the alternate day.

</details>

## Approach

The doctor wants a pill every **two days**; the patient instead takes one on every date whose day-of-month has the same parity as the start. Inside a month those agree perfectly — $d, d+2, d+4, \ldots$ are both alternate days and same-parity dates. The rules can only diverge at a **month boundary**.

So the question is when the crossing preserves the two-day spacing. Let $\ell$ be the length of the month just ending.

- **Odd start parity.** The last qualifying date is $\ell$ if $\ell$ is odd, else $\ell - 1$. The next is day $1$ of the following month. The gap is $1$ when $\ell$ is odd and $2$ when $\ell$ is even.
- **Even start parity.** The last qualifying date is $\ell$ if $\ell$ is even, else $\ell - 1$, and the next is day $2$. The gap is $2$ when $\ell$ is even and $3$ when $\ell$ is odd.

Both cases give the same rule: **the sequence survives a month boundary exactly when that month has an even number of days.** Parity of the start date does not matter at all.

Even-length months are April, June, September, November (all $30$) and February in a common year ($28$); every $31$-day month and a leap February break the chain. Since no two even-length months are adjacent, the run spans at most two months — but the code loops anyway rather than relying on that.

Counting within a month from day $d$ is $\lfloor (\ell - d)/2 \rfloor + 1$, and the next month restarts at day $1$ or $2$ according to the parity.

The sample, `2019:03:31`, starts on an odd date in a $31$-day month: one pill on March 31, then the chain breaks, since the patient would take the next on April 1 — a single day later. The answer is $1$.

Leap years follow the usual rule, so February can be either parity depending on the year.

## Solution (Python)

```python
import sys


def is_leap(y: int) -> bool:
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)


def month_len(y: int, m: int) -> int:
    if m == 2:
        return 29 if is_leap(y) else 28
    return 30 if m in (4, 6, 9, 11) else 31


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        y, m, d = (int(p) for p in data[1 + i].decode().split(":"))
        parity = d % 2
        total = 0
        while True:
            ell = month_len(y, m)
            total += (ell - d) // 2 + 1
            # The chain survives the boundary only from an even-length month.
            if ell % 2:
                break
            m += 1
            if m == 13:
                m, y = 1, y + 1
            d = 1 if parity else 2
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The chain survives a month boundary only from an even-length month.** From an odd-length month, stepping by two off the last correct day lands on the wrong parity: a $31$-day month's odd chain ends at $31$, and $+2$ gives day $2$ of the next month, which is even. That single observation is the whole problem.
- **An even-length month preserves parity either way**: the odd chain ends at $\ell-1$ and continues at day $1$; the even chain ends at $\ell$ and continues at day $2$.
- **February is the interesting month**: $28$ days is even and the chain continues, while a leap year's $29$ is odd and it breaks.
- **Leap years need the full rule** — divisible by $4$, except centuries unless divisible by $400$ — since the range $1900$–$2038$ includes $1900$ (not a leap year) and $2000$ (one).
- **Starting on the last day of an odd month** gives exactly one pill, which is the sample: $31$ March yields $1$.
- **The count within a month is $(\ell - d)/2 + 1$**, which handles both parities with the same expression.
- **The year may roll over**, so December is followed by January of the next year — and December has $31$ days, so the chain always breaks there anyway.

## Dry run

Starting $2019{:}03{:}31$ — day $31$, odd parity, in a $31$-day month.

| month | length | days taken | count | boundary survives? |
|---|---:|---|---:|---|
| March 2019 | 31 | $31$ | 1 | **no** ($31$ is odd) |

Output `1`. Had the start been $2019{:}04{:}2$, April's $30$ days would give $15$ pills and the chain would carry into May.

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#307 of 486): [../../by-rating/307-MEDIC.md](../../by-rating/307-MEDIC.md)
