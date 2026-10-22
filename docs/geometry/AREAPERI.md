# 108. Area OR Perimeter

> CodeChef problem code [`AREAPERI`](https://www.codechef.com/problems/AREAPERI) &middot; difficulty **590** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Geometry |
| **Technique** | Comparing area against perimeter |
| **Time** | $O(1)$ |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Write a program to obtain length $(L)$ and breadth $(B)$ of a rectangle and check whether its area is greater or perimeter is greater or both are equal.

**Input**

- First line will contain the length $(L)$ of the rectangle.
- Second line will contain the breadth $(B)$ of the rectangle.

**Output**

Output 2 lines.

In the first line print "Area" if area is greater otherwise print "Peri" and if they are equal print "Eq".(Without quotes).

In the second line print the calculated area or perimeter (whichever is greater or anyone if it is equal).

## Constraints

- $1 \leq L \leq 1000$
- $1 \leq B \leq 1000$

## Sample

**Sample input**

```
1
2
```

**Sample output**

```
Peri
6
```

<details><summary>Explanation</summary>

Area = 1 * 2 = 2 \
Peri = 2 * (1 + 2) = 6 \
Since Perimeter is greater than Area, hence the output is : \
Peri \
6

</details>

## Approach

For a rectangle with sides $L$ and $B$:

$$\text{area} = L \cdot B, \qquad \text{perimeter} = 2(L + B)$$

Compare them, print the label on the first line and the larger value on the second.

Comparing an area against a perimeter is dimensionally meaningless in physical terms — one is square units, the other linear — but as a numeric exercise it is well defined, and the problem simply wants the two numbers compared.

The output format is the part to get right: **two lines**, the word then the number. Print `Area`, `Peri`, or `Eq`, then the corresponding value. On a tie either value may be printed, and since they are equal it does not matter which expression is evaluated.

There is **no $T$** and the two inputs arrive on **separate lines** — $L$ first, then $B$. Reading them as one line of two tokens happens to work when parsing the whole stream as whitespace-separated tokens, which is what the solution below does, so the line structure is handled for free.

The sample is a thin rectangle where the perimeter wins: $L=1, B=2$ gives area $2$ against perimeter $6$. For most small rectangles the perimeter dominates; area overtakes it only once both sides grow past about $4$, with equality on cases such as $4 \times 4$ and $3 \times 6$.

## Solution (Python)

```python
import sys


def main() -> None:
    # Two values on separate lines, no test-case count.
    length, breadth = map(int, sys.stdin.buffer.read().split()[:2])
    area = length * breadth
    peri = 2 * (length + breadth)
    if area > peri:
        print("Area"); print(area)
    elif peri > area:
        print("Peri"); print(peri)
    else:
        print("Eq"); print(area)


main()
```

## Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

## Edge cases

- **Area equals perimeter**: then neither label applies and the answer is `Eq`. This happens for $L = B = 4$ (both $16$) and for $L = 3, B = 6$ (both $18$), so the third branch is genuinely reachable and must be there.
- **Smallest input** ($L = B = 1$): area $1$ against perimeter $4$, so `Peri` and $4$.
- **Largest input** ($L = B = 1000$): area $10^6$ against perimeter $4000$, so `Area`.
- **Output is two lines** — the label, then the winning value — and on `Eq` the value printed is the shared one.
- **Input shape**: two integers with no test-case count.

## Dry run

Input is $L = 1$, $B = 2$.

| step | value |
|---|---|
| area $L \times B$ | $2$ |
| perimeter $2(L + B)$ | $6$ |
| comparison | perimeter is larger |
| output | `Peri` then `6` |

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#31 of 486): [../../by-rating/031-AREAPERI.md](../../by-rating/031-AREAPERI.md)
