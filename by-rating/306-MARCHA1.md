[&larr; 305. Levy Conjecture](305-LEVY.md) &middot; [Index](README.md) &middot; [307. Chef Drinks Coke &rarr;](307-COKE.md)

# 306. Paying up

> [`MARCHA1`](https://www.codechef.com/problems/MARCHA1) &middot; difficulty **1510** &middot; time limit **1s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Subset-sum reachability as an integer bitset |
| **Complexity class** | Bitset knapsack $O(ND/w)$ |
| **Time** | $O(NM/w)$ word operations per test case |
| **Space** | $O(M/w)$ machine words |

## Question

In the mysterious country of Byteland, everything is quite different from what you'd

normally expect. In most places, if you were approached by two mobsters in a dark alley, they would

probably tell you to give them all the money that you have. If you refused, or didn't have any -

they might even beat you up.

In Byteland the government decided that even the slightest chance of someone getting injured has to be ruled out. So, they introduced a strict policy. When a mobster approaches you in a dark

alley, he asks you for a specific amount of money. You are obliged to show him all the money that

you have, but you only need to pay up if he can find a subset of your banknotes whose total value

matches his demand. Since banknotes in Byteland can have any positive integer value smaller than

one thousand you are quite likely to get off without paying.

Both the citizens and the gangsters of Byteland have very positive feelings about the system. No one ever

gets hurt, the gangsters don't lose their jobs, and there are quite a few rules that minimize that
probability of getting mugged (the first one is: don't go into dark alleys - and this one is said to work in other places also).

**Input**

The first line contains integer *t*, the number of test cases (about 100). Then *t* test cases follow. Each test case starts with *n*, the

number of banknotes in your wallet, and *m*, the amount of money the muggers asked of you. Then *n*

numbers follow, representing values of your banknotes. Your wallet does not hold more than 20 banknotes, and the value of a single banknote is never more than 1000.

**Output**

For each test case output a single line with the word 'Yes' if there is a subset of your banknotes that sums  to *m*, and 'No' otherwise.

## Constraints

- $1 \le t \le 100$
- $1 \le n \le 20$
- $1 \le m \le 20,000$

## Sample

**Sample input**

```
5
3 3
1
1
1
5 11
1
2
4
8
16
5 23
1
2
4
8
16
5 13
1
5
5
10
10
20 132
17
6
4
998
254
137
259
153
154
3
28
19
123
542
857
23
687
35
99
999
```

**Sample output**

```
Yes
Yes
Yes
No
Yes
```

<details><summary>Explanation</summary>

For example, in the last case you have to pay up, since: 6+3+123=132.

</details>

## Approach

Bit $s$ of an integer records whether a subset of processed notes sums to $s$. Initially only bit zero is set. For a note of value $v$, shifting the old bitset by $v$ represents taking that note; OR with the old bitset represents either taking or skipping it.

Mask out sums above the demand, since all values are positive and such sums can never become useful. Test the target bit after processing every note. Python's arbitrary-precision bit operations process many sum states at once; $w$ denotes its fixed-size integer limb width.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,target = int(next(tokens)),int(next(tokens))
        reachable = 1
        mask = (1 << (target+1))-1
        for _ in range(n):
            value = int(next(tokens))
            if value <= target:
                reachable |= (reachable << value)&mask
        out.append('Yes' if reachable >> target&1 else 'No')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- Each note can be used at most once.
- Equal-valued notes are separate items.
- Read all notes even after the target becomes reachable.

## Dry run

For three notes `[1,1,1]`, reachable sums evolve from `{0}` to `{0,1}`, then `{0,1,2}`, then `{0,1,2,3}`. Demand three is achievable.

---

Same problem grouped by topic: [../docs/dynamic-programming/MARCHA1.md](../docs/dynamic-programming/MARCHA1.md)
