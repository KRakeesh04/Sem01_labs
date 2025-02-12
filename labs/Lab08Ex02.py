INPUT_FILE_NAME = input()
########################################################################################
# Do not change anything above this line
########################################################################################

# Use INPUT_FILE_NAME variable to read the file instead of 'matrix_data.txt'
# Enter your code here

#function to read the input file and order the input in a list and call function to output the matrix
def read_mat(name :str) :
    file = open(name, 'r')
    mat_data = file.read()
    file.close

    if mat_data[-1] == '\n' :
        mat_data = mat_data[:-1]
    mat_data_list = mat_data.split('\n')
    matrix_count = mat_data_list[0]
    index = 0
    for count in range(1,int(matrix_count)+1) :
        index += 1
        mat_out = []
        for row in range(1,int(mat_data_list[index])+1) :
            mat_out.append(list(map(int, mat_data_list[index+1].split(','))))
            index += 1
        #calling function to output the results
        final_output(mat_out, count)



#function to calculate and print the output matrix
def final_output(mat :list, count :int) :
    print("Inverse of Matrix", str(count)+':')
    adj_mat = Adjoint_of_Matrix(mat)
    output_mat = mat_Inverse(adj_mat,mat)
    printing_matrix(output_mat)         #printing final outputs



#function for find the minor matrix , if the coloum and row number is given 
def minor(matrix :list, i :int, j :int) :
    minor_mat = []
    for row_j in range(len(matrix)):
        rows = []
        for colm_j in range(len(matrix[0])):
            if ((row_j) != i) and ((colm_j) != j) :
                rows.append(matrix[row_j][colm_j])
        if rows != [] :
            minor_mat.append(rows)
    return minor_mat



#function to calculate the adjoint of a matrix and return that adjointed matix in a 2-D list
def Adjoint_of_Matrix(matrix :list) :
    co_fac_mat = []
    if len(matrix) == 2 :           #if it's a 2x2 matrix, then give a special known format for co-factor matrix
        co_fac_mat =[[matrix[1][1], (-1)*matrix[1][0]], [(-1)*matrix[0][1], matrix[0][0]]]
    else :                              #if not, then use the co-factor equation to find the co-factor matrix
        for row_k in range(len(matrix)):
            row = []
            for col_k in range(len(matrix[0])):
                det = mat_Determinant(minor(matrix,row_k,col_k))
                co_fac = ((-1)**(row_k + col_k + 2)) * det
                row.append(co_fac)
            co_fac_mat.append(row)
    adj_mat = transpose_matrix(co_fac_mat)      #change the co-factor matrix to adjoint matrix by using transpose function
    return  adj_mat



#funtion to calculate the determinant of a matrix
def mat_Determinant(matrix :list) :
    #if the matrix is 2x2, then use the known format for the determinant
    if len(matrix) == 2 :       
        det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    #to reduce time to run the code
    elif len(matrix) == 3 :     #if the matrix is 3x3, then use the known format for the determinant
        det = matrix[0][0] * ((matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1])) - matrix[0][1] * ((matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0]))  + matrix[0][2] * ((matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0]))
    #if not, find determinant using minor and reduce to 3x3 matrix 
    else :       
        det = 0
        for col_k in range(len(matrix[0])):
            x = mat_Determinant(minor(matrix,0,col_k))
            det += ( matrix[0][col_k] * ( (-1)**((1 +(col_k+1))) ) * x )
    return det



#function to find the inverse by divide the adjoint matrix with the determinant of the matrix
def mat_Inverse(adj_matrix :list, matrix :list) :
    inv_mat = []
    for irow in range(len(adj_matrix)):
        row = []
        for icolm in range(len(adj_matrix[0])):
            if adj_matrix[irow][icolm] == 0 :       #the entry value is 0, then skip the division part
                row.append( adj_matrix[irow][icolm])
            else :
                row.append( adj_matrix[irow][icolm] / mat_Determinant(matrix) )
        inv_mat.append(row)
    
    return  inv_mat 



#function to change to transpose of a given matrix
def transpose_matrix(matrix :list) :
    matrix_list = []
    for j in range(len(matrix[0])) :
        row_lists = []
        for i in range(len(matrix)) :
            row_lists.append(matrix[i][j])
        matrix_list.append(row_lists)
    return matrix_list



#function to print 2-D list like a matrix 
def printing_matrix(mat :list) :
    for i in range(len(mat)):
        for element in mat[i] :
            print("".join(f"{element:7.2f}" ), end='')        #printing the inverse matrix with the given format
        print()




#main programme to take input file name and call all the defined function to find the inverse of the matrices
read_mat(INPUT_FILE_NAME)







