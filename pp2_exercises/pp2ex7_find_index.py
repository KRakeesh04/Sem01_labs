with open('pp2ex7_input.txt','r') as file :
    text = file.read()
    data = text.split(']')


targeted_value =int(data[1])
given_list = list(map(int,data[0][1:].split(',')))

output_list = []
with open('pp2ex7_output.txt','w') as output :
    for val_i in range(len((given_list))):
        for val_j in range(len((given_list))):
            if (given_list[val_i] + given_list[val_j] == targeted_value) and (val_j != val_i) and (val_j not in output_list and val_i not in output_list):
                output_list.append(val_i)
                output_list.append(val_j)
                final_result = str(val_i) + str(val_j) + '\n'
                output.write(final_result)
                print(val_i,val_j)





