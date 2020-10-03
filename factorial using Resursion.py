def factr(n):

    if n==0:
         return 1

    return n*factr(n-1)

n = int(input("Enter number to find factorial: "))
if n<0:
    print("Enter a valid number")
else:
    result = factr(n)
    print(result)
