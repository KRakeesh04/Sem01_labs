def grading(list :list) :
    # [['Maths', '86'], ['Chem', '73'], ['Phy', '71']]
    for i in range(len(list)) :
        if 80 < int(list[i][1]) <= 100 :
            list[i][1] = 'A'
        elif 60 < int(list[i][1]) <= 80 :
            list[i][1] = 'B'
        elif 40  < int(list[i][1]) <= 60 :
            list[i][1] = 'C'
        elif 20 < int(list[i][1]) <= 40 :
            list[i][1] = 'D'
        elif 0 <= int(list[i][1]) <= 20 :
            list[i][1] = 'F'
        else :
            print('Check the marks of',list[i][0] ,'and try again')
            exit()
    list.insert(0, ['Name', 'Grade'])
    return list

def max_len(list :list) :
    # [['Name', 'Grade'], ['Maths', 'A'], ['Chem', 'B'], ['Phy', 'B']]
    n = 0
    for i in range(len(list)-1) :
        if len(list[i][0]) > len(list[i+1][0]) :
            n = len(list[i][0])
        else :
            n = len(list[i+1][0])
        
    return n


def row_input(list :list) :
    # [['Name', 'Grade'], ['Maths', 'A'], ['Chem', 'B'], ['Phy', 'B']]

    # +-------+-------+
    # | Name  | Grade |
    # +-------+-------+
    # | maths | A     |
    # | chem  | C     |
    # | phy   | B     |
    # +-------+-------+
    print('+','-'*(max_len(list)+4), '+', '-'*(len(list[0][1])+4), '+', end='')
    print()
    print('|', list[0][0].rjust(int((max_len(list)+4+len(list[0][0]))/2)).ljust(max_len(list)+4), '|', list[0][1].rjust(2).ljust(len(list[0][1])+4), '|', end='')
    print()
    print('+','-'*(max_len(list)+4), '+', '-'*(len(list[0][1])+4), '+', end='')
    print()

    for i in range(1, len(list)) :
        print('|', list[i][0].rjust(int((max_len(list)+4+len(list[i][0]))/2)).ljust(max_len(list)+4) ,'|', list[i][1].rjust(2).ljust(len(list[0][1])+4) , '|', end='')
        print()
    
    print('+','-'*(max_len(list)+4), '+', '-'*(len(list[0][1])+4), '+', end='')
    print()


no_of_entry = int(input())
entry_list = []
for entry in range(no_of_entry) :
    entry_list.append(input().split())

list_with_grading = grading(entry_list)
row_input(list_with_grading)

print(max_len(entry_list))



# + ----------------------------------- + --------- +
# |              Name                   | Grade     |
# + ----------------------------------- + --------- +
# |             Maths                   |  A        |
# |         Chemistry                   |  B        |
# | Physichgjjhbjbhghbvgfhvnjyjghbs     |  B        |
# + ----------------------------------- + --------- +