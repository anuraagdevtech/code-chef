# LEMOUSE

The neighborhood of a new path cell can overlap only the previous two path cells: older cells have Manhattan distance at least three. Track the previous move to subtract exactly those overlaps.

Complexity: O(NM) time and O(NM) space.
