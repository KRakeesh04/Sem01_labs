n_input = int(input())


prime_num_list = []
i = 2
while n_input != len(prime_num_list) :
    if i == 2 :
        prime_num_list.append(i)
        i += 1
    else :
        is_prime = True
        for j in range(2,i) :
            if i%j == 0 :
                is_prime = False
            else :
                continue
        if is_prime == True :
            prime_num_list.append(i)
            i += 1
        else :
            i += 1

num_multiple = 1
for k in prime_num_list :
    num_multiple *= k


print(prime_num_list)
print(num_multiple + 1)
