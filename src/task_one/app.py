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
    Optimal Solution using Binary Search.
    
    Key Insight: For any city, the nearest tavern is either:
    - The largest tavern ≤ city (left neighbor)
    - The smallest tavern ≥ city (right neighbor)
    
    By sorting taverns, we can use binary search to find these candidates
    in O(log m) time instead of checking all taverns O(m).
    
    Time Complexity: O(m log m + n log m) where n = cities, m = taverns
    Space Complexity: O(n) for storing unique cities
    
    Args:
        inputPath: Path to the input file containing test data.
    Returns:
        The maximum distance from any city to its nearest tavern (integer).
    """
    import bisect
    
    with open(inputPath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Parse input
    num_cities = int(lines[0].strip())
    city_positions = list(map(int, lines[1].strip().split()))
    num_taverns = int(lines[2].strip())
    tavern_positions = list(map(int, lines[3].strip().split()))

    # Sort taverns for binary search - O(m log m)
    taverns = sorted(tavern_positions)
    
    # Remove duplicate cities - O(n)
    unique_cities = set(city_positions)
    
    # Track maximum distance
    max_distance = 0
    
    # For each city, find nearest tavern using binary search - O(n log m)
    for city in unique_cities:
        # Binary search for insertion point
        # idx is where 'city' would be inserted to keep array sorted
        idx = bisect.bisect_left(taverns, city)
        
        # Find minimum distance to nearest tavern
        min_distance = float('inf')
        
        # Check right neighbor: tavern at or after city position
        if idx < len(taverns):
            min_distance = min(min_distance, abs(taverns[idx] - city))
        
        # Check left neighbor: tavern before city position
        if idx > 0:
            min_distance = min(min_distance, abs(taverns[idx - 1] - city))
        
        # Update maximum of all minimum distances
        max_distance = max(max_distance, min_distance)
    
    return max_distance


def brute_force_solve(inputPath: str) -> int | str | float:
    """
    Approach (Brute Force):
    1. Parse input to get city and tavern positions
    2. For each city, find the minimum distance to any tavern
    3. Return the maximum of all these minimum distances

    Time Complexity: O(n * m) where n = cities, m = taverns
    Space Complexity: O(1) (ignoring input storage)

    Args:
        inputPath: Path to the input file containing test data.
    Returns:
        The maximum distance from any city to its nearest tavern (integer).

    Example:
        Cities: [1, 2, 4, 6, 7, 9]
        Taverns: [0, 1, 3, 6, 7, 8, 9, 10]
        Output: 1 (city at position 2 or 4 is 1 unit from nearest tavern)
    """
    with open(inputPath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Parse input
    num_cities = int(lines[0].strip())
    city_positions = list(map(int, lines[1].strip().split()))
    num_taverns = int(lines[2].strip())
    tavern_positions = list(map(int, lines[3].strip().split()))

    # Remove duplicates - multiple cities at same position have same nearest tavern
    unique_cities = set(city_positions)

    # Brute Force: For each city, find minimum distance to any tavern
    max_distance = 0

    for city in unique_cities:
        # Find the nearest tavern to this city
        min_distance = float("inf")

        for tavern in tavern_positions:
            distance = abs(city - tavern)
            min_distance = min(min_distance, distance)

        # Track the maximum of all minimum distances
        max_distance = max(max_distance, min_distance)

    return max_distance
