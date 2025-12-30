year=int(input("Enter Year"))

if(year < 1000 or year > 9999):
    print("Enter year with four digits")
else:
    if(year % 400==0):
        print("Leap Year")
    elif(year % 4==0 or year % 100 !=0):
        print("Leap Year")
    else:
        print("Not a Leap Year")
