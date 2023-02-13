def duplicate_data(arr):
    duplicate = set()
    for i in arr:
        if arr.count(i) > 1:
            duplicate.add(i)
    return duplicate

arr= list(map(int, input("Enter the elements of the array: ").split()))
print(duplicate_data(arr))
