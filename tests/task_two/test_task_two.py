"""Tests for Task Two."""
import pytest
from task_two.app import solve


class TestTaskTwo:
    
    def test_0(self):
        expected = [6, 5]
        inputPath = "Resources/Test0.txt"
        assert solve(inputPath) == expected

    def test_1(self):
        expected = [3, 3, 4, 3]
        inputPath = "Resources/Test1.txt"
        assert solve(inputPath) == expected

    def test_2(self):
        expected = [ 4, 5, 5, 3, 4 ]
        inputPath = "Resources/Test2.txt"
        assert solve(inputPath) == expected

    def test_3(self):
        expected = [3, 3, 4, 2, 2, 3, 4, 3]
        inputPath = "Resources/Test3.txt"
        assert solve(inputPath) == expected

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
