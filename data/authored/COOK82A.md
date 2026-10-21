---
topic: Conditionals & Case Work
subtopic: Parsing labelled input, then a single logical condition
time: $O(1)$ per test case
space: $O(1)$
---
Real Madrid leads by $3$ points and takes the title in every scenario **except one**: Real Madrid loses *and* Barcelona wins. So the condition for Barcelona is a single conjunction:

$$\text{RealMadrid} < \text{Malaga} \quad\text{and}\quad \text{Barcelona} > \text{Eibar}$$

Everything else — Real Madrid drawing, Barcelona drawing, both winning, both losing — leaves Real Madrid champion. Enumerating the nine win/draw/loss combinations is unnecessary once the exception is written down directly.

The parsing is the part that needs care. Each scenario gives **four lines of `name goals`, in arbitrary order**, so the values cannot be read positionally. Building a dictionary from team name to goals and then looking up the four teams by name is the robust approach; assuming a fixed order would pass sample case 1 and fail case 2, where the lines begin with Malaga rather than Barcelona.

Note which pairs actually play each other: Barcelona faces Eibar, and Real Madrid faces Malaga. Comparing Barcelona's goals against Real Madrid's would be meaningless, since they are in different matches.

Sample case 1 shows a draw not counting as a loss: Real Madrid and Malaga both score $1$, so despite Barcelona beating Eibar the title stays with Real Madrid. Sample case 2 is the sole losing scenario.

Team names must be matched exactly — `RealMadrid` is written as one word with no space.

## Edge cases

- **A draw keeps the title.** Barcelona needs Real Madrid to *lose* and itself to *win*, both strictly. The first sample has a $1$&ndash;$1$ draw in Real Madrid's match, so the title stays — a non-strict comparison would hand it to Barcelona.
- **Both conditions are needed**: Real Madrid slipping is not enough if Barcelona also fails to win.
- **The four lines arrive in arbitrary order**, so they must be indexed by team name rather than by position. The first sample lists Barcelona first and the second lists Malaga first, which is exactly what breaks a positional parse.
- **Goals can be $0$** and go up to $20$, so no assumption about scorelines holds.

## Dry run

First sample: Barcelona $2$, Malaga $1$, RealMadrid $1$, Eibar $0$.

| condition | value | met? |
|---|---|:---:|
| RealMadrid $<$ Malaga | $1 < 1$ | no |
| Barcelona $>$ Eibar | $2 > 0$ | yes |

One condition fails, so `RealMadrid`. In the second sample $2 < 3$ and $8 > 6$ both hold, so `Barcelona`.
