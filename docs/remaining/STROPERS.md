# STROPERS

Classify a substring by its length, number of ones, and number of zeros having an odd number of ones before them. Reversing a segment with an even number of ones preserves these values. Conversely, reversals with two ones move zeros between any two gaps of the same parity; hence all distributions with these totals are equivalent. Enumerate and deduplicate these triples.

Complexity: O(N^2) time and space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
