# 344. Prajit and bits

> CodeChef problem code [`ADDI`](https://www.codechef.com/problems/ADDI) &middot; difficulty **-1** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Zero bits inside the binary width |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

Prajit was trying to solve a tricky problem .As we all know he is a noob he failed to solve that and he gave up for the day.He left the problem and went to sleep.Can you solve it?

 There is a number $N$.We need to find total unset bits of that number.
### Input:
First line contains $T$,Test cases.

Second line contains a single integer $N$ .

### Output:
Print a single integer.

### Constraints:
- $1\leq T \leq 1000$
- $1\leq N \leq 10^{18}$

## Constraints

- $1\leq T \leq 1000$
- $1\leq N \leq 10^{18}$
###Example Input:
2
10
1
###Example Output:
2
0

## Sample

**Sample input**

```
2
10
1
```

**Sample output**

```
2
0
```

## Approach

"Unset bits" means the zeros in $N$'s binary representation **as written**, i.e. within its own width — leading zeros do not count, otherwise every answer would depend on an arbitrary word size.

The width is $\mathrm{bitlen}(N) = \lfloor \log_2 N \rfloor + 1$, and the number of ones is the population count, so

$$\text{answer} = \mathrm{bitlen}(N) - \mathrm{popcount}(N)$$

Python gives both directly: `n.bit_length()` and `n.bit_count()`.

For $N = 10 = 1010_2$ the width is $4$ and two bits are set, giving $2$. For $N = 1 = 1_2$ the width is $1$ with one bit set, giving $0$ — the smallest case, and the one that shows why counting against a fixed 64-bit word would be wrong (it would report $63$).

Since $N \leq 10^{18} < 2^{60}$, the answer never exceeds $59$. In C++ this is `63 - __builtin_clzll(n) + 1 - __builtin_popcountll(n)`; Python's arbitrary-precision integers make the width query exact without any clz juggling.

The statement's input description is garbled — it says the second line holds a single $N$ — but the actual format is $T$ followed by $T$ lines, each with one $N$, as the sample shows.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        # Only zeros inside N's own width count, so measure against bit_length.
        out.append(str(n.bit_length() - n.bit_count()))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
