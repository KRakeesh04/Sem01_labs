marks_list = []
for i in range(4) :                 #To get 4 different user inputs for the programme
    marks_list.append(list(map(int,input().split())))       #change the inputs into integers and add them to a 2D-list while getting input

for j in range(4) :         #To print the 4 ouputs(total marks and average marks) seperately
    total = sum(marks_list[j])      #calcute the sum of the nested list
    average = round(total/3, 1)     #calculate and round off the average value to one decimal point
    print("Total:",total,"Average:",average)

    
