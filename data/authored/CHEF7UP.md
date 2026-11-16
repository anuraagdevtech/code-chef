---
topic: Sorting
subtopic: Parity of the distance to Chef decides which officers can be cornered
time: $O(N \log N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
In every round each officer moves one cell and then Chef moves one cell, so the parity of the distance between Chef and any officer is the same at the start of every round.

An officer at an *even* distance can never be forced out: after the officers move, the gap to Chef is odd, so the cell next to Chef on that side is never needed by that officer, and it can always step towards Chef. Such an officer also shields everybody behind it, because the officers further out always have room to follow.

An officer at an *odd* distance with nothing protecting it is in trouble: Chef walks towards it and it must keep backing away, since an odd gap closes to distance 1 and the officer may not enter Chef's cell. The line is finite, so the whole group being pushed is eventually pressed against the boundary and loses officers one by one.

So look at each side of Chef separately, going outwards from Chef: every officer at odd distance met before the first even-distance officer can be eliminated, and from the first even-distance officer on nobody can. The answer is the sum of the two counts; Chef runs away exactly when that is all $N$ officers, otherwise he is eventually caught.

## Edge cases

- Only the parity of $P_i - C$ and the order of the officers on each side matter.
- An even-distance officer adjacent in order to Chef protects its whole side.
- Chef can clear one side and then the other, so the two counts add up.
- The second number is 1 only when every officer is eliminated.

## Dry run

`C = 2`, officers at `1` and `4`.

- Left side: the officer at 1 is at distance 1 (odd) - it can be cornered. Count 1.
- Right side: the officer at 4 is at distance 2 (even) - safe.

One officer is eliminated and one survives, so Chef is caught: `1 -1`.

With `C = 2` and a single officer at 1, the count is 1 = $N$: `1 1`.
