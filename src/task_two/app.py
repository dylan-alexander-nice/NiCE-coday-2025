from collections import Counter
from typing import List, Union


def longest_harmonized_group_one_array(crystals: List[int]) -> int:
    n = len(crystals)
    if n <= 1:
        return n

    # Using a dictionary for frequencies is generally faster than Counter for this specific case
    freq = {}
    for x in crystals:
        freq[x] = freq.get(x, 0) + 1

    # Base answer: all of one type
    ans = 0
    if freq:
        ans = max(freq.values())

    types = list(freq.keys())
    c = len(types)
    if c <= 1:
        return ans

    # Value compression to integer IDs
    type_id = {v: i for i, v in enumerate(types)}
    arr_ids = [type_id[x] for x in crystals]

    # Store indices for each crystal type
    positions = [[] for _ in range(c)]
    for idx, t in enumerate(arr_ids):
        positions[t].append(idx)

    # Precompute prefix counts for all types
    prefix_counts = [[0] * c for _ in range(n + 1)]
    for i in range(n):
        for j in range(c):
            prefix_counts[i+1][j] = prefix_counts[i][j]
        prefix_counts[i+1][arr_ids[i]] += 1

    for a_id in range(c):
        pos_A = positions[a_id]
        total_A = len(pos_A)
        if total_A <= 1:
            continue

        for k in range(1, total_A // 2 + 1):
            left_idx = pos_A[k-1]
            right_idx = pos_A[total_A-k]

            if left_idx >= right_idx:
                continue

            # Calculate counts of types in the middle segment using precomputed prefixes
            # This is the core optimization
            max_middle = 0
            
            # The middle part can be of any type, including type A.
            if right_idx > left_idx + 1:
                for b_id in range(c):
                    count_b_middle = prefix_counts[right_idx][b_id] - prefix_counts[left_idx+1][b_id]
                    if count_b_middle > max_middle:
                        max_middle = count_b_middle
            
            cand = 2 * k + max_middle
            if cand > ans:
                ans = cand

    return ans


def solve(inputPath: str) -> Union[int, float, str, List[int]]:
    """
    Solve Task Two for all arrays in the input file.

    Input format:
        T
        n1
        a11 a12 ... a1n1
        n2
        a21 a22 ... a2n2
        ...

    Returns:
        List[int] of answers (one per array).
    """
    with open(inputPath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    t = int(lines[0].strip())
    line_idx = 1
    results: List[int] = []

    for _ in range(t):
        size = int(lines[line_idx].strip())
        arr = list(map(int, lines[line_idx + 1].split()))
        line_idx += 2

        results.append(longest_harmonized_group_one_array(arr))

    return results
