def divisor_sum(num :int) :
    D_sum = 0
    for i in range(1, num+1) :
        if num % i == 0 :
            D_sum += i
        else :
            continue
    return D_sum

try :
    N_input = int(input("Input n: "))

    if 0 < N_input <= 100000 :
        if N_input*2 > divisor_sum(N_input) :
            print( N_input, "is deficient by", ( (N_input*2) - divisor_sum(N_input) )  ) 
        elif N_input*2 < divisor_sum(N_input) :
            print( N_input, "is abundant by", ( divisor_sum(N_input) - (N_input*2) )  ) 
        else :
            print(N_input, "is perfect number")
    else :
        print("Check the value")

except ValueError :
    print("Input should be integers")




