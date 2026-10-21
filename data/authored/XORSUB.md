---
topic: Bit Manipulation
subtopic: XOR linear basis over GF(2)
time: $O(N \log V + \log^2 V)$ per test case
space: $O(\log V)$
---
There are $2^N$ subsets, but far fewer distinct XOR values. Viewing each $A_i$ as a vector over $\mathrm{GF}(2)$, the subset XORs are exactly the **linear span** of $\{A_1, \ldots, A_N\}$ — a subspace, closed under XOR, with $2^r$ elements where $r$ is the rank. Since $A_i \leq 1000 < 2^{10}$, the rank is at most $10$, so the span has at most $1024$ members however large $N$ gets.

Build a basis in reduced form: keep one vector per pivot bit, and insert $v$ by repeatedly cancelling against the basis vector owning $v$'s highest set bit; if the slot is empty, $v$ claims it, and if $v$ reduces to $0$ it was already dependent.

Then maximise greedily from the top bit down. Start with $\mathrm{res} = K$ and for each pivot bit $b$ from high to low, if $\mathrm{res}$ has bit $b$ clear, XOR in the basis vector for $b$. This is correct because that vector is the only one in the basis that can touch bit $b$, so turning $b$ on is worth more than anything the lower bits could lose:

$$2^b > \sum_{j < b} 2^j$$

The empty subset is allowed, so $0$ is always in the span and the answer is at least $K$.

For the sample, $[1, 2, 3]$ has rank $2$ — $3 = 1 \oplus 2$ is dependent — so the span is $\{0,1,2,3\}$. With $K = 4 = 100_2$, bit $2$ is already set and no basis vector reaches it; bits $1$ and $0$ are clear and the basis supplies $2$ and $1$, giving $4 \oplus 3 = 7$.

Note that brute-forcing $2^N$ passes only subtask 1 ($N \leq 20$); the basis handles $N \leq 1000$ in the same code. An alternative is a reachability bitset over the $1024$ possible XOR values, which is also fine at these bounds, but the basis is the technique that scales to 64-bit values.
