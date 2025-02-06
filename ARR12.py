def intersection(nums1,nums2):
    set1 = set(nums1)
    intersection_set = []
    for num in nums2:
        if num in set1:
            intersection_set.append(num)
    return list(intersection_set)
nums1=[1,2,3,4]
nums2=[4,3,]
print(intersection(nums1,nums2))