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

    def test_4(self):
        expected = 1
        inputPath = str(RESOURCES_DIR / "Test4.txt")
        assert solve(inputPath) == expected
    
    def test_5(self):
        expected = 4
        inputPath = str(RESOURCES_DIR / "Test5.txt")
        assert solve(inputPath) == expected

    def test_6(self):
        expected = 3
        inputPath = str(RESOURCES_DIR / "Test6.txt")
        assert solve(inputPath) == expected

    def test_7(self):
        expected = 4
        inputPath = str(RESOURCES_DIR / "Test7.txt")
        assert solve(inputPath) == expected

    def test_8(self):
        expected = 2
        inputPath = str(RESOURCES_DIR / "Test8.txt")
        assert solve(inputPath) == expected

    def test_9(self):
        expected = 4
        inputPath = str(RESOURCES_DIR / "Test9.txt")
        assert solve(inputPath) == expected

    def test_10(self):
        expected = 5
        inputPath = str(RESOURCES_DIR / "Test10.txt")
        assert solve(inputPath) == expected

    def test_11(self):
        expected = 4
        inputPath = str(RESOURCES_DIR / "Test11.txt")
        assert solve(inputPath) == expected

    def test_12(self):
        expected = 3
        inputPath = str(RESOURCES_DIR / "Test12.txt")
        assert solve(inputPath) == expected

    def test_13(self):
        expected = 4
        inputPath = str(RESOURCES_DIR / "Test13.txt")
        assert solve(inputPath) == expected

    def test_14(self):
        expected = 5
        inputPath = str(RESOURCES_DIR / "Test14.txt")
        assert solve(inputPath) == expected

    def test_15(self):
        expected = 3
        inputPath = str(RESOURCES_DIR / "Test15.txt")
        assert solve(inputPath) == expected

    def test_16(self):
        expected = 3
        inputPath = str(RESOURCES_DIR / "Test16.txt")
        assert solve(inputPath) == expected

    def test_17(self):
        expected = 2
        inputPath = str(RESOURCES_DIR / "Test17.txt")
        assert solve(inputPath) == expected

    def test_18(self):
        expected = 3
        inputPath = str(RESOURCES_DIR / "Test18.txt")
        assert solve(inputPath) == expected

    def test_19(self):
        expected = 4
        inputPath = str(RESOURCES_DIR / "Test19.txt")
        assert solve(inputPath) == expected

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
