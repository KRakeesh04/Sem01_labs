matrix_list = []

row_input_01 = input()                          #take first input
if row_input_01 != "-1" :                       #check the input is "-1" to terminate the programme
    #check the errors while changing list string values into intergers
    try :
        matrix_list.append(list(map(int, row_input_01.split())))
    except :
        print("Error")
        exit()
else :
    exit()

#take multi inputs and check the input is "-1" to terminate the programme
while True :
    row_input = input()
    if row_input != "-1" :
        try :
            matrix_list.append(list(map(int, row_input.split())))
        except :
            print("Error")
            exit()
        #check the new nested list has the same length like the first nested list
        if len(matrix_list[0]) == len(matrix_list[-1]) :
            continue
        else :
            print("Invalid Matrix")
            exit()

    else :
        break

#printing the transposed matrix
for j in range(len(matrix_list[0])) :
    for i in range(len(matrix_list)) :
        print(matrix_list[i][j], end=' ')
    print()
    