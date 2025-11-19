"""
Task Two solution module - Master Artificer and Harmonized Crystals.

Problem: Find the longest "Harmonized Group" in crystal arrays.

A Harmonized Group has EXACTLY this structure:
- Part 1: k crystals of type A (homogeneous)
- Part 2: m crystals of type B (homogeneous, can be 0 crystals)
- Part 3: k crystals of type A (homogeneous, same count and type as Part 1)

Constraints:
- At most 2 distinct types total (A and B, where A can equal B)
- Must be a subsequence (can remove crystals, not rearrange)
- Pattern: A^k B^m A^k where k >= 1, m >= 0

Example: [90, 100, 90, 100, 36, 100]
Answer: 3 (subsequence "90, 100, 90" = A B A where A=90, B=100, k=1, m=1)
"""


def find_harmonized_group_length(arr: list[int], typeA: int, typeB: int) -> int:
    """
    Find longest harmonized group with pattern A^k B^m A^k.
    
    Strategy:
    - Count occurrences of typeA and typeB in array
    - Try all possible values of k (parts 1 & 3) and m (part 2)
    - For each (k, m), check if we can form the pattern as a subsequence
    
    Args:
        arr: Array of crystal identifiers
        typeA: Type for parts 1 and 3
        typeB: Type for part 2 (middle)
        
    Returns:
        Length of longest harmonized group (2k + m)
    """
    n = len(arr)
    
    # Precompute: For each position, count how many of typeA/typeB we've seen
    count_A = [0] * (n + 1)  # count_A[i] = number of typeA in arr[0:i]
    count_B = [0] * (n + 1)
    
    for i in range(n):
        count_A[i + 1] = count_A[i] + (1 if arr[i] == typeA else 0)
        count_B[i + 1] = count_B[i] + (1 if arr[i] == typeB else 0)
    
    total_A = count_A[n]
    total_B = count_B[n]
    
    max_length = 0
    
    # Try all possible k values (for parts 1 and 3)
    max_k = total_A // 2  # Need at least 2k instances of typeA
    
    for k in range(1, max_k + 1):
        # For this k, find the best position to split into part1, part2, part3
        # We need: k of typeA, then some of typeB, then k of typeA
        
        # Try different split points
        # Part 1 ends at position end1 (has k instances of typeA)
        # Part 2 ends at position end2 (has m instances of typeB)
        # Part 3 ends at position n (has k instances of typeA)
        
        # Find earliest position where we have k instances of typeA
        end1 = -1
        for i in range(n + 1):
            if count_A[i] >= k:
                end1 = i
                break
        
        if end1 == -1:
            continue
        
        # From end1 onwards, we need k more instances of typeA for part 3
        remaining_A_needed = k
        remaining_A_available = total_A - k
        
        if remaining_A_available < remaining_A_needed:
            continue
        
        # Try different amounts of typeB in the middle (m)
        for end2 in range(end1, n + 1):
            # Count typeB between end1 and end2 (part 2)
            m = count_B[end2] - count_B[end1]
            
            # Count typeA between end2 and n (potential part 3)
            typeA_in_part3 = count_A[n] - count_A[end2]
            
            # Check if we have enough typeA for part 3
            if typeA_in_part3 >= k:
                # Valid pattern: k typeA + m typeB + k typeA
                length = 2 * k + m
                max_length = max(max_length, length)
    
    return max_length


def find_longest_harmonized_group(crystals: list[int]) -> int:
    """
    Find the longest harmonized group in a crystal array.
    
    Strategy:
    1. Try all possible pairs of crystal types (typeA for outer, typeB for middle)
    2. For each pair, find longest pattern A^k B^m A^k
    3. Also try single type: A^k A^m A^k = A^(2k+m)
    4. Return maximum length found
    
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
    
    # Try using only 1 type (A=B, so pattern is just A^k A^m A^k = A^n)
    for crystal_type in unique_types:
        length = find_harmonized_group_length(crystals, crystal_type, crystal_type)
        max_length = max(max_length, length)
    
    # Try all pairs: typeA for outer parts, typeB for middle
    for typeA in unique_types:
        for typeB in unique_types:
            if typeA != typeB:
                length = find_harmonized_group_length(crystals, typeA, typeB)
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
