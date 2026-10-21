---
topic: Arrays
subtopic: Counting two categories in one pass
time: $O(N)$ per test case
space: $O(1)$
---
Every code is one of exactly two values, so counting one of them determines the other. Count the `START38` entries as $s$; the `LTIME108` count is then $N - s$, with no second scan and no dictionary.

That complement trick is the point of the problem. It is the same idea as counting evens and deriving the odds in the Mahasena problem: when a set is partitioned into two classes, one counter plus the total is enough.

For a general partition into many categories, `collections.Counter` would be the tool — but here it would allocate a dictionary per test case to hold two keys, and the answer still has to be emitted in a fixed order with zeros present. Sample case 3 has no `START38` at all and must print `0 2`, which a Counter-based solution gets wrong if it iterates over observed keys rather than the known pair.

Output order is fixed by the statement: `START38` count first, then `LTIME108`, regardless of which appears first in the input. Sample case 2 leads with `LTIME108` three times yet still prints `1 3`.

The codes are compared as whole tokens. Matching on a prefix such as `S` would work for these two particular strings but is the kind of shortcut that breaks the moment a third contest code appears.

## Edge cases

- **All problems from one contest** (the sample's third case, which has no `START38` at all): the answer is `0 2`, so a zero count is legitimate output.
- **Only two categories exist**, so counting one determines the other — $N$ minus the first count. Tallying both separately is harmless but redundant, and risks disagreeing if a code were ever misspelled.
- **$N = 1$**: a single problem, counted on one side.
- **Output is two numbers on one line** in a fixed order, `START38` first, so swapping them silently fails every mixed case.

## Dry run

| codes | `START38` | `LTIME108` ($N -$ first) | output |
|---|---:|---:|---|
| S, L, S | 2 | 1 | `2 1` |
| L, L, L, S | 1 | 3 | `1 3` |
| L, L | 0 | 2 | `0 2` |
| S, L, L, L, S, L | 2 | 4 | `2 4` |

(`S` is `START38`, `L` is `LTIME108`.)
