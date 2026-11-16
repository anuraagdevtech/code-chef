---
topic: Strings
subtopic: Pair supply must cover all odd-frequency centres
time: $O(|S|)$ per test case
space: $O(1)$ for the fixed alphabet
complexity_note: Auxiliary space excludes the buffered input and output.
---
Each palindrome of length at least two consumes at least one equal-letter pair and can contain at most one unpaired centre. Let $p=\sum\lfloor f_c/2\rfloor$ and $o$ be the number of odd frequencies.

Every unpaired character needs its own pair-supported palindrome, so $p\ge o$ is necessary. It is sufficient: form a length-three palindrome around each odd character using one pair, then use any remaining pairs as length-two palindromes. If $o=0$, the nonempty input must still contain at least one pair.

## Edge cases

- A single character cannot form a valid part.
- Even frequencies can always be divided into pairs.
- Odd centres may be surrounded by a different letter.

## Dry run

For `xyxyxy`, frequencies are three and three: two pairs and two odd centres. They form `xyx` and `yxy`, so the answer is `YES`.
