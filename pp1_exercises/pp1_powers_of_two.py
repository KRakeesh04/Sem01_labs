def is_product(num :int) :
    if num > 1 :
        while num > 1 :
            if num%2 == 0 :
                num = num//2
                continue
            else :
                return False
        return True
    elif num == 1 :
        return True
    else :
        return False


num_list = list(map(int, input("enter the numbers : ").split()))

count = 0
for num in num_list :
    if is_product(num) == True :
        count += 1
    else :
        continue

print("Number of powers of two: ", count)








