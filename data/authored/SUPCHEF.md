---
topic: Basic Math
subtopic: Strict comparison against a deadline
time: $O(1)$ per test case
space: $O(1)$
---
Watching $N$ episodes of $K$ minutes each takes $NK$ minutes, and Chef must finish **strictly before** the exam at minute $M$:

$$N \cdot K < M$$

The whole problem is that strict `<`. Sample case 1 is built on it: one episode of $10$ minutes against an exam $10$ minutes away means Chef finishes exactly as the exam starts, which does not count as "before", so the answer is `NO`. A `<=` would get this wrong while passing the other two samples — the classic way this problem is failed.

Sample case 3 is the straightforward overrun ($20$ minutes of episodes against a $15$-minute window), and case 2 the comfortable fit ($20 < 25$).

On magnitudes: $M$ reaches $10^9$ while $N$ and $K$ each reach $10^4$, so the product $NK$ can reach $10^8$ — comfortably inside a 32-bit signed integer, though a C solution multiplying before checking would want to be sure. In Python the question does not arise.

With $T$ up to $10^4$, reading the stream in one go and writing one joined block is worth doing; the arithmetic itself is free.
