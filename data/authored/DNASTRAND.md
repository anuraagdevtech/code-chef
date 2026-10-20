---
topic: Strings
subtopic: Character-wise mapping with a translation table
time: $O(N)$ per test case
space: $O(N)$ for the output string
---
Each nucleotide maps independently to its complement: `A` ↔ `T` and `C` ↔ `G`. Because no character's image depends on its neighbours, the whole answer is a position-by-position substitution.

Python has a built-in for exactly this. `str.maketrans("ATCG", "TAGC")` builds a translation table and `s.translate(table)` applies it in one C-level pass, which is both faster and less error-prone than a loop with an `if`/`elif` chain or a dictionary lookup per character.

The table is worth reading carefully — it is its own inverse. Position by position, `A`→`T`, `T`→`A`, `C`→`G`, `G`→`C`, so applying it twice returns the original strand, exactly as the biology implies.

A common slip is to build the complement with chained `replace` calls: `s.replace("A","T").replace("T","A")` destroys the data, because the second call also rewrites the `T`s the first one just produced, collapsing everything to `A`. A single simultaneous substitution avoids that entirely, which is the real reason `translate` is the right tool rather than merely a convenient one.

Note the problem gives $N$ on its own line before the string. It is redundant for Python, since the string carries its own length, but the token must still be consumed when walking the input.
