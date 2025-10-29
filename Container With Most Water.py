class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #Always move the pointer with the smaller height first.
        left = 0
        right = len(height)-1
        max_water = 0

        while  left < right:
            width = right-left
            current_water = width*min(height[left],height[right])
            max_water = max(max_water,current_water)

            if height[left] < height[right]:
                left += 1
            else:
                right-=1
        return max_water

                
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

✅ Time Complexity (TC)

O(n)

We use two pointers, and in each step, one pointer moves inward.

So maximum total movements = n steps

No nested loops → linear time

✅ Space Complexity (SC)

O(1)

We are not using any extra data structures

Just using a few integer variables (left, right, max_water)
