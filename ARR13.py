def union(nums1,nums2):
    result = []
    for num in nums1+nums2:
        if num not in result:
            result.append(num)
    return result
nums1=[1,2,3]
nums2=[3,4,5,6]

print(union(nums1,nums2))