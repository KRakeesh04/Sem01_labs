def is_lower_triangular(matrix :list) :
    for i in range(len(matrix)) :
        for j in range(i+1, len(matrix[0])) :
            if matrix[i][j] != 0 :
                return False
            else :
                continue
    return True

def is_upper_triangular(matrix :list) :
    for i in range(len(matrix)) :
        for j in range(i) :
            if matrix[i][j] != 0 :
                return False
            else :
                continue
    return True

def is_diagonal(matrix :list) :
    if is_lower_triangular(matrix) == True and is_upper_triangular(matrix) == True :
        return True
    else :
        return False


dimension = int(input("Enter N (size of matrix) : "))
print("Enter the matrix :")
matrix_list = []
if dimension <= 8 :
    for i in range(dimension) :
        try :
            row = list(map(int, input().split()))
            matrix_list.append(row)
        except :
            print("Invalid matrix")
            exit()

    
    if is_diagonal(matrix_list) :
        print(3)
    elif is_lower_triangular(matrix_list) == True :
        print(2)
    elif is_upper_triangular(matrix_list) == True :
        print(1)
    else :
        print(4)
            

else :
    print("Invalid dimension (dimension <= 8)")
    exit()


