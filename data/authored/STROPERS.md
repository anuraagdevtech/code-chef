---
topic: Strings
subtopic: A complete invariant - length, ones, and zeros seen after an odd number of ones
time: $O(N^2)$ per test case
space: $O(N^2)$ for the set of classes
complexity_note: Auxiliary space excludes the buffered input and output.
---
Describe a binary string by the zeros between its ones: with $m$ ones there are $m + 1$ gaps. Call a zero *odd* if an odd number of ones precede it.

Reversing a substring that contains an even number of ones keeps three things fixed: the length, the number of ones, and the number of odd zeros. Inside the reversed part the parity of "ones before me" is preserved for every zero, because the part contains an even number of ones in total.

Conversely these three numbers determine the class. Reversing a substring that starts just after some zeros, spans exactly two ones and ends before some zeros moves zeros between two gaps of the same parity, and reversing a block of zeros with nothing else is trivial; with such moves any distribution of the zeros over the even gaps and over the odd gaps can be reached. So two strings are equivalent exactly when (length, ones, odd zeros) agree.

Enumerate all substrings by fixing the left end and extending the right end, updating the three numbers in $O(1)$, and count the distinct triples.

## Edge cases

- A string with no ones has no odd zeros; its class is determined by its length.
- Different substrings with the same triple are counted once.
- The triple is packed into one integer to keep the set compact.
- The total length over the test cases allows the quadratic enumeration.

## Dry run

`S = 101`.

| substring | length | ones | odd zeros |
|---|---:|---:|---:|
| `1` (twice) | 1 | 1 | 0 |
| `0` | 1 | 0 | 0 |
| `10` | 2 | 1 | 1 |
| `01` | 2 | 1 | 0 |
| `101` | 3 | 2 | 1 |

Five distinct triples, so the answer is 5.
