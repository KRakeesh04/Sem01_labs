def is_anagram(word_1 :str, word_2 :str) :
    if len(word_1) == len(word_2) and word_1.isalpha() and word_2.isalpha():
        list_1 = sorted(list(word_1.lower()))
        list_2 = sorted(list(word_2.lower()))
        for i in range(len(word_1)) :
            if list_1[i] != list_2[i] :
                return False
        else :
            return True
    else :
        return False
    
def write_file(value) :
    value = value + '\n'
    file.write(value)

def __main_(file_name) :
    with open(file_name, 'r') as input_file :
        for line in input_file :
            if '\n' in line :
                line = line[:-1]
            word1,word2 = line.split()
            if is_anagram(word1,word2) == True :
                write_file('Anagram')
            else :
                write_file('Not Anagram')



with open('pp2ex2_output.txt', 'w') as file:
    input_file_name = input('Enter the file name :  ')
    __main_(input_file_name)



