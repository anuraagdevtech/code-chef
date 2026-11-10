# CNCTCT

The cheapest edge between two cities is the lowest shared set bit. For each bit in increasing order, all cities carrying it form a clique of edges of that weight; joining them through any one representative has the same connectivity effect. Kruskal’s algorithm over these compressed cliques gives the minimum spanning tree.

Complexity: O(30N alpha(N)) time and O(N) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
