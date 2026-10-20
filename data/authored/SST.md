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
