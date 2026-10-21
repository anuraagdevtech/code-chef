---
topic: Strings
subtopic: Substring search
time: $O(|S|)$ per test case
space: $O(1)$
---
The feedback is `Good` when the string contains `010` **or** `101` as a substring, and `Bad` otherwise. In Python that is directly

```python
"010" in s or "101" in s
```

The `in` operator on strings performs substring search — not character membership — and short-circuits on the first match.

What these two patterns actually detect is worth naming: a string is `Good` exactly when it contains a character that differs from **both** of its neighbours, i.e. an alternation of length three. A string with no such position must be a run of blocks each at least two long, like `11111110`.

That is sample case 1, which is `Bad` despite containing both digits — having a `0` and a `1` is not enough, they must alternate. A solution checking merely that both characters appear would wrongly call it `Good`.

Sample case 2 is a perfect alternation and matches immediately at position $0$.

Note that the two patterns must be searched as substrings, in order, not as a set of characters. And only one of them is needed, as the statement says explicitly.

With the summed length reaching $6 \times 10^6$, the C-implemented substring search plus bulk input reading matter; a Python-level sliding window over every triple would be far slower for the same result.

## Edge cases

- **The endpoints can never qualify.** `11111110` ends in a single $0$, but that $0$ has only one neighbour, so no character differs from *both* of its neighbours — hence `Bad`. Scanning for "a character unlike the one before it" would wrongly accept this.
- **Both patterns must be tested.** `0010` contains only `010` and `1101` only `101`, so checking one pattern misses half the valid strings.
- **$|S| \leq 2$**: there is no interior position at all, so the answer is always `Bad`.
- **Sum of lengths up to $6 \times 10^6$**: the substring search must be the library's C-level scan rather than a Python loop over indices, and the input is kept as bytes to avoid decoding six megabytes.

## Dry run

| $S$ | contains `010`? | contains `101`? | output |
|---|:---:|:---:|---|
| `11111110` | no | no | `Bad` |
| `10101010101010` | yes | yes | `Good` |

In the first string every character matches at least one neighbour; the trailing $0$ has no right neighbour to differ from.
