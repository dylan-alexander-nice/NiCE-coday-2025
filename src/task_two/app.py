from collections import Counter
from typing import List, Union


def longest_harmonized_group_one_array(crystals: List[int]) -> int:
    n = len(crystals)
    if n == 0:
        return 0

    freq = Counter(crystals)
    types = list(freq.keys())
    c = len(types)

    # Base answer: all of one type (covers A == B and k = 0)
    ans = max(freq.values())

    # Compress values to 0..c-1
    type_id = {v: i for i, v in enumerate(types)}
    arr_ids = [type_id[x] for x in crystals]

    positions = [[] for _ in range(c)]
    for idx, t in enumerate(arr_ids):
        positions[t].append(idx)

    for a_id in range(c):
        posA = positions[a_id]
        total_A = len(posA)
        if total_A <= 1:
            continue

        left_idx = posA[0]
        right_idx = posA[-1]

        if right_idx - left_idx <= 1:
            continue  # no middle segment

        # Count all types in initial middle (left_idx, right_idx)
        middle_counts = [0] * c
        for i in range(left_idx + 1, right_idx):
            middle_counts[arr_ids[i]] += 1

        l_ptr = 0
        r_ptr = total_A - 1
        max_k = total_A // 2

        for k in range(1, max_k + 1):
            max_middle = max(middle_counts) if middle_counts else 0
            cand = 2 * k + max_middle
            if cand > ans:
                ans = cand

            if k == max_k:
                break

            # shrink from the left
            old_left = posA[l_ptr]
            new_left = posA[l_ptr + 1]
            for i in range(old_left + 1, new_left + 1):
                middle_counts[arr_ids[i]] -= 1

            # shrink from the right (FIXED)
            old_right = posA[r_ptr]
            new_right = posA[r_ptr - 1]
            for i in range(new_right, old_right):
                middle_counts[arr_ids[i]] -= 1

            l_ptr += 1
            r_ptr -= 1

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
