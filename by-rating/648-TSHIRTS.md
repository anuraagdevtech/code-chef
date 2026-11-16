[&larr; 647. Distinct Values](647-DIST_VALS.md) &middot; [Index](README.md) &middot; [649. Chef and Ants &rarr;](649-ANTSCHEF.md)

# 648. Little Elephant and T-Shirts

> [`TSHIRTS`](https://www.codechef.com/problems/TSHIRTS) &middot; difficulty **2242** &middot; time limit **1.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Bitmask over people, processing the 100 shirts one at a time |
| **CodeChef tags** | `Advanced Algorithms`, `Advanced DP`, `Mathematics`, `Bit Manipulation`, `DP Bitmask`, `Bitmasking` |
| **Complexity class** | Exponential subset DP $O(2^K K^2)$ |
| **Time** | $O(100 \cdot 2^N \cdot N)$ per test case |
| **Space** | $O(2^N)$ |

## Question

Little Elephant and his friends are going to a party. Each person has his own collection of T-Shirts. There are **100** different kind of T-Shirts. Each T-Shirt has a unique id between **1** and **100**. No person has two T-Shirts of the same ID.

They want to know how many arrangements are there in which no two persons wear same T-Shirt. One arrangement is considered different from another arrangement if there is at least one person wearing a different kind of T-Shirt in another arrangement.

**Input**

First line of the input contains a single integer ** T ** denoting number of test cases. Then **T** test cases follow.

For each test case, first line contains an integer **N**, denoting the total number of persons. Each of the next **N** lines contains at least **1** and at most **100** space separated distinct integers, denoting the ID's of the T-Shirts **i**^th person has.

**Output**

For each test case, print in single line the required number of ways modulo **1000000007 = 10^9+7**.

**Constraints**

- **1 ≤ T ≤ 10**

- **1 ≤ N ≤ 10**

**Example**

```
**Input:**
2
2
3 5
8 100
3
5 100 1
2
5 100

**Output:**
4
4
```

**Explanation**

For the first case, **4** possible ways are **(3,8)**, **(3,100)**, **(5,8)** and **(5,100)**.For the second case, **4** possible ways are **(5,2,100)**, **(100,2,5)**, **(1,2,100)**, and **(1,2,5)**.

## Constraints

- 1 ≤ T ≤ 10
- 1 ≤ N ≤ 10

## Approach

There are at most 10 people but 100 shirt ids, so the state is the set of people who already have a shirt, and the shirts are the items processed one by one.

`ways[mask]` is the number of ways to dress exactly the people in `mask` using the shirts considered so far. For the next shirt id either nobody wears it, or exactly one person who owns it and is not yet dressed wears it: `ways[mask | bit] += ways[mask]`. Iterating the masks in decreasing order guarantees that a shirt is not handed out twice within the same step, since the target mask is always larger than the source.

The answer is `ways[full mask]`. Each line of the input lists one person's shirts and has variable length, so the input is read line by line.

## Solution

```python
import sys


def main():
    lines = iter(sys.stdin.buffer.read().splitlines())
    t = int(next(lines))
    out = []
    MOD = 1000000007
    for _ in range(t):
        n = int(next(lines))
        owners = [[] for _ in range(101)]
        for i in range(n):
            for shirt in map(int, next(lines).split()):
                owners[shirt].append(1 << i)
        ways = [0] * (1 << n)
        ways[0] = 1
        for people in owners:
            for mask in range((1 << n) - 1, -1, -1):
                if ways[mask]:
                    for bit in people:
                        if not mask & bit:
                            ways[mask | bit] = (ways[mask | bit] + ways[mask]) % MOD
        out.append(str(ways[-1]))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- A shirt nobody owns changes nothing.
- A person with a single shirt forces that shirt, which the DP handles naturally.
- If two people only own the same single shirt the answer is 0.
- Results are modulo $10^9 + 7$.

## Dry run

Two people with shirts `{3, 5}` and `{8, 100}`. Masks are written as (person 2, person 1).

- shirt 3: `01` gets 1 way.
- shirt 5: `01` gets one more: 2 ways.
- shirt 8: from `00` to `10` (1 way), from `01` to `11` (2 ways).
- shirt 100: from `00` to `10` (now 2), from `01` to `11` (now 4).

Answer 4.

---

Same problem grouped by topic: [../docs/dynamic-programming/TSHIRTS.md](../docs/dynamic-programming/TSHIRTS.md)
