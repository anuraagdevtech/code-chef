[&larr; 540. Per Capita Income](PERCAPTA.md) &middot; [Index](../../README.md) &middot; [542. Road Decoration &rarr;](AMR14B.md)

# 541. FCAR

> CodeChef problem code [`INSQ15_F`](https://www.codechef.com/problems/INSQ15_F) &middot; difficulty **unrated** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | Dijkstra on city and current travel mode |
| **Time** | $O((N+R)\log N)$ overall |
| **Space** | $O(N+R)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Cars of future no longer need fuel to run, but they are fitted with special engines which can only operate in one of the two **modes** at a time ,either go **up the road**, or go **down the road**.

There are **N** towns in country. i^th town is at height **H[i] (1 ≤ i ≤ N)** above the sea level.

Changing mode of the car requires permissions from mayor of the town you are currently at. Mayor of **i^th **town charges amount **C[i] (1 ≤ i ≤ n)** for giving permission to change mode of the car.

These N towns are connected by **R** bidirectional roads. Initially no mode is set, so you need permissions to set a mode.

You have to travel from town 1 to N, in minimum amount of cost. Print minimum money required to make the travel. If it is impossible print -1.

**Note:**

- Go up the road mode: when you are at town A and want to go to town B, where H[A] <= H[B]

- Go down the road mode: when you are at town A and want to go to town B, where H[A] >= H[B]

- If you continue with the same mode, you do not need to take permissions from mayor.

 

**Input**

- First line contains two space separated integer N and R, number of towns and number of roads.

- Next line contains N space separated integer where i^th integer is H[i], height of i^th town.

- Next line contains N space separated integer where i^th integer is C[i], cost charged by mayor of i^th town to give permission for changing the mode.

- Next R lines contains two space separated integer u and v, specifying there is a bidirectional road between town u and v.

 

**Output**

Print minimum cost required for travel. If it is impossible print -1.

**Constraints**

- **2** ≤ **N** ≤ **100000**

- **1** ≤ **R** ≤ **500000**

- **1** ≤ **H[i]** ≤ **10^9**

- **1** ≤ **C[i]** ≤ **10^9**

 

**Example**

```
**Input:**
6 6
10 5 7 15 20 6
1 1 1 1 1 1
1 2
2 3
3 6
1 4
4 5
5 6

**Output:**
2
```

 

**Explanation**

There are two paths from 1 - 6

**P1: (1, 2, 3, 6)**

You need to pay $1 to mayor of town 1 to chose down mode. (H[1] >= H[2])

You need to pay $1 to mayor of town 2 to chose up mode. (H[2] <= H[3])
You need to pay $1 to mayor of town 3 to chose down mode. (H[3] >= H[6])

Total cost = $3

**P2: (1, 4, 5, 6)**

You need to pay $1 to mayor of town 1 to chose up mode. (H[1] <= H[4])

You continue with the previous up mode. (H[4] <= H[5])

You need to pay $1 to mayor of town 5 to chose down mode. (H[5] >= H[6])

Total cost = $2

So minimum money required is $2.

## Constraints

- 2 ≤ N ≤ 100000
- 1 ≤ R ≤ 500000
- 1 ≤ H[i] ≤ 10^9
- 1 ≤ C[i] ≤ 10^9

## Approach

Use two states for each city: uphill mode and downhill mode. Switching mode at city $u$ costs $C_u$. A road can be traversed at zero additional cost in uphill mode when the next height is no smaller, and in downhill mode when it is no greater. Equal heights permit either mode.

Initialising either mode at city 1 costs $C_1$, as required by the statement. Run Dijkstra on these implicit state transitions and take the smaller destination-state distance.

## Solution (Python)

```python
import sys
from heapq import heappush,heappop


def main() -> None:
    tokens = iter(map(int,sys.stdin.buffer.read().split()))
    n,m = next(tokens),next(tokens)
    height = [next(tokens) for _ in range(n)]
    cost = [next(tokens) for _ in range(n)]
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u,v = next(tokens)-1,next(tokens)-1
        graph[u].append(v)
        graph[v].append(u)
    infinity = 10**30
    distance = [infinity]*(2*n)
    distance[0] = distance[1] = cost[0]
    heap = [(cost[0],0),(cost[0],1)]
    while heap:
        d,state = heappop(heap)
        if d != distance[state]:
            continue
        u,mode = divmod(state,2)
        switched = state^1
        if d+cost[u] < distance[switched]:
            distance[switched] = d+cost[u]
            heappush(heap,(distance[switched],switched))
        for v in graph[u]:
            if (mode == 0 and height[v] >= height[u]) or (mode == 1 and height[v] <= height[u]):
                target = 2*v+mode
                if d < distance[target]:
                    distance[target] = d
                    heappush(heap,(d,target))
    answer = min(distance[-2:])
    print(answer if answer < infinity else -1)

if __name__ == '__main__':
    main()
```

## Complexity

- **Time:** $O((N+R)\log N)$ overall
- **Space:** $O(N+R)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Initial mode selection must be paid for.
- Equal-height roads preserve either mode.
- A disconnected destination returns minus one.
- A more expensive path in road length may still have lower mode-switch cost.

## Dry run

For the statement sample, path `1-4-5-6` chooses uphill at city 1 for one unit, stays uphill to city 5, then switches downhill for one unit. Total cost is 2.

---

Same problem in rating order (#726 of 735): [../../by-rating/726-INSQ15_F.md](../../by-rating/726-INSQ15_F.md)
