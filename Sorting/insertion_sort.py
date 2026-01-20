def insertion_sort(arr):
    """
    Docstring for insertion_sort
    
    :param arr: list of integer values

    return : returns sorted list
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr

arr = [5, 6, 7, 3, 2, 1]
print(insertion_sort(arr))