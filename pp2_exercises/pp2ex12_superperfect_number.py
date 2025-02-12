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



with open('pp2ex12_input.txt','r') as input :
    data = []
    for line in input:
        data.append(int(line))
    with open('pp2ex12_output.txt','w') as output :
        for val in data :
            superperfect_numbers = []
            for i in range(1,val+1):
                if i*2 == sum_of_factors_of_n(sum_of_factors_of_n(i)):
                    superperfect_numbers.append(i)
            
            max_val = max(superperfect_numbers)
            output.write(str(max_val)+'\n')
            print(max_val)
