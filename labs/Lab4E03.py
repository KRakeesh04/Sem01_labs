message = str(input("Enter message: "))             #Asking the message for encryption

base = int(input("Enter base: "))


if  11 > base > 0 :                 #make sure the base stays between 0 and 11
    ASCII_val= ""
    final_val = ''
    for i in message :
        ASCII_val = ord(i)          #change ASCII value into decimal value
        remainder = ''
        
        while ASCII_val != 0 :                  #divide the value by base until it reaches the zero
            remainder += str(ASCII_val%base)
            ASCII_val = ASCII_val//base

        final_val += remainder[::-1]            #reversely assign the remainders to a new variable

    else :
        print(final_val)                    #print encrypted message

else :
    exit

 