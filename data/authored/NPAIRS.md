---
topic: Combinatorics
subtopic: Counting pairs that share an invariant key
time: $O(N)$ per test case
space: $O(N)$
---
Removing the absolute value splits the condition $j - i = |S_j - S_i|$ (with $i < j$) into two linear cases:

$$S_j - S_i = j - i \iff S_j - j = S_i - i$$
$$S_i - S_j = j - i \iff S_i + i = S_j + j$$

So a nice pair is exactly a pair of indices agreeing on the key $S_i - i$, **or** a pair agreeing on the key $S_i + i$. Each case automatically carries its own sign condition — if $S_j - j = S_i - i$ then $S_j - S_i = j - i > 0$, so the absolute value is indeed $j - i$ — and no pair can satisfy both, since that would force $j - i = 0$.

The answer is therefore a sum of two independent tallies, with no double counting to correct:

$$\sum_{v} \binom{\mathrm{cnt}^-_v}{2} \;+\; \sum_{v} \binom{\mathrm{cnt}^+_v}{2}$$

Two `Counter` passes and a sum, giving $O(N)$ with no dependence on the alphabet.

There is also a cheaper-looking shortcut: digits bound $|S_j - S_i| \leq 9$, so only gaps $j - i \leq 9$ can ever qualify, and brute force over those nine offsets is $O(9N)$. That works here, but the key-counting formulation is both faster and indifferent to the alphabet.

The third sample shows the two tallies carrying different weight. For `94241234`, the key $S_i - i$ takes the value $-4$ at four positions, contributing $\binom{4}{2} = 6$, while $S_i + i$ has three colliding pairs, for a total of $9$.
