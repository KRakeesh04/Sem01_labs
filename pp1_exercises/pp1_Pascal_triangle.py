n = int(input('Enter n (height of the triangle) :'))
if n == 1 :
    triangle_list = [[1]]
elif n == 2 :
    triangle_list = [[1], [1, 1]]

# n=5
# [ [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1] ]
elif 2 < n < 50 :
    triangle_list = [[1], [1, 1]]
    for i in range(1,n-1) :
        nested_list = [1]
        for k in range(len(triangle_list[i])-1) :
            nested_list.append(triangle_list[i][k] + triangle_list[i][k+1]) 
        
        if len(nested_list) > 1 :
            nested_list.append(1)
        triangle_list.append(nested_list)
else :
    print('check the n ')


   #print(triangle_list)

row_list = []
for row in range(len(triangle_list)) :
    rows = ''
    for element in range(len(triangle_list[row])) :
        rows += (str(triangle_list[row][element]) + ' '*(n+2))
    row_list.append(rows)

   #print(row_list)
for line in row_list :
    print(line.center(len(row_list[n-1])))

