#alphabet diamond

letter_input = input('enter letter : ')
letter_input = letter_input.upper()
 #print(letter_input)

alph_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

n = alph_list.index(letter_input)
 #print(n)


output_list = []
for i in range(n+1) :
    line = alph_list[i]
    for j in range(i-1,-1,-1) :
        line = (alph_list[j]) + line + (alph_list[j])
    output_list.append(line)
for element in output_list[n-1::-1] :
    output_list.append(element)

 #print(output_list)


for outputs in output_list :
    print(outputs.center((n*2)+1))


