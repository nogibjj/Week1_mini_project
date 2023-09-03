"""Import appropriate modules to select src filepath"""

import unittest
from project_template.src import source_code  # Import the module you want to test


class TestSourceCode(unittest.TestCase):
    """unit test class which will test source code"""

    def test_add(self):
        """Test the add function"""
        result = source_code.add(1, 1)
        expected_result = 2
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
