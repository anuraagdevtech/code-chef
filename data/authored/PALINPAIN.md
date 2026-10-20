---
topic: Constructive
subtopic: Counting distinct palindrome halves
time: $O(X + Y)$ per test case
space: $O(X + Y)$
---
A palindrome is determined entirely by its **first half** (plus a middle character when the length is odd), since the second half is forced as the mirror image. So counting distinct palindromes with given letter counts means counting distinct halves.

Two conditions must hold.

**A palindrome must exist at all.** At most one letter count may be odd, so $X$ and $Y$ cannot both be odd — sample case 2, $X = Y = 3$, fails here and prints $-1$.

**Two *different* palindromes must exist.** The half contains $\lfloor X/2 \rfloor$ `a`s and $\lfloor Y/2 \rfloor$ `b`s, and there is more than one arrangement exactly when **both** are at least $1$ — that is, when $X \geq 2$ and $Y \geq 2$. With $X = 1$, say, every half is all `b`s and the palindrome is unique, so the answer is $-1$ even though a palindrome exists.

When both conditions hold, build two halves that differ: one with the `a`s first, and one starting with a `b` before the remaining letters. Each is completed by the middle character (`a` if $X$ is odd, `b` if $Y$ is odd, nothing if both are even) and the reversed half.

Sample case 1, $X=2, Y=4$: the half holds one `a` and two `b`s, so `abb` and `bab` are two distinct halves, giving `abbbba` and `babbab` — exactly the published answer, though **any** valid pair is accepted and this is judged by a checker.

Note that both counts being even is fine and both being odd is fatal; exactly one odd simply places that letter in the centre.
