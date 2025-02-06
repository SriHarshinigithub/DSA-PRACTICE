def is_palindrome(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        if arr[start]!=arr[end]:
            return False
        start += 1
        end -= 1 
    return True

arr = [1,'a',1]
arr1= [1,2,3,2,1]
print(is_palindrome(arr1))