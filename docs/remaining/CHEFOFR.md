# CHEFOFR

Discard zero contributions (they can be absorbed by neighboring clusters). Greedily test AND bits from high to low, using partition DP over at most 50 positive slices; bitsets encode possible cluster counts.

Complexity: O(Q log(sum sweetness) P²) time and O(P) big integers, P<=50.
