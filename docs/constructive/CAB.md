[&larr; 478. Same Parity Swaps in Binary Strings](MAX01EVSWP.md) &middot; [Index](../../README.md) &middot; [511. Chef and Hamming Distance of arrays &rarr;](CHEFHAM.md)

# 495. Cybalphabit

> CodeChef problem code [`CAB`](https://www.codechef.com/problems/CAB) &middot; difficulty **1771** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Split powers of two until the required length |
| **Time** | $O(N+\log K)$ per test case |
| **Space** | $O(N+\log K)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

In the new world, we also have a new system called Cybalphabit system.
The system assigns points to each Latin lowercase alphabet as follows:-
'a' is assigned $2^0$ , 'b' is assigned $2^1$, 'c' $2^2$ and so on. Thus, finally 'z' is assigned $2^{25}$ points.

A Cyberstring is a sequence of lowercase Latin alphabets.

Now, the total score of a Cyberstring will be the sum of points of its characters.
You will be given two integers $N$ and $K$.
Construct a Cyberstring $X$ of length $N$ with total score $K$ or print $-1$ if it is not possible to form the Cyberstring ($X$).
If there are multiple answers, print any.

**INPUT:**
- First line contains $T$, the number of test cases.
- Each of the next $T$ lines denotes a different test case :
- The ${(i+1)}^{th}$ line denotes the $i^{th}$ test case, and contains two integers $N$ and $K$, the length of the string that is to be constructed, and the score of the string respectively.

**OUTPUT:**
- For each test case, provide the output on a different line.
- Output the required string $X$, if one exists, otherwise output $-1$.

**Constraints:-**
- $1 \leq T \leq 10^5$
- $1 \leq n \leq 10^5$
- $1  \leq k  \leq 5*10^7$

The sum of $n$ over all test cases is less than $10^{5}$

## Constraints

- 1 <= T <= 10^5.
- 1 <= N <= 10^5; sum of N over cases is less than 10^5.
- 1 <= K <= 5 * 10^7.
- Use only lowercase English letters, with scores 2^0 through 2^25.

## Sample

**Sample input**

```
4
2 2
2 5
4 5
3 2
```

**Sample output**

```
aa
ac
baaa
-1
```

<details><summary>Explanation</summary>

In the first test case, $n=2$ and $k=2$. So,we have to construct a string of length $2$ with total score $2$. It can be easily seen that the only possible string is "aa". Its total score will be equal to $2^0 + 2^0 = 2$.

In the second case, "ac" will have score $2^0 + 2^2 = 5$. Obviously, "ca" will also have the same score and is also a possible answer.

In the fourth test case, it can be shown that there is no possible string which satisfies the conditions.

</details>

## Approach

Represent the score as a sum of powers of two, with no power larger than $2^{25}$. This is a representation with the fewest allowed letters. Splitting one power $2^b$ into two copies of $2^{b-1}$ preserves the score and increases the length by one. Repeated splitting reaches every length from this minimum to $K$.

Reject lengths outside that interval. Otherwise split larger powers until exactly $N$ terms remain and map exponent zero to `a`, exponent one to `b`, and so on.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, k = int(next(tokens)), int(next(tokens))
        counts = [0] * 26
        counts[25], rest = divmod(k, 1 << 25)
        for b in range(25):
            counts[b] = (rest >> b) & 1
        size = sum(counts)
        if size > n or n > k:
            out.append('-1')
            continue
        for b in range(25, 0, -1):
            split = min(counts[b], n-size)
            counts[b] -= split
            counts[b-1] += 2*split
            size += split
        out.append(''.join(chr(97+b)*counts[b] for b in range(25,-1,-1)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N+\log K)$ per test case
- **Space:** $O(N+\log K)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- The alphabet ends at exponent 25.
- Each character has positive score, so $N>K$ is impossible.
- Any ordering of the final characters is valid.

## Dry run

For `N=4, K=5`, start with `4+1`, split `4` into `2+2`, then split one `2` into `1+1`: the letters can be `baaa`.

> CodeChef tags: `Algorithms`

---

Same problem in rating order (#494 of 735): [../../by-rating/494-CAB.md](../../by-rating/494-CAB.md)
