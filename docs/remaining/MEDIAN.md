# MEDIAN

Replace maximum-valued entries by one and all others by zero. Memoize masks reachable by useful median operations. For each left endpoint keep only the farthest right endpoint having at least half ones; discard successor masks dominated by a superset.

Complexity: O(2^N N²) worst-case time and O(2^N) space; maximal-interval and dominance pruning reduce the reached states for N<=30.

Reference: [CodeChef editorial](https://discuss.codechef.com/t/830). Implementation and validation are original Python code.
