---
topic: Combinatorics
subtopic: A condition pinned down by its singletons
time: $O(N)$ per test case
space: $O(1)$
---
The condition must hold for **every** subarray of $B$, including the length-one ones $B[i,i]$. So every surviving element must itself be even — and conversely, if all survivors are even then every subarray sum is a sum of evens and automatically even.

So a removal is good exactly when the elements left behind are all even. That means **every odd element must be removed**, while each even element may independently be kept or removed:

$$2^{e}, \qquad e = \#\{i : A_i \text{ even}\}$$

choices in total, where the empty $B$ is allowed because the statement declares the empty sum to be $0$.

The one adjustment is that the removal must be **non-empty**. If the array contains at least one odd element, every one of the $2^e$ choices removes it and is automatically non-empty. But if there are no odd elements, the choice that keeps all the evens removes nothing — so subtract one:

$$\text{answer} = \begin{cases} 2^{e} & \text{some } A_i \text{ odd} \\ 2^{e} - 1 & \text{all } A_i \text{ even} \end{cases}$$

Reducing an all-subarrays condition to its singletons is the move worth keeping; it is the same collapse that appeared in the *Magic Set* problem.

Sample case 1, $[2,1,4]$, has two evens and one odd, giving $2^2 = 4$. Sample case 2, $[1,2,3]$, has one even and two odds, giving $2$.

The power is taken modulo $10^9+7$ with `pow(2, e, MOD)`, and the $-1$ applied afterwards.
