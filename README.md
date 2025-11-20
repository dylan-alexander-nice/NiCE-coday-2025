<div align="center">

# ⚡ NiCE Coday 2025 - Prometheus

**Solo Victory: Competing Against 60+ Teams**

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Competition Date](https://img.shields.io/badge/date-November%2019%2C%202025-green.svg)]()
[![Team](https://img.shields.io/badge/team-Prometheus%20(Solo)-red.svg)]()
[![Division](https://img.shields.io/badge/division-RDI-orange.svg)]()

*Solutions and test framework for NiCE's internal algorithmic competition*

</div>

---

## 📖 About Coday

**Coday** is NiCE's annual internal coding competition—a LeetCode-style algorithmic battleground where teams compete to develop the most efficient solutions to challenging computational problems. The 2025 edition featured fantasy-themed algorithmic puzzles that tested participants' mastery of data structures, algorithm optimization, and problem-solving under pressure.

**Competition Stats:**
- **Date:** November 19, 2025
- **Format:** 3 tasks, time-boxed contest
- **Participants:** 60+ teams (4-5 members each) + 1 solo competitor
- **Solo Team:** **Prometheus** (RDI Division)

This repository contains complete solutions, comprehensive test suites, and the original problem statements for all three tasks.

---

## 🎯 Challenge Overview

Each task is wrapped in a rich narrative, but the algorithmic core is pure competitive programming:

| Task | Title | Difficulty | Core Algorithm | Complexity |
|------|-------|-----------|----------------|------------|
| **1** | The Taverns of NiCE Realm | 🟢 **Easy** | Two-Pointer Sweep | O(n log n + m log m) |
| **2** | Harmonized Crystals | 🟡 **Medium** | Dynamic Sliding Window | O(n² × k) worst case |
| **3** | The Longest Story | 🔴 **Hard** | DP + Binary Search | O(m log m) |

### Task 1: Maximum Minimum Distance (Taverns) 🏛️

**Problem Type:** Nearest Neighbor Search, Two-Pointer Optimization

Given cities and taverns on a number line, find the **maximum** distance any city must travel to reach its **nearest** tavern.

**Key Insights:**
- Sort both arrays for O(n log n) preprocessing
- Use two-pointer technique to find nearest tavern for each city
- Track the worst-case distance (maximum of all minimums)

**Example:**
```
Cities:   [1, 2, 4, 7, 9]
Taverns:  [0, 3, 6, 8, 10]
Output:   1  (city at position 2 is furthest from any tavern)
```

---

### Task 2: Longest Palindromic Subsequence with Constraints (Crystals) 💎

**Problem Type:** Constrained Palindrome, Two-Pointer with Counting

Find the longest subsequence that:
1. Forms a palindrome (reads same forwards/backwards)
2. Uses **at most 2 distinct values**
3. Has symmetric outer groups (pattern: A...B...A)

**Key Insights:**
- Enumerate all pairs of distinct crystal types (A, B)
- For each pair, use two pointers on positions of type A
- Count type B crystals in the middle segment
- Result: `2 × count(A) + count(B in middle)`

**Example:**
```
Crystals: [1, 2, 1, 2, 1]
Valid:    [1, 2, 2, 1] → length 4
          [1, 1, 1]    → length 3
Output:   4
```

---

### Task 3: Longest Increasing Path in DAG (Books) 📚

**Problem Type:** Dynamic Programming on DAG, Longest Increasing Subsequence Variant

Given directed edges between books with weights (word counts), find the longest path where:
1. Word counts are **strictly increasing**
2. Edge indices are **non-decreasing** (can only move forward in input order)

**Key Insights:**
- Maintain sorted lists of (word_count, dp_value) for each destination node
- Use binary search to find best previous reference with fewer words
- O(m log m) complexity using efficient state management

**Example:**
```
6 books, 5 references:
1→2 (1 word)
2→3 (2 words)
3→4 (3 words)
2→4 (1 word)  ← blocks this path
4→5 (4 words)
Output: 4 (path: 1→2→3→4→5)
```

---

## 🏗️ Repository Structure

```
NiCE-coday-2025/
├── src/
│   ├── task_one/
│   │   ├── app.py              # Two-pointer solution
│   │   └── Resources/          # Test inputs (Test0-3.txt)
│   ├── task_two/
│   │   ├── app.py              # Sliding window + counting
│   │   └── Resources/          # Test inputs (Test0-3.txt)
│   └── task_three/
│       ├── app.py              # DP with binary search
│       └── Resources/          # Test inputs (Test0-19.txt)
├── tests/
│   ├── task_one/
│   │   └── test_task_one.py    # Comprehensive test suite
│   ├── task_two/
│   │   └── test_task_two.py    # Edge case validation
│   └── task_three/
│       └── test_task_three.py  # Large input stress tests
├── task_documents/             # Original problem PDFs + text
│   ├── TaskOne.txt
│   ├── TaskTwo.txt
│   └── TaskThree.txt
├── pyproject.toml              # Python 3.12+ configuration
├── Makefile                    # Quick commands
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.12+** (uses modern type hints and performance optimizations)
- `pip` package manager

### Installation

```powershell
# Clone the repository
git clone https://github.com/dylan-alexander-nice/NiCE-coday-2025.git
cd NiCE-coday-2025

# Install dependencies
pip install -e .
```

### Running Solutions

Each task has a `solve()` function that reads input from a file:

```python
from src.task_one.app import solve

# Run with test input
result = solve("src/task_one/Resources/Test0.txt")
print(result)
```

### Running Tests

```powershell
# Run all tests
pytest

# Run specific task tests
pytest tests/task_one/
pytest tests/task_two/
pytest tests/task_three/

# Run with coverage report
pytest --cov=src --cov-report=html
```

### Using Make Commands

```powershell
make test      # Run all tests
make coverage  # Generate coverage report
make lint      # Check code quality
make format    # Format code
```

---

## 💡 Algorithm Breakdown

### Task 1: Two-Pointer Optimization

**Naive Approach:** O(n × m)
```python
# For each city, check distance to every tavern
for city in cities:
    min_dist = min(abs(city - tavern) for tavern in taverns)
    max_dist = max(max_dist, min_dist)
```

**Optimized Approach:** O(n log n + m log m)
```python
# Sort both arrays once
cities.sort()
taverns.sort()

# Single pass with two pointers
tavern_ptr = 0
for city in cities:
    # Advance pointer to find optimal tavern segment
    while tavern_ptr < len(taverns) - 1 and taverns[tavern_ptr + 1] <= city:
        tavern_ptr += 1
    # Check both neighbors
    min_dist = min(abs(city - taverns[tavern_ptr]), 
                   abs(city - taverns[tavern_ptr + 1]) if tavern_ptr + 1 < len(taverns) else float('inf'))
```

**Why it's faster:** Eliminates redundant comparisons by exploiting sorted order.

---

### Task 2: Constrained Palindrome Search

**Challenge:** Standard palindrome DP won't work—we need subsequences, not substrings, with a two-type constraint.

**Approach:**
1. **Enumerate type pairs:** Try all combinations of two distinct crystal types (A, B)
2. **Two-pointer on outer type:** For each pair, place pointers on leftmost and rightmost positions of type A
3. **Count middle type:** Calculate how many type B crystals exist between pointers
4. **Symmetric structure:** Result is `2 × matched_A_pairs + middle_B_count`

**Edge Case Handling:**
- Single type (all same crystals): Just count occurrences
- Empty middle segment: Pure palindrome of one type
- Overlapping positions: Careful index management

**Complexity:** O(k² × n) where k = unique crystal types, n = array length

---

### Task 3: DP with Binary Search on DAG

**Problem Decomposition:**
- This is a **Longest Increasing Path** problem with two ordering constraints
- Classic DP: `dp[i] = max length path ending at reference i`
- Transition: `dp[i] = max(dp[j] + 1)` where j satisfies constraints

**Optimization Key:**
Instead of checking all previous references (O(m²)), maintain a **sorted list of (word_count, dp_value)** for each book:

```python
# For each reference (book_from → book_to, words)
best_dp = binary_search(book_state[book_from], words)
new_dp = best_dp + 1
book_state[book_to].insert_sorted((words, new_dp))
```

**Why binary search works:**
- We only care about references with **strictly fewer words**
- Among those, we want the **maximum dp value**
- Sorted structure enables O(log m) lookups

**Space Optimization:** Could prune dominated states, but not necessary for m ≤ 100,000.

---

## 📊 Performance Characteristics

| Task | Input Size | Time Complexity | Space Complexity | Bottleneck |
|------|-----------|----------------|------------------|------------|
| **1** | n, m ≤ 10⁵ | O(n log n + m log m) | O(n) | Sorting |
| **2** | n ≤ 10⁵ | O(k² × n) | O(n × k) | Type enumeration |
| **3** | m ≤ 10⁵ | O(m log m) | O(n × m) worst | Binary search |

**All solutions pass test suites with:**
- ✅ Edge cases (empty inputs, single elements)
- ✅ Large inputs (stress tests near constraints)
- ✅ Worst-case scenarios (all elements identical, fully connected graphs)

---

## 🎓 Learning Resources

### For Future Competitors

**Task 1 Practice:**
- [LeetCode 849 - Maximize Distance to Closest Person](https://leetcode.com/problems/maximize-distance-to-closest-person/)
- Two-pointer technique on sorted arrays

**Task 2 Practice:**
- [LeetCode 5 - Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [LeetCode 516 - Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)
- Constrained DP with subset constraints

**Task 3 Practice:**
- [LeetCode 329 - Longest Increasing Path in Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)
- [LeetCode 1048 - Longest String Chain](https://leetcode.com/problems/longest-string-chain/)
- DP on DAGs, topological ordering

### Key Concepts

- **Greedy + Two Pointers:** Efficient for sorted array problems
- **DP State Design:** Choosing the right state representation is 80% of the solution
- **Binary Search on Answer:** When transition involves finding optimal previous states
- **Space-Time Tradeoffs:** Sometimes O(n²) space enables O(n log n) time

---

## 🏆 Competition Tips

1. **Read carefully:** Problem constraints often hint at the intended complexity
2. **Start simple:** Brute force first, optimize second
3. **Test edge cases:** Empty inputs, single elements, duplicates
4. **Complexity analysis:** Know your Big-O before implementing
5. **Clean code matters:** Even in competition, readable code = debuggable code

---

## 📝 License & Usage

This repository is intended as a learning resource for future Coday participants. Feel free to:
- ✅ Study the solutions and test frameworks
- ✅ Use as practice material
- ✅ Reference algorithmic approaches

Please **do not** submit these solutions in actual competitions—that defeats the purpose of competitive programming! 🎯

---

## 🤝 Contributing

Found a more efficient solution? Want to add more test cases? PRs welcome!

```powershell
# Fork the repo, make changes, then:
git checkout -b feature/optimization-task-2
git commit -m "Improve Task 2 space complexity"
git push origin feature/optimization-task-2
```

---

## 📬 Contact

**Author:** Dylan Alexander (Prometheus Team)  
**Division:** Research, Development & Incubation (RDI)  
**Company:** NiCE  

*"The only way to do great work is to love what you do."* - Steve Jobs

---

<div align="center">

**⚡ Powered by Python 3.12+ | Built for Coday 2025 | Prometheus Division ⚡**

</div>
```powershell
black --check src tests
```

### Type Checking

Run MyPy for static type checking:
```powershell
mypy src
# or
make type-check
```

### All Quality Checks

Run all checks at once:
```powershell
make check-all
```

## 📝 How to Use During Competition

### For Each Task:

1. **Add the real input files** to the corresponding `Resources/` directory:
   - `src/task_one/Resources/Test0.txt`, `Test1.txt`, etc.
   - `src/task_two/Resources/Test0.txt`, `Test1.txt`, etc.
   - `src/task_three/Resources/Test0.txt`, `Test1.txt`, etc.

2. **Implement the `solve()` function** in the corresponding `app.py`:
   - `src/task_one/app.py`
   - `src/task_two/app.py`
   - `src/task_three/app.py`

3. **Update the test file** with the expected results:
   - Modify the assertion in `test_example_case()` with the correct expected value
   - Add more test cases as needed

4. **Run tests** to verify your solution:
   ```powershell
   pytest tests/task_one/ -v
   ```

### Function Signature

Each `solve()` function follows this pattern:

```python
def solve(input_path: str) -> int | str | float:
    """
    Solve the task for the Coday coding competition.
    
    Args:
        input_path: Path to the input file containing test data.
        
    Returns:
        The computed result as an integer, string, or float.
    """
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Your implementation here
    
    return result
```

### Key Points

- **No printing**: Return the result; don't print it
- **No input()**: Read from the file path provided
- **Pure functions**: Keep functions small and testable
- **Type hints**: Add type annotations to all functions
- **Docstrings**: Document your approach

## 🎯 Competition Workflow

1. Receive task description and test files
2. Copy test files to appropriate `Resources/` directory
3. Implement solution in `app.py`
4. Run tests with `pytest tests/task_X/`
5. Debug and refine until all tests pass
6. Move to next task

## 📦 Dependencies

### Runtime
- None (pure Python)

### Development
- `pytest>=8.0.0` - Testing framework
- `pytest-cov>=4.1.0` - Coverage reporting
- `ruff>=0.6.0` - Fast Python linter
- `black>=24.0.0` - Code formatter
- `mypy>=1.11.0` - Static type checker

## 🤝 Contributing

This is a competition template. Customize as needed for your specific Coday tasks.

## 📄 License

This is a personal competition boilerplate. Use as you see fit.

## 🏆 Good Luck!

Focus on solving the problems efficiently. The boilerplate handles the rest! 🚀
