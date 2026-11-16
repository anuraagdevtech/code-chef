[&larr; 584. Total Diamonds](VK18.md) &middot; [Index](../../README.md) &middot; [608. Way Out &rarr;](WOUT.md)

# 594. Gerrymander

> CodeChef problem code [`GERMANDE`](https://www.codechef.com/problems/GERMANDE) &middot; difficulty **1904** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Circular sliding window grouped by starting offset |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

The country of BitLand is divided into **N** districts, and these districts are arranged in a circle: **1, 2, 3, ..., N**, where **i** and **i+1** are adjacent for all **1 ≤ i ≤ N-1**, and also **1** and **N** are adjacent. It is given that **N = o_1 * o_2**, where **o_1** and **o_2** are odd integers.

There are only 2 political parties in BitLand: the Zeros and the Ones. There was an election, in which each district chose it's representative who is either a Zero or a One. We know this data. i.e. for each of the **N** districts, we know whether their representative is a Zero or a One.

The **N** districts should be partitioned into **o_1** states, where each state consists of **o_2** consecutive districts.

For example, if **o_1 = 5** and **o_2=3**, then **N=15**, and {1,2,3} would be a valid state. {2,3,4}, {13,14,15}, {14,15,1}, {15,1,2} are other examples of valid states. But {3,5,6} is not a valid state, because the districts are not consecutive.

A state gets a One Governor if, among all the **o_2** district representatives belonging to it, there are more One district representatives than Zero representatives. And it gets a Governor who is from the Zero party, if the majority of its district representatives are from the Zero party. And because **o_2** is odd, there will be no ties.

The President of BitLand will be a One if the majority of the **o_1** state Governors are Ones. Otherwise, the President will be from the Zero party.

But the state boundaries have not been fixed yet. Given just the district-wise data (i.e. whether each district's representative is a Zero or a One), you need to find if there is a way to partition them into states such that the President is a One.

**Input**

- The first line contains one integer, **T**, which is the number of testcases.
- The first line of each testcase contains two space separated integers, **o_1** and **o_2**, which are the number of states, and number of districts in each state, respectively.

- The next line of each testcase contains **N = o_1 * o_2** space separated integers: **d_1, d_2, .., d_N**. If **d_i** is **1**, then it signifies that District **i** has chosen a One representative. If **d_i** is **0**, then they have a Zero representative.

**Output**

- Each testcase should be in a new line, and should contain **1**, if the President can be a One, and **0** otherwise.

**Constraints**

For all subtasks you may assume that:

-
**1 ≤ T ≤ 100**

- **o_1,o_2** will be odd positive integers.

- **1 ≤** Summation of **o_1*o_2** over all testcases **≤ 10^6**

- **0 ≤ d_i ≤ 1**

**Subtask 1**: For 10% of the score,

- **1 ≤** Summation of **o_1*o_2** over all testcases **≤ 10^4**

**Subtask 2**: For further 20% of the score,

-
**1 ≤ o_1 ≤ 10^4**

-
**1 ≤ o_2 ≤ 10^2**

**Subtask 3**: For further 70% of the score,

-
No further constraints.

## Constraints

For all subtasks you may assume that:
-
1 ≤ T ≤ 100
- o_1,o_2 will be odd positive integers.
- 1 ≤ Summation of o_1*o_2 over all testcases ≤ 10^6
- 0 ≤ d_i ≤ 1

## Sample

**Sample input**

```
4
5 1
1 0 0 1 1
3 3
0 0 1 1 0 1 1 0 0
3 3
1 1 1 0 1 0 0 1 0
3 3
1 0 0 1 1 0 1 0 0
```

**Sample output**

```
1
1
1
0
```

<details><summary>Explanation</summary>

In the first testcase, each state should have only 1 district, and hence, there is no actual choice in constructing the states. There will be three One Governors, and two Zero Governors, and hence the President will be a One.

In the second testcase, each of the three states should should have 3 districts each. Consider the following partitioning of the districts into states: {2,3,4}, {5,6,7} and {8,9,1}. So, the first state consists of the districts {2,3,4}, and the representatives of these correspond to {0,1,1}. The majority is One, and hence the first state will have a One Governor. The representatives corresponding to the second state are {0,1,1}, and so again, this will have a One Governor. The third state has representatives {0,0,0}, and hence will have a Zero Governor. On the whole, there are two One Governors, and one Zero Governor, and hence the President will be a One. And since there is a way to partition the districts into states, in which the President is a One, the answer is 1.

In the third testcase, each of the three states should should have 3 districts each. Consider the following partitioning of the districts into states: {3,4,5}, {6,7,8} and {9,1,2}. So, the first state consists of the districts {3,4,5}, and the representatives of these correspond to {1,0,1}. The majority is One, and hence the first state will have a One Governor. The representatives corresponding to the second state are {0,0,1}, and since the majority is Zero, this will have a Zero Governor. The third state has representatives {0,1,1}, and as Ones are in majority, this will have a One Governor. On the whole, there are two One Governors, and one Zero Governor, and hence the President will be a One. And since there is a way to partition the districts into states, in which the President is a One, the answer is 1.

In the fourth testcase, you can check that no matter how you construct the states, the President cannot be a One. Hence, the answer is 0.

</details>

## Approach

The states are $o_1$ consecutive blocks of $o_2$ districts on a circle, so a partition is completely determined by where the first block starts, and only the start modulo $o_2$ matters - there are just $o_2$ different partitions.

Slide a window of width $o_2$ around the circle (append the first $o_2$ values to unroll it) and record for each start whether the window holds more ones than zeros. A window starting at $i$ belongs to the partition with offset $i \bmod o_2$, so add its result to that offset's counter. The president can be a One exactly when some offset collects more than $o_1 / 2$ One-governors.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        states, width = (next(tokens), next(tokens))
        n = states * width
        votes = [next(tokens) for _ in range(n)]
        votes += votes[:width]
        wins = [0] * width
        ones = sum(votes[:width])
        for i in range(n):
            wins[i % width] += ones > width // 2
            ones += votes[i + width] - votes[i]
        out.append(str(int(max(wins) > states // 2)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $o_2 = 1$: every district is its own state and there is only one partition.
- $o_1 = 1$: one state containing everything; the offset does not matter.
- Both numbers are odd, so neither vote can be tied.
- Windows that wrap past district $N$ are valid states and are covered by the unrolled array.

## Dry run

`o1 = 3, o2 = 3`, districts `0 0 1 1 0 1 1 0 0`.

Window sums by start: `1 2 2 2 2 2 1 0 0`; a window is won with at least 2 ones, so wins by start are `0 1 1 1 1 1 0 0 0`.

Offset 0 collects starts 0, 3, 6: 1 win. Offset 1 collects starts 1, 4, 7: 2 wins. Offset 2 collects starts 2, 5, 8: 2 wins. Two governors out of three is a majority, so the answer is 1.

---

Same problem in rating order (#549 of 735): [../../by-rating/549-GERMANDE.md](../../by-rating/549-GERMANDE.md)
