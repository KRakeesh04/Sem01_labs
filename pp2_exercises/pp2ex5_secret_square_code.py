def decoded_msg(data_list :list):
    try :
        text_msg = ''
        for k in range(int(data_list[0])) :
            for j in data_list[1].split() :
                text_msg += j[k]
        return text_msg
    
    except IndexError :
        return text_msg

with open('pp2ex5_input.txt','r') as data :
    input_list = []
    for i in data:
        input_list.append(i)

msg = decoded_msg(input_list)

print(msg)

