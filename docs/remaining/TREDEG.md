# Trees and Degrees (TREDEG)

[Problem statement](https://www.codechef.com/problems/TREDEG) · [Python solution](../../solutions/TREDEG.py)

## Approach

Pruefer codes give degrees one plus occurrence counts, so the answer is (N-2)! times the coefficient of x^(N-2) in (sum (d+1)^K*x^d/d!)^N, divided by N^(N-2). For K=1 use exp(Nx)*(1+x)^N and a linear summand recurrence. Otherwise invert the series, form N*F'/F, and solve the coefficient recurrence by divide-and-conquer convolution. Fixed-width packing into Python integers makes convolution exact without external libraries.

## Complexity

- Time: K=1: O(N). General K: O(N log K + M(Nb) log N), where b=O(log(N MOD squared)) and M(s) is Python's cost to multiply two s-bit integers.
- Space: O(N) coefficient storage plus bigint workspace.

For the largest general-K cases, use PyPy. Local maximum-subtask smoke tests used N=100000 with K=123456789, and N=2000000 with K=1; timings depend on the judge and interpreter. No online acceptance is claimed.
