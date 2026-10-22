[&larr; 242. Parallel Processing](242-PLPROCESS.md) &middot; [Index](README.md) &middot; [244. Full Barrier Alchemist &rarr;](244-PIPSQUIK.md)

# 243. Reversing directions

> [`DIRECTI`](https://www.codechef.com/problems/DIRECTI) &middot; difficulty **1426** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Parsing and reversing a route |
| **CodeChef tags** | `Data Structures`, `Algorithms`, `String`, `Implementation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

Chef recently printed directions from his home to a hot new restaurant across the town, but forgot to print the directions to get back home. Help Chef to transform the directions to get home from the restaurant.

A set of directions consists of several instructions. The first instruction is of the form "Begin on XXX", indicating the street that the route begins on. Each subsequent instruction is of the form "Left on XXX" or "Right on XXX", indicating a turn onto the specified road.

When reversing directions, all left turns become right turns and vice versa, and the order of roads and turns is reversed. See the sample input for examples.

**Input**

Input will begin with an integer **T**, the number of test cases that follow. Each test case begins with an integer **N**, the number of instructions in the route. **N** lines follow, each with exactly one instruction in the format described above.

**Output**

For each test case, print the directions of the reversed route, one instruction per line. Print a blank line after each test case.

**Constraints**

- 1 ≤ **T** ≤ 15

- 2 ≤ **N** ≤ 40

- Each line in the input will contain at most 50 characters, will contain only alphanumeric characters and spaces and will not contain consecutive spaces nor trailing spaces. By alphanumeric characters we mean digits and letters of the English alphabet (lowercase and uppercase).

## Constraints

- 1 ≤ T ≤ 15
- 2 ≤ N ≤ 40
- Each line in the input will contain at most 50 characters, will contain only alphanumeric characters and spaces and will not contain consecutive spaces nor trailing spaces. By alphanumeric characters we mean digits and letters of the English alphabet (lowercase and uppercase).

## Sample

**Sample input**

```
2
4
Begin on Road A
Right on Road B
Right on Road C
Left on Road D
6
Begin on Old Madras Road
Left on Domlur Flyover
Left on 100 Feet Road
Right on Sarjapur Road
Right on Hosur Road
Right on Ganapathi Temple Road
```

**Sample output**

```
Begin on Road D
Right on Road C
Left on Road B
Left on Road A

Begin on Ganapathi Temple Road
Left on Hosur Road
Left on Sarjapur Road
Left on 100 Feet Road
Right on Domlur Flyover
Right on Old Madras Road
```

<details><summary>Explanation</summary>

In the first test case, the destination lies on Road D, hence the reversed route begins on Road D. The final turn in the original route is turning left from Road C onto Road D. The reverse of this, turning right from Road D onto Road C, is the first turn in the reversed route.

</details>

## Approach

Separate each instruction into its **turn** and its **road**. The first line is `Begin on <road>`; every later line is `Left on <road>` or `Right on <road>`. Splitting on the first occurrence of `" on "` is the safe way to do it, since road names contain spaces — `Old Madras Road` would break a naive `split()`.

Reversing the route pairs each road with a *different* turn. Driving out, the turn listed with road $i$ is the one taken to **enter** road $i$. Driving back, that same junction is taken in the opposite sense and now leads onto road $i-1$. So:

- the new `Begin on` road is the **last** road of the original;
- for $i$ from $N-1$ down to $1$, emit the **flip** of turn $i$ together with road $i-1$.

Each `Left` becomes `Right` and vice versa.

That index shift is where this problem is usually lost. Reversing the list and keeping each turn attached to its own road produces a route of the right length that turns the wrong way at every junction. Sample case 1 shows the offset clearly: the outbound route ends `Left on Road D`, and the return route starts `Begin on Road D` and immediately turns **Right** onto Road C — the flipped version of the turn that *entered* Road C, not the one that entered Road D.

The output format needs a **blank line after each test case**, including the last. Omitting it is a common presentation error.

With $N \leq 40$ the cost is irrelevant; the whole difficulty is the pairing and the parsing.

## Solution

```python
import sys

FLIP = {"Left": "Right", "Right": "Left"}


def main() -> None:
    lines = sys.stdin.read().split("\n")
    idx = 0
    t = int(lines[idx].strip()); idx += 1
    out = []
    for _ in range(t):
        n = int(lines[idx].strip()); idx += 1
        turns, roads = [], []
        for _ in range(n):
            # Road names contain spaces, so split on the first " on " only.
            turn, road = lines[idx].strip().split(" on ", 1)
            idx += 1
            turns.append(turn)
            roads.append(road)
        out.append(f"Begin on {roads[-1]}")
        # Turn i entered road i on the way out; coming back it leads to i - 1.
        for i in range(n - 1, 0, -1):
            out.append(f"{FLIP[turns[i]]} on {roads[i - 1]}")
        out.append("")                 # blank line after every test case
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Road names contain spaces and digits**, so the split must be on the *first* `" on "` only. `100 Feet Road` and `Ganapathi Temple Road` both break a naive split on whitespace, and a split without `maxsplit=1` would also mangle any name containing the word `on`.
- **The turn and the road are offset by one on the way back.** Turn $i$ was what took you *onto* road $i$; returning, that same junction leads you onto road $i-1$. Pairing turn $i$ with road $i$ is the natural mistake and shifts the whole output.
- **`Begin` is never flipped.** It is dropped entirely and replaced by a fresh `Begin on <last road>`.
- **A blank line follows every test case**, including the last one.
- **$N \geq 2$ is guaranteed**, so there is always at least one turn to reverse.
- **Only `Left` and `Right` occur** as turns after the first, so a two-entry lookup table covers every flip.

## Dry run

First sample.

| outward | | return |
|---|---|---|
| Begin on Road A | | Begin on Road D |
| Right on Road B | turn 4 was `Left`, previous road is C | Right on Road C |
| Right on Road C | turn 3 was `Right`, previous road is B | Left on Road B |
| Left on Road D | turn 2 was `Right`, previous road is A | Left on Road A |

Each returned turn is the flip of the turn that *followed* the road being entered.

---

Same problem grouped by topic: [../docs/strings/DIRECTI.md](../docs/strings/DIRECTI.md)
