# 63. Too many Floors

> CodeChef problem code [`FLOORS`](https://www.codechef.com/problems/FLOORS) &middot; difficulty **717** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Mapping an index to its block |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Chef and Chefina are residing in a hotel.

There are $10$ floors in the hotel and each floor consists of $10$ rooms.

- Floor $1$ consists of room numbers $1$ to $10$.
- Floor $2$ consists of room numbers $11$ to $20$.
$\ldots$
- Floor $i$ consists of room numbers $10 \cdot (i-1) + 1$ to $10 \cdot i$.

You know that Chef's room number is $X$ while Chefina's Room number is $Y$.
If Chef starts from his room, find the number of floors he needs to travel to reach Chefina's room.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers $X, Y$, the room numbers of Chef and Chefina respectively.

**Output**

For each test case, output the number of floors Chef needs to travel to reach Chefina's room.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X, Y \leq 100$
- $X \neq Y$

## Sample

**Sample input**

```
4
1 100
42 50
53 30
81 80
```

**Sample output**

```
9
0
3
1
```

<details><summary>Explanation</summary>

**Test Case $1$:** Since Room $1$ is on $1^{st}$ floor and Room $100$ is on $10^{th}$ floor, Chef needs to climb $9$ floors to reach Chefina's Room.

**Test Case $2$:** Since Room $42$ is on $5^{th}$ floor and Room $50$ is also on $5^{th}$ floor, Chef does not need to climb any floor.

**Test Case $3$:** Since Room $53$ is on $6^{th}$ floor and Room $30$ is on $3^{rd}$ floor, Chef needs to go down $3$ floors to reach Chefina's Room.

**Test Case $4$:** Since Room $81$ is on $9^{th}$ floor and Room $80$ is on $8^{th}$ floor, Chef needs to go down $1$ floors to reach Chefina's Room.

</details>

## Approach

Rooms are grouped ten to a floor, with floor $i$ holding rooms $10(i-1)+1$ through $10i$. Inverting that gives the floor of room $r$:

$$\text{floor}(r) = \left\lfloor \frac{r - 1}{10} \right\rfloor + 1$$

and the answer is the absolute difference of the two floors.

The $-1$ and $+1$ are doing the work, and they are there because the numbering is **one-based**. Room $10$ must land on floor $1$ and room $11$ on floor $2$; the naive `r // 10 + 1` puts room $10$ on floor $2$ and breaks on every multiple of ten. Shifting to zero-based with $r - 1$, dividing, then shifting back is the general recipe for one-based block arithmetic, and it is the same manoeuvre used for the bus-seat problem.

Since only the *difference* of the two floors is wanted, the trailing $+1$ cancels and `(x - 1) // 10` would do just as well for both rooms. The code keeps it for readability — the helper genuinely returns a floor number.

The absolute value is needed because Chef may live above or below Chefina; sample case 3 goes downward, from floor $6$ to floor $3$.

Sample case 2 is the same-floor case: rooms $42$ and $50$ both sit on floor $5$, so the answer is $0$ despite the rooms differing by $8$. Sample case 4 is its neighbour — rooms $81$ and $80$ differ by just one yet straddle a floor boundary, giving $1$.

## Solution (Python)

```python
import sys


def floor_of(room: int) -> int:
    # Rooms are numbered from 1, so shift to zero-based before dividing.
    return (room - 1) // 10 + 1


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        out.append(str(abs(floor_of(x) - floor_of(y))))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Mathematics`
