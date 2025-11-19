# NiCE Coday 2025 - Coding Competition Boilerplate

A modern Python 3.12+ boilerplate for solving LeetCode-style coding competition tasks. This project is structured to handle three independent tasks in a time-boxed contest format.

## 📁 Project Structure

```
.
├── src/
│   ├── task_one/
│   │   ├── __init__.py
│   │   ├── app.py              # solve() function for Task One
│   │   └── Resources/
│   │       └── Test0.txt       # Sample input file
│   ├── task_two/
│   │   ├── __init__.py
│   │   ├── app.py              # solve() function for Task Two
│   │   └── Resources/
│   │       └── Test0.txt       # Sample input file
│   └── task_three/
│       ├── __init__.py
│       ├── app.py              # solve() function for Task Three
│       └── Resources/
│           └── Test0.txt       # Sample input file
├── tests/
│   ├── task_one/
│   │   └── test_task_one.py
│   ├── task_two/
│   │   └── test_task_two.py
│   └── task_three/
│       └── test_task_three.py
├── pyproject.toml              # Project configuration
├── Makefile                    # Build and test shortcuts
└── README.md                   # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```powershell
git clone <repository-url>
cd NiCE-coday-2025
```

2. Install the project in editable mode with dev dependencies:
```powershell
pip install -e .[dev]
```

Or using a virtual environment (recommended):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # On Windows PowerShell
# or
# source .venv/bin/activate    # On Unix/macOS
pip install -e .[dev]
```

## 🧪 Running Tests

Run all tests:
```powershell
pytest
# or
make test
```

Run tests for a specific task:
```powershell
pytest tests/task_one/
pytest tests/task_two/
pytest tests/task_three/
```

Run tests with coverage:
```powershell
pytest --cov=src --cov-report=html
```

## 🛠️ Development Tools

### Linting

Run Ruff to check for code issues:
```powershell
ruff check src tests
# or
make lint
```

Auto-fix issues:
```powershell
ruff check --fix src tests
```

### Formatting

Format code with Black:
```powershell
black src tests
# or
make format
```

Check formatting without changes:
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
