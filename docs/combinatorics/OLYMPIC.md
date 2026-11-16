[&larr; 616. Chef World](CHEFWD.md) &middot; [Index](../../README.md) &middot; [618. The Uncountable Ways &rarr;](CNTWAYS.md)

# 617. Gifts at Olympics

> CodeChef problem code [`OLYMPIC`](https://www.codechef.com/problems/OLYMPIC) &middot; difficulty **2696** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Burnside for reversal, with multinomials updated along a sweep over box sizes |
| **Time** | $O(S + Q \log Q + E \log N)$, $S$ the total number of chocolates and $E = \sum O(\sqrt{count})$ breakpoints |
| **Space** | $O(S + Q + E)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

The Olympic Games, world's foremost sports competition,
will be hosted by London next month.
Tens of thousands of participants from over 200 nations will be participating this year.
Each game has only 3 winners, so the organizers have decided to give special chocolate gift pack to each participant.

A huge number of chocolates have just arrived from **N** different villages, numbered 1 to **N**.
The organizers have decided the number of chocolates to be given to each participant.
This is given in **count**, where **count**[*i*] is the number of chocolates from *i*^th village,
to be placed in each gift pack.
Now they need to order boxes for these chocolates.
A box of size **S** can store at most **S** chocolates.
A gift pack is made as follows.

Each of the **N** villages is assigned a unique colored box
and chocolates from a village are placed only in boxes assigned to it.
The organizers always want to minimize the number of boxes in each gift pack.
E.g., for given **N** = 3 villages and **count** = {3, 12, 7}, suppose colors assigned are *A*, *B*, *C*.
If size of each box is **S** = 4, then we need 1 box of color A, 3 boxes of color B and 2 boxes of color C.
All the boxes for a gift pack are then packed in a row using transparent wrapper.
So in the above example, a gift pack can be "*ABBBCC*" or "*ABCBCB*" etc.

To make everyone feel special, no two participants are given same gift packs.
Two gift packs are different if and only if they have the different order of colored boxes, even in reverse order.
For example "*ABBBCC*" is same as "*ABBBCC*" and also same as "*CCBBBA*".
Given **Q** queries, each specifying the size of a box **S**,
find the total number of different gift packs possible if we use boxes of size **S** each.
Output the result modulo 1000000007 (10^9+7).

**Input**

The first line has an integer **N**. The second line has the array **count**, **N** space separated integers.
The next line has integer **Q**, followed by **Q** lines, each having an integer size **S**.

1 ≤ **N**, **count**[*i*], **Q** ≤ 100000 (10^5)

1 ≤ sum of all **count**[*i*] ≤ 100000 (10^5)

1 ≤ **S** ≤ 1000000000 (10^9)

**Output**

Output **Q** lines, one for each query,
the total number of different gift packs possible, using boxes of size **S**, specified in that query modulo 1000000007 (10^9+7).

**Example**

```
**Input:**
3
5 3 12
4
4
5
2
12

**Output:**
30
10
2320
3
```

**Explanation:**

In the last query, size of each box **S** = 12.

Suppose the colors assigned to the 3 villages are *A*, *B*, *C* respectively,
we need 1 box of each color.

Only 3 different gift packs can be made. They are "*ABC*", "*ACB*", "*BAC*".

## Constraints

- 1 <= N, count[i], Q <= 10^5.
- 1 <= sum of all count[i] <= 10^5.
- 1 <= S <= 10^9.

## Approach

With box size $s$, village $i$ needs $b_i = \lceil count_i / s \rceil$ boxes of its own colour, and the boxes are laid in a row where a row and its mirror image are the same pack. By Burnside's lemma for the two-element group {identity, reversal}

$$\text{answer} = \frac{\text{all arrangements} + \text{palindromic arrangements}}{2}.$$

All arrangements: the multinomial $(\sum b_i)! / \prod b_i!$. A palindrome exists only if at most one $b_i$ is odd; it is determined by its first half, so there are $(\lfloor \sum b_i / 2 \rfloor)! / \prod \lfloor b_i / 2 \rfloor!$ of them.

Recomputing this per query is too slow. Instead sort the distinct query sizes and sweep $s$ upwards: $\lceil c / s \rceil$ takes only $O(\sqrt{c})$ different values, so precompute for each distinct village count the sizes at which its box count drops, and at each such breakpoint patch the running total, the number of odd counts and the two denominators (multiply by old factorial, divide by new). Equal village counts are merged and handled with one modular power.

## Solution (Python)

```python
import sys
from collections import Counter


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(tokens)
    village = [next(tokens) for _ in range(n)]
    queries = [next(tokens) for _ in range(next(tokens))]
    MOD = 1000000007
    chocolates = sum(village)
    fact = [1] * (chocolates + 1)
    for i in range(1, chocolates + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (chocolates + 1)
    inv_fact[chocolates] = pow(fact[chocolates], MOD - 2, MOD)
    for i in range(chocolates, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    events = {}
    total = chocolates
    denominator = half_denominator = 1
    odd = 0
    for value, multiplicity in Counter(village).items():
        denominator = denominator * pow(inv_fact[value], multiplicity, MOD) % MOD
        half_denominator = half_denominator * pow(inv_fact[value // 2], multiplicity, MOD) % MOD
        odd += value % 2 * multiplicity
        size = 1
        old = value
        while old > 1:
            end = (value - 1) // (old - 1)
            size = end + 1
            new = (value + size - 1) // size
            events.setdefault(size, []).append((old, new, multiplicity))
            old = new
    answers = {}
    keys = iter(sorted(events))
    nextsize = next(keys, None)
    for size in sorted(set(queries)):
        while nextsize is not None and nextsize <= size:
            for old, new, multiplicity in events[nextsize]:
                total += (new - old) * multiplicity
                odd += (new % 2 - old % 2) * multiplicity
                denominator = denominator * pow(fact[old] * inv_fact[new] % MOD, multiplicity, MOD) % MOD
                half_denominator = half_denominator * pow(fact[old // 2] * inv_fact[new // 2] % MOD, multiplicity, MOD) % MOD
            nextsize = next(keys, None)
        ways = fact[total] * denominator % MOD
        pal = fact[total // 2] * half_denominator % MOD if odd <= 1 else 0
        answers[size] = (ways + pal) * ((MOD + 1) // 2) % MOD
    print('\n'.join((str(answers[size]) for size in queries)))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(S + Q \log Q + E \log N)$, $S$ the total number of chocolates and $E = \sum O(\sqrt{count})$ breakpoints
- **Space:** $O(S + Q + E)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- More than one odd box count means no palindromic row at all.
- A box size at least as large as every count gives one box per village: $N!$ arrangements, halved (plus palindromes only when $N \le 1$).
- The same box size may be queried repeatedly; answers are stored per distinct size.
- Division by 2 is multiplication by $(p + 1) / 2$.

## Dry run

Villages `5 3 12`.

- $s = 4$: boxes `2 1 3`. All: $6! / (2! \, 1! \, 3!) = 60$. Two odd counts, so no palindromes. Answer $60 / 2 = 30$.
- $s = 2$: boxes `3 2 6`. All: $11! / (3! \, 2! \, 6!) = 4620$. One odd count; half sizes `1 1 3` give $5! / 3! = 20$ palindromes. Answer $(4620 + 20) / 2 = 2320$.
- $s = 12$: boxes `1 1 1`: $(6 + 0) / 2 = 3$.

---

Same problem in rating order (#707 of 735): [../../by-rating/707-OLYMPIC.md](../../by-rating/707-OLYMPIC.md)
