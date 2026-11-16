[&larr; 576. Permutation Split](PERMSPL.md) &middot; [Index](../../README.md) &middot; [578. Chef and Pepperoni Pizza Again &rarr;](PEPPERA.md)

# 577. Coin Partition

> CodeChef problem code [`COINPART`](https://www.codechef.com/problems/COINPART) &middot; difficulty **2804** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Balanced partition by subset-sum bitset, then a simulated hand-out order |
| **Time** | $O(N \cdot S / w)$ per test case, $S$ the sum of the values |
| **Space** | $O(N \cdot S / w)$ machine words - one bitset per prefix for reconstruction |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Chef is a cook. He has a son Chefu and a daughter Chefa. He also has $N$ coins, numbered $1$ through $N$; for each valid $i$, the $i$-th coin has value $V_i$.

Chef wants to give all coins to his two children in the following way: He traverses all coins in a particular order; for each coin, he checks which child currently has less money in total and gives this coin to that child (if both have the same amount of money, Chefu is given the coin).

Chefu is studying computer science, so he knows that this method is not necessarily the most fair way of partitioning the coins, but Chef does not understand why, since he is only a cook.

Now, Chefu wants to take advantage of that and choose the order in which Chef should give out the coins in such a way that the amount of money he gets is maximised. Can you help him?

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $V_1, V_2, \dots, V_N$.

**Output**
For each test case, print a single line containing $N$ space-separated integers — a permutation of numbers $1$ through $N$ denoting the indices of the coins in the order in which Chef should traverse them. If there is more than one optimal solution, you may print any one.

**Constraints**
- $1 \le T \le 100$
- $1 \le N \le 500$
- $1 \le V_i \le 500$ for each valid $i$
- the sum of $N$ for all test cases does not exceed $500$

**Subtasks**
**Subtask #1 (50 points):** the sum of $N$ for all test cases does not exceed $80$

**Subtask #2 (50 points):** original constraints

**Example Input**
```
2
4
5 3 20 9
4
2 2 2 2
```

**Example Output**
```
2 4 1 3
1 2 3 4
```

## Constraints

- $1 \le T \le 100$
- $1 \le N \le 500$
- $1 \le V_i \le 500$ for each valid $i$
- the sum of $N$ for all test cases does not exceed $500$

## Approach

Whatever the order, just before the last coin he receives Chefu holds at most as much as Chefa. The best he can do is therefore to be as close to level as possible on all coins but one and then receive the largest coin last.

Set the largest coin aside and split the other coins into two parts whose sums are as close as possible: a subset-sum bitset over them gives the largest reachable sum not exceeding half of their total, and keeping the bitset after every coin lets us walk backwards and recover which coins form that part. Chefu is given the smaller part, Chefa the other.

To turn the split into an order, simulate Chef's rule: whenever Chefu is not ahead, hand out the next coin from his pile, otherwise the next one from Chefa's pile. The reserved coin sits at the bottom of Chefu's pile, so he takes it at the moment his own part is exhausted and he is still not ahead. He ends with (total + largest - minimum difference) / 2. Any order achieving the maximum is accepted.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        values = [next(tokens) for _ in range(n)]
        big = max(range(n), key=values.__getitem__)
        others = [i for i in range(n) if i != big]
        history = [1]
        for i in others:
            history.append(history[-1] | history[-1] << values[i])
        target = sum((values[i] for i in others)) // 2
        while not history[-1] >> target & 1:
            target -= 1
        low = []
        high = []
        for j in range(len(others) - 1, -1, -1):
            i = others[j]
            if history[j] >> target & 1:
                high.append(i)
            else:
                low.append(i)
                target -= values[i]
        low.insert(0, big)
        chefu = chefa = 0
        order = []
        while low or high:
            if chefu <= chefa:
                i = low.pop()
                chefu += values[i]
            else:
                i = high.pop()
                chefa += values[i]
            order.append(str(i + 1))
        out.append(' '.join(order))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N \cdot S / w)$ per test case, $S$ the sum of the values
- **Space:** $O(N \cdot S / w)$ machine words - one bitset per prefix for reconstruction
- Auxiliary space excludes the buffered input and output.

## Edge cases

- A single coin: the order is just `1` and Chefu takes it because of the tie rule.
- Several coins share the maximum value: reserving any one of them is equally good.
- Ties go to Chefu, so the simulation uses `chefu <= chefa`.
- The output is a permutation of indices, not the values.

## Dry run

Coins `[3, 1, 2]`. Reserve the 3. The other coins `{1, 2}` total 3, so the target is 1: Chefu's part is `{1}`, Chefa's is `{2}`.

Simulation: level at 0, so Chefu takes value 1 (coin 2). He is ahead, so Chefa takes value 2 (coin 3). Now 1 against 2, so Chefu takes the reserved 3 (coin 1).

Order `2 3 1`; Chefu ends with 4 out of 6.

---

Same problem in rating order (#710 of 735): [../../by-rating/710-COINPART.md](../../by-rating/710-COINPART.md)
