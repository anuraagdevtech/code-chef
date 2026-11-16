[&larr; 376. Zebra Crossing](376-ZEBRA.md) &middot; [Index](README.md) &middot; [378. Stamps 100 &rarr;](378-S100.md)

# 377. Count palindromes

> [`COUNTPAL`](https://www.codechef.com/problems/COUNTPAL) &middot; difficulty **1631** &middot; time limit **0.5s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Count prefix partitions using rolling palindrome states |
| **Complexity class** | Quadratic $O(n^2)$ |
| **Time** | $O(|S|^2)$ overall |
| **Space** | $O(|S|)$ |

## Question

Each palindrome can be always created from the other palindromes, since a single character is also a palindrome. For example, the string "bobseesanna" can be created by some ways:

* bobseesanna = bob + sees + anna

* bobseesanna = bob + s + ee + s + anna

* bobseesanna = b + o + b + sees + a + n + n + a

...

We want to take the value of function CountPal(s) which is the number of different ways to use the palindromes to create the string s by the above method.

**Input**

The string s

**Output**

The value of function CountPal(s), taking the modulo of 1 000 000 007 (10^9+7)

**Limitations**

0 < |s| <= 1000

## Constraints

- 0 < |s| <= 1000.

## Sample

**Sample input**

```
bobseesanna
```

**Sample output**

```
18
```

## Approach

Let $ways[r]$ count palindromic partitions of the prefix of length $r$, with $ways[0]=1$. For every palindrome $S[l:r]$, add $ways[l]$ to $ways[r]$; its final part uniquely determines this transition.

For each new right endpoint, maintain whether every substring ending there is a palindrome. The recurrence compares its endpoints and the interior substring from the previous right endpoint. Update left endpoints in ascending order, so the old interior state at `left+1` remains available. This avoids a quadratic palindrome table.

## Solution

```python
import sys


def main() -> None:
    s = sys.stdin.buffer.read().strip()
    n = len(s)
    palindrome = bytearray(n)
    ways = [0]*(n+1)
    ways[0] = 1
    for right in range(n):
        total = 0
        for left in range(right+1):
            palindrome[left] = s[left] == s[right] and (right-left < 2 or palindrome[left+1])
            if palindrome[left]:
                total += ways[left]
        ways[right+1] = total%1000000007
    print(ways[n])

if __name__ == '__main__':
    main()
```

## Edge cases

- A single character always gives a valid final part.
- Partition boundaries, rather than distinct palindrome texts, determine different ways.
- Apply modulus $10^9+7$ to the accumulated count.

## Dry run

For `bob`, prefix partition counts are `1,1,1,2`: the final prefix can use `b|o|b` or `bob`. The full sample `bobseesanna` has 18 partitions.

---

Same problem grouped by topic: [../docs/dynamic-programming/COUNTPAL.md](../docs/dynamic-programming/COUNTPAL.md)
