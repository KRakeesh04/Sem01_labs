def is_prime(value :int):
    if value == 2 and value == 3 :
        return True
    elif value > 2 :
        for i in range(2,int(value**(1/2))+1):
            if value % i == 0 :
                 return False
        else :
            return True
    else :
        return False
    
def prime_numbers(number :int) :
    prime_lst = []
    for i in range(2,number):
        if is_prime(i) :
            prime_lst.append(i)
    return prime_lst

with open('pp2ex10_input.txt','r') as input :
    data = []
    for line in input:
        data.append(int(line))
    with open('pp2ex10_output.txt','w') as output :
        for i in data :
            prime_pairs = []
            for j in prime_numbers(i):
                if is_prime(2*i - j) :
                    prime_pairs.append([j, 2*i-j])
                    #print([j, 2*i-j])
            count = str(len(prime_pairs))
            print(count)
            output.write(count+'\n')





