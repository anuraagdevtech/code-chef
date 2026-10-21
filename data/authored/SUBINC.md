---
topic: Arrays
subtopic: Counting subarrays by maximal runs
time: $O(N)$ per test case
space: $O(1)$
---
A subarray is non-decreasing exactly when **every adjacent pair inside it** is non-decreasing, so the property is determined entirely by the positions where $A_i > A_{i+1}$. Those breaks cut the array into maximal non-decreasing runs, and a subarray is valid iff it lies wholly inside one run. A run of length $L$ contains

$$\binom{L+1}{2} = \frac{L(L+1)}{2}$$

subarrays, and summing over the runs gives the answer.

The one-pass form avoids even finding the runs explicitly. Let $r_i$ be the length of the longest non-decreasing stretch ending at $i$:

$$r_i = \begin{cases} r_{i-1} + 1 & A_i \geq A_{i-1} \\ 1 & \text{otherwise}\end{cases}$$

Then $r_i$ is precisely the number of valid subarrays *ending* at $i$ — their left endpoints are the last $r_i$ positions — so the total is $\sum_i r_i$. This is the same count regrouped by right endpoint instead of by run, and it needs no second pass.

Every single element is a valid subarray, so the answer is never below $N$; the second sample is that minimum, $N = 1$ giving $1$.

For $[1, 4, 2, 3]$ the running lengths are $1, 2, 1, 2$, summing to $6$. Equivalently the runs are $[1,4]$ and $[2,3]$, each contributing $\tfrac{2 \cdot 3}{2} = 3$.

The count reaches $\tfrac{N(N+1)}{2} \approx 5 \times 10^9$ for a fully sorted array, which overflows 32-bit arithmetic — C++ needs `long long` here, while Python is safe by default.
