from collections import Counter

import numpy as np


def longest_harmonized_group_one_array(crystals: list[int]) -> int:
    n = len(crystals)
    if n == 0:
        return 0

    freq = Counter(crystals)
    types = list(freq.keys())
    c = len(types)

    # Base answer: all of one type
    ans = max(freq.values())

    # Compress values to 0..c-1 for array indexing
    type_id = {v: i for i, v in enumerate(types)}
    arr_ids = [type_id[x] for x in crystals]

    # Build positions for each type
    positions = [[] for _ in range(c)]
    for idx, t in enumerate(arr_ids):
        positions[t].append(idx)

    # For each crystal type that appears at least twice
    for a_id in range(c):
        pos_a = positions[a_id]
        total_a = len(pos_a)
        if total_a < 2:
            continue

        max_k = total_a // 2

        # Start with k=1 (widest span)
        left_idx = 0
        right_idx = total_a - 1
        left_pos = pos_a[left_idx]
        right_pos = pos_a[right_idx]

        # Build initial middle counter using numpy array (faster than list)
        middle_counts = np.zeros(c, dtype=np.int32)
        for i in range(left_pos + 1, right_pos):
            middle_counts[arr_ids[i]] += 1

        # Process all k values
        for k in range(1, max_k + 1):
            # Use numpy's optimized max
            max_middle = int(np.max(middle_counts))
            cand = 2 * k + max_middle
            ans = max(ans, cand)

            if k == max_k:
                break

            # Remove crystals from left boundary
            old_left_pos = pos_a[left_idx]
            left_idx += 1
            new_left_pos = pos_a[left_idx]

            for i in range(old_left_pos + 1, new_left_pos + 1):
                middle_counts[arr_ids[i]] -= 1

            # Remove crystals from right boundary
            old_right_pos = pos_a[right_idx]
            right_idx -= 1
            new_right_pos = pos_a[right_idx]

            for i in range(new_right_pos, old_right_pos):
                middle_counts[arr_ids[i]] -= 1

    return ans


def solve(input_path: str) -> int | float | str | list[int]:
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
    with open(input_path, encoding="utf-8") as f:
        lines = f.readlines()

    t = int(lines[0].strip())
    line_idx = 1
    results: list[int] = []

    for _ in range(t):
        _ = int(lines[line_idx].strip())  # size unused but in format
        arr = list(map(int, lines[line_idx + 1].split()))
        line_idx += 2

        results.append(longest_harmonized_group_one_array(arr))

    return results
