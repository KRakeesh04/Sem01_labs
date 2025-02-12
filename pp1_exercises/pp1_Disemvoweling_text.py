vowels = ['a', 'e', 'i', 'o', 'u']

input_text = input("Original string (INPUT): ")

output_list = list(input_text)
removed_letters = ""
for letter in input_text :
        if  letter == ' ' :
            output_list.remove(' ')
        elif letter.isalpha == False :
            print("check the text")
            exit()
        elif letter.lower() in vowels :
            output_list.remove(letter)
            removed_letters += letter
        else :
            continue
        
output_text = ""
for i in output_list :
    output_text += i

print("Disemvoweled string:", output_text)

print("Removed vowels:", removed_letters, "(In original order)")


