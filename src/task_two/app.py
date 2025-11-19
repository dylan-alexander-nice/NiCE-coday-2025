"""
Task Two solution module - Master Artificer and Harmonized Crystals.

Problem: Find the longest "Harmonized Group" in crystal arrays.

A Harmonized Group must:
1. Be a palindrome (reads same forwards and backwards)
2. Use at most 2 distinct crystal types
3. Be formed by removing crystals (subsequence, not substring)
4. Have structure: [k crystals of type A] + [middle] + [k crystals of type A]

Example: [90, 100, 90, 100, 36, 100]
Answer: 3 (subsequence "90, 100, 90" is palindrome with 2 types)
"""


def longest_palindrome_subsequence(arr: list[int], type1: int, type2: int) -> int:
    """
    Find longest palindromic subsequence using only type1 and type2 crystals.
    
    Uses dynamic programming approach:
    - Filter array to only include allowed types
    - Find longest palindromic subsequence (LPS) in filtered array
    
    Args:
        arr: Array of crystal identifiers
        type1: First allowed crystal type
        type2: Second allowed crystal type
        
    Returns:
        Length of longest palindromic subsequence
    """
    # Filter to only crystals of allowed types
    filtered = [x for x in arr if x == type1 or x == type2]
    
    if len(filtered) == 0:
        return 0
    
    n = len(filtered)
    
    # DP table: dp[i][j] = length of LPS in filtered[i:j+1]
    dp = [[0] * n for _ in range(n)]
    
    # Every single crystal is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Build up for increasing substring lengths
    for length in range(2, n + 1):  # length of substring
        for i in range(n - length + 1):
            j = i + length - 1
            
            if filtered[i] == filtered[j]:
                # If ends match, add 2 to the inner subsequence
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                # If ends don't match, take max of excluding one end
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    return dp[0][n - 1]


def find_longest_harmonized_group(crystals: list[int]) -> int:
    """
    Find the longest harmonized group in a crystal array.
    
    Strategy:
    1. Try all possible pairs of crystal types (including same type)
    2. For each pair, find longest palindromic subsequence
    3. Return maximum length found
    
    Args:
        crystals: Array of crystal identifiers
        
    Returns:
        Length of longest harmonized group
    """
    if len(crystals) == 0:
        return 0
    
    # Get unique crystal types in this array
    unique_types = list(set(crystals))
    
    max_length = 0
    
    # Try using only 1 type (both type1 and type2 are the same)
    for crystal_type in unique_types:
        length = longest_palindrome_subsequence(crystals, crystal_type, crystal_type)
        max_length = max(max_length, length)
    
    # Try all pairs of different types
    for i, type1 in enumerate(unique_types):
        for type2 in unique_types[i + 1:]:
            length = longest_palindrome_subsequence(crystals, type1, type2)
            max_length = max(max_length, length)
    
    return max_length


def solve(inputPath: str) -> int | str | float:
    """
    Solve Task Two - Find longest harmonized groups for multiple crystal arrays.
    
    Simple approach:
    - For each crystal array, try all combinations of at most 2 crystal types
    - Find longest palindromic subsequence for each combination
    - Return the maximum
    
    Time Complexity: O(T * C² * N²) where:
        T = number of arrays
        C = unique crystal types per array (≤ 200)
        N = array length (≤ 200,000 but sum ≤ 200,000)
    
    Args:
        input_path: Path to the input file containing test data.
        
    Returns:
        List of integers representing longest harmonized group for each array.
    """
    with open(inputPath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Parse input
    num_arrays = int(lines[0].strip())
    
    results = []
    line_idx = 1
    
    for _ in range(num_arrays):
        # Read array size and crystals
        array_size = int(lines[line_idx].strip())
        crystals = list(map(int, lines[line_idx + 1].strip().split()))
        line_idx += 2
        
        # Find longest harmonized group for this array
        max_length = find_longest_harmonized_group(crystals)
        results.append(max_length)
    
    return results
