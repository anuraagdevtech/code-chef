[&larr; 571. Subtree Removal](571-SUBREM.md) &middot; [Index](README.md) &middot; [573. Yet Another Problem About Sequences &rarr;](573-EARTSEQ.md)

# 572. Alternative Sufferings

> [`ALTSUFF`](https://www.codechef.com/problems/ALTSUFF) &middot; difficulty **2011** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Simulation |
| **Technique** | One simulated step, then distance to the nearest seed and parity |
| **CodeChef tags** | `Algorithms`, `Constructive`, `ad-hoc`, `Observation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

You are given a binary string $S$.

In one second, the following scenario happens **simultaneously** and **independently** for **all** the bits which are set to $1$ in the string:

- Change the bit from $1$ to $0$.
- If the left neighbour exists and is $0$, change it to $1$.
- If the right neighbour exists and is $0$, change it to $1$.

For example, if $S = 010$ initially, then after $1$ second, $S = 101$ (the $1$ bit and both its neighbours were changed). After another second, $S = 010$. Here, the first and the last bit were changed to $0$ because earlier they were $1$. The middle bit was changed because it was $0$ earlier and it was a neighbour of a $1$ bit.

Find out the string $S$ after $K$ seconds.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $K$ — the length of string $S$ and the number of seconds.
    - The next line describes the string $S$.

**Output**

For each test case, output the string $S$ after exactly $K$ seconds.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- $1 \leq K \leq 10^9$
- The sum of $N$ over all test cases won't exceed $10^6$.
- $S$ can only contain the characters $0$ or $1$.

## Sample

**Sample input**

```
3
3 1
101
5 2
10001
14 3
10011010111000
```

**Sample output**

```
010
10101
01100101010101
```

<details><summary>Explanation</summary>

**Test case $1$:** The middle bit is changed to $1$ since it had a neighbouring set bit (in this case both left and right) and both the set bits are changed to $0$. Hence, after one second, it is $101$.

**Test case $2$:** After first second, the string $S$ will be $01010$. After another second , the string becomes $10101$.

</details>

## Approach

After the first second the picture becomes regular. Every old 1 turns into 0, and a position is 1 exactly when it was 0 and had a neighbouring 1. Call these positions the seeds. If there are none (all zeros, or all ones), the string is all zeros from then on.

From this moment each seed behaves like a source that sends a front outwards one cell per second while the cells behind the front alternate between 1 and 0. A cell at distance $d$ from its nearest seed is first reached $d$ seconds later and from then on is 1 every second step. Fronts coming from two different seeds agree in parity wherever they meet, or meet between two adjacent cells, so taking the nearest seed is enough.

So with $k = K - 1$ seconds remaining after the first one, cell $i$ is 1 exactly when $d_i \le k$ and $k - d_i$ is even. The distances come from one left-to-right and one right-to-left pass.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        k = int(next(tokens))
        bits = next(tokens).decode()
        seeds = [i for i in range(n) if bits[i] == '0' and (i and bits[i - 1] == '1' or (i + 1 < n and bits[i + 1] == '1'))]
        if not seeds:
            out.append('0' * n)
            continue
        k -= 1
        distance = [n + 1] * n
        last = -2 * n
        for i in range(n):
            if bits[i] == '0' and (i and bits[i - 1] == '1' or (i + 1 < n and bits[i + 1] == '1')):
                last = i
            distance[i] = i - last
        last = 3 * n
        for i in range(n - 1, -1, -1):
            if bits[i] == '0' and (i and bits[i - 1] == '1' or (i + 1 < n and bits[i + 1] == '1')):
                last = i
            distance[i] = min(distance[i], last - i)
        out.append(''.join(('1' if v <= k and (k - v) % 2 == 0 else '0' for v in distance)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- No seed after the first second: the answer is all zeros.
- $K$ is up to $10^9$; nothing is simulated beyond the first step.
- $K = 1$ gives exactly the seed string ($d = 0$, $k = 0$).
- A string of length 1 containing `1` becomes `0` and stays there.

## Dry run

`S = 10001`, `K = 2`.

After one second the seeds are the zeros next to a one: positions 2 and 4, i.e. `01010`. One second remains, $k = 1$.

Distances to the nearest seed: `1 0 1 0 1`. A cell is 1 when $d \le 1$ and $1 - d$ is even, i.e. $d = 1$: positions 1, 3, 5.

Answer `10101`.

---

Same problem grouped by topic: [../docs/simulation/ALTSUFF.md](../docs/simulation/ALTSUFF.md)
