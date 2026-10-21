---
topic: Number Theory
subtopic: Smallest multiplier for divisibility
time: $O(\log \min(N,K))$ per test case
space: $O(1)$
---
Buying $P$ pizzas yields $KP$ slices, and sharing them equally among $N$ friends with none left over means

$$N \mid KP$$

So we need the smallest positive $P$ making $KP$ a multiple of $N$.

Write $g = \gcd(N, K)$. Then $K$ already supplies the factor $g$ of $N$, and what remains to be covered is $N/g$ — which shares no factor with $K/g$. So $P$ must be a multiple of $N/g$, and the smallest choice is

$$P = \frac{N}{\gcd(N, K)}$$

Framing it through the gcd is what makes this immediate; searching for the smallest $P$ directly would be hopeless with $N, K$ up to $10^9$.

Sample case 1 has $N = K = 2$: the gcd is $2$, so a single pizza's two slices split one apiece. Sample case 2 has $N = 2, K = 3$ with gcd $1$, so $P = 2$ — two pizzas give six slices, three each. Sample case 3 has $N = 4, K = 2$ with gcd $2$, giving $P = 2$ and one slice per friend.

Note the answer never exceeds $N$ and equals it exactly when $K$ and $N$ are coprime. It is also the reason $K > N$ does not automatically mean one pizza: with $N = 4$ and $K = 6$ the gcd is $2$, so two pizzas are still needed.

Both `math.gcd` and the division stay in integers, so there is nothing to watch numerically.
