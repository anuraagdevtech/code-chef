# 266. Harrenhal

> CodeChef problem code [`HHAL`](https://www.codechef.com/problems/HHAL) &middot; difficulty **1495** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Covering a two-letter string with palindromes |
| **Time** | $O(|H|)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

*Harrenhal is the largest castle in the Seven Kingdoms and is the seat of House Whent in the Riverlands, on the north shore of the Gods Eye lake. Since the War of Conquest, however, it has become a dark and ruinous place.*

(c) A Wiki of Ice and Fire

<img src="https://codechef_shared.s3.amazonaws.com/download/LTIME15/harrenhal.jpg" height="250" alt="harrenhal.jpg" />

Now Harrenhal is too dangerous since it's a nice place for bandits to hide, or even for rebels to start planning overthrowing of the king. So, the current Lord of the Seven Kingdoms has decided, that it's time to completely ruin the castle. For that puposes, he's planning to send some military troops.

In this problem we assume, that Harrenhal can be described as a string **H**, which consists only of symbols *'a'* and *'b'*. Harrenhal is completely ruined if and only if the length of **H** is equal to zero.

So, how to make **H** empty? Send a military troop! When a military troop of the king reach the castle, they delete some palindromic subsequence **S** of **H**. For example, let **H** = *'abbabaab'*. Then the current military troop can choose **S** = *'ababa'*(Let's make symbols of **S** bold in **H**: *'**ab**b**ab**a**a**b'*). After deleting **S**, **H** will be equal to *'bab'*. Military troops are free to choose any possible palindromic subsequence of **H**.

Your task is pretty simple: determine the minimal number of military troops, that the Lord of the Seven Kingdoms has to send in order to ruin Harrenhal.

**Note**

Maybe, some of you aren't familiar with definitions from the statement. Here're some articles that could help you to understand the problem correctly:

- Subsequence: [http://en.wikipedia.org/wiki/Subsequence](http://en.wikipedia.org/wiki/Subsequence)

    - Palindrome: [http://en.wikipedia.org/wiki/Palindrome](http://en.wikipedia.org/wiki/Palindrome)

**Input**

The first line of the input contains an integer **T**, denoting the number of test cases.

The next **T** lines contain a string **H** each, denoting the string, that describes the current state of Harrenhal for the corresponding test cases.

It's guaranteed, that each **H** consists only of symbols *'a'* and *'b'*.

**Output**

The output should contain exactly **T** lines. **i**'th line of the output should contain the only integer: the minimal number of military troops, that the Lord of the Seven Kingdoms has to send in order to ruin Harrenhal for the corresponding test cases.

**Constraints**

- 1 ≤ **|H|** ≤ 100000, for each **H**.

- Subtask 1(30 points): each **H** in the input is a palindrome, 1 ≤ **T** ≤ 6;

- Subtask 2(70 points): 1 ≤ **T** ≤ 9.

## Constraints

- 1 ≤ |H| ≤ 100000, for each H.
- Subtask 1(30 points): each H in the input is a palindrome, 1 ≤ T ≤ 6;
- Subtask 2(70 points): 1 ≤ T ≤ 9.

## Sample

**Sample input**

```
1
abbabaab
```

**Sample output**

```
2
```

<details><summary>Explanation</summary>

There're multiple ways to ruin Harrenhal in the example test. Let's consider one of them.

The first troop can delete **S** = *'ababa'*(*'**ab**b**ab**a**a**b'*). After that, **H** = *'bab'*.

The second troop can delete **S** = *'bab'*(*'**bab**'*). After that, **H** is empty and that's it.

</details>

## Approach

The alphabet has only two letters, and that makes the answer one of three values.

- **Empty string** → $0$ troops.
- **Already a palindrome** → $1$: delete the whole thing in one go, since a string is a subsequence of itself.
- **Anything else** → $2$.

The upper bound of $2$ is the key observation. A subsequence consisting of *all* the `a`s is a run of identical characters, which is trivially a palindrome; deleting it leaves only `b`s, which is likewise a palindrome. So two troops always suffice, no matter how tangled the string is.

And a non-palindrome clearly cannot be cleared in one, since the single deleted subsequence would have to be the entire string.

That makes the whole problem a palindrome check, `h == h[::-1]`, in $O(|H|)$ with no search at all. The elaborate framing about choosing palindromic subsequences is a distraction — the structure of the string beyond "is it a palindrome" never matters.

The sample, `abbabaab`, reverses to `baababba` and so is not a palindrome, giving $2$. One valid pair of troops is the subsequence `ababa` followed by the remaining `bab` — but the simpler all-`a`s-then-all-`b`s split works equally well.

Note the constraint $|H| \geq 1$, so the empty case never actually arises in the input; it is worth stating only because it completes the reasoning.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        h = data[1 + i]
        # All the 'a's form one palindrome and all the 'b's another, so two
        # troops always suffice; one is enough only for a palindrome.
        out.append("1" if h == h[::-1] else "2")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(|H|)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Data Structures`, `Algorithms`
