---
topic: Basic Math
subtopic: Recovering a whole from a percentage
time: $O(1)$ per test case
space: $O(1)$
---
An offer of $A$ dollars for $10\%$ of the company implies the investor values the whole company at ten times that:

$$V_1 = \frac{A}{0.10} = 10A$$

Likewise $B$ dollars for $20\%$ implies

$$V_2 = \frac{B}{0.20} = 5B$$

Devendra takes the higher valuation, so the answer is a three-way comparison of $10A$ against $5B$.

The instinct to compare $A$ with $B$ directly is what the problem is testing, and it is wrong: a smaller cheque can imply a larger company if it buys a smaller slice. Sample case 3 makes the point — $B = 500$ dwarfs $A = 200$, yet $10 \times 200 = 2000$ against $5 \times 500 = 2500$ still favours the second investor, while in case 2 the larger cheque loses.

Both multipliers are exact integers, so no floats are needed; dividing by $0.1$ would be the fragile way to write the same thing. The comparison can even be halved to $2A$ versus $B$, though keeping the full valuations makes the reasoning legible.

Equal valuations are possible — case 1 has both at $1000$ — so the `ANY` branch must be handled explicitly rather than folded into one of the others.

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
