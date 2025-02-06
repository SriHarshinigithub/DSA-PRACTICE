def find_second_largest(arr):
    if len(arr) < 2:
        return None 
    largest = second_largest = float('-inf')
    if second_largest != float('-inf'):
        return None 
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num 
    return second_largest 
arr = [1,5,7,8,10]
print(find_second_largest(arr))