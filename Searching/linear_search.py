def linear_search(arr, target):
    """
    Implements Linear search for the given arr
    
    :param arr: list of integer values 
    :param target:integer value

    return : returns index of target value 
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    return -1

arr = [1, 4, 6, 7, 5, 3]
target = 10
result = linear_search(arr, target)
if result != -1:
    print(f"Element Found at index {result}")
else:
    print("Element not Found")