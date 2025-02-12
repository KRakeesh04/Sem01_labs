def palindrome_square(num_range) :
    square_add = 0
    #range 1 - 100 , range 400 - 1000
    # 1 4 9 
    for i in range(int(num_range[0]**(1/2)), int(num_range[1]**(1/2)) + 1) :
        if str(i**2) == str(i**2)[::-1] :
            if (i**2) <= num_range[1] :
                square_add += (i**2)
            else :
                return square_add
        else :
            continue
    return square_add



def palindrome_prime(num_range) :
    prime_add = 0
    #1 2 3 5 7 11 
    for j in range(num_range[0], num_range[1]) :
        if j == 1 :
            continue
        elif str(j) == str(j)[::-1] :
            for k in range(2,j) :
                if j%k != 0 :
                    continue
                else :
                    j = 0
            prime_add += j
        else :
            continue
    return prime_add
    

num_range = list( map(int, input("enter the range : ").split() ) )
print("Sum of palindrome square numbers : ", palindrome_square(num_range))
print("Sum of palindrome prime numbers : ", palindrome_prime(num_range))

print('Total of palindrome prime and square : ',palindrome_square(num_range) + palindrome_prime(num_range))

