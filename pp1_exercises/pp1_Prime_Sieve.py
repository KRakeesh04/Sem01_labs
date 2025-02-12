num_list = []
u_limit = int(input())
for num in range(1,u_limit+1) :
    num_list.append(num)

num_list.remove(1)

non_prime_list = []

for i in num_list :
    if i == 2 :
        continue
    elif i%2 == 0 :
        non_prime_list.append(i)
    elif i == 3 :
        continue
    elif i%3 == 0 :
        non_prime_list.append(i)
    else :
        for n in range(2, (u_limit//i)+1) :
            if i*n in num_list :
                non_prime_list.append(i*n)
            else :
                continue


for j in num_list :
    if j not in non_prime_list :
        print(j, end=' ')
    else :  
        continue
    