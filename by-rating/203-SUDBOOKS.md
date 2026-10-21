# 203. Sudhanva and Books

> [`SUDBOOKS`](https://www.codechef.com/problems/SUDBOOKS) &middot; difficulty **1300** &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Simulation |
| **Technique** | A stack, with an empty-pop guard |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(1)$ per query |
| **Space** | $O(Q)$ |

## Question

As we all know, Sudhanva is fond of reading books and taking photographs. His dad (after gifting him an iPad last birthday) gifted him a custom-made bookshelf this birthday. This shelf is made in such a way that books can be inserted and removed only from the top. Books are placed one over the other in that shelf. Now to remember each book, Sudhanva develops an algorithm. He first writes a number in his iPad, then takes a photo of that number in his DSLR and then pastes that photograph on the cover of each book. Initially the bookshelf is empty.

You have given $Q$ queries of either of the two types

•	Type 1. $(1, N)$ In this type of query Sudhanva places a book with photo of number N on the top. You don't have to print anything in this query

•	Type 2.  $(-1)$ In this Query Sudhanva takes out the topmost book, you have to print the number on the book he just took out. If the shelf is empty and Sudhanva is trying to take out a book, print "kuchbhi?" Without quotes

**Input:**
- First line will contain $Q$, number of queries
- Following $Q$ lines will contain queries of one of the types mentioned
- Type 1:    $1$ $N$
	This query specifies that Sudhanva places a book with number $N$ on it, at the top of the shelf.
- Type 2:    $-1$
	This query specifies that Sudhanva takes out the topmost books from the shelf.

**Output:**
For each query of Type 2, print the number $N$ on the book he just took out, if the shelf was empty and it was not possible to take out a book, then print "kuchbhi?" (without quotes)  Each output should be printed on a new line.

**Constraints**
- $1 \leq Q \leq 10^6$
- $1 \leq N \leq 10^9$

**Subtasks**
- 100 points : Original Constraints

## Constraints

- $1 \leq Q \leq 10^6$
- $1 \leq N \leq 10^9$

## Sample

**Sample input**

```
5
1 2
1 45
-1
-1
-1
```

**Sample output**

```
45
2
kuchbhi?
```

## Approach

Books are inserted and removed only from the top, which is the definition of a **stack** (last in, first out). Python's `list` is exactly that: `append` pushes and `pop` removes the most recent element, both in amortised $O(1)$.

So the whole problem is two cases:

- `1 N` → `append(N)`, printing nothing;
- `-1` → `pop()` and print the value, or print `kuchbhi?` when the shelf is empty.

The empty check is the only real requirement — calling `pop` on an empty list raises `IndexError`, so the guard is not defensive padding but necessary for correctness on valid input.

The sample exercises it: two books go on, both come off in reverse order (`45` then `2`), and the third removal finds nothing left.

With $Q$ up to $10^6$, the dominant cost is **I/O**, not the stack. Reading the whole stream at once and collecting the outputs into a list for a single joined write avoids a million separate `input()` and `print()` calls, which would otherwise dominate the runtime by an order of magnitude.

Note the input is not uniformly shaped — a type-1 query occupies two tokens and a type-2 query only one — so the parser advances a cursor by a variable amount rather than reading fixed-size records.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    pos = 1
    shelf = []
    out = []
    for _ in range(q):
        # Type 1 takes two tokens, type -1 only one.
        if data[pos] == b"1":
            shelf.append(data[pos + 1])
            pos += 2
        else:
            pos += 1
            out.append(shelf.pop().decode() if shelf else "kuchbhi?")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/simulation/SUDBOOKS.md](../docs/simulation/SUDBOOKS.md)
