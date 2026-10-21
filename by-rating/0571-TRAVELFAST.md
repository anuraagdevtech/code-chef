# 571 &middot; Car or Bike

> CodeChef problem code [`TRAVELFAST`](https://www.codechef.com/problems/TRAVELFAST) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Three-way comparison |
| **CodeChef tags** | `Mathematics`, `Basic Math` |
| **CodeChef category** | extcontest |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/conditionals-case-work/TRAVELFAST.md](../docs/conditionals-case-work/TRAVELFAST.md)

## Question

Chef wants to reach home as soon as possible. He has two options:

- Travel with his `BIKE` which takes $X$ minutes.
- Travel with his `CAR` which takes $Y$ minutes.

Which of the two options is faster or do they both take same time?

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains a single line of input, two integers $X, Y$ representing the time taken to travel with `BIKE` and `CAR` respectively.

**Output**

For each test case, print `CAR` if travelling with Car is faster, `BIKE` if travelling with Bike is faster, `SAME` if they both take the same time.

You may print each character of `CAR`, `BIKE` and `SAME` in uppercase or lowercase (for example, `CAR`, `Car`, `cAr` will be considered identical).

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X,Y \leq 10$

## Sample

**Sample input**

```
3
1 5
4 2
6 6
```

**Sample output**

```
BIKE
CAR
SAME
```

<details><summary>Explanation</summary>

**Test case-1:** Travelling with `BIKE` takes $1$ minute while travelling with `CAR` takes $5$ minutes. So travelling with `BIKE` is faster.

**Test case-2:** Travelling with `BIKE` takes $4$ minutes while travelling with `CAR` takes $2$ minutes. So travelling with `CAR` is faster.

**Test case-3:** Travelling with both `BIKE` and `CAR` takes the `SAME` time i.e. $6$ minutes.

</details>

## Approach

$X$ is the bike's travel time and $Y$ is the car's, and lower time means faster. The answer is a three-way branch on the comparison of two numbers: `BIKE` when $X < Y$, `CAR` when $Y < X$, and `SAME` when they are equal.

The only thing to be careful about is not inverting the relation. "Faster" is *smaller* time, so the vehicle with the **minimum** value wins. Reading $X < Y$ as "car wins" is the natural slip, and the samples catch it immediately: $X = 1, Y = 5$ answers `BIKE`.

There are exactly three outcomes and they are mutually exclusive, so an `if / elif / else` covers the space completely with no possibility of falling through. Unlike the sale-discount ladder, the order of the branches here carries no meaning — any ordering is correct, because the conditions do not overlap.

Note also that the equality case must be handled explicitly. Writing only `if x < y: BIKE else: CAR` would silently report `CAR` for a tie, which is wrong; whenever a comparison problem offers a "same" answer, the `==` branch needs its own place.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Lower time wins; the tie needs its own branch.
        out.append("BIKE" if x < y else "CAR" if y < x else "SAME")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
