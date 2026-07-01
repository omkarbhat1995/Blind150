from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            # Prevents integer overflow in strict typed languages; good habit in Python too
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # Target must be in the right half
                left = mid + 1
            else:
                # Target must be in the left half
                right = mid - 1

        # Target was not found in the array
        return -1