"""Task One solution module."""


def solve(input_path: str) -> int | str | float:
    """
    Solve Task One (Taverns) - Find maximum distance from any city to nearest tavern.

    Problem: Given cities and taverns on a number line, find the longest distance
    any traveler must walk from their city to reach the nearest tavern.

    Approach (Brute Force):
    1. Parse input to get city and tavern positions
    2. For each city, find the minimum distance to any tavern
    3. Return the maximum of all these minimum distances

    Args:
        input_path: Path to the input file containing test data.

    Returns:
        The maximum distance from any city to its nearest tavern (integer).

    Example:
        Cities: [1, 2, 4, 6, 7, 9]
        Taverns: [0, 1, 3, 6, 7, 8, 9, 10]
        Output: 1 (city at position 2 or 4 is 1 unit from nearest tavern)
    """
    with open(input_path, "r", encoding="utf-8") as f:
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
