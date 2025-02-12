#funtion to get input from user according to it's dimension
def get_input() :
    matrix_list = []
    for i in range(dimension[0]) :
        try :
            row_wise_inputs = list( map( int, input().split() ) )
        except :
            print("error")
            exit()
            
        if dimension[1] == len(row_wise_inputs) :
            matrix_list.append(row_wise_inputs)
        else :
            print('Invalid Matrix')
            exit()

    return matrix_list


#function to take the dimention and taking 'matrix A' and 'matrix B'
def get_matrix() :    
    global dimension    #to use this 'dimension' variable in the main programme or in the other functions

    print("Enter the dimension: " , end='')
    dimension = list(map( int, input().split(',') ) )
    print("Enter Matrix A:")
    matrix_A_list = get_input()
    print("Enter Matrix B:")
    matrix_B_list = get_input()
    
    matrix_B_list = transpose_matrix(matrix_B_list)
    return matrix_A_list , matrix_B_list


#function to change to transpose of a given matrix
def transpose_matrix(matrix_list) :
    New_matrix_list = []
    for j in range(len(matrix_list[0])) :
        row_lists = []
        for i in range(len(matrix_list)) :
            row_lists.append(matrix_list[i][j])
        New_matrix_list.append(row_lists)
    return New_matrix_list


#function to print the given matrix in a matrix format
def print_matrix(matrix_list) :
    for i in range(len(matrix_list)) :
        for j in range(len(matrix_list[0])) :
            print(matrix_list[i][j], end=' ')
        print()


#function to multiply 2 matrices if it's given as parameter
def matrix_product(matrix_01,matrix_02) :
    try :                   #to handle the error if anything in this function 
        matrix_output = []
        for j in range(len(matrix_01)):
            row_list = []
            for k in range(len(matrix_02[0])):
                element_val = 0
                for i in range(len(matrix_01[0])):
                    product = matrix_01[j][i] * matrix_02[i][k]
                    element_val += product
                row_list.append(element_val)
            matrix_output.append(row_list)    
                
        return matrix_output

    except :
        print("Error")
        exit()


#calling functions to take inputs and print the matrix multiplication
mat_A , mat_B = get_matrix()
print_matrix(matrix_product(mat_A , mat_B))


'''
mat_file = open("output.txt", 'w')      #open file to print the output matrix
#writing the output matrix row by row
for i in range(len(output_mat)) :
        val = ''
        for j in range(len(output_mat[0])) :
            val += (str(output_mat[i][j]) + ' ')
        val += '\n' 
        mat_file.write(val)

mat_file.close()

'''
