Abundant_num = []  #Creating an empty list for the abundant numbers

num=int(input("Input number: "))  #Getting user input for the range

if num > 2 :     #Make sure the least range is 1 to 3
    
    for i in range(2 , num + 1 ) :
        sum = 0
        j = 1
        while j < i :
            if i%j == 0 :       #Finding divisors and adding
                sum += j
                j += 1
            else :
                j += 1

        if sum > i :                    #Find out the abundant numbers
             Abundant_num.append(i)     #Adding new abundant numbers into the list
        else :
            pass


    count = len(Abundant_num)                 #Finding the length of abundant numbers
    print("Number of abundant numbers from 1 to", num , "is" , count)        #Show the final output

else :
    print("Invalid Input")
    