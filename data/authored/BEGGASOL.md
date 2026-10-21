---
topic: Simulation
subtopic: Collecting fuel while moving forward
time: $O(N)$ per test case
space: $O(1)$
---
You start at car $1$ with $f_1$ litres and drive clockwise, spending one litre per unit and absorbing each car's fuel as you pass it. The simulation is a single forward pass, but two details decide correctness.

**Stealing happens on arrival, even at zero fuel.** The statement is explicit: passing a car takes its fuel "even if you'd run out of gasoline exactly at that point". So the loop must spend the litre, arrive, *then* collect — not test for fuel after collecting. Sample case 2, with every car holding $1$ litre, depends on this: you arrive at each car with exactly zero and are refuelled each time.

**After the last car, the leftover is pure distance.** Once car $N$ has been passed there is nothing more to collect, so whatever fuel remains converts directly into distance. Stopping the simulation at car $N$ would under-count.

Putting those together: walk from car $1$ to car $N$, spending one litre and collecting $f_i$ at each step, halting early if the tank is empty; then add the remaining fuel to the distance.

Sample case 1, $[3,0,0,0,0]$, runs dry: three litres carry you to car $4$, which is empty, and you stop at distance $3$. Sample case 3, $[5,4,3,2,1]$, collects everything — total fuel $15$, and since the track is only length $5$ you lap it three times over empty cars, giving $15$.

That lapping is why the answer can exceed $N$ and why the track being circular barely matters: the cars are emptied on the first pass.

## Edge cases

- **Arriving with exactly zero fuel still collects that car's fuel.** The decrement happens before the pickup, so `1 1 1 1 1` works: the tank hits $0$ on arrival at every car and is immediately refilled to $1$.
- **The stop test comes before the move**, not after. With `3 0 0 0 0` the car travels three units and halts at car $4$ because there is no fuel left to reach car $5$.
- **Leftover fuel past the last car converts one-for-one into distance.** The third row arrives at car $5$ with $11$ units spare and adds every one of them, so the final `dist += fuel` is not an afterthought — it supplies most of the answer.
- **$f_i$ may be $0$, including $f_1$**, in which case the car never moves and the answer is $0$.
- **$N = 1$**: the loop body never runs and the answer is $f_1$ alone.

## Dry run

Third sample: fuel per car $5, 4, 3, 2, 1$.

| at car | fuel on arrival | distance | collects | fuel after |
|---:|---:|---:|---:|---:|
| 1 | — | 0 | 5 | 5 |
| 2 | 4 | 1 | 4 | 8 |
| 3 | 7 | 2 | 3 | 10 |
| 4 | 9 | 3 | 2 | 11 |
| 5 | 10 | 4 | 1 | 11 |

Past car $5$ the remaining $11$ units carry the car $11$ further: $4 + 11 = $ `15`.
