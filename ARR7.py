def count_frequency(arr):
    if not arr:
        return None
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency
arr = [1,1,1,2,2,2,2,3,3,3,4,4,5]
print(count_frequency(arr))