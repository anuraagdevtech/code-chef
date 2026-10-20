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
