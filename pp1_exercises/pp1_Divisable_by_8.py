def num_out(num_list :list) :
    num = ''
    for i in num_list :
        num += str(i)
    return int(num) 

def is_exist(num_list, n=8) :
    possible_outputs = []
    # [ 9 , 6 , 4  ]
    for i in range(len(num_list)) :
        if num_out(num_list[:i] + num_list[i+1:]) % 8 == 0 :
            possible_outputs.append(num_out(num_list[:i] + num_list[i+1:]))
        else :
            continue
    if len(possible_outputs) == 0 :
        return False
    else :
        m = max(possible_outputs)
        return m


num = int(input("Input: ").strip())
if 1 < len(str(num)) < 100 :
    if num % 8 == 0 :
        print("YES")
    elif is_exist(list(str(num))) == False :
        print("NO")
    else :
        m = is_exist(list(str(num)))
        print("Yes", "m="+str(m))
else :
    print("check the number")
    exit()