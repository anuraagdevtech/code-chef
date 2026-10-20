---
topic: Arrays
subtopic: Last index satisfying a predicate
time: $O(N)$ per test case
space: $O(1)$
---
Coefficient $A_i$ belongs to the term $x^i$, so the array index *is* the exponent. The degree is the highest power with a non-zero coefficient, which makes this a scan for the **last non-zero entry** and a report of its index.

Scanning from the right and stopping at the first non-zero is the natural phrasing and exits early. Scanning left to right while remembering the most recent non-zero index works equally well and is what the code below does, since it reads cleanly and still costs one pass.

Three things make this less trivial than it looks.

**Trailing zeros are not part of the polynomial.** Sample case 4 is $1 + 2x + 4x^2 + 0x^3$, whose degree is $2$, not $3$. Taking $N - 1$ as the answer ignores the actual coefficients and fails exactly here.

**Leading zeros are fine.** Sample case 3 is $0 + 0x + 5x^2$, degree $2$ — zeros below the top term are irrelevant, so the scan must look at the highest non-zero index rather than the first.

**Coefficients may be negative.** The test is `!= 0`, not `> 0`. Sample case 2 has $A_0 = -3$, and a truthiness-style check for "positive" would mishandle such terms in general.

The guarantee that at least one coefficient is non-zero means the scan always finds something, so the zero polynomial — whose degree is conventionally undefined or $-\infty$ — never arises. Sample case 1 is the constant polynomial $5$, of degree $0$.
