import pytest
from task_three.app import solve


class TestTaskThree:
    
    def test_0(self):
        expected = 4
        inputPath = "Resources/Test0.txt"
        assert solve(inputPath) == expected

    def test_1(self):
        expected = 3
        inputPath = "Resources/Test1.txt"
        assert solve(inputPath) == expected
        
    def test_2(self):
        expected = 3
        inputPath = "Resources/Test2.txt"
        assert solve(inputPath) == expected

    def test_3(self):
        expected = 2
        inputPath = "Resources/Test3.txt"
        assert solve(inputPath) == expected

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
