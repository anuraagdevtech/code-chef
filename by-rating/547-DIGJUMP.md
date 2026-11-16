[&larr; 546. ChefTown Parade](546-CHEFTOWN.md) &middot; [Index](README.md) &middot; [548. Petersen Graph &rarr;](548-PETERSEN.md)

# 547. Chef and Digit Jumps

> [`DIGJUMP`](https://www.codechef.com/problems/DIGJUMP) &middot; difficulty **1886** &middot; time limit **1.5s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | BFS with each equal-digit group expanded once |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ overall |
| **Space** | $O(N)$ |

## Question

Chef loves games! But he likes to invent his own. Now he plays game "Digit Jump". Chef has a sequence of digits $S_{1}, S_{2}, \ldots , S_{N}$. He is staying in the first digit $S_{1}$ and wants to reach the last digit $S_{N}$ in the minimal number of jumps.

While staying in some index $i$ Chef can jump into $i - 1$ and $i + 1$, but he can't jump out from sequence. Or he can jump into any digit with the same value $S_i$.

Help Chef to find the minimal number of jumps he need to reach digit $S_{N}$ from digit $S_1$. 

**Input**
Input contains a single line consist of string $S$ of length $N$ - the sequence of digits.

**Output**
In a single line print single integer - the minimal number of jumps he needs.

**Constraints**
- $1\leq N \leq 10^5$
- Each symbol of $S$ is a digit from $0$ to $9$.

## Constraints

- $1\leq N \leq 10^5$
- Each symbol of $S$ is a digit from $0$ to $9$.

## Sample

**Sample 1 input**

```
01234567890
```

**Sample 1 output**

```
1
```

<details><summary>Explanation</summary>

***Test Case 1:*** Chef can directly jump from the first digit (it is $0$) to the last (as it is also $0$).

</details>

**Sample 2 input**

```
012134444444443
```

**Sample 2 output**

```
4
```

<details><summary>Explanation</summary>

***Test Case 2:*** Chef should follow the following path: $1 - 2 - 4 - 5 - 15$.

</details>

## Approach

Positions are vertices. Adjacent positions and positions with the same digit are connected by unit-cost jumps. Ordinary BFS yields the shortest route, but explicitly adding every equal-digit edge could be quadratic.

Store the positions of each of the ten digits. The first time BFS visits a digit, enqueue every still-unvisited position in its group and clear that group. Later expansions cannot improve those distances, so each position participates in one group expansion and at most two adjacency checks.

## Solution

```python
import sys
from collections import deque


def main() -> None:
    s = sys.stdin.buffer.read().strip()
    n = len(s)
    positions = [[] for _ in range(10)]
    for i,c in enumerate(s):
        positions[c-48].append(i)
    distance = [-1]*n
    distance[0] = 0
    queue = deque([0])
    while queue:
        u = queue.popleft()
        if u == n-1:
            print(distance[u])
            return
        digit = s[u]-48
        group = positions[digit]
        positions[digit] = []
        for v in group:
            if distance[v] == -1:
                distance[v] = distance[u]+1
                queue.append(v)
        for v in (u-1,u+1):
            if 0 <= v < n and distance[v] == -1:
                distance[v] = distance[u]+1
                queue.append(v)

if __name__ == '__main__':
    main()
```

## Edge cases

- A one-character string requires zero jumps.
- Equal first and last digits allow a direct one-jump route.
- Clear each digit group after its first expansion.

## Dry run

For `01234567890`, positions zero and ten both contain zero. Expanding the initial digit group immediately reaches the last position at distance one.

---

Same problem grouped by topic: [../docs/graphs/DIGJUMP.md](../docs/graphs/DIGJUMP.md)
