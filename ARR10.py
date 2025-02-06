def sort_zeros_ones_twos(arr):
    low = 0
    current = 0
    high = len(arr)-1
    while current <= high:
        if arr[current]==0:
            arr[low],arr[current] = arr[current],arr[low]
            low += 1
            current += 1
        elif arr[current]==2:
            arr[current],arr[high] = arr[high],arr[current]
            high -=1
        else:
            current +=1
    return arr
arr = [0,1,2,1,2,0]
print(sort_zeros_ones_twos(arr)) # Output: [0, 0, 1, 1, 2, 2]
