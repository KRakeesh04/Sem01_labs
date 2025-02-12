def write_on_file(count) :
    with open('pp2ex1_output.txt','w') as output :
        line = str(count) + '\n'
        output.write(line)


def is_prime(num :int) :
    if num <= 1 :
        return False 
    if num == 2 :
        return True
    else :
        for i in range(2,int(num**(1/2))+1) :
            if num%i == 0 :
                return False
        else :
            return True
        
def nums_GCD(number_1 :int, number_2 :int) :
    if number_2 == 0 :
        return number_1
    else :
        return nums_GCD(number_2, number_1%number_2)



filedata = []
with open("pp2ex1_input.txt", 'r') as file :
    for line in file :
        if line == '\n' :
            continue
        elif '\n' in line :
            line = line[:-1]
        filedata.append(int(line))

#### filedata = [10,100,30]
with open('pp2ex1_output.txt','w') as output :
    for N in filedata :
        prime_numbers = []
        for i in range(1,N+1) :
            for j in range(1,N+1) :
                value = nums_GCD(i,j)
                #print(value,end=', ')
                if is_prime(value) == True :
                    prime_numbers.append(value)
        prime_count = len(prime_numbers)
        output.write(str(prime_count) + '\n')

    else :
        print("*****fully completed")


