---
topic: Strings
subtopic: Counting characters, then a three-way branch
time: $O(|S|)$ per test case
space: $O(1)$
---
Score the string first. A `C` gives Carlsen $2$ points, an `N` gives Chef $2$, and a `D` gives both $1$:

$$\text{Carlsen} = 2\,n_C + n_D, \qquad \text{Chef} = 2\,n_N + n_D$$

Since the string has a fixed length of $14$, counting two of the three characters is enough — but counting all three with `str.count` is clearer and still a single pass each.

Then the prize depends on three cases, and the middle one is the trap:

- Carlsen strictly ahead → $60X$
- Chef strictly ahead → Carlsen takes the loser's share, $40X$
- **Tied** → Carlsen is declared champion but receives only $55X$

The tie is not folded into the win. A solution treating "Carlsen wins ties" as simply a win would pay $60X$ and fail sample case 3, where $4$ wins each and $6$ draws leave both on $14$ points and the correct answer is $55 \times 30 = 1650$.

Sample case 4 is the losing case: Chef takes eight games to Carlsen's none, so Carlsen collects $40X = 40$.

Note the draws cancel — $n_D$ appears identically on both sides — so the comparison reduces to $n_C$ against $n_N$. The code keeps the full expressions because they mirror the statement, but recognising the cancellation is a useful check that draws can never decide the title.

With $X$ up to $10^6$ the prize reaches $6 \times 10^7$, which is comfortably inside any integer type.
