def read_file():
    with open('pp2ex17_input.txt','r') as input :
        movie_types = []
        for line in input:
            initial_index = line.index('(')
            final_index = line.index(')')
            if '|' in line :
                movie_types.extend(line[initial_index+1:final_index].strip().split('|'))
            else :
                movie_types.append(line[initial_index+1:final_index].strip())
        #print(movie_types)
    return movie_types

with open('pp2ex17_output.txt' , 'w') as output :
    data = []
    for type in read_file():
        data.append(type.strip().title())
    #print(data)

    common_type = []
    for type in data :
        if type not in common_type:
            common_type.append(type)
            count = data.count(type)
            final_result = f"{type} {count}\n"
            print(final_result, end='')
            output.write(final_result)

#print('greenland'.title())