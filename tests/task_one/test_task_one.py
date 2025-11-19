import pytest
from task_one.app import solve


class TestTaskOne:
    
    def test_0(self):
        expected = 5
        inputPath = "Resources/Test0.txt"
        assert solve(inputPath) == expected
    
    def test_1(self):
        expected = 3
        inputPath = "Resources/Test1.txt"
        assert solve(inputPath) == expected

    def test_2(self):
        expected = 244
        inputPath = "Resources/Test2.txt"
        assert solve(inputPath) == expected

    def test_3(self):
        expected = 1
        inputPath = "Resources/Test3.txt"
        assert solve(inputPath) == expected

if __name__ == "__main__":
    pytest.main([__file__, "-v"])