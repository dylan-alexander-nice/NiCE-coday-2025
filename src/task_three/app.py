"""Task Three solution module."""

from collections import defaultdict


def solve(input_path: str) -> int | str | float:
    """
    Solve Task Three for the Coday coding competition.

    This function reads input from a file, processes it according to the task
    requirements, and returns the computed result.

    Optimized approach using hash maps to avoid O(m²) worst case by grouping
    references by their source book.

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
    
    # Group references by destination book for O(1) lookup
    # dest_book -> list of (index, word_count) tuples
    by_dest = defaultdict(list)
    references = []
    
    for i in range(m):
        book_from, book_to, words = map(int, lines[i + 1].split())
        references.append((book_from, book_to, words))
        by_dest[book_to].append((i, words))
    
    # Dynamic programming: dp[i] = maximum chain length ending at reference i
    dp = [1] * m
    max_length = 1
    
    for i in range(m):
        from_i, to_i, words_i = references[i]
        
        # Only check references that end at our starting book
        for j, words_j in by_dest[from_i]:
            # Must be earlier in catalogue and have fewer words
            if j < i and words_j < words_i:
                dp[i] = max(dp[i], dp[j] + 1)
                max_length = max(max_length, dp[i])
    
    return max_length
