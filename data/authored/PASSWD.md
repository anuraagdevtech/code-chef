---
topic: Strings
subtopic: Several predicates, one with a positional restriction
time: $O(|S|)$ per test case
space: $O(1)$
---
Five conditions must all hold, and the one that makes this more than a checklist is **where** each character is allowed to count.

- **Lowercase** — anywhere in the string.
- **Uppercase**, **digit**, **special** — each must appear *strictly inside*, meaning the first and last characters do not count.
- **Length** at least $10$.

So the interior is the slice `s[1:-1]`, and three of the four character tests run against that slice while the lowercase test runs against the whole string. Taking the interior once and reusing it keeps the four tests symmetrical and avoids repeating the index arithmetic.

Sample case 1, `#cookOff#P1`, is built precisely on this distinction. It is long enough, has lowercase letters, has an uppercase `O` inside and a special `#` inside — but its only digit is the final `1`, which sits on the boundary and therefore does not count. The answer is `NO`.

Sample case 3, `gR3@tPWD`, satisfies every character rule inside but is only $8$ characters long, failing the length check alone.

Sample case 2 passes all five.

The length check should come first in practice: for a string shorter than $3$ the interior slice is empty, and while that merely makes the other tests false rather than erroring, checking the cheap condition first is the clearer order.

The special set is exactly $\{$ `@`, `#`, `%`, `&`, `?` $\}$ — five characters, no more.
