class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf')
        second = float('inf')

        for i in nums:
            if i <= first:
                first = i
            elif i<=second:
                second = i
            else:
                return True
        return False
#Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: One of the valid triplet is (3, 4, 5), because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.#

✅ Time Complexity — O(n)

We loop through the array only once.

Just comparisons and variable updates → very efficient.

✅ Space Complexity — O(1)

We only use two variables: first and second.

No extra arrays or data structures.
 
