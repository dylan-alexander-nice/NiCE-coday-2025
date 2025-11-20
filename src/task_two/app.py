from collections import Counter
from typing import List, Union


def longest_harmonized_group_one_array(crystals: List[int]) -> int:
    n = len(crystals)
    if n == 0:
        return 0

    # Store indices for each crystal type
    positions = {}
    for i, crystal_type in enumerate(crystals):
        if crystal_type not in positions:
            positions[crystal_type] = []
        positions[crystal_type].append(i)

    crystal_types = list(positions.keys())

    # Base answer: all of one type
    ans = 0
    for t in crystal_types:
        ans = max(ans, len(positions[t]))

    # Case where we have two different types, A and B
    for type_a in crystal_types:
        pos_a = positions[type_a]
        if len(pos_a) < 2:
            continue

        for type_b in crystal_types:
            if type_a == type_b:
                continue

            pos_b = positions.get(type_b, [])
            if not pos_b:
                continue

            # Create a prefix sum array for type_b counts
            b_counts = [0] * (n + 1)
            b_idx = 0
            for i in range(n):
                b_counts[i+1] = b_counts[i]
                if b_idx < len(pos_b) and pos_b[b_idx] == i:
                    b_counts[i+1] += 1
                    b_idx += 1

            # Use two pointers on pos_a array
            l, r = 0, len(pos_a) - 1
            while l < r:
                start_a_idx = pos_a[l]
                end_a_idx = pos_a[r]

                # Number of B's between the two A's
                middle_b_count = b_counts[end_a_idx] - b_counts[start_a_idx + 1]

                # k is the number of A's on each side
                k = l + 1

                ans = max(ans, 2 * k + middle_b_count)

                l += 1
                r -= 1

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
