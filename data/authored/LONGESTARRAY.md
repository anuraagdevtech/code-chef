---
topic: Bit Manipulation
subtopic: Two pointers with per-bit counts - every bit must appear both inside and outside
time: $O(30 \cdot N)$ per test case
space: $O(30 \cdot N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
The OR of the subarray and the OR of the rest are both submasks of the OR of the whole array, and together they cover it. If they are equal, both equal the total OR. So the condition is: every bit that occurs in the array occurs at least once inside the window and at least once outside it.

"At least once outside" means the window must not contain *all* occurrences of any bit; this property is lost by growing the window and regained by shrinking it. So for every right end, advance the left end while some bit has all its occurrences inside - this gives the longest window ending there that leaves every bit outside. If that window also contains every bit it is a valid answer; if it does not, no shorter window ending at the same place can, since shrinking only loses bits.

Maintain for every bit its count inside the window, the number of distinct bits present inside, and the number of bits whose inside count equals their total count.

## Edge cases

- A bit that occurs only once in the whole array makes the answer $-1$.
- $N = 1$: the remaining part is empty and can never match.
- The window is always a proper subarray because the "outside" condition forbids taking everything.
- Each element's set bits are extracted once and reused when it enters and leaves the window.

## Dry run

`A = [2, 3, 4, 7]`. Bit totals: bit 0 twice (3, 7), bit 1 three times (2, 3, 7), bit 2 twice (4, 7).

- right end at 4 (index 3): window `[2, 3, 4]` contains bit 0 once, bit 1 twice, bit 2 once - none completely, and all three bits are present. Length 3 is valid.
- right end at 7: the window `[2, 3, 4, 7]` would contain every occurrence of every bit, so the left end moves right until each bit has an occurrence outside again; that leaves only `[7]`, length 1.

Answer 3.
