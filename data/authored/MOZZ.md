---
topic: Basic Math
subtopic: Inverting a reward, then a ceiling division
time: $O(1)$ per test case
space: $O(1)$
---
Two steps, run in sequence.

**Recover the sticks eaten.** Chef is paid $30$ rupees for each stick beyond $X$, so $R$ rupees means $R/30$ extra sticks and a total of

$$S = X + \frac{R}{30}$$

The guarantee that $R$ is a multiple of $30$ makes this exact. Note that $R = 0$ does not mean Chef ate nothing — it means he ate no *extra*, so $S = X$, which is the most he could have eaten without earning anything. Sample case 2 is exactly this, with $S = 16$.

**Convert sticks to plates.** Plates hold $Y$ sticks, and the rules say Chef finishes each plate before ordering the next but may leave the **final** plate unfinished. The question asks for the *maximum* possible number of plates, so assume he abandoned the last one after a single stick:

$$\left\lceil \frac{S}{Y} \right\rceil$$

The "maximum" wording is what makes this a ceiling. Were the question the minimum number of plates, the answer would be the same ceiling for a different reason — but here the subtlety is that any partially eaten plate still counts as ordered, which is precisely what rounding up expresses.

Sample case 3 shows it: $S = 15 + 4 = 19$ sticks at $9$ per plate means two full plates and one stick from a third, so $3$ plates.
