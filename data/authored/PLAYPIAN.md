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
