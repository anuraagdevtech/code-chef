---
topic: Prefix Sums
subtopic: Per-letter counts over hash-delimited blocks
time: $O(|S| + 26 h)$ per test case, where $h$ is the number of '#'
space: $O(|S|)$
---
The extra condition — no '#' of $S$ may lie between the first and second chosen '#', nor between the second and third — is the whole key. It forces the three chosen '#' to be **consecutive among the '#' of $S$**. So if the '#' sit at $h_0 < h_1 < \cdots < h_{k-1}$, the only candidates are the $k-2$ windows $(h_t, h_{t+1}, h_{t+2})$.

With the window fixed, the four sides are independent, since each draws from a disjoint stretch of $S$ and must consist of one repeated character. The best a stretch can give is simply the count of its most frequent letter, so

$$\text{length} = 3 + \mathrm{pre}[t] + \mathrm{gap}[t] + \mathrm{gap}[t+1] + \mathrm{suf}[t+2]$$

where $\mathrm{gap}[i]$ is that maximum over the open interval $(h_i, h_{i+1})$, and $\mathrm{pre}[t]$, $\mathrm{suf}[t]$ are the same over $S[0, h_t)$ and $S(h_t, |S|)$. All four must be non-zero, since every side of the W must be non-empty.

Each quantity is a prefix/suffix tally: sweep left to right keeping 26 running counts and snapshot the maximum at each '#' for $\mathrm{pre}$, sweep right to left for $\mathrm{suf}$, and tally each inter-'#' stretch once for $\mathrm{gap}$. Total work is linear plus $26$ per '#', so no per-window scanning. Note the two middle sides contain no '#' by construction, while the outer stretches may — those are simply ignored, as the sides must be letters.

The third sample is the one that needs the window search: `abc#dda#bb#bb#aca` has four '#', and the later window scores $3 + 2 + 2 + 2 + 2 = 11$ against the earlier window's $10$, because shifting right turns the one-letter prefix `abc` into `abc#dda` with its two `d`s.
