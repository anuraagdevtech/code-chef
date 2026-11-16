[&larr; 583. Pizza Delivery](DBOY.md) &middot; [Index](../../README.md) &middot; [586. String Merging &rarr;](STRMRG.md)

# 585. Trip

> CodeChef problem code [`TRIP`](https://www.codechef.com/problems/TRIP) &middot; difficulty **2005** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Sliding reachability window and shortest-level prefix counts |
| **Time** | $O(N)$ overall |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

You are starting out on a long (really long) trip. On the way, there are N gas stations, the locations of which are given as a_1,a_2,...,a_N. Initially you are located at the gas station at a_1, and your destination is at location a_N. Your car can only store enough fuel to travel atmost M units without refilling. You can stop at any station and refill the car by any amount. Now you wish to plan your trip such that the number of intermediate stops needed to reach the destination is minimum, and also how many ways are there to plan your trip accordingly.

**
Input :
**

The first line two space seperated integers N and M. N lines follow, and the ith line has the value a_i (0 <= a_i <= 1000000000). The input will be such that a solution will always exist.

**
Output :
**

Output two space seperated integers : The least number of stops, and the number of ways to plan the trip which uses the least number of stops. Output this value modulo 1000000007.

**
Constraints :**

```
2 <= N <= 1000000
1 <= M <= 1000
a_1 < a_2 < .. < a_N
```

## Constraints

2 <= N <= 1000000
1 <= M <= 1000
a_1 < a_2 < .. < a_N

## Sample

**Sample input**

```
6 3
0
1
3
4
7
10
```

**Sample output**

```
3 2
```

## Approach

Let $dist[j]$ be the least number of drives to station $j$. Reachable predecessor stations form a sliding suffix interval of earlier stations. Distances are nondecreasing with station position, so its leftmost predecessor has the smallest distance. All predecessors with that distance give shortest routes to $j$.

Maintain the last processed index at each distance level and a prefix sum of route counts. This gives the sum of ways over the optimal predecessor interval in constant time. Advance the left boundary while stations fall out of fuel range. Subtract one from the final number of drives to obtain the number of intermediate stops.

## Solution (Python)

```python
import sys
from array import array


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    n,capacity = int(next(tokens)),int(next(tokens))
    position = array('q',(int(next(tokens)) for _ in range(n)))
    del tokens
    distance = array('i',[0])*n
    prefix = array('i',[0])*(n+1)
    prefix[1] = 1
    level_end = [0]
    left = 0
    mod = 1000000007
    for j in range(1,n):
        while position[j]-position[left] > capacity:
            left += 1
        level = distance[left]
        ways = (prefix[level_end[level]+1]-prefix[left])%mod
        distance[j] = level+1
        if distance[j] == len(level_end):
            level_end.append(j)
        else:
            level_end[distance[j]] = j
        prefix[j+1] = (prefix[j]+ways)%mod
    print(distance[-1]-1,(prefix[n]-prefix[n-1])%mod)

if __name__ == '__main__':
    main()
```

## Complexity

- **Time:** $O(N)$ overall
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Starting and destination stations are not intermediate stops.
- A direct drive gives zero stops and one route.
- Stations are already strictly increasing.
- The input guarantees every necessary gap is traversable.

## Dry run

In the sample, routes `0->1->4->7->10` and `0->3->4->7->10` both use four drives, hence three intermediate stops and two optimal plans.

---

Same problem in rating order (#567 of 735): [../../by-rating/567-TRIP.md](../../by-rating/567-TRIP.md)
