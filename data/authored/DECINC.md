---
topic: Conditionals & Case Work
subtopic: Single divisibility branch
time: $O(1)$
space: $O(1)$
---
One number in, one number out: if $N$ is divisible by $4$ print $N + 1$, otherwise print $N - 1$.

$$\text{answer} = \begin{cases} N + 1 & N \equiv 0 \pmod 4 \\ N - 1 & \text{otherwise} \end{cases}$$

The sample is the "otherwise" branch — $5$ is not a multiple of $4$, so the answer is $4$.

Two details are worth pinning down. First, there is **no $T$** here: the input is a single number, not a count followed by test cases. Reading a test-case count would consume $N$ itself and then wait for input that never arrives.

Second, $N = 0$ is inside the constraints, and $0$ *is* divisible by $4$ — the branch taken is the increment, giving $1$. It is tempting to treat zero as a special case, but `0 % 4 == 0` is true and the general rule already handles it. The only input that could produce a negative answer would be an $N$ below $1$ that is not a multiple of $4$, which the constraints exclude.

## Edge cases

- **$N = 0$**: $0$ is divisible by $4$, so the answer is $0 + 1 = 1$. Taking the other branch would print $-1$, which is why the divisibility test has to come first.
- **$N = 4$** (smallest positive multiple of four): $5$.
- **$N = 1$**: not a multiple of four, so $0$ — the result may legitimately be zero.
- **$N = 1000$** (the bound, and a multiple of four): $1001$.
- **Input shape**: a single integer with *no* leading test-case count, unlike almost every other problem here — reading a count first would consume the value itself.

## Dry run

Input is the single value $N = 5$.

| step | value |
|---|---|
| $N$ | $5$ |
| $N \bmod 4$ | $1$ |
| branch | not divisible, so $N - 1$ |
| output | `4` |
