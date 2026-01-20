def binary_search(arr, target):
    """
    Implements Binary Search for the given list
    
    :param arr: list of integer values 
    :param target: integer value

    return : returns the index of target value
    """

    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
    return -1

arr = [1, 3, 5, 7, 8, 9]
target = 2
result = binary_search(arr, target)
if result != -1:
    print(f"Element Found at index {result}")

else:
    print("Element Not Found")