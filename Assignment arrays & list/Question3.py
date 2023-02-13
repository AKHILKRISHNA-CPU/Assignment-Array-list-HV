def highest_frequency(array):
    freq = {}
    for i in array:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return max(freq, key=freq.get)

array = list(map(int, input("Enter the elements : ").strip().split()))
print("The highest repeated element is:", highest_frequency(array))
