---
topic: Strings
subtopic: Wildcard matching, position by position
time: $O(|X|)$ per test case
space: $O(1)$
---
The strings are the same length and `?` stands for any single lowercase letter. Because the wildcard matches exactly one character — never zero, never many — the comparison stays **positional**: index $i$ of $X$ is matched against index $i$ of $Y$, with no alignment to work out.

Position $i$ matches when

$$X_i = \texttt{?} \quad\text{or}\quad Y_i = \texttt{?} \quad\text{or}\quad X_i = Y_i$$

and the strings match when every position does — `all(...)` over `zip(x, y)`.

The detail easy to miss is that **both** strings may contain wildcards, not just one. A `?` in either position is enough, so the test is symmetric. Sample case 1 relies on it: `s?or?` against `sco??` matches at index $1$ because $X$ has the wildcard, and at index $4$ because *both* do.

Sample case 2 fails at index $1$, where `t` meets `c` — two concrete and different letters, which no wildcard can reconcile.

It is worth noting what makes this far simpler than general wildcard matching. The `*` wildcard, which matches any *number* of characters, breaks the positional correspondence and needs dynamic programming or a two-pointer algorithm with backtracking. With only `?` and equal lengths, a single linear scan suffices.

Strictly, two `?`s matching each other means some letter could fill both — true, since any letter works. So the symmetric rule is correct, not merely convenient.
