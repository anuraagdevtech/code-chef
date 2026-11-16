---
topic: Number Theory
subtopic: Polynomials over GF(2) split at the highest exponent bit
time: $O(60 \cdot 2^{M} \cdot M)$ worst case per test case with memoisation, $M \le 15$
space: $O(60 \cdot 2^{M})$ worst case
complexity_note: Auxiliary space excludes the buffered input and output.
---
Only parities matter, so work with polynomials over GF(2). Two equal exponents cancel, so first reduce the list to the set of exponents that occur an odd number of times.

Over GF(2), $(1+x)^{2^b} = 1 + x^{2^b}$. Let $2^b$ be the highest bit of the largest exponent and split the set into the exponents that have this bit (group $H$, with the bit removed) and those that do not (group $L$). Then

$$\sum (1+x)^{a} = P_L(x) + (1 + x^{2^b}) P_H(x),$$

where both $P_L$ and $P_H$ have degree below $2^b$. The coefficients below $x^{2^b}$ are those of $P_L + P_H$, and the coefficients from $x^{2^b}$ up are those of $P_H$, so

$$W = W(P_L + P_H) + W(P_H).$$

$P_L + P_H$ is again a sum of powers of $(1+x)$, over the symmetric difference of the two exponent sets, so the same routine recurses on smaller exponents. A single exponent $a$ contributes $2^{\text{popcount}(a)}$ odd coefficients by Lucas' theorem, and an empty set contributes 0.

## Edge cases

- Equal exponents cancel in pairs, so `2 5 5` gives 0.
- An exponent 0 is the constant polynomial 1 and is handled by the single-exponent rule ($2^0 = 1$).
- Exponents go up to about $2^{60}$, so nothing can be expanded explicitly.
- The memo is keyed by the sorted tuple of exponents; identical sub-problems appear often after the symmetric difference.

## Dry run

Exponents `{1, 3}`. The highest bit of 3 is 2.

- $H$: 3 has the bit, leaving 1, so $H = \{1\}$.
- $L$ together with $H$ by symmetric difference: 1 (from $L$) and 1 (from $H$) cancel, leaving the empty set.

$W = W(\emptyset) + W(\{1\}) = 0 + 2^{1} = 2$, matching $(1+x) + (1+x)^3 = 2 + 4x + 3x^2 + x^3$.
