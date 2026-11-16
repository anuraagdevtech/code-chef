---
topic: Prefix Sums
subtopic: Reverse sweep over commands with two difference arrays
time: $O(N + M)$ per test case
space: $O(N + M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A type-2 command can only refer to earlier commands, so how many times a command is executed depends only on later commands. Process the commands from last to first.

Let `count[i]` be the total number of executions of command $i$: one for itself plus one for every execution of a later type-2 command whose range contains $i$. Maintain those extra executions with a difference array over command indices; because we move right to left, an update for range $[l, r]$ is "add at $r$, cancel below $l$", and the running sum at $i$ is the pending extra count.

When command $i$ is of type 2, push `count[i]` onto its command range. When it is of type 1, add `count[i]` to the array range $[l, r]$ through a second, ordinary difference array. A final prefix sum produces the array. Everything is modulo $10^9 + 7$.

## Edge cases

- The counts grow exponentially (the third sample doubles nine times), so they must be reduced modulo $10^9 + 7$.
- A type-2 range starting at command 1 has no "below $l$" slot; a spare cell absorbs the cancellation.
- Type-2 commands only reference earlier indices, so the reverse order always has the final count ready.
- The subtraction in the difference array needs a non-negative modular result.

## Dry run

Sample 1, commands: (1) add `[1,2]`, (2) add `[4,5]`, (3) run 1-2, (4) run 1-3, (5) run 3-4.

Backwards: command 5 runs once and gives +1 to commands 3 and 4. Command 4 runs $1 + 1 = 2$ times and gives +2 to commands 1-3. Command 3 runs $1 + 1 + 2 = 4$ times and gives +4 to commands 1 and 2. Commands 2 and 1 therefore run $1 + 2 + 4 = 7$ times each.

Array: `7 7 0 7 7`.
