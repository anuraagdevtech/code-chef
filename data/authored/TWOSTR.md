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

## Edge cases

- **A `?` in either string matches**, so the test is a three-way disjunction rather than substituting one string's wildcards into the other.
- **Both strings may hold `?` in the same position** — the final column of the first sample row — and that still matches, since any single letter satisfies both.
- **Equal lengths are guaranteed**, so `zip` never silently truncates a longer string.
- **One mismatched letter fails the pair.** The second row differs only at index $1$ (`t` against `c`) and every other column matches.
- **Length can be $1$**, giving a single column to compare.
- Only lowercase letters and `?` appear, so no case folding is needed.

## Dry run

| index | X | Y | verdict |
|---:|---|---|---|
| 0 | `s` | `s` | equal |
| 1 | `?` | `c` | wildcard in X |
| 2 | `o` | `o` | equal |
| 3 | `r` | `?` | wildcard in Y |
| 4 | `?` | `?` | wildcard in both |

All five columns pass, so `s?or?` against `sco??` is `Yes`. Replacing index $1$ with a literal `t` fails immediately against `c`, giving the second row's `No`.
