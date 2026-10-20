---
topic: Arrays
subtopic: Sum of flags mapped to a label
time: $O(1)$ per contestant
space: $O(1)$
---
Each contestant's row is five $0/1$ flags, so the number of problems solved is simply their **sum**. The classification then depends only on that count, which makes a lookup table the natural structure:

$$0 \to \texttt{Beginner},\ 1 \to \texttt{Junior Developer},\ \ldots,\ 5 \to \texttt{Jeff Dean}$$

Indexing a six-element tuple by the sum replaces a six-branch `if`/`elif` ladder with a single expression, and makes it obvious that every count from $0$ to $5$ is covered.

The labels must be reproduced exactly, including the internal spaces in `Junior Developer` and `Jeff Dean`. These are the sort of strings where a typo costs a wrong answer with no hint why.

Note the input shape: there is **no $T$**. The first line is $N$, the number of contestants, and each of the next $N$ lines holds five flags. Every contestant produces one output line.

The samples sweep all six categories, and the last two rows are worth comparing: `0 1 1 1 1` and `1 1 1 1 0` both sum to $4$ and both print `Hacker`, confirming that *which* problems were solved is irrelevant — only how many.

With $N$ up to $5000$ and five values each, reading the whole stream at once and emitting one joined write keeps this comfortably fast.
