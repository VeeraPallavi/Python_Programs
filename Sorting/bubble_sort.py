def bubble_sort(arr):
    """
    Docstring for bubble_sort
    
    :param arr: list of integer values

    return : returns sorted list
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

arr = [4, 2, 7, 9, 1]
print(bubble_sort(arr))
