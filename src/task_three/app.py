"""Task Three solution module."""


def solve(input_path: str) -> int | str | float:
    """
    Solve Task Three for the Coday coding competition.

    This function reads input from a file, processes it according to the task
    requirements, and returns the computed result.

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
    references = []
    
    for i in range(1, m + 1):
        book_from, book_to, words = map(int, lines[i].split())
        references.append((book_from, book_to, words))
    
    # Dynamic programming approach
    # dp[i] = maximum chain length ending at reference i
    # References are processed in catalogue order (order in input file)
    dp = [1] * m  # Each reference is at least a chain of length 1
    
    for i in range(m):
        from_i, to_i, words_i = references[i]
        
        # Try to extend chains from previous references (earlier in catalogue)
        for j in range(i):
            from_j, to_j, words_j = references[j]
            
            # Check if we can extend: 
            # The previous reference's destination book must equal current source book
            # (we continue reading from where the last reference led us)
            # AND word count must be strictly increasing
            if to_j == from_i and words_j < words_i:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum chain length
    return max(dp) if dp else 0
