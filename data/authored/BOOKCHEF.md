---
topic: Sorting
subtopic: Sorting on a composite key
time: $O(M \log M)$
space: $O(N + M)$
---
The ordering rule has two levels, which map directly onto a **tuple sort key**:

1. posts from *special* friends come first, regardless of popularity;
2. within each of those two groups, higher popularity comes first.

So sort by `(not special, -popularity)`. The first component is `False` (i.e. $0$) for special posts and `True` ($1$) otherwise, so special posts sort ahead; the negated popularity turns Python's ascending sort into a descending one on that field.

Expressing both levels in one key avoids a two-pass partition-and-merge, and makes the precedence explicit — the special flag dominates because it comes first in the tuple.

Membership of the special list is tested against a `set`, giving $O(1)$ lookups rather than an $O(N)$ scan per post.

The guarantee that **no two posts share a popularity** means the sort is fully determined, so no stability question arises and any correct implementation produces the same order.

In the sample, friends $1$ and $2$ are special. Their posts have popularities $1$ and $2$, so they lead with the more popular first — `WinterIsComing` then `WhoDoesntLoveChefBook`. The remaining posts follow by popularity, so the $10$-popularity post from friend $3$ beats the $3$-popularity post from friend $4$ — note it outranks both special posts on popularity yet still comes after them.

Only the contents are printed, not the identifiers. There is **no $T$**: the first line holds $N$ and $M$.

## Edge cases

- **Two sort keys in one tuple.** `friend not in special` puts special friends first (since `False < True`), and `-popularity` orders each group most-popular first — so one `sort` does the whole algorithm.
- **A special friend's post outranks every non-special post** regardless of popularity, which is exactly what the sample shows: a post of popularity $1$ from a special friend beats one of popularity $10$ from another.
- **Within the special group popularity still rules**, so the two special posts come out as $2$ then $1$.
- **Negating the popularity is what gives a descending order** inside an ascending sort, avoiding a custom comparator.
- **No tie rule is specified** for equally popular posts in the same group, so the post text serves as a deterministic third key.
- **There is no test-case count**: the first line holds $N$ and $M$ together.
- **Friend ids are matched as raw byte tokens** against the special set, safe because the input has no leading zeros.

## Dry run

Special friends $\{1, 2\}$.

| post | friend | special? | popularity | sort key |
|---|---:|:---:|---:|---|
| `WhoDoesntLoveChefBook` | 1 | yes | 1 | $(\text{False}, -1)$ |
| `WinterIsComing` | 2 | yes | 2 | $(\text{False}, -2)$ |
| `TheseViolentDelights…` | 3 | no | 10 | $(\text{True}, -10)$ |
| `ComeAtTheKing…` | 4 | no | 3 | $(\text{True}, -3)$ |

Sorted: `WinterIsComing`, `WhoDoesntLoveChefBook`, `TheseViolentDelights…`, `ComeAtTheKing…`
