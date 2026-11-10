# CSUBQ

A segment tree counts subarrays with every value <=R and subtracts those with every value <L. Each monoid records segment length, good prefix/suffix lengths and all-good subarray count; merge adds cross-boundary suffix×prefix pairs.

Complexity: O((N+Q) log N) time and O(N) space using packed integer arrays.
