---
topic: Strings
subtopic: Enumerate feasible alphabet sizes and retain most occurrences
time: $O(|S|+26^2)$ per test case
space: $O(26)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
If exactly $d$ letters appear, each must occur $|S|/d$ times, so $d$ divides $|S|$ and $d\le26$. For a fixed target count $f$, choosing a letter with initial frequency $c$ preserves $\min(c,f)$ characters. The largest frequencies maximise this total.

Pad to 26 frequencies, sort descending, and try all valid $d$. The answer is the length minus the largest number of preservable characters.

## Edge cases

- Newly introduced letters have frequency zero and must be considered.
- A one-letter target is always feasible.
- Skip alphabet sizes that do not divide the length.

## Dry run

For `ABCB`, frequencies are `[2,1,1]`. With two letters appearing twice, preserve `2+1=3` of four positions, requiring one replacement.
