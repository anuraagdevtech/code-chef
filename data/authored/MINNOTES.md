---
topic: Number Theory
subtopic: Prefix and suffix GCD after one removal
time: $O(N \log V)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
If employee $i$ is changed, every other salary must be divisible by the denomination. Its largest possible value is the GCD $g$ of those other salaries. Set the changed salary to $g$, which needs one note. The exact cost is $(S-A_i)/g+1$; no smaller denomination improves it.

Prefix and suffix GCDs give $g$ for every removed employee in constant many GCD calls. Minimise this cost. For one employee, choose their existing salary as the denomination and pay one note.

## Edge cases

- $N=1$ must bypass the GCD of an empty array.
- The changed salary must be positive: it costs one note, not zero.
- Equal salaries already need exactly $N$ notes.

## Dry run

For salaries `[1,2,3]`, excluding `3` leaves GCD `1`. Replace `3` by `1`, requiring `1+2+1=4` notes.
