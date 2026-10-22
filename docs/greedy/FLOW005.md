[&larr; 82. Single-use Attack](SINGLEUSE.md) &middot; [Index](../../README.md) &middot; [127. Peaceful Party &rarr;](MAYOR_PARTY.md)

# 104. Smallest Numbers of Notes

> CodeChef problem code [`FLOW005`](https://www.codechef.com/problems/FLOW005) &middot; difficulty **750** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Greedy change-making in a canonical system |
| **Time** | $O(k)$ per test case, $k = 6$ denominations |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Consider a currency system in which there are notes of six denominations, namely, Rs. 1, Rs. 2, Rs. 5, Rs. 10, Rs. 50, Rs. 100.
 If the sum of Rs. **N** is input, write a program to compute smallest number of notes that will combine to give Rs. **N**.

**Input**

The first line contains an integer **T**, total number of testcases. Then follow **T** lines, each line contains an integer **N**.

**Output**

For each test case, display the smallest number of notes that will combine to give **N**, in a new line.

**Constraints**

- 1 **≤** **T** **≤** 1000

- 1 **≤** **N** **≤** 1000000

## Constraints

- 1 ≤ T ≤ 1000
- 1 ≤ N ≤ 1000000

## Sample

**Sample input**

```
3 
1200
500
242
```

**Sample output**

```
12
5
7
```

## Approach

Minimise the number of notes summing to $N$, using denominations $\{1, 2, 5, 10, 50, 100\}$. Walk the denominations from largest to smallest, taking as many of each as fit:

```
count += n // d
n %= d
```

The greedy works here, but it is worth being precise about *why*, because greedy change-making is **not** correct in general. A currency system is called **canonical** when the greedy algorithm is optimal for every amount, and this one is. The classic counterexample is $\{1, 3, 4\}$: greedily making $6$ takes $4 + 1 + 1$ for three coins, while $3 + 3$ needs only two. For such systems the minimum requires dynamic programming, at $O(N \cdot k)$.

What saves this system is that each denomination divides fairly neatly into the next, so taking a large note never strands the remainder in a position where smaller notes do worse. The same property licensed the greedy in the $\{5, 10\}$ coins problem.

Iterating over a tuple of denominations, rather than writing six divisions by hand, keeps the structure visible and makes the ordering requirement explicit — the list **must** be sorted descending, since processing $1$ first would consume the whole amount in ones.

Sample case 3: $242 \to$ two $100$s, leaving $42 \to$ four $10$s, leaving $2 \to$ one $2$. That is $2 + 4 + 1 = 7$ notes.

## Solution (Python)

```python
import sys

# Must be descending: greedy takes the largest note that still fits.
NOTES = (100, 50, 10, 5, 2, 1)


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        count = 0
        for d in NOTES:
            count += n // d
            n %= d
        out.append(str(count))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(k)$ per test case, $k = 6$ denominations
- **Space:** $O(1)$

## Edge cases

- **An amount needing the smallest notes** ($N = 242$): two hundreds, four tens and a two — seven notes, so the tail of the denomination list genuinely gets used.
- **Smallest inputs**: $N = 1$ takes one note, $N = 3$ takes two ($2 + 1$).
- **The list must be descending.** Iterating the denominations the other way round takes $N$ ones and returns $N$ instead of the minimum.
- **Greedy is optimal here because the system is canonical** — with notes $1, 2, 5, 10, 50, 100$ the largest-first rule always reaches the minimum. That is a property of *this* set, not of greedy in general: for a set like $\{1, 3, 4\}$ and $N = 6$, greedy takes $4 + 1 + 1$ while the optimum is $3 + 3$.

## Dry run

$N = 242$, taking the largest note that still fits at each step:

| note | taken | remainder |
|---:|---:|---:|
| 100 | 2 | 42 |
| 50 | 0 | 42 |
| 10 | 4 | 2 |
| 5 | 0 | 2 |
| 2 | 1 | 0 |
| 1 | 0 | 0 |

Seven notes in total, so the output is `7`.

> CodeChef tags: `Mathematics`, `Algorithms`

---

Same problem in rating order (#80 of 486): [../../by-rating/080-FLOW005.md](../../by-rating/080-FLOW005.md)
