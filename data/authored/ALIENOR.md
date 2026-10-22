---
topic: Bit Manipulation
subtopic: Single-bit values are necessary and sufficient
time: $O(NK)$ per test case
space: $O(K)$
---
The condition quantifies over all $2^K - 1$ targets, but it reduces to a check on $K$ of them.

**Necessity.** Consider the target $j = 2^b$, a single bit. An OR only ever adds bits, so every chosen $A_i$ must be a subset of $\{b\}$ — i.e. $0$ or $2^b$ — and at least one must be non-zero. So the array must literally **contain** the string with a single $1$ at position $b$, for every $b$.

**Sufficiency.** If all $K$ single-bit strings are present, any $j$ is the OR of the single bits in its own binary expansion, so every target is reachable.

So the whole problem is: does $A$ contain each of the $K$ powers of two? That reduces an apparent $2^K$ search to one pass over the input, which is what makes $K$ up to $100$ — and $2^K$ astronomically large — irrelevant. Note the all-zero string and any string with two or more bits set are useless for this test, though they are harmless.

The samples are built around it. Sample 1 has exactly `01` and `10`, so both single bits are present and the answer is `YES`. Sample 3 holds `001`, `010` and `100` among six strings, again `YES` — the extra multi-bit strings `011` and `101` add nothing. Sample 2 is the instructive failure: it has `010` and `100` but no `001`, so the target $j = 1$ is unreachable even though `011` *contains* that bit, and the answer is `NO`.

## Edge cases

- **Only the $K$ single-bit strings matter.** An OR can never lose bits, so producing a value with exactly one bit set requires an element that *is* that single bit — and conversely, having all $K$ of them lets any $j$ be assembled from its own bits.
- **So the whole question reduces to $K$ membership tests**, not an enumeration of $2^K - 1$ targets.
- **The strings are built by position, not by integer value**, since each $A_i$ is a $K$-character string: bit $b$ corresponds to `0`*b + `1` + `0`*(K-b-1).
- **An all-zeros element is harmless but useless** — it contributes nothing to any OR, so its presence neither helps nor hurts.
- **A missing single bit is fatal** however many other strings are present: the second sample has $4$ distinct strings and still fails for want of `001`.
- **$j$ ranges over $1 \dots 2^K - 1$**, excluding $0$, which is why an all-zeros array is not required to be representable.
- **Sum of $N \leq 500$**, so a set of the raw byte strings is ample.

## Dry run

Second sample: $K = 3$ with strings `000`, `010`, `011`, `100`.

| bit | required string | present? |
|---:|---|:---:|
| 0 | `100` | yes |
| 1 | `010` | yes |
| 2 | `001` | **no** |

Output `NO`. The value $j = 1$ (binary `001`) is unreachable, since every element containing that bit — namely `011` — also carries another bit that no OR can remove.
