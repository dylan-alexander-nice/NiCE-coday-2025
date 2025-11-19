"""Task Three solution module."""

from collections import defaultdict
from bisect import bisect_left


def solve(input_path: str) -> int | str | float:
    """
    Solve Task Three for the Coday coding competition.

    Optimal O(m log m) solution using binary search and dynamic programming.
    
    For each destination book, we maintain a sorted list of (word_count, dp_value)
    pairs. When processing a new reference, we binary search to find the best
    previous reference with fewer words.

    Args:
        input_path: Path to the input file containing test data.

    Returns:
        The computed result as an integer, string, or float depending on
        the problem requirements.

    Example:
        >>> result = solve("Resources/Test0.txt")
        >>> print(result)
    """
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Parse the input
    n, m = map(int, lines[0].split())
    
    if m == 0:
        return 0
    
    # For each book, maintain list of (word_count, max_dp_value) in sorted order
    # This allows binary search for best previous reference
    book_state = defaultdict(list)
    max_length = 1
    
    for i in range(m):
        book_from, book_to, words = map(int, lines[i + 1].split())
        
        # Find best previous reference ending at book_from with words < current
        state = book_state[book_from]
        dp_value = 1
        
        if state:
            # Binary search for largest word_count < words
            idx = bisect_left(state, (words, float('inf'))) - 1
            if idx >= 0:
                dp_value = state[idx][1] + 1
        
        max_length = max(max_length, dp_value)
        
        # Update state for book_to
        dest_state = book_state[book_to]
        
        # Maintain Pareto frontier: strictly increasing word_count AND dp_value
        # Remove entries dominated by (words, dp_value)
        while dest_state and dest_state[-1][0] >= words and dest_state[-1][1] <= dp_value:
            dest_state.pop()
        
        # Add ONLY if it strictly improves the Pareto frontier
        # Both word_count AND dp_value must be better than all previous entries
        if not dest_state or (dest_state[-1][0] < words and dest_state[-1][1] < dp_value):
            dest_state.append((words, dp_value))
    
    return max_length
