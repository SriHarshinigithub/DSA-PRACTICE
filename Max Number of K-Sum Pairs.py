class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        nums.sort()
        left=0
        right=len(nums)-1
        while left<right:
            current_sum=nums[left]+nums[right]
            if current_sum == k:
                ans+=1
                left+=1
                right-=1
            elif current_sum < k:
                left += 1
            else:
                right-=1

        return ans

✅ Time Complexity (TC)

O(n log n)

Because we do a sort first → O(n log n)

Then we use two pointers scan only once → O(n)

So total = O(n log n)

✅ Space Complexity (SC)

O(1)

We are modifying in place

No extra data structures used

Only using a few variables (left, right, ans, etc.)
Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 
