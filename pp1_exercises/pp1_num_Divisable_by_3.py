n = int(input("Enter Input: "))


print("Output:")

while n > 1 :
    if n % 3 == 0 :
        print(n, ' - ', 0)
        n = int(n/3)
    elif (n+1) % 3 == 0 :
        print(n, ' - ', 1)
        n = int((n+1) / 3)
    elif (n-1) % 3 == 0 :
        print(n, ' - ', -1)
        n = int((n-1) / 3)

print(1)

