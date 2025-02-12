def divising_by_denominator(numer :list, denom :list, K01 :int, count :int = 1):
    for i in range(len(numer)):
        if K01 % denom[i] == 0 :
            K01 = (K01 / denom[i])*numer[i]
            if count == 50 :
                return K01
            count += 1
            return divising_by_denominator(numer,denom,K01,count)
    else :
        return K01



def process() :
    with open('pp2ex13_input.txt', 'r') as inputs :
        K_1_data = []
        fraction_list = []
        for line in inputs :
            k_1 , fractions = line.split('|')
            fraction_list.append(fractions)
            K_1_data.append(int(k_1))

    with open('pp2ex13_output.txt','w') as output :
        for i in range(len(K_1_data)):
            fractions_of_i = fraction_list[i].split(',')

            numerator = []
            denominator = []
            for val in fractions_of_i :
                numer, denom = val.split('/')
                numerator.append(int(numer))
                denominator.append(int(denom))
            
            Kp_or_K50 = str(int(divising_by_denominator(numerator,denominator,K_1_data[i])))

            output.write(Kp_or_K50+'\n')
            print(Kp_or_K50)
    
###################### main ########
process()
