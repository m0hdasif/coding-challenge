import unittest
from unittest.mock import patch
from io import StringIO
from basic.patterns.odd_triangle import triangle

class TestTrianglePattern(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_triangle(self, mock_stdout):
        triangle(5)

        # Get the printed output
        output = mock_stdout.getvalue()

        expected = (
            "    *\n"
            "   ***\n"
            "  *****\n"
            " *******\n"
            "*********\n"
        )

        # Assert the output is as expected
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
