# FIND LARGEST AND SMALLEST ELEMENT IN AN ARRAY
def find_largest_and_smallest(arr):
    if not arr:
        return None,None
    largest = smallest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
        elif i < smallest:
            smallest = i    
    return largest,smallest 
arr = [1,-3,9,10,17,0]
print(find_largest_and_smallest(arr))