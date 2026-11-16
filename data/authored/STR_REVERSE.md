---
topic: Strings
subtopic: Keep the longest target prefix that is already a subsequence
time: $O(|S|)$ per test case
space: $O(1)$ auxiliary
complexity_note: Auxiliary space excludes the buffered input and output.
---
Characters never moved keep their relative order and appear before all moved characters. Thus they must form a prefix of the target reversal. Conversely, keep any subsequence matching a target prefix and move all other characters to the end in target-suffix order.

Greedily match as much of the reversed target as a subsequence of the original string as possible. If $k$ characters are kept, exactly $|S|-k$ operations are necessary and sufficient. Access the reversed target by index without allocating another string.

## Edge cases

- A palindrome needs no moves.
- Repeated characters are matched greedily by position.
- A one-character string returns zero.

## Dry run

For `abdeba`, the target is `abedba`. The original string can keep target prefix `abe` as a subsequence, length three, so three moves suffice.
