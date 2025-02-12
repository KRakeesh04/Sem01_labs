#create sample chess
def chess_8x8() :
    chess_place = []
    for i in range(8):
        row = []
        for j in range(8):
            row.append(0)
        chess_place.append(row)
    return chess_place


#cut a row if there is  queen on that row 
def row_cut(chess_list :list, row :list):
    for i in range(len(chess_list)):
        if i+1 in row:
            for j in range(len(chess_list[i])):
                chess_list[i][j] = 1
    return chess_list


#cut a coloum if there is  queen on that coloum 
def colm_cut(chess_list :list, colm :list):
    for i in range(len(chess_list)):
        for j in range(len(chess_list[i])):
            if j in colm :
                chess_list[i][j] = 1
    return chess_list


#cutting diagonal-wise 
def diagonal_cut_1(chess_list :list, x :list, y :list):
    if x+y % 2 == 0 :
        count_i = 0
    else :
        count_i = 1
    
    for i in range(len(chess_list)):
        for j in range(len(chess_list[i])):
            if i - count_i == x and j - count_i == y :            ###############$$$$$$$$$$
                count_i +=2
    
        

    pass



######################################
def show_chess(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            print(list[i][j] , end='  ')
        print()
######################################



#ordering the input values for the process
dict= {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
input_val_colm = ['a','b','c','e','f','h']
input_val_row = [1,7,4,8,2,3]

input_val_colm_num = []
for k in input_val_colm :
    input_val_colm_num.append(dict[k])

#create chess sample and cheeck the suitable places for the balance queens
chess = chess_8x8()
colm_cut(row_cut(chess,input_val_row),input_val_colm_num)
#   diagonal_cut_1()


######################
show_chess(chess)
print('\n')
######################

#select the suitable pairs for the output
output_list = []
for row_i in range(len(chess)):
    for colm_i in range(len(chess[row_i])):
        if chess[row_i][colm_i] == 0 :
            output_list.append([colm_i,row_i+1])


#######################
print(output_list)
#######################


#print the final output 
for m,n in output_list:
    for l in dict:
        if dict[l] == m : 
            value = l + str(n) 
            print(value)



