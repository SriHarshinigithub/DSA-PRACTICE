def find_subarr_max_sum(arr):
    if not arr:
        return None
    current_max = global_max = arr[0]
    for num in arr[1:]:
        current_max = max(num,current_max+num)
        global_max = max(global_max,current_max)
    return global_max
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(find_subarr_max_sum(arr))