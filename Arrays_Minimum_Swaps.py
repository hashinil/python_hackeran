def minimumSwaps(arr):
    swaps = 0
    i = 0

    while i < len(arr):
        # If the current element is not in its correct position
        if arr[i] != i + 1:
            # Swap the current element with its correct position
            temp = arr[i]
            print(temp)
            arr[i] = arr[temp - 1]
            print(arr)
            arr[temp - 1] = temp
            print(arr)
            swaps += 1
        else:
            i += 1
    return swaps
        
            


q = [1, 3, 5, 2, 4, 6, 7]
print(minimumSwaps(q))
