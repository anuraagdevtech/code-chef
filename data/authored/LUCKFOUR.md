---
topic: Strings
subtopic: Counting a digit
time: $O(d)$ per number
space: $O(1)$
---
Count how many times the digit `4` appears in each number. Treating the input as **text** makes this a single call to `str.count`, with no arithmetic at all:

```python
s.count("4")
```

The arithmetic alternative peels digits with `n % 10` and `n //= 10`, incrementing when the digit is $4$. It is equally correct, but needs a guard for $n = 0$ — a `while n > 0` loop never executes and reports $0$ fours, which is right here only by luck, since $0$ genuinely contains no `4`. The constraints do admit $0$, so it is worth noticing.

Reading digits as characters sidesteps that entirely and is faster in Python, since `count` runs in C. With $T$ up to $10^5$, the per-call overhead is what dominates, so bulk-reading the whole input and emitting one joined write matters more than the counting itself.

The sample covers the shapes that matter: a number of all-fours-and-sevens (`447474` → $4$), one with no fours (`228` → $0$), one where `4` sits at the end (`6664` → $1$), and one where it leads (`40` → $1$). Position is irrelevant — every occurrence counts.

Note the problem asks only about the digit $4$, not about "lucky numbers" in the usual CodeChef sense of numbers built from $4$s and $7$s.
