# 133. HOW MANY DIGITS DO I HAVE

> CodeChef problem code [`HOWMANY`](https://www.codechef.com/problems/HOWMANY) &middot; difficulty **520** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Counting digits |
| **Time** | $O(d)$ |
| **Space** | $O(d)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Write a program to obtain a number $(N)$ from the user and display whether the number is a one digit number, 2 digit number, 3 digit number or more than 3 digit number

**Input**

First line will contain the number $N$,

**Output**

Print "1" if N is a 1 digit number.

Print "2" if N is a 2 digit number.

Print "3" if N is a 3 digit number.

Print "More than 3 digits" if N has more than 3 digits.

## Constraints

- $0 \leq N \leq 1000000$

## Sample

**Sample input**

```
9
```

**Sample output**

```
1
```

## Approach

Classify $N$ by its digit count: print `1`, `2`, `3`, or the string `More than 3 digits`.

The shortest correct route is to read the input **as a string** and take its length. That avoids arithmetic entirely and handles every case uniformly:

```python
d = len(s)
print(d if d <= 3 else "More than 3 digits")
```

The arithmetic alternative — repeatedly dividing by $10$ and counting, or using $\lfloor \log_{10} N \rfloor + 1$ — works but needs a guard. The logarithm of $0$ is undefined, and $N = 0$ is inside the constraints. As a string, `"0"` has length $1$, which is the right answer with no special case.

That zero is the trap here. The constraint $0 \leq N \leq 10^6$ deliberately admits it, and a `while n > 0` digit-counting loop would terminate immediately and report $0$ digits.

The upper end matters too: $N$ may be $1000000$, which has seven digits and must print the string rather than a number. So the output type is not uniform — three of the four branches emit an integer and one emits a sentence, which has to be spelled exactly as given.

There is **no $T$**: a single number is the whole input. The sample `9` is a one-digit number, giving `1`.

## Solution (Python)

```python
import sys


def main() -> None:
    # Single value. Reading it as text counts digits without special-casing 0.
    s = sys.stdin.buffer.read().split()[0].decode()
    d = len(s)
    print(d if d <= 3 else "More than 3 digits")


main()
```

## Complexity

- **Time:** $O(d)$
- **Space:** $O(d)$

> CodeChef tags: `Special`, `Basic Programming Concepts`, `Mathematics`
