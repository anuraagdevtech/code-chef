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

## Edge cases

- **Each operation removes exactly three consecutive characters**, so the length only ever drops by $3$ — and the surviving positions fall into fixed residue classes mod $3$.
- **$N \equiv 1 \pmod 3$ is always possible**, since the string can be whittled down to a single character, and one character is a palindrome.
- **Otherwise the survivors must pair up**, and the reachable pairs are exactly a position $p \equiv 1 \pmod 3$ with a later position $q \equiv N \pmod 3$ holding the same character. Verified by brute force over all $29{,}523$ strings of length at most $9$ on a three-letter alphabet, with no mismatch.
- **The scan order matters.** A position is tested against the set of earlier $p \equiv 1$ characters *before* being added to it, which enforces $p < q$.
- **All identical characters** (the first row) succeed as soon as the residues line up.
- **All distinct characters** (the second row) fail, since no pair can match.
- **The operation needs $|S| \geq 3$**, so a string of length $1$ or $2$ admits no moves at all — length $1$ is already a palindrome, and length $2$ needs its two characters equal.

## Dry run

Third sample: $N = 5$, $S = $ `aabcd`, so $N \bmod 3 = 2$.

| position | residue mod 3 | role | character | match? |
|---:|---:|---|---|:---:|
| 1 | 1 | candidate $p$ | `a` | recorded |
| 2 | 2 | candidate $q$ | `a` | **yes** — `a` already seen |

Output `YES`: removing positions $3,4,5$ leaves `aa`, a palindrome.
