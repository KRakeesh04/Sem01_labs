def is_prime(num :int) :
    if num == 2:
        return True
    elif num  > 2 :
        for i in range(2,int(num**(1/2))+1):
            if num % i == 0 :
                return False
        else :
            return True
    else :
        return False
    

with open('pp2ex16_input.txt', 'r') as input :
    data = []
    for num in input:
        data.append(int(num))
with open('pp2ex16_output.txt', 'w') as output :
    for nums in data :
        prime_triplets = []
        for i in range(2,nums):
            if is_prime(i) and is_prime(i+2) and is_prime(i+6) and i+6 < nums:
                prime_triplets.append([i,i+2,i+6])
            elif is_prime(i) and is_prime(i+4) and is_prime(i+6) and i+6 < nums:
                prime_triplets.append([i,i+4,i+6])
        count = str(len(prime_triplets))
        #print(prime_triplets)
        print(count)
        output.write(count + '\n')
                