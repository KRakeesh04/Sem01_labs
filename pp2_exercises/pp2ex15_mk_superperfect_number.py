def summation_of_factors(factors :list) :
    total_sum = 0
    for num in factors :
        total_sum += num
    return total_sum


def sum_of_factors_of_n(number :int) :
    factors_lst = []
    for i in range(1,number+1) :
        if number % i == 0 :
            factors_lst.append(i)
    summation = summation_of_factors(factors_lst)
    return summation


with open('pp2ex15_input.txt','r') as input_file:
    data = []
    for line in input_file:
        data.append(list(map(int,line.split())))

with open('pp2ex15_output.txt','w') as output :
    for val in data :
        p, m, k = val
        mk_perfect_num = []
        for num in range(1,p+1):
            value = num
            for i in range(1,m+1):
                value = sum_of_factors_of_n(value)
            if value == num*k :
                mk_perfect_num.append(num)
        max_val = max(mk_perfect_num)
        print(max_val)
        output.write(str(max_val)+'\n')
