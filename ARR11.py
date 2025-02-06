def find_duplicates(arr):
    seen = list(set())
    duplicates = list(set())
    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen.append(num)
    return duplicates
arr = [1,2,3,1,2,4]
print(find_duplicates(arr))