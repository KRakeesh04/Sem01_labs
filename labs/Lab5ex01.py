numbers = input()
str_list = numbers.split()          #split and add the inputs to a list
num_list = []
for i in str_list :
    try :                   #to prevent the errors from affecting the outputs
        if '.' in i :
            num_list.append(float(i))       #change string into float type which are float value and add them to a new list.
        else :
            num_list.append(int(i))         #change string number into interger type and add them to a new list.
    except :
        exit()
        
#finding minimum and maximum values
max_num = max(num_list)
min_num = min(num_list)

#print the outputs
print("Minimum =", min_num)
print("Maximum =", max_num)



 
