---
topic: Basic Math
subtopic: Reading an off-by-one from the statement
time: $O(1)$ per test case
space: $O(1)$
---
The base economy $M$ already accounts for the driver, so only the **extra** passengers reduce it. With $P$ people in the car there are $P - 1$ extras, each costing $1$ km/l:

$$\text{economy} = M - (P - 1) = M - P + 1$$

and the distance is that economy multiplied by the fuel available:

$$V \cdot (M - P + 1)$$

The whole problem is the $-1$. Reading the penalty as $P$ rather than $P - 1$ gives a plausible-looking formula that fails every sample, and the statement goes out of its way to warn about it — both by defining the base case as "only the driver" and by the closing note that the $P$ people *include* the driver.

Sample case 2 is the one that isolates it: a single occupant means no extras at all, so the economy is the full $M = 6$ and the answer is $60$. A formula using $M - P$ would give $50$.

Sample case 1 shows the penalty biting hardest: five people drop a $10$ km/l car to $6$ km/l, giving $120$ km from $20$ litres.

The constraints keep the economy positive — $M \geq 6$ while $P \leq 5$, so $M - P + 1 \geq 2$ — meaning no clamping is needed and the distance is never zero or negative.
