"""Tests for Task One."""

import pytest
from pathlib import Path

from task_one.app import solve


class TestTaskOne:
    """Test suite for Task One."""

    @pytest.fixture
    def resources_dir(self) -> Path:
        """Get the resources directory for Task One."""
        return Path(__file__).parent.parent.parent / "src" / "task_one" / "Resources"

    def test_example_case(self, resources_dir: Path) -> None:
        """Test Task One with the example input."""
        input_path = resources_dir / "Test0.txt"
        result = solve(str(input_path))

        # TODO: Update expected value based on task requirements
        assert result == 0

    def test_input_file_exists(self, resources_dir: Path) -> None:
        """Verify that the test input file exists."""
        input_path = resources_dir / "Test0.txt"
        assert input_path.exists(), f"Test input file not found: {input_path}"
