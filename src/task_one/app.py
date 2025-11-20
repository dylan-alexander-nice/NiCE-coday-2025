"""
Task One solution module.

Task One (Taverns) - Find the maximum of all minimum distances.

Problem: Given cities and taverns on a number line, find the longest distance
any traveler must walk from their city to reach the nearest tavern.

- Duplicates don't matter: multiple cities at the same position have the same nearest tavern.
- We're finding the worst case: Find the city that is furthest from its nearest tavern.
- Distance formula: |city_position - tavern_position|
"""

def solve(inputPath: str) -> int | str | float:
    """
    Optimal solution using a two-pointer approach.

    Key Insight: By sorting both cities and taverns, we can find the nearest
    tavern for each city in a single pass (O(n+m)). The overall complexity
    is dominated by the sorting step.

    This approach is generally faster than binary searching for each city
    because it has better data locality and avoids the overhead of repeated
    search function calls.

    Time Complexity: O(n log n + m log m) where n = cities, m = taverns
    Space Complexity: O(n) for storing unique cities

    Args:
        inputPath: Path to the input file containing test data.
    Returns:
        The maximum distance from any city to its nearest tavern (integer).
    """
    with open(inputPath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Parse input
    city_positions = list(map(int, lines[1].strip().split()))
    tavern_positions = list(map(int, lines[3].strip().split()))

    # Sort unique cities and taverns
    cities = sorted(list(set(city_positions)))
    taverns = sorted(list(set(tavern_positions)))

    max_dist = 0
    tavern_ptr = 0

    for city in cities:
        # Advance tavern pointer to find the segment containing the city
        while tavern_ptr < len(taverns) - 1 and taverns[tavern_ptr + 1] <= city:
            tavern_ptr += 1

        # Distance to the tavern at or before the city
        dist1 = abs(city - taverns[tavern_ptr])
        
        min_dist = dist1

        # If there's a next tavern, consider it as well
        if tavern_ptr + 1 < len(taverns):
            dist2 = abs(city - taverns[tavern_ptr + 1])
            min_dist = min(dist1, dist2)

        max_dist = max(max_dist, min_dist)

    return max_dist
