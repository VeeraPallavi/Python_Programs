"""
    Sum of three Integer adds to ZERO
    a. Desc -> A program with cubic running time. Read in N integers and counts the
    number of triples that sum to exactly 0.
    b. I/P -> N number of integer, and N integer input array
    c. Logic -> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
    d. O/P -> One Output is number of distinct triplets as well as the second output is to
    print the distinct triplets.
"""


def three_sum(arr):
    arr.sort()
    n = len(arr)
    triplets=[]

    for i in range(n-2):
        if i> 0 and arr[i]== arr[i+1]:
            continue
        left = i+1
        right = n-1

        while(left < right):
            total = arr[i] + arr[left] + arr[right]
            if total == 0:
                triplets.append([arr[i], arr[left], arr[right]])
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
            
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return triplets


N = int(input("Enter Number of values: "))
arr = list(map(int,input("Enter Elements: ").split()))

result = three_sum(arr)

print(f"Number of distinct triplets: {len(result)}")
print("Distinct triplets:")
for value in result:
    print(value)