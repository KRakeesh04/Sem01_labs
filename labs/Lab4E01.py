
while True :
    num = int(input())          #Getting input from the user
    if num < 0 :            #Terminate the programme when the input is a negative number or zero 
        break
    elif num > 1 :         #Skip special case of prime & non-prime set which is 1
        for i in range(2, int(num**(1/2) + 1) ) :     #Finding whether it's prime or not
            if num%i == 0 :
                print("non-prime")
                break
            else :
                continue
        else :
            print("prime")

    else :                      #printing 1 is a non-prime
        print("non-prime")       



