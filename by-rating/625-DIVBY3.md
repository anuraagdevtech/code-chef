[&larr; 624. Chef Goes Shopping](624-CHEFSHOPPING.md) &middot; [Index](README.md) &middot; [626. Sum of Goodness &rarr;](626-SEQGOODNESS.md)

# 625. Minimize swaps

> [`DIVBY3`](https://www.codechef.com/problems/DIVBY3) &middot; difficulty **2164** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Ones on even positions modulo three; the answer is always 0, 1, 2, 3 or -1 |
| **CodeChef tags** | `Special`, `Algorithms`, `Constructive`, `Case work`, `Dynamic Programming`, `ad-hoc` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

You are given a binary string $S$.
In one operation, you can pick an index $i$ $(1\le i \lt |S|)$ and swap the characters $S_i$ and $S_{(i+1)}$.

Find the **minimum** number of operations required, such that, the decimal representation of the final binary string is **divisible** by $3$. If it is impossible to do so, print $-1$ instead.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of single line of input, containing a binary string $S$.

**Output**

For each test case, output on a new line, the **minimum** number of operations required, such that, the decimal representation of the final binary string is **divisible** by $3$. If it is impossible to do so, print $-1$ instead.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq |S| \leq 3\cdot 10^5$
- $S$ consists of $0$ and $1$ only.
- The sum of $|S|$ over all test cases won't exceed $3\cdot 10^5$.

## Sample

**Sample input**

```
3
0000
111
11001
```

**Sample output**

```
0
-1
1
```

<details><summary>Explanation</summary>

**Test case $1$:** There is no need to apply any operation since the decimal representation of $0000$ is $0$ which is divisible by $3$.

**Test case $2$:** It can be shown that we cannot make the decimal representation of the string divisible by $3$ using any number of operations.

**Test case $3$:** The decimal representation of $11001$ is $25$ . Using one operation, we pick $i = 2$ and swap $S_2$ and $S_3$. Thus, the string becomes $10101$, whose decimal representation is $21$, which is divisible by $3$.

</details>

## Approach

Powers of two alternate between $1$ and $-1$ modulo 3, so the number is divisible by 3 exactly when the ones on even positions and the ones on odd positions are equally many modulo 3. With $E$ ones on even indices out of `ones` in total this reads $E \equiv 2 \cdot \text{ones} \pmod 3$.

A swap of two equal neighbours does nothing; a swap of `01` or `10` moves one `1` to the other parity, changing $E$ by exactly $\pm 1$. So we need to shift $E$ by $+1$ or $-1$ (the other one would also be reachable as two steps the opposite way).

- Already satisfied: 0.
- $E$ can only take values between $\max(0, \text{ones} - \lfloor n/2 \rfloor)$ and $\min(\text{ones}, \lceil n/2 \rceil)$; if no value in that range has the right residue: $-1$.
- Some unequal adjacent pair moves $E$ in the needed direction: 1.
- Otherwise every available swap moves $E$ the wrong way; two of them on disjoint positions shift it by two, which is the same residue: 2.
- If the unequal pairs are too close together to be used independently, a third swap is needed: 3.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        bits = next(tokens).decode()
        n = len(bits)
        ones = bits.count('1')
        even_ones = bits[::2].count('1')
        target = 2 * ones % 3
        if even_ones % 3 == target:
            out.append('0')
            continue
        fewest = max(0, ones - n // 2)
        most = min(ones, (n + 1) // 2)
        if fewest + (target - fewest) % 3 > most:
            out.append('-1')
            continue
        first = -1
        last = -1
        single = False
        for i in range(n - 1):
            if bits[i] == bits[i + 1]:
                continue
            effect = 1 if (bits[i] == '0') == (i % 2 == 0) else -1
            if (even_ones + effect) % 3 == target:
                single = True
                break
            if first < 0:
                first = i
            last = i
        out.append('1' if single else '2' if last - first >= 2 else '3')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- All zeros: the value is 0, already divisible.
- All ones of a length that is not balanced, such as `111`: no swap changes anything, answer $-1$.
- The range check is essential - a residue may be unreachable because there are not enough even or odd slots.
- Leading zeros are allowed, so the string is just a multiset of positions.

## Dry run

`S = 11001`: three ones, target residue $2 \cdot 3 \bmod 3 = 0$. Even indices 0, 2, 4 hold `1 0 1`, so $E = 2$.

$E$ may range from $\max(0, 3 - 2) = 1$ to $\min(3, 3) = 3$, and 3 has the right residue.

The pair at indices 1-2 is `10`; swapping it moves that one from an odd to an even index, $E = 3$. One swap: `10101` = 21.

---

Same problem grouped by topic: [../docs/basic-math/DIVBY3.md](../docs/basic-math/DIVBY3.md)
