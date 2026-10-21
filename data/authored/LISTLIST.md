---
topic: Greedy
subtopic: Counting how many singletons can survive
time: $O(N)$ per test case
space: $O(N)$
---
Appending keeps a list's **first** element and takes its **last** from whatever was appended, so every final list begins and ends with the common value $v$. Each merge reduces the number of lists by exactly one, so starting from $N$ lists and finishing with $f$ costs $N - f$ operations — minimising work means **maximising the number of final lists**.

Now count how $v$ is spent. A final list of length $1$ is just $[v]$ and uses one copy; a final list of length $\geq 2$ uses two, one at each end, and can hold any number of other values in its middle. So if $v$ occurs $c$ times and the other $N - c$ values are non-zero in number, they must all be buried inside lists, and one such list suffices:

$$f_{\max} = 1 + (c - 2) = c - 1$$

Adding a second non-singleton list would consume two more copies of $v$ to gain one list, a net loss — which is why one container is optimal rather than merely sufficient. So the cost is $N - c + 1$, minimised by choosing $v$ to be the **most frequent** value.

Two boundary cases fall outside that formula. If every element already equals $v$, each is already a valid list and the answer is $0$. And if the top frequency is $1$ while some other value exists, no container can be closed at both ends, so the answer is $-1$.

The samples are exactly these three cases: a single element needs nothing; $[1,2]$ has no repeated value to wrap the other, giving $-1$; and $[1,1,2]$ buries the $2$ between the two $1$s, which is $2$ merges into the single list $[1,2,1]$.
