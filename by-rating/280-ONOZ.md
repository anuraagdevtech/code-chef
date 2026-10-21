# 280. Digital clock

> [`ONOZ`](https://www.codechef.com/problems/ONOZ) &middot; difficulty **1482** &middot; time limit **2s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Brute Force |
| **Technique** | Enumerating a small product space |
| **CodeChef tags** | `Data Structures`, `Algorithms`, `String`, `Brute Force` |
| **Complexity class** | Product of two sizes $O(n m)$ |
| **Time** | $O(H \cdot M)$ per test case |
| **Space** | $O(1)$ |

## Question

*3:33*

It's possible for all the digits displayed on a digital clock in the *hours:minutes* format to be identical. The time shown above (*3:33*) is an example of such a situation. Other examples are *2:2* and *1:11*. Note that the digits of *33:33* are identical, but it is not a valid time on a usual digital clock.

The above example was for a usual 24-hour format digital clock. Let's consider a more general clock, where an hour lasts **M** minutes and a day lasts **H** hours (therefore, the clock can show any number of hours between **0** and **H-1**, inclusive, and any number of minutes between **0** and **M-1**, inclusive). Both the hours and the minutes are shown **without leading zeroes** in decimal notation and their separator (e.g., ':') doesn't matter.

Can you tell how many minutes during a day will the digital clock have identical digits displayed on it?

**Input**

- The first line of the input contains an integer **T** - the number of test cases.

- Each of the next **T** lines contains two space-separated integers **H** and **M** for one test case.

**Output**

For each test case, output a single line corresponding to the answer of the problem.

**Constraints**

- **1 ≤ T ≤ 50**

- **1 ≤ H, M ≤ 100**

## Constraints

- 1 ≤ T ≤ 50
- 1 ≤ H, M ≤ 100

## Sample

**Sample input**

```
6
24 60
34 50
10 11
10 12
11 11
1 1
```

**Sample output**

```
19
20
10
11
10
1
```

<details><summary>Explanation</summary>

**Example case 1.** A clock shows two identical digits at times *0:0*, *1:1*, .., *9:9*, three identical digits at times *11:1*, *22:2*, *1:11*, *2:22*, *3:33*, *4:44*, *5:55*, and four identical digits at times *11:11* and *22:22*. So, there are 19 minutes during which the time displayed by the clock will have identical digits.

**Example case 2.** Compared to the previous case, the clock doesn't show *5:55*, but can show *33:3* and *33:33*.

**Example case 6.** In this example, our day consists of one hour and one hour consists of one minute. Hence, the entire day is just 1 minute - the only time the digital clock will display is 0:0 during the entire day, (i.e. the entire hour, i.e. entire minute). And 0:0 has all digits identical, so the answer is 1.

</details>

## Approach

With $H, M \leq 100$ there are at most $10^4$ distinct times in a day, so simply generate every one and test it. No formula is needed, and deriving one would be delicate given the leading-zero rule.

For each hour $h \in [0, H)$ and minute $m \in [0, M)$, build the displayed string by concatenating the two numbers **without leading zeros** — exactly what `str(h) + str(m)` gives — and check that every character matches the first.

The leading-zero rule is the whole subtlety, and it is why `str()` is the right tool. The time $0{:}0$ displays as `00`, which is all-identical and counts; but $0{:}5$ displays as `05`, which is not. A formulation that pads to two digits would classify these differently, and one that strips zeros entirely would lose the $0{:}0$ case.

The separator does not matter, so concatenation is a faithful model of the display.

Sample case 6 is the minimal clock: $H = M = 1$ admits only $0{:}0$, which qualifies, giving $1$. Sample cases 3 and 4 differ only in $M$ ($11$ against $12$), and the extra minute $11$ pairs with hour $1$ to display `111`, lifting the count from $10$ to $11$ — a good illustration of why multi-digit times must be handled rather than assumed invalid.

At $T \leq 50$ the total work is $5 \times 10^5$ string builds, comfortably fast.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        h, m = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        count = 0
        for hour in range(h):
            hs = str(hour)                 # no leading zeros, as displayed
            for minute in range(m):
                s = hs + str(minute)
                if s.count(s[0]) == len(s):
                    count += 1
        out.append(str(count))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **No leading zeros** in the display, so hour $10$ shows as `10` and already contains two different digits — it can never qualify however the minutes fall. Zero-padding to two digits would change the answer.
- **Multi-digit matches do count.** The $H = 10$, $M = 12$ case gains one over $H = 10$, $M = 11$ purely from hour $1$ with minute $11$, giving `111`.
- **Hour $0$ with minute $0$ shows `00`**, which always qualifies — so the answer is never zero for valid input.
- **$H$ and $M$ are exclusive upper bounds**: hours run $0 \dots H-1$ and minutes $0 \dots M-1$.
- **$H = M = 1$** → the single time `00`, giving `1`.
- **$H, M \leq 100$** means at most $10^4$ pairs per case, so the direct double loop is affordable at $T \leq 50$; the uniform test `s.count(s[0]) == len(s)` handles any digit count.

## Dry run

$H = 11$, $M = 11$.

| hour | minute that matches | display |
|---:|---:|---|
| 0 | 0 | `00` |
| 1 | 1 | `11` |
| … | … | … |
| 9 | 9 | `99` |
| 10 | none | `10…` already mixed |

Ten qualifying times, so `10`. Raising $M$ to $12$ adds hour $1$ with minute $11$ (`111`), giving `11`.

---

Same problem grouped by topic: [../docs/brute-force/ONOZ.md](../docs/brute-force/ONOZ.md)
