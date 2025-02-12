
input_text = input("Input: ")
vowels = ['a', 'e', 'i', 'o', 'u']
output_text = ''
for i in input_text :
    if i.isalpha() == True :
        if i in vowels or i.lower() in vowels :
            output_text += i
        else :
            output_text += (i+'o'+i.lower())
    else :
        output_text += i
    

if input_text[-1] == '!' :
    print("Output(Encoded): ", output_text)
else :
    print("Output(Encoded): ", (output_text + '!'))




