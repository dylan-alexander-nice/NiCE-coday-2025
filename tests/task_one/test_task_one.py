import pytest
from pathlib import Path
from task_one.app import solve

RESOURCES_DIR = Path(__file__).parent.parent.parent / "src" / "task_one" / "Resources"

class TestTaskOne:
    
    def test_example(self):
        expected = 1  # Updated to match the example problem
        inputPath = str(RESOURCES_DIR / "TestExample.txt")
        assert solve(inputPath) == expected

    def test_0(self):
        expected = 5
        inputPath = str(RESOURCES_DIR / "Test0.txt")
        assert solve(inputPath) == expected
    
    def test_1(self):
        expected = 3
        inputPath = str(RESOURCES_DIR / "Test1.txt")
        assert solve(inputPath) == expected

    def test_2(self):
        expected = 244
        inputPath = str(RESOURCES_DIR / "Test2.txt")
        assert solve(inputPath) == expected

    def test_3(self):
        expected = 1
        inputPath = str(RESOURCES_DIR / "Test3.txt")
        assert solve(inputPath) == expected

if __name__ == "__main__":
    pytest.main([__file__, "-v"])