---
topic: Constructive
subtopic: Cancelling a XOR with a 1-2-3 triple
time: $O(N)$ per test case
space: $O(N)$
---
Start from the identity permutation $[1, 2, \ldots, N]$. Every adjacent difference is $1$, and there are $N-1$ of them, so the XOR is $1$ when $N-1$ is odd and $0$ when it is even.

**$N$ odd.** Then $N-1$ is even, the $1$s cancel in pairs, and the identity permutation already works.

**$N$ even.** The identity leaves a stray $1$ that needs cancelling. Rearranging the opening to $[2, 3, 1, 4, 5, \ldots, N]$ does it. The differences become

$$\underbrace{|2-3|,\ |3-1|,\ |1-4|}_{1,\ 2,\ 3} ,\ \underbrace{1,\ 1,\ \ldots,\ 1}_{N-4 \text{ of them}}$$

The leading triple satisfies $1 \oplus 2 \oplus 3 = 0$, so it vanishes. And because $N$ is even, $N-4$ is even as well, so the trailing $1$s cancel in pairs. The whole XOR is $0$.

Note that the third difference, $|1 - 4| = 3$, is the junction into the untouched tail — the reordering of three elements is what manufactures the $1, 2, 3$ triple out of what would otherwise be three $1$s.

So $[2, 3, 1, 4, 5, \ldots, N]$ is attractive for every even $N \geq 4$.

**$N = 2$ is impossible.** Both permutations, $[1,2]$ and $[2,1]$, give the single difference $1$, whose XOR is $1 \neq 0$. With only one term there is nothing to cancel against, so the answer is $-1$.

Checking $N = 6$: $[2,3,1,4,5,6]$ gives differences $1, 2, 3, 1, 1$, and $1 \oplus 2 \oplus 3 \oplus 1 \oplus 1 = 0$.

**Any attractive permutation is accepted**, so this is judged by a checker. The samples show different arrangements — `3 2 1` for $N=3$ and `5 2 3 6 4 1` for $N=6$ — both equally valid, so a verbatim diff would report a false mismatch.

## Edge cases

- **$N = 2$ is impossible.** The only adjacent pair gives a difference of $1$, and a single $1$ cannot XOR to $0$, so the answer is $-1$. This is the lone infeasible case.
- **Odd $N$ needs no construction at all.** The identity permutation has $N - 1$ adjacent differences, every one of them $1$, and $N - 1$ is even — so they cancel in pairs.
- **Even $N \geq 4$ needs a seed.** Starting $2, 3, 1$ produces differences $1, 2, 3$, which XOR to $0$ because $1 \oplus 2 = 3$; the remaining $N - 4$ differences are all $1$ and there is an even number of them, so the whole XOR stays $0$.
- **$N = 4$** is the smallest even case: $2, 3, 1, 4$ gives exactly $1, 2, 3$ and nothing else.
- **This answer differs from the sample's** at $N = 3$ and $N = 6$ (`1 2 3` against `3 2 1`, and `2 3 1 4 5 6` against `5 2 3 6 4 1`); the statement asks for *any* attractive permutation, so a special judge verifies the XOR.
- **Sum of $N \leq 2 \cdot 10^5$**: each line is built by joining a range, with no per-element Python arithmetic.

## Dry run

$N = 6$ gives $A = 2, 3, 1, 4, 5, 6$.

| adjacent pair | difference |
|---|---:|
| $2, 3$ | 1 |
| $3, 1$ | 2 |
| $1, 4$ | 3 |
| $4, 5$ | 1 |
| $5, 6$ | 1 |

$1 \oplus 2 \oplus 3 = 0$, and the trailing $1 \oplus 1 = 0$, so the total XOR is `0`.
