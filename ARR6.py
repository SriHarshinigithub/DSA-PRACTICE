def missing_numbers(arr):
    n = len(arr)+1
    expected = n*(n+1)//2
    actual = sum(arr)
    return expected - actual