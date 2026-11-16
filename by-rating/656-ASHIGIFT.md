[&larr; 655. ABC-Strings](655-ABCSTR.md) &middot; [Index](README.md) &middot; [657. Longest Subarray &rarr;](657-LONGESTARRAY.md)

# 656. Saving a gift of love

> [`ASHIGIFT`](https://www.codechef.com/problems/ASHIGIFT) &middot; difficulty **2265** &middot; time limit **1.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Walk the path backwards, keeping the group size needed for the rest |
| **CodeChef tags** | `Algorithms`, `Searching`, `Dynamic Programming`, `Binary Search` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O((B + C) \log (B + C))$ per test case |
| **Space** | $O(B + C)$ |

## Question

Suraj, the Chief Prankster is back in action now and this time he has stolen the valentine's day gift given by Ashi (the love of Chef) to the Chef and ran away with it to Byteland.

Byteland is a not a regular place like Chef's town. The safest way from Chef's town to Byteland is through *the path of tasty dishes*. The path is named so because there are magical tasty dishes which appear to the traveler that no one can resist eating. Also, Suraj has added a strong sleep potion to each of the dish on this path to stop anyone from following him.

Knowing the devilish nature of Suraj, Ashi is concerned about the Chef and has asked all of Chef's town people to help. The distance from Chef's town to Byteland through the *the path of tasty dishes* is **X** units. They have the location where the magic dishes are and how many people are required to eat it completely. Anyone who eats a dish would go to a long sleep and won't be able to continue. They have the information about the tribal clans that live along the *the path of tasty dishes* who can be of real help in this journey.

The journey Chef and his friends can be described as follows: There is a total of **B** dishes on *the path of tasty dishes*. Each dish is located at some distance from Chef's town denoted by **x_i** for the i^th dish ( **x_i-1** <  **x_i**). To minimize the number of friends Chef has to leave behind, all of them have decided that exactly **y_i** of them will eat the i^th dish, which is the required number of people needed to finish it completely. Also, there are a total of **C** tribal chef clans, each with their own population and location on the path that Chef and his friends will meet on their way to Byteland. They know that for some clan (say *i*), they are located at a distance of **p_i** ( **p_i-1** <  **p_i**) from Chef's town with a population of **r_i**. And if a group of **at least q_i** men approaches them, they would be able to convince them to join their forces against Suraj.

Given the information about all this, help the Chef to find out the minimum size of the group (including him and his friends) he should start with to reach Byteland and get back Ashi's gift from Suraj.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. Each test case contains three lines which are as follows:

First line of each test case contains **X**, the distance of Byteland from Chef's town.

Next line contains an integer **B**, the number of dishes on *the path of tasty dishes*. Then follows **B** pairs of space separated integers of the form **x_i y_i**, where **x_i y_i** are as defined above for the i^th dish.
Next line contains an integer **C**, followed **C** space separated triplets of integers **p_i q_i r_i** as defined above.

**Output**

For each test case, print the minimum size of the group  (including Chef) that is needed to reach Byteland.

**Constraints**

- **1** ≤ **T** ≤ **10**

- **1** ≤ **X** ≤ **10^9**

- **1** ≤ **B** ≤ **10000**

-  Constraints on **C**

- Subproblem 1 (25 points): ** C = 0**

- Subproblem 2 (75 points): **1** ≤ **C** ≤ **10000**

- **1** ≤ **x_i** < **X**, **x_i** < **x_i+1**

- **1** ≤ **p_i** < **X**, **p_i** < **p_i+1**

- **1** ≤ **y_i** ≤ **10^14**

- **1** ≤ **q_i** ≤ **10^14**

- **1** ≤ **r_i** ≤ **10^14**

- All the positions, of the tasty dishes and tribal clans are distinct.

## Constraints

- 1 ≤ T ≤ 10
- 1 ≤ X ≤ 10^9
- 1 ≤ B ≤ 10000
-  Constraints on C
- Subproblem 1 (25 points):  C = 0
- Subproblem 2 (75 points): 1 ≤ C ≤ 10000
- 1 ≤ x_i < X, x_i < x_i+1
- 1 ≤ p_i < X, p_i < p_i+1
- 1 ≤ y_i ≤ 10^14
- 1 ≤ q_i ≤ 10^14
- 1 ≤ r_i ≤ 10^14
- All the positions, of the tasty dishes and tribal clans are distinct.

## Sample

**Sample input**

```
3
10
2 1 3 8 1
0
10
2 1 3 8 5
0
10
2 2 3 8 5
3 1 2 1 4 3 2 9 1 1
```

**Sample output**

```
5
9
6
```

<details><summary>Explanation</summary>

**Example case 1.** In the first case, there are no tribal clans, and two dishes, one which needs to be eaten by 3 chefs on their way and one to be eaten by 1 chef. Hence, we have to start with atleast 5 people in total to pass *the path of tasty dishes*.

**Example case 2.** Similar as Example Case 1.

**Example case 3.** In this case, if we start with 5 Chefs. At point 1, we have more than or equal to 2 chefs, hence the tribal clan of size 1 adds to the Chef's party and now they have size of 6. At position 2, three of them would be left behind eating a dish, leaving 3 of them to go ahead. At position 4, since the size is exactly 3, the tribal clan joins the chef's party making it of size 5. At position 8, all 5 of them will stop to eat the dish and none would go ahead. Similarly, if we start with 6, one of them would be able to pass position 8 and reach position 9, where it will also add one of the tribal clans to its party and reach Byteland.

</details>

## Approach

Let `need` be the smallest group that can complete the remaining part of the path from the current point; at the destination it is 1 (Chef himself must arrive). Sort dishes and clans by position and process them from the far end back to the start.

- A dish that must be eaten by $y$ people: those $y$ stay behind, so before the dish the group must be $y$ larger: `need += y`.
- A clan at this point with threshold $q$ and $r$ members: arriving with $g \ge q$ people gives $g + r$ afterwards. To have `need` after the clan we can either ignore the clan and arrive with `need`, or arrive with $\max(q, \text{need} - r)$ and recruit. So `need = min(need, max(q, need - r))`.

Each step is the exact inverse of "what group size before this point guarantees the required size after it", so the value at the start is the answer. Binary search on the starting size with a forward simulation would work as well; the backward pass avoids it.

## Solution

```python
import sys


def solve(tokens):
    next(tokens)
    dishes = next(tokens)
    events = [(next(tokens), 0, next(tokens), 0) for _ in range(dishes)]
    clans = next(tokens)
    events += [(next(tokens), 1, next(tokens), next(tokens)) for _ in range(clans)]
    events.sort()
    need = 1
    for _, kind, first, second in reversed(events):
        if kind == 0:
            need += first
        else:
            need = min(need, max(first, need - second))
    return str(need)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- No clans: the answer is 1 plus the sum of all dish requirements.
- A clan whose threshold exceeds the current need is never worth joining - the `min` keeps the old value.
- Recruits can make the requirement before a clan much smaller than after it, but never below the threshold.
- Positions of dishes and clans are distinct, so the sort order is unambiguous.

## Dry run

Third sample: dishes at 2 (3 people) and 8 (5 people); clans at 1 ($q=2, r=1$), 4 ($q=3, r=2$), 9 ($q=1, r=1$).

Backwards from `need = 1`:

- clan at 9: $\min(1, \max(1, 0)) = 1$
- dish at 8: $1 + 5 = 6$
- clan at 4: $\min(6, \max(3, 4)) = 4$
- dish at 2: $4 + 3 = 7$
- clan at 1: $\min(7, \max(2, 6)) = 6$

Answer 6.

---

Same problem grouped by topic: [../docs/greedy/ASHIGIFT.md](../docs/greedy/ASHIGIFT.md)
