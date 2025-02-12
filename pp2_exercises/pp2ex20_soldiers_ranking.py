def move_left_side(list :list, index :int, count :int) :
    if count == 0 :
        return list
    else :
        list[index-1], list[index] = list[index], list[index-1]
        return move_left_side(list,index-1,count-1)


with open('pp2ex20_input.txt','r') as input :
    data = []
    for line in input:
        data.append(list(map(int,line.split())))

with open('pp2ex20_output.txt','w') as output: 
    for val in data:
        ordered_list = []
        for i in range(len(val)):
            ordered_list.append(i+1)
        #ordered = [1,2,3]
        #val = [0,1,0]
        for j in range(len(val)):
            move_left_side(ordered_list,j,val[j])
        output.write(str(ordered_list)+'\n')
        print(ordered_list)