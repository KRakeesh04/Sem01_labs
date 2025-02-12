def palindrome(num, n=0) :
    num_str = str(num)
    while True :
        if num_str == num_str[::-1] :
            print("palindrome=",num ,"number of additions", n)
            break
        else :
            n += 1
            palindrome(num + int(num_str[::-1]), n)
            break


while True :
    num = int(input("Enter a number : "))
    if num == -1 :
        exit()
    else :
        palindrome(num)