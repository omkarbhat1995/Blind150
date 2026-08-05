import unittest
from solution import Solution

class TestMultiplyStrings(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_multiply(self):
        # List of test cases: (num1, num2, expected_output)
        test_cases = [
            # 1. Edge Case: Both zero
            ("0", "0", "0"),
            
            # 2. Edge Case: One zero
            ("0", "123", "0"),
            
            # 3. Edge Case: Other zero
            ("123", "0", "0"),
            
            # 4. Single digits
            ("1", "1", "1"),
            
            # 5. Example 1 from problem
            ("3", "4", "12"),
            
            # 6. Example 2 from problem
            ("111", "222", "24642"),
            
            # 7. Carry-over testing
            ("9", "9", "81"),
            
            # 8. Multi-digit with carry over
            ("99", "99", "9801"),
            
            # 9. General case
            ("123", "456", "56088"),
            
            # 10. Trailing zeros
            ("1000", "1000", "1000000"),
            
            # 11. Large numbers
            ("123456789", "987654321", "121932631112635269"),
            
            # 12. Asymmetric lengths
            ("2", "3456", "6912"),
            
            # 13. Asymmetric lengths reversed
            ("9876", "5", "49380"),
            
            # 14. Edge Case: Long sequence of 9s
            ("9" * 10, "9" * 10, str((10**10 - 1)**2)),
            
            # 15. Edge Case: Max limits constraint (Length ~ 200)
            ("1" * 100, "2" * 100, str(int("1"*100) * int("2"*100)))
        ]
        
        for num1, num2, expected in test_cases:
            with self.subTest(num1=num1, num2=num2):
                self.assertEqual(self.sol.multiply(num1, num2), expected)

if __name__ == '__main__':
    unittest.main()
