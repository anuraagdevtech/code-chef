[&larr; 23. Nearest Exit](NEARESTEXIT.md) &middot; [Index](../../README.md) &middot; [27. Qualify the round &rarr;](QUALIFY.md)

# 25. Sasta Shark Tank

> CodeChef problem code [`SST`](https://www.codechef.com/problems/SST) &middot; difficulty **592** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Recovering a whole from a percentage |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Devendra just had a million-dollar idea and he needs funds to startup. He was recently invited to Sasta Shark Tank (A TV show where entrepreneurs pitch their ideas to investors hoping to get investment in return).

He was offered deals from two investors. The first investor offers  $A$ dollars for $10$% of his company and the second investor offers $B$ dollars for $20$% of his company. Devendra will accept the offer from the investor whose valuation of the company is more. Determine which offer will Devendra accept or if both the offers are equally good.

For example, if the first investor offers $300$ dollars for $10$% of the company, then the first investor's valuation of the company is $3000$ dollars since $10$% of $3000 = 300$. If the second investor offers $500$ dollars for $20$% of the company, then the second investor's valuation of the company is $2500$ dollars since $20$% of $2500 = 500$.

**Input**

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $A$ and $B$ - the amount offered by first investor for $10$% of Devendra's company and the amount offered by second investor for $20$% of Devendra's company respectively.

**Output**

For each test case, Output `FIRST` if Devendra should accept the first investor's deal, output `SECOND` if he should accept the second investor's deal, otherwise output `ANY` if both deals are equally good.

You may print each character of the strings in uppercase or lowercase (for example, the strings "FiRst", "First", "FIRST", and "FIrst" will all be treated as identical).

## Constraints

- $1 \leq T \leq 100$
- $100 \leq A,B \leq 10000$
- $A$ and $B$ are multiples of $100$

## Sample

**Sample input**

```
3
100 200
200 100
200 500
```

**Sample output**

```
ANY
FIRST
SECOND
```

<details><summary>Explanation</summary>

**Test case 1:** First investor's valuation of Devendra's company was $1000$ since $10$% of $1000 = 100$ which is the amount he offered for $10$% of the company.

Second investor's valuation of Devendra's company was also $1000$ since $20$% of $1000 = 200$ which is the amount he offered for $20$% of the company.

Therefore he can accept any of the deal.

**Test case 2:** First investor offered a better deal as he valued Devendra's company at $2000$ dollars (since $10$% of $2000 = 200$) compared to the second investor who valued Devendra's company at $500$ dollars (since $20$% of $500 = 100$).

**Test case 3:** Second investor offered a better deal as he valued Devendra's company at $2500$ dollars compared to the first investor who valued Devendra's company $2000$ dollars.

</details>

## Approach

An offer of $A$ dollars for $10\%$ of the company implies the investor values the whole company at ten times that:

$$V_1 = \frac{A}{0.10} = 10A$$

Likewise $B$ dollars for $20\%$ implies

$$V_2 = \frac{B}{0.20} = 5B$$

Devendra takes the higher valuation, so the answer is a three-way comparison of $10A$ against $5B$.

The instinct to compare $A$ with $B$ directly is what the problem is testing, and it is wrong: a smaller cheque can imply a larger company if it buys a smaller slice. Sample case 3 makes the point — $B = 500$ dwarfs $A = 200$, yet $10 \times 200 = 2000$ against $5 \times 500 = 2500$ still favours the second investor, while in case 2 the larger cheque loses.

Both multipliers are exact integers, so no floats are needed; dividing by $0.1$ would be the fragile way to write the same thing. The comparison can even be halved to $2A$ versus $B$, though keeping the full valuations makes the reasoning legible.

Equal valuations are possible — case 1 has both at $1000$ — so the `ANY` branch must be handled explicitly rather than folded into one of the others.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # a buys 10% so values the firm at 10a; b buys 20% so values it at 5b.
        first, second = 10 * a, 5 * b
        out.append("FIRST" if first > second else "SECOND" if second > first else "ANY")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Equal valuations** ($A = 100$, $B = 200$: both imply a firm worth $1000$): the answer is `ANY`, so the tie needs its own branch.
- **Comparing the cash offers directly is wrong.** In that same row the first offer is $100$ and the second $200$, yet they are worth the same, because the first buys only $10\%$ and the second $20\%$. Whoever compares $A$ with $B$ gets this row backwards.
- **Largest inputs** ($A = B = 10000$): $100000$ against $50000$, so `FIRST` — the $10\%$ stake always wins on equal cash.
- **$A$ and $B$ are guaranteed multiples of $100$**, so the implied valuations $10A$ and $5B$ are exact integers and no rounding question arises.

## Dry run

| $A$ (for $10\%$) | $B$ (for $20\%$) | first values firm at $10A$ | second at $5B$ | output |
|---:|---:|---:|---:|---|
| 100 | 200 | 1000 | 1000 | `ANY` |
| 200 | 100 | 2000 | 500 | `FIRST` |
| 200 | 500 | 2000 | 2500 | `SECOND` |

Row 1 is the tie that makes the naive $A$-versus-$B$ comparison fail.

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#32 of 486): [../../by-rating/032-SST.md](../../by-rating/032-SST.md)
