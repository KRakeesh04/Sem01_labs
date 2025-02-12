def read_file():
    with open('pp2ex14_input.txt','r') as input_file :
        data = []
        for line in input_file:
            data.append(line.split())
            #print(line.split())
    return data

def sorting_the_names(name_list :list) :
    name01, name02 = name_list
    iterration_count = min([len(name01),len(name02)])
    for i in range(iterration_count):
        if ord(name01[i]) < ord(name02[i]) :
            return name01, name02
        elif ord(name01[i]) > ord(name02[i]) :
            return name02, name01
        else :
            continue
    else :
        return name01, name02 

with open('pp2ex14_output.txt','w') as output :
    for val in read_file() :
        name_order = ''
        for name in sorting_the_names(val) :
            name_order += name + ' '
            print(name, end=' ')
        output.write(name_order+'\n')
        print()