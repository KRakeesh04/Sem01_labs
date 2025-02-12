def F(n):
    if n == 0:
        return 1
    else:
        lst = [n]
        for i in range(n):
            lst.append(lst[i]-M(F(lst[i]-1)))
        #print(lst)
        return lst[n]
 
def M(n):
    if n == 0:                                              #
        return 0                                            #
    else:                                                   #
        lst = [n]                                           #
        for i in range(n):                                  #
            lst.append(lst[i]-F(M(lst[i]-1)))               #
        #print(lst)                                         #
        return lst[n]                                       #
                                                            #
#############################################################



def Female(n):
    if n == 0 :
        return 1
    elif n > 0 :
        return  n - Male(Female(n-1)) 

def  Male(n):
    if n == 0 :
        return 0
    elif n > 0 :
        return   n - Female(Male(n-1))


with open('pp2ex9_input.txt','r') as file :
    data = []
    for line in file:
        data.append(int(line))
    with open('pp2ex9_output.txt','w') as output_data:
        for val in data:
            output = "{}: F={} M={}".format(val,Female(val),Male(val))
            output_data.write(output+'\n')
            print(output)




