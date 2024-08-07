def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        # Find the index of the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

def print_array(arr):
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    selection_sort(arr)
    print("Sorted array:")
    print_array(arr)
