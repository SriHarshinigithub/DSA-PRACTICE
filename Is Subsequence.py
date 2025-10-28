class Solution(object):
    def isSubsequence(self, s, t):
        i = 0  # pointer for s
        j = 0  # pointer for t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # move s pointer only if match
            j += 1  # always move t pointer

        return i == len(s)
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 ✅ Time Complexity (TC)

O(n) — where n = len(t)

Why?

We scan through the string t only once using pointer j

i only moves forward when there's a match, so no backward movement

✅ Space Complexity (SC)

O(1) — constant space

Why?

We are not using any extra data structure

Only two integer pointers (i, j) → constant memory
