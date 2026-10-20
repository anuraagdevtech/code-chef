# 6. Mahasena

> CodeChef problem code [`AMR15A`](https://www.codechef.com/problems/AMR15A) &middot; difficulty **720** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Parity counting in a single pass |
| **Time** | $O(N)$ |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Kattapa, as you all know was one of the greatest warriors of his time. The kingdom of Maahishmati had never lost a battle under him (as army-chief), and the reason for that was their really powerful army, also called as **Mahasena**.

Kattapa was known to be a very superstitious person. He believed that a soldier is "lucky" if the soldier is holding an **even number** of weapons, and "unlucky" otherwise. He considered the army as "READY FOR BATTLE" if the count of "lucky" soldiers is strictly greater than the count of "unlucky" soldiers, and "NOT READY" otherwise.

Given the number of weapons each soldier is holding, your task is to determine whether the army formed by all these soldiers is "READY FOR BATTLE" or "NOT READY".

**Note**: You can find the definition of an even number [here](https://simple.wikipedia.org/wiki/Even_number).

**Input**

The first line of input consists of a single integer **N** denoting the number of soldiers. The second line of input consists of **N** space separated integers **A_1**, **A_2**, ..., **A_N**, where **A_i** denotes the number of weapons that the **i**^th soldier is holding.

**Output**

Generate one line output saying "READY FOR BATTLE", if the army satisfies the conditions that Kattapa requires or "NOT READY" otherwise (quotes for clarity).

## Constraints

- **1** ≤ **N** ≤ **100**

- **1** ≤ **A_i** ≤ **100**

## Sample

**Sample 1 input**

```
1
1
```

**Sample 1 output**

```
NOT READY
```

<details><summary>Explanation</summary>

- **Example 1**: For the first example, **N = 1** and the array **A = [1]**. There is only 1 soldier and he is holding 1 weapon, which is odd. The number of soldiers holding an even number of weapons = 0, and number of soldiers holding an odd number of weapons = 1. Hence, the answer is "NOT READY" since the number of soldiers holding an even number of weapons is not greater than the number of soldiers holding an odd number of weapons.

</details>

**Sample 2 input**

```
1
2
```

**Sample 2 output**

```
READY FOR BATTLE
```

<details><summary>Explanation</summary>

**Example 2**: For the second example, **N = 1** and the array **A = [2]**. There is only 1 soldier and he is holding 2 weapons, which is even. The number of soldiers holding an even number of weapons = 1, and number of soldiers holding an odd number of weapons = 0. Hence, the answer is "READY FOR BATTLE" since the number of soldiers holding an even number of weapons is greater than the number of soldiers holding an odd number of weapons.

</details>

**Sample 3 input**

```
4
11 12 13 14
```

**Sample 3 output**

```
NOT READY
```

<details><summary>Explanation</summary>

**Example 3**: For the third example, **N = 4** and the array **A = [11, 12, 13, 14]**. The 1^st soldier is holding 11 weapons (which is odd), the 2^nd soldier is holding 12 weapons (which is even), the 3^rd soldier is holding 13 weapons (which is odd), and the 4^th soldier is holding 14 weapons (which is even). The number of soldiers holding an even number of weapons = 2, and number of soldiers holding an odd number of weapons = 2. Notice that we have an **equal** number of people holding even number of weapons and odd number of weapons. The answer here is "NOT READY" since the number of soldiers holding an even number of weapons is **not strictly greater than** the number of soldiers holding an odd number of weapons.

</details>

**Sample 4 input**

```
3
2 3 4
```

**Sample 4 output**

```
READY FOR BATTLE
```

<details><summary>Explanation</summary>

**Example 4**: For the fourth example, **N = 3** and the array **A = [2, 3, 4]**. The 1^st soldier is holding 2 weapons (which is even), the 2^nd soldier is holding 3 weapons (which is odd), and the 3^rd soldier is holding 4 weapons (which is even). The number of soldiers holding an even number of weapons = 2, and number of soldiers holding an odd number of weapons = 1. Hence, the answer is "READY FOR BATTLE" since the number of soldiers holding an even number of weapons is greater than the number of soldiers holding an odd number of weapons.

</details>

**Sample 5 input**

```
5
1 2 3 4 5
```

**Sample 5 output**

```
NOT READY
```

<details><summary>Explanation</summary>

**Example 5**: For the fifth example, **N = 5** and the array **A = [1, 2, 3, 4, 5]**. The 1^st soldier is holding 1 weapon (which is odd), the 2^nd soldier is holding 2 weapons (which is even), the 3^rd soldier is holding 3 weapons (which is odd), the 4^th soldier is holding 4 weapons (which is even), and the 5^th soldier is holding 5 weapons (which is odd). The number of soldiers holding an even number of weapons = 2, and number of soldiers holding an odd number of weapons = 3. Hence, the answer is "NOT READY" since the number of soldiers holding an even number of weapons is not greater than the number of soldiers holding an odd number of weapons.

</details>

## Approach

A soldier is "lucky" when the number of weapons they hold is even, and the army is ready when the lucky soldiers *strictly* outnumber the unlucky ones. So the task reduces to counting how many of the $N$ values are even.

Two observations keep this to one pass and constant memory. First, parity is decided by `a % 2` alone — the magnitude of $A_i$ is irrelevant, so nothing needs to be stored. Second, every soldier is either lucky or unlucky, so if $E$ is the number of even values then the odd count is simply $N - E$. There is no need to maintain two counters.

The comparison $E > N - E$ rearranges to

$$2E > N$$

which is the cleanest form: a strict majority of the soldiers must be even. Note that for odd $N$ a tie is impossible, but for even $N$ the split $E = N/2$ is exactly a tie and must answer `NOT READY` — which `2E > N` handles correctly.

Unlike most problems in this set there is no $T$ wrapper: the input is a single test case, one $N$ followed by one array.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    # "Lucky" means an even weapon count; a strict majority wins.
    evens = sum(1 for v in data[1:1 + n] if int(v) % 2 == 0)
    print("READY FOR BATTLE" if 2 * evens > n else "NOT READY")


main()
```

## Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

> CodeChef tags: `Basic Programming Concepts`, `Mathematics`
