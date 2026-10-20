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
