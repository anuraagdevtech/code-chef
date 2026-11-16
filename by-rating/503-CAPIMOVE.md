[&larr; 502. Palpal Strings](502-PALPALS.md) &middot; [Index](README.md) &middot; [504. K-Concatenation &rarr;](504-KCON.md)

# 503. Capital Movement

> [`CAPIMOVE`](https://www.codechef.com/problems/CAPIMOVE) &middot; difficulty **1780** &middot; time limit **1.5s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | Scan population order while marking each closed neighbourhood |
| **CodeChef tags** | `Data Structures`, `Sets` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N\log N)$ per test case |
| **Space** | $O(N)$ |

## Question

Chef is playing a video game. In a video game, there's a advanced civilization that has a total of **N** planets under control. All of those planets are connected with **N-1** teleports in such a way, that it's possible to travel between any two planets using those teleports.

There's a chance that some planet gets infected. In this case it takes 24 hours for civilization to find out infection and prevent it from spreading. During this time infection uses teleport one time and infect all the planets that can be achieved in one teleport jump. So, once infection is detected at planet **V**, scientists already know that all planets connected to **V** via teleport are also infected. All the neccessary teleports are disabled right away and medics start working on eliminating the infection.

Each planet has population. Planets are numbered from **1** to **N** and their populations are **P_1**, **P_2**, ..., **P_N**. It is known that all the **P_i** are distinct.

There's a capital among all those planets. The capital is known to have the biggest population.

Once infection is detected at planet **V**, after disabling teleports on planet **V** and all connected to them, government has to establish a new capital if needed in the remaining not-infected planets. So, they list all the planets that are not connected to **V** and are not **V**. Then they pick the planet with biggest population. Your task is to find the number of this planet for every possible **V**.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of each test case contains one integer **N**.

Next line contains **N** space-separated integers **P_1**, **P_2**, ..., **P_N** denoting the population of each planet.

Next **N-1** lines contain two space-separated integers each **V** and **U** denoting that there's a teleport between planet **V** and **U**.

**Output**

For each test case, output a single line containing **N** integers **A_1**, **A_2**, ..., **A_N** separated by a space. Here **A_i** denotes the number of the planet picked to be new capital in case infection starts spreading from the planet **i**. In case infection affects all the planets output **0**.

**Constraints**

- **1** ≤ **T** ≤ **5**

- **1** ≤ **N** ≤ **50000**

- **1** ≤ **P_i** ≤ **10^9**

- All **P_i** are distinct

- **1** ≤ **V** ≤ **N**

- **1** ≤ **U** ≤ **N**

**Subtasks**

- **Subtask #1 (20 points): N ≤ 100**

- **Subtask #2 (30 points): N ≤ 10000**

- **Subtask #3 (50 points): No additional constraints**

## Constraints

- 1 ≤ T ≤ 5
- 1 ≤ N ≤ 50000
- 1 ≤ P_i ≤ 10^9
- All P_i are distinct
- 1 ≤ V ≤ N
- 1 ≤ U ≤ N

## Sample

**Sample input**

```
1
6
5 10 15 20 25 30
1 3
2 3
3 4
4 5
4 6
```

**Sample output**

```
6 6 6 2 6 5
```

## Approach

Sort vertices by descending population. For each possible infected vertex, temporarily mark itself and all its neighbours. The first unmarked vertex in population order is the best surviving capital; return zero if none remains.

If a scan skips $k$ vertices, all of them belong to that vertex's closed neighbourhood. Thus its scan is bounded by degree plus two. Summing tree degrees gives $2(N-1)$, so all scans together are linear after sorting. Timestamp marks avoid clearing a full array per vertex.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        population = [int(next(tokens)) for _ in range(n)]
        graph = [[] for _ in range(n)]
        for _ in range(n-1):
            u, v = int(next(tokens))-1, int(next(tokens))-1
            graph[u].append(v)
            graph[v].append(u)
        order = sorted(range(n), key=population.__getitem__, reverse=True)
        marks = [-1]*n
        answer = []
        for u in range(n):
            marks[u] = u
            for v in graph[u]:
                marks[v] = u
            capital = next((v+1 for v in order if marks[v] != u), 0)
            answer.append(capital)
        out.append(' '.join(map(str,answer)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- The infected vertex itself cannot be the capital.
- A star centre leaves no survivor.
- A one-vertex tree returns zero.

## Dry run

In the sample, infection at vertex 4 excludes vertices `3,4,5,6`. Among survivors `1,2`, vertex 2 has larger population, so its answer is 2.

---

Same problem grouped by topic: [../docs/graphs/CAPIMOVE.md](../docs/graphs/CAPIMOVE.md)
