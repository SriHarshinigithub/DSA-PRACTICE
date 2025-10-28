#Two Pointer
class Solution:
    def compress(self, chars):
        write = 0  # where we write the compressed result
        read = 0   # where we read characters

        while read < len(chars):
            char = chars[read]  # current character
            count = 0

            # Step 1: count how many times this character repeats
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # Step 2: write the character once
            chars[write] = char
            write += 1

            # Step 3: if more than 1, write the number (as string)
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write  # final compressed length
Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

  ✅ Time & Space Complexity
Complexity Type	Value	Explanation
Time Complexity (TC)	O(n)	We traverse the array only once using the read pointer → linear time
Space Complexity (SC)	O(1)	We modify the input array in place — only use a few variables (read, write, count) → constant space
