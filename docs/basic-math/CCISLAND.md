[&larr; 119. Drunk Alcoholic](DRUNKALK.md) &middot; [Index](../../README.md) &middot; [124. Secret Recipe &rarr;](CHEFRUN.md)

# 120. Chef On Island

> CodeChef problem code [`CCISLAND`](https://www.codechef.com/problems/CCISLAND) &middot; difficulty **878** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Two independent supply checks |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Suppose Chef is stuck on an island and currently he has $x$ units of food supply and $y$ units of water supply in total that he could collect from the island. He needs $x_r$ units of food supply and $y_r$ units of water supply per day at the minimal to have sufficient energy to build a boat from the woods and also to live for another day. Assuming it takes exactly $D$ days to build the boat and reach the shore, tell whether Chef has the sufficient amount of supplies to be able to reach the shore by building the boat?

**Input:**
- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, five integers $x, y, x_r, y_r, D$.

**Output:**
For each testcase, output in a single line answer "YES" if Chef can reach the shore by building the boat and "NO" if not (without quotes).

You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

**Constraints**
- $1 \leq T \leq 300$
- $1 \leq x, y \leq 100$
- $1 \leq x_r, y_r, D \leq 10$

## Constraints

- $1 \leq T \leq 300$
- $1 \leq x, y \leq 100$
- $1 \leq x_r, y_r, D \leq 10$

## Sample

**Sample input**

```
3
4 2 1 1 1
4 2 1 3 1
4 2 4 2 2
```

**Sample output**

```
YES
NO
NO
```

<details><summary>Explanation</summary>

**TestCase 1:** Chef's food supply will last for $\frac{4}{1} = 4$ days and water supply will last for $\frac{2}{1} = 2$ days, so in total he will be able to survive for $min(4, 2) = 2$ days and since required time to reach the shore is $1$ day, he will be able to reach there.

**TestCase 2:** Chef's food supply will last for $\frac{4}{1} = 4$ days and water supply will last for $\frac{2}{3} = 0.67$ days, so in total he will be able to survive for $min(4, 0.67) = 0.67$ days and since required time to reach the shore is $1$ day, he won't be able to reach there.

**TestCase 3:** Chef's food supply will last for $\frac{4}{4} = 1$ day and water supply will also last for $\frac{2}{2} = 1$ day, so in total he will be able to survive for $min(1, 1) = 1$ day and since required time to reach the shore is $2$ days, he won't be able to reach there.

</details>

## Approach

Chef needs $x_r$ food and $y_r$ water **per day** for $D$ days, so the totals required are $x_r \cdot D$ and $y_r \cdot D$. He survives only if **both** stocks cover their demand:

$$x \geq x_r \cdot D \quad\text{and}\quad y \geq y_r \cdot D$$

The two resources are independent and non-substitutable — surplus food does not offset a water shortfall — so this is an `and`, and each must be checked on its own. That is the same asymmetry as the shoes problem, and the reason a combined test such as $x + y \geq (x_r + y_r)D$ is wrong: it would let an abundance of one supply mask the absence of the other.

Sample case 2 is built exactly on that. Food is fine ($4 \geq 1$) but water fails ($2 < 3$), so the answer is `NO` even though the totals $6$ against $4$ would pass a pooled check.

Sample case 3 fails on food instead, with $4 < 4 \times 2 = 8$, and also shows that $D$ multiplies the daily rate rather than being compared against the stock directly.

The comparisons are inclusive — finishing with exactly zero supplies left still counts as reaching the shore, as sample case 1 nearly illustrates. All values are small, so there is nothing to watch numerically.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, xr, yr, d = map(int, data[1 + 5 * i:6 + 5 * i])
        # Food and water are not interchangeable, so both must hold.
        out.append("YES" if x >= xr * d and y >= yr * d else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Exactly enough of a resource** ($x = x_r \cdot D$): still survivable, so the comparisons are non-strict.
- **One resource short while the other is plentiful** (the second row has ample water but too little food): `NO`. Food and water are **not interchangeable**, so both conditions must hold — an `or`, or a check on the combined total, passes this row wrongly.
- **$D = 1$**: a single day's requirement.
- **Both short** (the third row): `NO`, failing on the first test alone.
- The two checks are independent, which is why they are ANDed rather than summed.

## Dry run

| $x$ | $y$ | $x_r$ | $y_r$ | $D$ | need $x_r D$ | need $y_r D$ | both met? | output |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 4 | 2 | 1 | 1 | 1 | 1 | 1 | yes | `YES` |
| 4 | 2 | 1 | 3 | 1 | 1 | 3 | no (second) | `NO` |
| 4 | 2 | 4 | 2 | 2 | 8 | 4 | no (both) | `NO` |

> CodeChef tags: `Basic Programming Concepts`, `Mathematics`

---

Same problem in rating order (#120 of 486): [../../by-rating/120-CCISLAND.md](../../by-rating/120-CCISLAND.md)
