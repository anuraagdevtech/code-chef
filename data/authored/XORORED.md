---
topic: Bit Manipulation
subtopic: Choosing X bit by bit against an OR
time: $O(N)$ per test case
space: $O(1)$
---
XOR acts on each bit separately and OR is also computed per bit, so bit $b$ of the answer depends only on bit $b$ of the array and of $X$. Three cases:

- **Every $A_i$ has the bit set.** Choose $X$'s bit $1$: all of them flip to $0$, so the OR bit is $0$.
- **No $A_i$ has it.** Choose $X$'s bit $0$: they stay $0$, so the OR bit is $0$.
- **Mixed.** Either choice leaves at least one element with the bit set, so the OR bit is $1$ no matter what.

So the uniform bits are all clearable and the mixed bits are all unavoidable. "All set" is exactly a bit of the AND, and "at least one set" exactly a bit of the OR, so with

$$\mathcal{A} = A_1 \,\&\, \cdots \,\&\, A_N, \qquad \mathcal{O} = A_1 \mid \cdots \mid A_N$$

taking $X = \mathcal{A}$ achieves the minimum, which is

$$\mathcal{O} \oplus \mathcal{A} \;=\; \mathcal{O} \;\&\; \neg\mathcal{A}$$

(the XOR equals the AND-NOT because $\mathcal{A} \subseteq \mathcal{O}$ as bit sets). Both reduce in a single pass, so no bit loop is needed.

$X$ is **not unique**: its bits on the mixed positions are free, since they change nothing. The sample $[4, 6]$ has $\mathcal{A} = 4$ and $\mathcal{O} = 6$, so the minimum is $2$; our $X = 4$ gives $\{0, 2\}$ and the sample's $X = 6$ gives $\{2, 0\}$ — different arrays, same OR, both accepted by the judge.

Note $X$ may freely exceed the array values; here it is bounded by $\mathcal{A} \leq \max A_i$ anyway.

## Edge cases

- **Each bit is decided independently.** A bit set in *every* element can be cleared from the OR by setting it in $X$; a bit set in only some elements survives whatever $X$ does; a bit set in none must be left clear in $X$, or every element would gain it.
- **So $X$ is the AND of the whole array** and the minimum OR is the OR with those bits removed, i.e. $(\text{OR}) \oplus (\text{AND})$.
- **The accumulator for the AND starts at $-1$**, which in Python is an all-ones integer of unbounded width — starting at $0$ would make the AND collapse to $0$ immediately.
- **$X$ is not unique.** On a mixed bit either choice gives the same OR, so the sample prints $X = 6$ where this prints $X = 4$; both yield the minimum OR of $2$, and a special judge checks the OR.
- **$N = 1$** makes the AND and the OR both equal $A_1$, so $X = A_1$ and the minimum OR is $0$.
- **All elements equal** likewise gives an OR of $0$.
- **$A_i$ may be $0$**, which forces the AND to $0$ and leaves the OR unchanged.

## Dry run

Sample: $A = 4, 6$ — binary $100$ and $110$.

| bit | in 4 | in 6 | in all? | $X$'s bit | OR's bit after |
|---:|:---:|:---:|:---:|---:|---:|
| 2 | 1 | 1 | **yes** | 1 | 0 |
| 1 | 0 | 1 | no | free | 1 |
| 0 | 0 | 0 | no | 0 | 0 |

With $X = 4$: $0$ and $2$, OR $= 2$. With the sample's $X = 6$: $2$ and $0$, OR $= 2$ as well.
