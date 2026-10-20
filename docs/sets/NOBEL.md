# 182. Nobel Prize

> CodeChef problem code [`NOBEL`](https://www.codechef.com/problems/NOBEL) &middot; difficulty **1372** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Sets |
| **Technique** | Counting distinct values against a capacity |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

The growth of Computer Science has forced the scientific community to award Nobel Prize in CS starting from this year.

Chef knows that the Nobel community is going to award the prize to that person whose research is different from others (ie. no other researcher should work on the same topic). If there are multiple such people, who work on unique topics, then they will all share the prize. It might also happen that no one wins this time.

Chef also knows the $N$ researchers which the community who will be considered for the prize, and the topics in which each of them work.

In total the CS field can be divided into $M$ broad topics. Given the topics in which each of the $N$ researchers are working on, in the form of an array $A$, and given that Chef can master any topic instantly, find whether he can win the prize. That is, can the Chef choose to work on some topic which will guarantee that he will win the prize? Chef doesn't mind sharing the prize with others.

**Input**

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of two lines of input.
- First line contains two space separated integers $N$, $M$, number of researchers excluding Chef and total number of fields respectively.
- Second line contains $N$ space separated integers $A_1, A_2, \ldots A_N$, research topic of the researchers.

**Output**

For each testcase, output in a single line answer, "Yes" if Chef can win the prize and "No" if not.

You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

## Constraints

- $1 \leq N, M \leq 10^5$
- $1 \leq A_i \leq M$
- Sum of $N$ over all tests is at most $10^6$
- Sum of $M$ over all tests is at most $10^6$

## Sample

**Sample input**

```
3
4 4
1 2 3 4
5 4
4 2 1 1 1
4 4
4 4 4 4
```

**Sample output**

```
No
Yes
Yes
```

<details><summary>Explanation</summary>

**TestCase 1:** Since all the $4$ available topics have been taken up, Chef can't choose a distinct topic and hence can't win the prize. No one will win the prize this year.

**TestCase 2:** Since only $3$ distinct topics out of the $4$ available have been taken up, Chef can choose the remaining one, i.e, topic $3$ to win the prize jointly with the first and the second researcher.

**TestCase 3:** Since only $1$ distinct topic out of the $4$ available has been taken up, Chef can choose any of the remaining ones to win the prize.

</details>

## Approach

Chef shares the prize if his topic is one **nobody else** works on. He can master any of the $M$ topics instantly, so he simply needs a topic that is currently unused.

An unused topic exists exactly when the researchers do not cover every field:

$$\bigl|\{A_1, \ldots, A_N\}\bigr| < M$$

so the whole solution is comparing the number of **distinct** topics against $M$.

The trap is reasoning about the researchers' own uniqueness. It is tempting to look for a topic held by exactly one person, or to count how many researchers are already unique — but none of that matters. Chef cannot displace anyone; he needs an *empty* field, so only coverage counts.

Sample case 3 makes this vivid: all four researchers crowd onto topic $4$, so three fields stand empty and Chef wins easily — even though not one researcher is unique. Sample case 1 is the opposite, with four researchers spread across all four topics leaving Chef nowhere to go, despite every researcher being unique.

Sample case 2 has $5$ researchers on only $3$ distinct topics out of $4$, so one field is free.

A Python `set` gives the distinct count in one pass. With the sum of $N$ reaching $10^6$, that linear pass with bulk input reading is what keeps this comfortable; an $O(N^2)$ uniqueness check would not survive.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        topics = set(data[pos + 2:pos + 2 + n])
        pos += 2 + n
        # Chef needs an entirely empty field, so only coverage matters.
        out.append("Yes" if len(topics) < m else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
