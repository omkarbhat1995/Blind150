class Solution:
    def isNonCyclical(self, n: int) -> bool:
        """
        Determines if a number resolves to 1 using the sum of its squared digits.
        Utilizes Floyd's Tortoise and Hare algorithm for O(1) space complexity.
        """
        def get_next(number: int) -> int:
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        # Initialize slow and fast pointers
        slow = n
        fast = get_next(n)

        # Traverse until fast reaches 1 (success) or catches up to slow (cycle detected)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1