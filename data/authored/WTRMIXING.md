---
topic: Conditionals & Case Work
subtopic: Signed difference against one-sided supplies
time: $O(1)$ per test case
space: $O(1)$
---
Each litre of hot water raises the temperature by one degree and each litre of cold lowers it by one, so the reachable temperatures form the interval

$$[A - Y,\; A + X]$$

and the question is whether $B$ lies inside it.

The cleaner way to think about it is through the signed difference $d = B - A$, because its **sign** selects which supply is relevant:

- $d > 0$: the bath must warm up, needing $d$ litres of hot water, so the test is $d \leq X$. The cold supply is irrelevant.
- $d < 0$: it must cool, needing $|d|$ litres of cold, so the test is $|d| \leq Y$.
- $d = 0$: nothing to do, always `YES`.

The trap is treating the two supplies as interchangeable. They are not — hot water cannot cool a bath. Sample case 3 is exactly this: it needs to drop $10$ degrees and there are $10$ litres of *hot* water available but only $9$ of cold, so the answer is `NO` despite the totals looking sufficient. Sample case 4 is the mirror image, needing one degree of warming with no hot water at all.

The interval form `a - y <= b <= a + x` expresses the same rule in a single line without branching, and is the version used below.

Sample case 2 covers $d = 0$, where both supplies go unused.
