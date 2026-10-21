---
topic: Conditionals & Case Work
subtopic: Three-way comparison
time: $O(1)$ per test case
space: $O(1)$
---
$X$ is the bike's travel time and $Y$ is the car's, and lower time means faster. The answer is a three-way branch on the comparison of two numbers: `BIKE` when $X < Y$, `CAR` when $Y < X$, and `SAME` when they are equal.

The only thing to be careful about is not inverting the relation. "Faster" is *smaller* time, so the vehicle with the **minimum** value wins. Reading $X < Y$ as "car wins" is the natural slip, and the samples catch it immediately: $X = 1, Y = 5$ answers `BIKE`.

There are exactly three outcomes and they are mutually exclusive, so an `if / elif / else` covers the space completely with no possibility of falling through. Unlike the sale-discount ladder, the order of the branches here carries no meaning — any ordering is correct, because the conditions do not overlap.

Note also that the equality case must be handled explicitly. Writing only `if x < y: BIKE else: CAR` would silently report `CAR` for a tie, which is wrong; whenever a comparison problem offers a "same" answer, the `==` branch needs its own place.

## Edge cases

- **Equal times** ($6$ and $6$): neither is faster, so `SAME` needs its own branch — a plain two-way `if/else` would wrongly pick a winner. The sample tests it.
- **Extremes** ($1$ against $10$): the gap does not matter, only the direction.
- $X$ is the bike's time and $Y$ the car's, which the sample's first row pins down: $X = 1 < Y = 5$ answers `BIKE`.
- Both bounds are small positive integers, so there is no zero-time or negative case to consider.

## Dry run

| $X$ (bike) | $Y$ (car) | comparison | output |
|---:|---:|---|---|
| 1 | 5 | $X < Y$ | `BIKE` |
| 4 | 2 | $Y < X$ | `CAR` |
| 6 | 6 | equal | `SAME` |

The three rows walk through all three branches.
