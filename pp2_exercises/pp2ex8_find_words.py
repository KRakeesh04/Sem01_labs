def lower(word_lst :list):
    lst = []
    for i in word_lst:
        lst.append(i.lower())
    return lst


def find_words(content_1 :list, content_2 :list):
    output_list = []
    for chars in content_1:
        for word1 in lower(content_2):
            if word1 in chars and word1 not in output_list:
                output_list.append(word1)
    return output_list

def printing_writting(lst :list):
    with open('pp2ex8_output.txt', 'w') as output :
        for word in lst:
            output.write(word+'\n')
            print(word)



with open('pp2ex8_input01.txt','r') as file01 :
    data = []
    for line in file01:
        data.extend(line.split())
    content_1 = []
    for word in data:
        chars = ""
        for char in word:
            if char.isalpha():
                chars += char
        content_1.append(chars)
    
with open('pp2ex8_input02.txt','r') as file02 :
    content_2 = []
    for line in file02:
        content_2.extend(line.split())
    

printing_writting(find_words(content_1,content_2))









