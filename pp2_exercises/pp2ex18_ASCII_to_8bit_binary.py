def ASCII_to_binary(character :str):
    ASCII_value = ord(character)
    #ASCII_value = character
    binary_value = ''
    while ASCII_value > 0 :
        binary_value = str(ASCII_value % 2) + binary_value
        ASCII_value //= 2
    return f"{int(binary_value):08}"

#print(ASCII_to_binary('a'))

with open('pp2ex18_input.txt','r') as input:
    data = []
    for line in input :
        data.append(line)

with open('pp2ex18_output.txt','w') as output :
    for val in data :
        #print(val)
        result = ''
        for i in val:
            if i != '\n' :
                result += ASCII_to_binary(i) + ' '
        output.write(result + '\n')
        print(result)

#print(ord('8'))
#print(ASCII_to_binary('f'))