---
topic: Constructive
subtopic: Split powers of two until the required length
time: $O(N+\log K)$ per test case
space: $O(N+\log K)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Represent the score as a sum of powers of two, with no power larger than $2^{25}$. This is a representation with the fewest allowed letters. Splitting one power $2^b$ into two copies of $2^{b-1}$ preserves the score and increases the length by one. Repeated splitting reaches every length from this minimum to $K$.

Reject lengths outside that interval. Otherwise split larger powers until exactly $N$ terms remain and map exponent zero to `a`, exponent one to `b`, and so on.

## Edge cases

- The alphabet ends at exponent 25.
- Each character has positive score, so $N>K$ is impossible.
- Any ordering of the final characters is valid.

## Dry run

For `N=4, K=5`, start with `4+1`, split `4` into `2+2`, then split one `2` into `1+1`: the letters can be `baaa`.
