def getMaxValue(arr):
    arr.sort()  # Step 1: Sort the array
    arr[0] = 1  # Step 2: Ensure first element is 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1] + 1:
            arr[i] = arr[i - 1] + 1  # Reduce value to maintain constraint

    return arr[-1]  # Step 3: Return the last element as max possible value

# Reading input from stdin
n = int(input())  # Read the number of elements
arr = [int(input()) for _ in range(n)]  # Read the array elements
print(getMaxValue(arr))  # Print only the final output
