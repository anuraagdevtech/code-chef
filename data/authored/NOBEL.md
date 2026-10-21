---
topic: Sets
subtopic: Counting distinct values against a capacity
time: $O(N)$ per test case
space: $O(N)$
---
Chef shares the prize if his topic is one **nobody else** works on. He can master any of the $M$ topics instantly, so he simply needs a topic that is currently unused.

An unused topic exists exactly when the researchers do not cover every field:

$$\bigl|\{A_1, \ldots, A_N\}\bigr| < M$$

so the whole solution is comparing the number of **distinct** topics against $M$.

The trap is reasoning about the researchers' own uniqueness. It is tempting to look for a topic held by exactly one person, or to count how many researchers are already unique — but none of that matters. Chef cannot displace anyone; he needs an *empty* field, so only coverage counts.

Sample case 3 makes this vivid: all four researchers crowd onto topic $4$, so three fields stand empty and Chef wins easily — even though not one researcher is unique. Sample case 1 is the opposite, with four researchers spread across all four topics leaving Chef nowhere to go, despite every researcher being unique.

Sample case 2 has $5$ researchers on only $3$ distinct topics out of $4$, so one field is free.

A Python `set` gives the distinct count in one pass. With the sum of $N$ reaching $10^6$, that linear pass with bulk input reading is what keeps this comfortable; an $O(N^2)$ uniqueness check would not survive.

## Edge cases

- **Only coverage matters, not popularity.** The third row has all four people on one topic, which still leaves three fields untouched — so counting people per topic is beside the point.
- **Every topic taken** (the first row, four people on four distinct topics) → `No`.
- **The comparison is strict**: if all $M$ topics are covered there is no empty field left, so $\mathrm{distinct} < M$ rather than $\leq$.
- **$A_i \leq M$ is guaranteed**, so no out-of-range topic can appear and the distinct count never exceeds $M$.
- **$N$ may exceed $M$** (the second row has five people and four topics), which forces duplicates and therefore guarantees a free field.
- **Sum of $N$ and of $M$ each up to $10^6$**: one pass with a set per case, and the values stay as raw byte tokens.

## Dry run

| $N$ | $M$ | topics chosen | distinct | $< M$? | output |
|---:|---:|---|---:|:---:|---|
| 4 | 4 | $1,2,3,4$ | 4 | no | `No` |
| 5 | 4 | $4,2,1,1,1$ | 3 | yes | `Yes` |
| 4 | 4 | $4,4,4,4$ | 1 | yes | `Yes` |
