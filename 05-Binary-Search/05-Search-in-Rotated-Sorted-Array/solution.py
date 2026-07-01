from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
                
            # Check if the Left portion is strictly sorted
            if nums[left] <= nums[mid]:
                # Is the target within this strictly sorted left portion?
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # Otherwise, the Right portion must be strictly sorted
            else:
                # Is the target within this strictly sorted right portion?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1