class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast]!=0:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow += 1

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

✅ Time Complexity (TC)

O(n) — because we are scanning the array only once using the fast pointer.

✅ Space Complexity (SC)

O(1) — constant space,
because we are not using any extra array or memory,
we are modifying nums in-place.
