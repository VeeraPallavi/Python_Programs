def selection_sort(arr):
    """
    Docstring for selection_sort
    
    :param arr: list of integer values

    return : return sorted list
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

arr = [4,6,7,2,8,1]
print(selection_sort(arr))