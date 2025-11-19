import pytest
from pathlib import Path

from task_three.app import solve

RESOURCES_DIR = Path(__file__).parent.parent.parent / "src" / "task_three" / "Resources"


class TestTaskThree:
    
    def test_0(self):
        expected = 4
        inputPath = str(RESOURCES_DIR / "Test0.txt")
        assert solve(inputPath) == expected

    def test_1(self):
        expected = 3
        inputPath = str(RESOURCES_DIR / "Test1.txt")
        assert solve(inputPath) == expected
        
    def test_2(self):
        expected = 3
        inputPath = str(RESOURCES_DIR / "Test2.txt")
        assert solve(inputPath) == expected

    def test_3(self):
        expected = 2
        inputPath = str(RESOURCES_DIR / "Test3.txt")
        assert solve(inputPath) == expected

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
