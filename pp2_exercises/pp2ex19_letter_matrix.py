with open('pp2ex19_input.txt','r')as input :
    data = []
    for line in input:
        data.append(line.split())

def transpose(list):
    result = []
    for j in range(len(list[0])):
        text = ''
        for i in range(len(list)):
            text += list[i][j]
        result.append(text)
    return result

def printing_text(list):
    for i in list:
        print(i, end='')

for value in data:
    row_count = int(value[1])
    text = value[0]
    new_text = text + '*'*(row_count - (len(text)%row_count))
    text_list = []
    for i in range(0,len(new_text),row_count):
        text_list.append(new_text[i:i+row_count])
    print(text_list)
    transposed_text = transpose(text_list)
    printing_text(transposed_text)
