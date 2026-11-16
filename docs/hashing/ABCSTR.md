[&larr; 519. IS IT DSU HARD!!](CFMAR04.md) &middot; [Index](../../README.md) &middot; [727. Max Shift After XOR &rarr;](MAXCYCSHIFT.md)

# 693. ABC-Strings

> CodeChef problem code [`ABCSTR`](https://www.codechef.com/problems/ABCSTR) &middot; difficulty **2264** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Hashing |
| **Technique** | Equal prefix states (A-B, A-C) mark balanced substrings |
| **Time** | $O(N)$ expected |
| **Space** | $O(N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

Mike likes strings. He is also interested in algorithms. A few days ago he discovered for himself a very nice problem:

*
You are given an AB-string **S**. You need to count the number of substrings of S, which have an equal number of 'A'-s and 'B'-s.
*

Do you know how to solve it? Good. Mike will make the problem a little bit more difficult for you.

*
You are given an ABC-string **S**. You need to count the number of substrings of S, which have an equal number of 'A'-s, 'B'-s and 'C'-s.
*

A string is called AB-string if it doesn't contain any symbols except 'A' or 'B'. A string is called ABC-string if it doesn't contain any symbols except 'A', 'B' or 'C'.

**Input**

The first line of the input contains an ABC-string **S**.

**Output**

Your output should contain the only integer, denoting the number of substrings of **S**, which have an equal number of 'A'-s, 'B'-s and 'C'-s.

The answer can go above a 32-bit integer. Please, use 64-bit integers for storing and processing data.

**Constraints**

1 ≤ **|S|** ≤  1 000 000; where **|S|** denotes the length of the given ABC-string.

**Example**

```
**Input:**
ABACABA

**Output:**
2
```

**Explanation**

In the example you should count **S**[2..4] = "BAC" and **S**[4..6] = "CAB".

## Constraints

1 ≤ |S| ≤  1 000 000; where |S| denotes the length of the given ABC-string.

## Approach

Let $a_i, b_i, c_i$ be the numbers of each letter in the first $i$ characters. The substring $(i, j]$ has equally many of each letter exactly when

$$a_j - b_j = a_i - b_i \quad\text{and}\quad a_j - c_j = a_i - c_i,$$

i.e. the pair $(a - b,\; a - c)$ is the same at both ends.

So scan the string keeping this pair as the current state, with a dictionary counting how many earlier prefixes had each state (the empty prefix has state $(0, 0)$). For every position add the number of earlier prefixes with the same state to the answer, then record the current state.

## Solution (Python)

```python
import sys


def main():
    text = sys.stdin.buffer.read().strip()
    x = y = total = 0
    seen = {(0, 0): 1}
    for char in text:
        if char == 65:
            x += 1
            y += 1
        elif char == 66:
            x -= 1
        else:
            y -= 1
        key = (x, y)
        total += seen.get(key, 0)
        seen[key] = seen.get(key, 0) + 1
    print(total)


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ expected
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- The empty prefix must be counted, otherwise balanced substrings starting at the first character are lost.
- The answer can be about $N^2 / 6$ and needs 64 bits.
- A string missing one of the letters has no balanced substring.
- The input is a single line; trailing whitespace is stripped.

## Dry run

`S = ABACABA`. States after each prefix:

`(0,0)` -> A `(1,1)` -> B `(0,1)` -> A `(1,2)` -> C `(1,1)` -> A `(2,2)` -> B `(1,2)` -> A `(2,3)`.

`(1,1)` occurs at prefixes 1 and 4 (substring `BAC`), and `(1,2)` at prefixes 3 and 6 (substring `CAB`).

Answer 2.

> CodeChef tags: `Data Structures`, `Algorithms`, `Simple Algos`

---

Same problem in rating order (#655 of 735): [../../by-rating/655-ABCSTR.md](../../by-rating/655-ABCSTR.md)
