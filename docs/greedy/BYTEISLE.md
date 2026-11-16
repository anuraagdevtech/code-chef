[&larr; 532. Abdullah and Toll Discounts](ABDTOLL.md) &middot; [Index](../../README.md) &middot; [654. Wishcraft &rarr;](MAJIK.md)

# 562. Byteknights and Byteknaves

> CodeChef problem code [`BYTEISLE`](https://www.codechef.com/problems/BYTEISLE) &middot; difficulty **1919** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Valid total counts followed by lexicographic candidate elimination |
| **Time** | $O(N\log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

A long school holiday has come, and you decided to visit the famous Byte Island. You know there are only two types of Bytelandians: Byteknights and Byteknaves. A Byteknight always tells the truth, whereas a Byteknave always lies.

It is known that there are *N* Bytelandians in the island, and now you meet all of them. You are curious about their types. Because you are a smart logician, you don't want to ask them questions that immediately reveal their types (that's too boring). Instead, to each Bytelandian you ask, "How many Byteknights are there here?"

To your surprise, they also don't answer your questions directly. Instead, the *i*-th Bytelandian answers of the form "The number of Byteknights here is between *a_i* and *b_i*, inclusive". You record all answers in your pocket note.

Now that you have collected all information you need, determine the type of each Bytelandian.

**Input**

The first line contains a single integer *T*, the number of test cases. *T* test cases follow. The first line of each test case contains a single integer *N*. *N* lines follow. The *i*-th line contains two integers *a_i* and *b_i*.

**Output**

For each test case, output two lines. In the first line, output a single integer indicating the number of different solutions, modulo 1000000007. In the next line, output the lexicographically smallest solution. A solution is a string consisting of *N* characters, where the *i*-th character of the string is '1' if the *i*-th Bytelandian is a Byteknight, or '0' in case of a Byteknave. It is guaranteed that there is at least one valid solution.

**Constraints**

- 1 <= *T* <= 5

- 1 <= *N* <= 50000

- 0 <= *a_i* <= *b_i* <= *N*

## Constraints

- 1 <= T <= 5
- 1 <= N <= 50000
- 0 <= a_i <= b_i <= N

## Sample

**Sample input**

```
3
1
0 1
4
1 4
2 4
3 4
4 4
3
1 2
0 0
1 3
```

**Sample output**

```
1
1
5
0000
1
101
```

## Approach

If the total number of knights is $k$, person $i$ must be a knight exactly when $a_i\le k\le b_i$. Use a difference array to count how many intervals cover every $k$ from zero through $N$. A valid assignment corresponds exactly to a total satisfying `coverage[k] == k`.

To construct the lexicographically smallest assignment, maintain all currently possible totals in sorted order. At person $i$, choose zero if any possible total lies outside their interval; delete every candidate inside it. Otherwise every candidate forces one. Whether all candidates lie inside is decided from the minimum and maximum remaining candidates. A successor DSU skips deleted candidates, so each candidate is removed at most once. Binary search locates the first candidate in a deletion interval. Count the initial valid totals before applying this greedy filter.

## Solution (Python)

```python
import sys
from bisect import bisect_left


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        intervals = [(int(next(tokens)),int(next(tokens))) for _ in range(n)]
        difference = [0]*(n+2)
        for left,right in intervals:
            difference[left] += 1
            difference[right+1] -= 1
        valid = []
        coverage = 0
        for k in range(n+1):
            coverage += difference[k]
            if coverage == k:
                valid.append(k)
        count = len(valid)
        parent = list(range(count+1))
        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i
        last = count-1
        answer = []
        for left,right in intervals:
            first = find(0)
            if left <= valid[first] and valid[last] <= right:
                answer.append('1')
            else:
                answer.append('0')
                i = find(bisect_left(valid,left))
                while i < count and valid[i] <= right:
                    parent[i] = find(i+1)
                    i = find(i)
                while parent[last] != last:
                    last -= 1
        out.append(str(count%1000000007))
        out.append(''.join(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N\log N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Zero knights is a possible total.
- Interval endpoints are inclusive.
- The smallest valid total does not necessarily give the lexicographically smallest assignment.
- A valid assignment is guaranteed to exist.

## Dry run

For intervals `[1,4],[2,4],[3,4],[4,4]`, every total from zero to four is consistent. There are five assignments; total zero yields `0000`, which is lexicographically smallest.

---

Same problem in rating order (#552 of 735): [../../by-rating/552-BYTEISLE.md](../../by-rating/552-BYTEISLE.md)
