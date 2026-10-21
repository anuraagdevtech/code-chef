---
topic: Strings
subtopic: Validating fixed-size blocks
time: $O(|s|)$ per test case
space: $O(1)$
---
Each day both sisters play exactly once, in either order. So a valid log is a concatenation of two-character blocks, each of which is `AB` or `BA` — equivalently, each block contains one of each letter.

That gives a simple test: walk the string two characters at a time and require the pair to **differ**.

$$s_{2i} \neq s_{2i+1} \quad\text{for every } i$$

The constraint that $|s|$ is even is what guarantees the string splits cleanly into whole days, so no partial block needs handling.

The trap is checking a global property instead of the per-day one. Counting letters and requiring equal numbers of `A` and `B` is *necessary* but not *sufficient* — sample case 3, `ABAABB`, has three of each yet is invalid, because its second day reads `AA` and its third `BB`. Only the block-local check catches it.

Sample case 2, `ABBA`, shows that the order within a day may vary freely: `AB` then `BA` is perfectly legal, so the sisters need not alternate across days.

Sample case 4, `AA`, is the minimal failure — a single day with the same sister twice.

In Python this reads cleanly as `all(s[i] != s[i+1] for i in range(0, len(s), 2))`, which short-circuits on the first bad day.

## Edge cases

- **Block alignment is the point, not the letter counts.** `ABBA` passes because its blocks are `AB` and `BA`, while `ABAABB` fails on its middle block `AA` — and both strings contain three of each letter in the second case, so a counting argument cannot distinguish them.
- **$|s|$ is guaranteed even**, so there is never a trailing partial block to decide about.
- **The shortest input** ($|s| = 2$) is a single block: `AB` passes, `AA` fails.
- **A failure anywhere fails the whole string**, so `all` short-circuits on the first bad block.

## Dry run

| $s$ | blocks of two | all differ? | output |
|---|---|:---:|---|
| `AB` | `AB` | yes | `yes` |
| `ABBA` | `AB`, `BA` | yes | `yes` |
| `ABAABB` | `AB`, `AA`, `BB` | no | `no` |
| `AA` | `AA` | no | `no` |

Rows 2 and 3 have the same letter counts in different alignments.
