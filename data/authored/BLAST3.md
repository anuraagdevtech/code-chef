---
topic: Strings
subtopic: Residue classes of the surviving positions
time: $O(N)$ per test case
space: $O(1)$
---
Run the operation **backwards**: building $S$ from the final string means inserting blocks of $3$ contiguous characters. Insertions into the same slot stay one run, so every maximal run of *deleted* positions has length divisible by $3$ — and conversely any such deletion pattern is realisable. So the surviving positions $p_1 < \cdots < p_L$ are exactly those with

$$p_1 \equiv 1, \quad p_{i+1} \equiv p_i + 1, \quad N \equiv p_L \pmod 3 \qquad\Longrightarrow\qquad p_i \equiv i \pmod 3$$

Now take the shortest useful palindrome, by case on $N \bmod 3$:

- **$N \equiv 1$:** keep a single character at any position $\equiv 1 \pmod 3$ — position $1$ always qualifies, and one character is a palindrome. Always `YES`.
- **$N \equiv 2$ or $0$:** a palindrome of length $L \equiv N \pmod 3$ has outer positions $p_1 \equiv 1$ and $p_L \equiv N \pmod 3$ with $S_{p_1} = S_{p_L}$. So that pair is **necessary**, and it is also sufficient: for $N \equiv 2$ the pair itself is a length-$2$ palindrome, and for $N \equiv 0$ the position $p_1 + 1 \equiv 2 \pmod 3$ lies strictly inside (since $p_L \geq p_1 + 2$) and serves as the middle.

So apart from the $N \equiv 1$ case the whole question is: **is there $p \equiv 1 \pmod 3$ before some $q \equiv N \pmod 3$ with the same character?** One left-to-right pass with a set of characters seen at positions $\equiv 1$ answers it.

The samples are all $N = 5$, so $N \equiv 2$ and the relevant positions are $\{1,4\}$ and $\{2,5\}$. `aaaaa` matches at once. `aabcd` matches $S_1 = S_2 = $ `a`. But `abcde` offers only the pairs $(a,b), (a,e), (d,e)$ — no match — so `NO`, even though three characters could in principle be dropped.
