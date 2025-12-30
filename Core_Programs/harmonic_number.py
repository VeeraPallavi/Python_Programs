def harmonic_number(N):
    """
    a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
    b. I/P -> The Harmonic Value N. Ensure N != 0
    c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
    d. O/P -> Print the Nth Harmonic Value
    """

    if(N ==0):
        print("Invalid input")
    total = 0
    for i in range(1,N+1):
        total = total +(1/i)
    return total

N = int(input("Enter a Number"))
print(harmonic_number(N))