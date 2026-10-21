---
topic: Basic Math
subtopic: Tournament rounds, and separators between them
time: $O(1)$ per test case
space: $O(1)$
---
Each round halves the field, so starting from $N$ teams the tournament runs

$$R = \log_2 N$$

rounds before one team remains. The problem guarantees $N$ is a power of two, so this is an exact integer.

Rounds take $A$ minutes each, and breaks of $B$ minutes sit **between** rounds with none after the last. That makes breaks separators, not round markers, so there are $R - 1$ of them:

$$R \cdot A + (R - 1) \cdot B$$

This is the same *$n$ items have $n-1$ gaps* structure as the gaming-breaks problem, and it is again the likeliest place to go wrong — charging $R$ breaks adds a phantom $B$ to every answer.

Computing $R$ deserves care. `math.log2(n)` returns a float, and for large powers of two the result can land a hair off an integer, so `int(math.log2(n))` may round down to $R - 1$. Since $N$ is a power of two, `n.bit_length() - 1` gives $\log_2 N$ exactly using pure integer arithmetic — `(1024).bit_length()` is $11$, so $R = 10$. That is the right habit whenever an exact integer logarithm is needed.

Checking sample 4: $N = 1024$ gives $R = 10$, so $10 \times 23 + 9 \times 9 = 230 + 81 = 311$.

With $T$ up to $10^5$, reading the whole input at once and emitting one joined write matters more here than the arithmetic does.

## Edge cases

- **$N = 2$**: a single round and **zero** breaks, so the answer is just $A$. The $(\text{rounds} - 1)$ factor must not go negative or invent a break.
- **Breaks sit between rounds**, so there is always one fewer break than round — the usual separator-versus-group trap.
- **$N$ is guaranteed a power of two**, which is what makes `bit_length() - 1` an exact $\log_2$. For a non-power it would silently round and give the wrong round count.
- **Largest input** ($N = 2^{20}$): twenty rounds and nineteen breaks.

## Dry run

| $N$ | rounds $\log_2 N$ | breaks | play $\text{rounds} \cdot A$ | rest $(\text{rounds}-1) \cdot B$ | output |
|---:|---:|---:|---:|---:|---|
| 4 | 2 | 1 | 20 | 5 | `25` |
| 16 | 4 | 3 | 120 | 15 | `135` |
| 32 | 5 | 4 | 225 | 60 | `285` |
| 1024 | 10 | 9 | 230 | 81 | `311` |
