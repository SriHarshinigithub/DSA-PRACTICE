def brute(arr,target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j] == target:
                return (arr[i],arr[j])
    return None
arr = [2,7,11,5]
target = 9
print(brute(arr, target))