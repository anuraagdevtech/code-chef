---
topic: Strings
subtopic: Comparing character frequencies
time: $O(|S|)$ per test case
space: $O(1)$ — at most 26 counters
---
Split the string at its midpoint and ask whether the two halves use **the same characters with the same multiplicities**. That is a multiset comparison, which `collections.Counter` performs directly:

```python
Counter(s[:h]) == Counter(s[len(s) - h:])
```

Counting is essential, not optional. Comparing `set(left) == set(right)` checks only which letters appear, ignoring how often — and the statement calls that out explicitly with `abbaab`, whose halves `abb` and `aab` share the same letters in different quantities. That is sample case 5, and it is the whole point of the problem.

Note this is **not** a palindrome test either. `gaga` is a lapindrome but reads differently backwards, while `rotor` happens to be both. Order within each half is irrelevant.

For odd lengths the middle character is discarded. Taking the left half as `s[:n//2]` and the right as `s[n - n//2:]` handles both parities with the same expression: for even $n$ the two slices meet exactly, and for odd $n$ they skip the single middle character. Sample cases 3 and 4, `rotor` and `xyzxy`, both rely on that.

Sample case 6, `ababc`, has halves `ab` and `bc` — same length, different contents — and fails.

With $|S| \leq 1000$ the linear pass is trivial; the counter holds at most 26 entries, so the space is effectively constant.

## Edge cases

- **Odd length skips the middle character.** `rotor` compares `ro` against `or` and ignores the central `t`; slicing from $|S| - h$ rather than from $h$ is what achieves that.
- **Frequencies, not order**: `ro` and `or` match, so the halves need not be equal as strings.
- **Multiplicities matter.** `abbaab` splits into `abb` and `aab`, which use the same letters but in different quantities, so the answer is `NO` — comparing *sets* instead of counts would wrongly say `YES`. This is the sharpest case in the sample.
- **Shortest input** ($|S| = 2$): two halves of one character each.
- At most 26 distinct letters, so the counters are effectively constant space.

## Dry run

| $S$ | first half | last half | counts match? | output |
|---|---|---|:---:|---|
| `gaga` | `ga` | `ga` | yes | `YES` |
| `abcde` | `ab` | `de` | no | `NO` |
| `rotor` | `ro` | `or` | yes | `YES` |
| `xyzxy` | `xy` | `xy` | yes | `YES` |
| `abbaab` | `abb` | `aab` | **no** | `NO` |
| `ababc` | `ab` | `bc` | no | `NO` |

Row 5 uses the same two letters in both halves and still fails, on the counts.
