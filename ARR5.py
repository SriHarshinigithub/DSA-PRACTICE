def rotate_array(arr,k):
    n = len(arr)
    k = k % n
    def reverse(start,end):
        while start < end:
            arr[start],arr[end] = arr[end],arr[start]
            start += 1
            end -=1
    reverse(0,n-1)
    reverse(0,k-1)
    reverse(k,n-1)
    return arr
arr = [1,2,3,4,5]
k = 2
print(rotate_array(arr,k))