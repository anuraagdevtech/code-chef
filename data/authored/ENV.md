---
topic: Greedy
subtopic: Choosing which elements to add rather than multiply
time: $O(N)$ per test case
space: $O(N)$
---
$S$ starts at $0$, so the first step must be an addition — multiplying would pin $S$ at $0$ forever. Beyond that, the best shape is clear: do all the additions first and then all the multiplications, giving

$$S = \Bigl(\sum_{x \in T} x\Bigr) \cdot \prod_{x \notin T} x$$

for the chosen non-empty added set $T$. An addition made after a multiplication contributes only its own value, so it is never better.

Now choose $T$. For values $\geq 2$ it never pays to add two of them: $a + b \leq ab$ whenever $a, b \geq 2$, so moving one back into the product is at least as good. And adding a *single* value $a$ gives $a \cdot (\Pi/a) = \Pi$ — the same total whichever one it is. So with no ones present the answer is simply the full product $\Pi$.

Ones are the interesting case, because multiplying by $1$ wastes an element while adding it gains $1$. Let $c$ be the number of ones and $\Pi'$ the product of the rest:

- $c = 0$: answer $\Pi'$.
- $c \geq 2$: add all the ones, multiply everything else: $c \cdot \Pi'$. Pulling a value $a$ out of the product to add it would give $\frac{(c+a)}{a}\Pi' \leq c\Pi'$ exactly when $c \geq \frac{a}{a-1}$, which holds for $c \geq 2$.
- $c = 1$: that inequality flips, so add the one *and* the smallest other value $a$, giving $(1+a) \cdot \Pi'/a$. The smallest $a$ maximises $1 + 1/a$.
- all ones: nothing can be multiplied usefully, so the answer is $N$.

The samples show two of these. $[4,2,5,2]$ has no ones, so the answer is $4 \cdot 2 \cdot 5 \cdot 2 = 80$. $[1,2,1]$ has $c = 2$, giving $2 \cdot 2 = 4$ — the same as adding everything, and better than the $3$ that multiplying by a one would waste.

The case analysis is exact, so the modulus is applied only at the end; comparisons are never made on reduced values.

## Edge cases

- **$S$ starts at $0$, so the first element must be added** — multiplying leaves $S$ at zero forever. Something has to seed the product.
- **Ones are worthless as multipliers**, since $S \times 1$ does nothing, so every $1$ should be added instead.
- **Two or more ones make a free seed**: add all of them and multiply by everything else. The second sample's two ones seed $2$, then $\times 2$ gives $4$.
- **With no ones, adding exactly one element is optimal** and *which* one does not matter: $a \times \prod(\text{rest}) = \prod(\text{all})$ either way. Adding two instead gives $(a+b)\prod(\text{rest})$, which is worse because $a + b \leq ab$ for $a, b \geq 2$.
- **With exactly one 1, adding the smallest other element too is strictly better.** The seed becomes $1 + a$ and the answer $\frac{1+a}{a}\prod(\text{all})$, maximised by the smallest $a$ — better than adding the $1$ alone, which gives just $\prod(\text{all})$.
- **All ones** means nothing is worth multiplying, and the answer is simply $N$.
- **The modulus is applied to the product**, but the comparisons that drive the choice are made on the true values — which is safe here because the decisions depend only on counts and the smallest element, never on the reduced product.

## Dry run

First sample: $A = 4, 2, 5, 2$ — no ones.

| step | value |
|---|---:|
| smallest element, added as the seed | 2 |
| remaining factors | $4, 5, 2$ |
| product of the rest | 40 |
| total | **80** |

Output `80`, which equals $\prod A$. Adding two elements instead — say $2 + 2 = 4$ then $\times 4 \times 5$ — gives only $80$… in fact $4 \cdot 20 = 80$ here too, but on $A = 3, 3$ adding both gives $6$ against the product's $9$.
