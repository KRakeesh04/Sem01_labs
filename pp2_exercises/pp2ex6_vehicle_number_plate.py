def add_letter(list :list):
    list[2] += 1
    if list[2] == 26 :
        list[1] += 1
        list[2] = 0
    return list


alph_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
#get inputs from the given file
with open('pp2ex6_input.txt','r') as filedata :
    data = []
    for line in filedata:
        data.append(line.split('-'))


with open('pp2ex6_output.txt','w') as outputfile :
    output = []
    for number in data:
        letters_num = ''
        for char in number[0]:
            letters_num += (str(alph_list.index(char)) + '-')
        letter_num_list = list(map(int,letters_num[:-1].split('-')))

        #assinging new values for the new number plates
        new_plate_letters = number[0]
        new_num = str(int(number[1]) + 1).rjust(4,'0')

        #if it reaches the '9999' then make changes in letters of the number plate
        if new_num == '10000' :
            new_num = '0001'
            new_letters = add_letter(letter_num_list)

            new_plate_letters = ''
            for i in new_letters :
                new_plate_letters += alph_list[i]

        #ordering the final results to correct format and print the final output
        final_number_plate_num = new_plate_letters + '-' + new_num
        outputfile.write(final_number_plate_num + '\n')
        print(final_number_plate_num)






