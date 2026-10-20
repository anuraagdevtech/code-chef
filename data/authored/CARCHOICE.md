---
topic: Basic Math
subtopic: Comparing ratios by cross-multiplication
time: $O(1)$ per test case
space: $O(1)$
---
A car with fuel economy $x$ km/l burning fuel at $y$ rupees per litre costs $y/x$ rupees per kilometre. Since both cars cost the same to buy and the distance driven is the same either way, the cheaper car is simply the one with the lower cost per kilometre:

$$\frac{y_1}{x_1} \quad\text{versus}\quad \frac{y_2}{x_2}$$

Cross-multiplying by the positive quantity $x_1 x_2$ gives an exact integer comparison:

$$y_1 \cdot x_2 \quad\text{versus}\quad y_2 \cdot x_1$$

with Car 1 better when $y_1 x_2 < y_2 x_1$.

Note the direction of the ratio. Fuel economy sits in the **denominator** — higher km/l is better, while higher rupees/litre is worse — so the comparison is not simply "cheaper fuel wins" or "better mileage wins". Sample case 1 makes this vivid: diesel at $3$ rupees against petrol at $20$, with Car 1 also managing twice the mileage, so Car 1 wins on both counts. Sample case 3 inverts it, with Car 2 winning despite being the petrol car.

Sample case 2 is the exact tie at $1$ rupee per km each, which is why integer arithmetic matters — float division could miss the equality and print $-1$ or $1$ instead of $0$.

The output encoding is unusual and worth re-reading: $-1$ for Car 1, $0$ for a tie, $1$ for Car 2.
