def clockwise(arr, n):
    if n > len(arr):
        n = n % len(arr)
    return arr[-n:] + arr[:-n]
arr =  list(map(int, input("Enter input separated by space: ").split()))
n = int(input("Enter number of steps to rotate the array in clockwise: "))
print(clockwise(arr, n))