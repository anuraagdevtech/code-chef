---
topic: Sets
subtopic: Keep everything except the forbidden value
time: $O(N)$ per test case
space: $O(N)$
---
MEX here is the smallest **positive** integer missing, so MEX $= M$ says two things: every value in $1, \ldots, M-1$ must appear among the chosen elements, and $M$ must not.

The second condition is the only reason to discard anything. Every element other than $M$ is harmless — values above $M$ and repeats of values below $M$ cannot change the MEX, since the MEX is determined solely by which of $1, 2, \ldots$ are present. So the maximum selection is "everything except the copies of $M$":

$$\text{answer} = N - \mathrm{cnt}(M)$$

and that selection automatically satisfies the first condition, provided each of $1, \ldots, M-1$ occurs in $A$ at all. If any of them is missing, no selection can work and the answer is $-1$.

Note the problem's MEX starts from $1$, not $0$ — so $0$ never matters, and the constraint $A_i \geq 1$ means every element is a candidate value.

The sample has $A = [1,2,4]$ and $M = 3$. Both $1$ and $2$ are present and no element equals $3$, so all three elements are kept and the MEX of $\{1,2,4\}$ is indeed $3$. Had the array been $[1,2,3,4]$, the $3$ would have to go, leaving $3$ elements again — but from a longer array.

A set is enough for the presence test and a single counter for $\mathrm{cnt}(M)$, so one pass suffices. Checking $1 \ldots M-1$ costs $O(M) \leq O(N)$.

## Edge cases

- **The MEX is over *positive* integers**, so $0$ never enters the reasoning and the required values are $1 \dots M-1$.
- **Only copies of $M$ must be dropped.** Every other element is harmless: values above $M$ cannot lower the MEX, and duplicates of the small values cannot either — so the answer is $N$ minus the count of $M$.
- **A missing value below $M$ makes it impossible** → $-1$, since the MEX would land there instead.
- **$M$ may be absent entirely**, in which case nothing is dropped and the answer is $N$ — the sample, where $M = 3$ does not occur.
- **$M \leq N$ is guaranteed**, so the required run $1 \dots M-1$ could in principle fit.
- **$A_i$ reaches $10^9$** while $M \leq N$, so the large values are counted but never need inspecting individually.
- **The membership test compares encoded tokens**, which is safe because the input has no leading zeros.

## Dry run

Sample: $N = 3$, $M = 3$, $A = 1, 2, 4$.

| required value | present? |
|---:|:---:|
| 1 | yes |
| 2 | yes |

Both are there, and $M = 3$ appears $0$ times — so everything can be kept. Output `3`, with the chosen set $\{1, 2, 4\}$ whose MEX is $3$.
