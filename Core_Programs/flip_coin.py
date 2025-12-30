import random

n=int(input("Enter number of times the coin has to flip: "))

if(n < 0):
    print("Enter Positive Number")
else:
    heads=0
    tails=0
    for _ in range(n):
        if(random.random() < 0.5):
            tails = tails + 1
        else:
            heads = heads + 1
heads = (heads / n) * 100
tails = (tails / n) * 100

print(f"Percentage of Heads: {heads}")
print(f"Percentage of Tails: {tails}")