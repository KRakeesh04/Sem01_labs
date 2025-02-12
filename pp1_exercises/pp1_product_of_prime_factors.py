prime_list = []
def primeFactors_List(input_num):
    for i in range(2,input_num) :
        if input_num / i == 1 :
            prime_list.append(i)
            break
        elif input_num % i == 0 :
            if i == 2 :
                prime_list.append(i)
                primeFactors_List(int(input_num/i))
            else :
                for j in range(2,i) :
                    if i % j != 0 :
                        continue
                    else :
                        i = 0
                        break
                if i != 0 :
                    prime_list.append(i)
                    primeFactors_List(int(input_num/i))
                else :
                    break
        else :
            continue

    num = 1
    for i in range(len(prime_list)) :
        if prime_list[i]*num == input_num :
            return  prime_list[:i+1]
        else :
            num *= prime_list[i]


    
def short_list(num_list) :
    numbers = []
    for i in range(len(num_list)) :
        if num_list[i] not in numbers :
            numbers.append(num_list[i])
        else :
            continue
    return numbers




def exponent(num_list, num) :
    numbers = []
    n = 0
    for i in range(len(num_list)) :
        if num == num_list[i] :
            n += 1
        else :
            continue
    return n

#print(68456)
#print(primeFactors_List(68456))
#print(exponent_of_num(primeFactors_List(68456),2))
#print(short_list(primeFactors_List(68456)))

num_input = int(input())
sorted_list = short_list(primeFactors_List(num_input))
for k in range(len(sorted_list)-1) :
    if exponent(primeFactors_List(num_input), sorted_list[k]) > 1 :
        print(sorted_list[k] , exponent(primeFactors_List(num_input), sorted_list[k]) ,sep='^', end=' X ')
    else :
        print(sorted_list[k], end=' X ')

if exponent(primeFactors_List(num_input), sorted_list[-1]) > 1 :
    print(sorted_list[-1], exponent(primeFactors_List(num_input), k) ,sep='^')
else :
    print(sorted_list[-1])