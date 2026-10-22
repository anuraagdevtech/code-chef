---
topic: Bit Manipulation
subtopic: Grouping a halving process by bit length
time: $O(N \log N + L)$, where $L$ is the number of moves reached
space: $O(N + L)$
---
Two facts turn this from a simulation into bookkeeping.

**The divided values come out in non-increasing order.** Hussain always removes the maximum, and what he puts back, $\lfloor v/2 \rfloor$, is strictly smaller than $v$. So no later move can divide something larger than an earlier one.

**The whole sequence is known up front.** Every value ever divided is some $\lfloor a / 2^k \rfloor > 0$ for an initial element $a$. Combined with the first fact, the answer sequence is simply that entire multiset sorted descending — and the $Q$-th query reads off position $Q$.

That multiset is up to $63N \approx 6 \times 10^7$ entries, so it must not be built at once. **Bit length** slices it perfectly. A positive $v$ with $\mathrm{bitlen}(v) = \ell$ satisfies $2^{\ell-1} \leq v < 2^{\ell}$, so every value of bit length $\ell$ precedes every value of bit length $\ell - 1$ in the descending order. And each starting $a$ contributes **exactly one** value per bit length $\ell \leq \mathrm{bitlen}(a)$, namely $a \gg (\mathrm{bitlen}(a) - \ell)$ — halving drops the bit length by exactly one each time.

So let $L_\ell$ be the sorted list of values of bit length $\ell$. The recurrence is the payoff:

$$L_\ell = \mathrm{merge}\bigl(\{\, v \gg 1 : v \in L_{\ell+1} \,\},\; \{\, a : \mathrm{bitlen}(a) = \ell \,\}\bigr)$$

Right-shifting a sorted list keeps it sorted, so each level is a merge of two sorted runs — no level is ever re-sorted from scratch. Process $\ell$ from $63$ down, keeping a running count of moves consumed, and answer each query from the level whose block contains it. Because the queries arrive in increasing order, one descending sweep serves them all, and the sweep can stop at the last query instead of running the process out.

The sample makes the levels visible. From $\{8,5,3,1\}$: level 4 is $[8]$, level 3 is $[5,4]$ (the $4$ being $8 \gg 1$), level 2 is $[3,2,2]$, level 1 is $[1,1,1,1]$. Reading positions $1,2,3,4,6,8$ off that concatenation gives $8, 5, 4, 3, 2, 1$.

Elements can reach $2^{63}$, which overflows signed 64-bit arithmetic in C++ — Python's integers make this a non-issue, though at $N, M = 10^6$ this problem is really sized for a compiled language.

## Edge cases

- **The maximum always has the greatest bit length**, so every number of bit length $b$ is divided before any of bit length $b-1$ — which groups the whole process into $64$ levels.
- **Halving preserves order**, so a level's values are the previous level's halves merged with the newly arriving numbers — both sorted runs, so one sort per level suffices.
- **Within a level the divisions run in descending order**, which is why a query is answered by counting from the *end* of the ascending level list.
- **Queries arrive in chronological order**, which lets a single pointer sweep them as the levels are built — no per-query search.
- **A number reaching $0$ leaves the multiset**, which the level construction handles implicitly: halving a value of bit length $1$ gives $0$, which never enters the next level.
- **Empty levels are skipped**, since a bit length may have no numbers at all.
- **Values reach $2^{63}$**, so $65$ buckets are needed and the arithmetic must be exact.
- **The loop breaks once every query is answered**, which matters when $N$ is large and the queries are all early.

## Dry run

Sample: the multiset $\{8, 5, 3, 1\}$.

| bit length | values at this level (ascending) | moves | answers |
|---:|---|---:|---|
| 4 | $8$ | 1 | move 1 → `8` |
| 3 | $4, 5$ | 2–3 | move 2 → `5`, move 3 → `4` |
| 2 | $2, 2, 3$ | 4–6 | move 4 → `3`, move 6 → `2` |
| 1 | $1, 1, 1, 1$ | 7–10 | move 8 → `1` |

Each level's divisions go from its largest value down, which is why move $4$ takes the $3$ rather than a $2$.
