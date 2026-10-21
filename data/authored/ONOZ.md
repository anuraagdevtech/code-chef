---
topic: Brute Force
subtopic: Enumerating a small product space
time: $O(H \cdot M)$ per test case
space: $O(1)$
---
With $H, M \leq 100$ there are at most $10^4$ distinct times in a day, so simply generate every one and test it. No formula is needed, and deriving one would be delicate given the leading-zero rule.

For each hour $h \in [0, H)$ and minute $m \in [0, M)$, build the displayed string by concatenating the two numbers **without leading zeros** — exactly what `str(h) + str(m)` gives — and check that every character matches the first.

The leading-zero rule is the whole subtlety, and it is why `str()` is the right tool. The time $0{:}0$ displays as `00`, which is all-identical and counts; but $0{:}5$ displays as `05`, which is not. A formulation that pads to two digits would classify these differently, and one that strips zeros entirely would lose the $0{:}0$ case.

The separator does not matter, so concatenation is a faithful model of the display.

Sample case 6 is the minimal clock: $H = M = 1$ admits only $0{:}0$, which qualifies, giving $1$. Sample cases 3 and 4 differ only in $M$ ($11$ against $12$), and the extra minute $11$ pairs with hour $1$ to display `111`, lifting the count from $10$ to $11$ — a good illustration of why multi-digit times must be handled rather than assumed invalid.

At $T \leq 50$ the total work is $5 \times 10^5$ string builds, comfortably fast.

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
