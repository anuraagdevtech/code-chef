---
topic: Greedy
subtopic: Tracking a global flip as parity
time: $O(|S|)$ per test case
space: $O(1)$
---
Waving the wand flips **every** door at once, so the board is never partially modified — after $k$ waves, the door written as $S_i$ currently shows

$$S_i \oplus (k \bmod 2)$$

That is the key simplification: the entire history of wand use collapses into a single parity bit. There is no need to maintain a mutable copy of the string, which would be $O(n)$ work per wave and far too slow.

Walking left to right, Chef needs each door open when he reaches it. If the door's effective value is $0$, he has no choice but to wave — and because waving is the only tool, waving exactly then is forced, so the greedy is also optimal. Flipping earlier would only have to be undone.

So the algorithm is: hold a parity bit, and for each character, if `S[i] ^ parity == 0`, flip the parity and increment the counter.

Sample case 2, `010`, is the worst case: every door is closed when reached, so the wand is used three times — once per door. Sample case 1, `111`, never needs it. Sample case 3, `10011`, needs two waves, matching the statement's own walkthrough.

Note that a wave is counted even if it happens immediately before the first door, so the answer can equal the string length. With the sum of $|S|$ reaching $2 \times 10^6$, the $O(1)$-per-character pass and bulk input reading are both necessary.
