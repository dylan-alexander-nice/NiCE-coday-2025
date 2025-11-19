"""Tests for Task Two."""

import pytest
from pathlib import Path

from task_two.app import solve


class TestTaskTwo:
    """Test suite for Task Two."""

    @pytest.fixture
    def resources_dir(self) -> Path:
        """Get the resources directory for Task Two."""
        return Path(__file__).parent.parent.parent / "src" / "task_two" / "Resources"

    def test_example_case(self, resources_dir: Path) -> None:
        """Test Task Two with the example input."""
        input_path = resources_dir / "Test0.txt"
        result = solve(str(input_path))

        # TODO: Update expected value based on task requirements
        assert result == 0

    def test_input_file_exists(self, resources_dir: Path) -> None:
        """Verify that the test input file exists."""
        input_path = resources_dir / "Test0.txt"
        assert input_path.exists(), f"Test input file not found: {input_path}"
