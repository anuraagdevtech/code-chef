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

###Note:
Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100; the centurial years that are exactly divisible by 400 are still leap years. For example, the year 1900 is not a leap year; the year 2000 is a leap year.

###Input:

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, in the format $yyyy:mm:dd$

###Output:
For each testcase, output in a single line the required answer.

###Constraints
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

> CodeChef tags: `Mathematics`
