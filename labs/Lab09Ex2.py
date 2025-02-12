from cs1033_evaluator import evaluate_lab9

################################################################################
# Do not change anything above this line
################################################################################

# Enter your code here
# Use INPUT_FILE_NAME variable to read the file instead of 'contamination_analysis.txt'


#function to read data from input file and return a 2-D dictionary using the file data
def read_file(filename :str) :
    file = open(filename, 'r')
    file_data = file.readlines()
    file.close()

    input_data_list = [ ]
    for data in file_data :         #to remove the '\n' and split the data into chemical name and chemical compound
        if data[-1] == '\n' :
            data = data.replace("\n", '')
        input_data_list.extend(data.split())
    input_data_dict = { }
    for index in range(0,len(input_data_list)-1,2) :        #creating 2D dictionary using the data
        val = input_data_list[index+1].strip().split('-')   #splitting chemical compounds 
        dictionary = { }
        for i in val :
            try :
                elem_count = int(i[-1])
            except ValueError :         #add element count 1 for some single elements like one Mg or one Na 
                i = i + '1'
                elem_count = 1
            if i[:-1] not in dictionary :       
                dictionary[i[:-1]] = elem_count
            else :                                  #if there's an element already in the dict then add the count with the old count
                dictionary[i[:-1]] += elem_count
        input_data_dict[input_data_list[index]] = dictionary
    
    return input_data_dict


#function to delete some elements from an existing dictionary
def leftover(start_elements :dict, used_elements :dict) :
    if start_elements == False or used_elements == False :
        return False
    else :
        start_elements = start_elements.copy()
        for element in used_elements :
            if element in start_elements :
                start_elements[element] -= used_elements[element]
            else :
                return False
        return start_elements

#function to check the data which is belongs to level 1
def isLevel_1(data :dict) :
    if data == False :
        return False
    elif ('S' in data) and ('O' in data) and ('Na' in data) :
        if (data['S'] >= 1) and (data['O'] >= 4) and (data['Na'] >= 1) :
            return True
        else :
            return False
    else :
        return False

#function to check the data which is belongs to level 2
def isLevel_2(data :dict) :
    if data == False :
        return False
    elif ('S' in data) and ('O' in data) and ('Mg' in data) :
        if (data['S'] >= 1) and (data['O'] >= 3) and (data['Mg'] >= 1) :
            return True
        else :
            return False
    else :
        return False

#function to check the data which is belongs to level 3
def isLevel_3(data :dict) :
    if data == False :
        return False
    elif ('O' in data) and ('Cl' in data) :
        if (data['O'] >= 2) and (data['Cl'] >= 3) :
            return True
        else :
            return False
    else :
        return False

#function to check the data have 3 no. of levels
def have_3_levels(data :dict) :
    dict_1 = {'S':1, 'O':4, 'Na':1}
    dict_2 = {'S':1, 'O':3, 'Mg':1}
    dict_3 = {'O':2, 'Cl':3}
    if isLevel_1(data)   and   isLevel_2(leftover(data,dict_1))   and  isLevel_3(leftover(leftover(data,dict_1),dict_2))  :
        return True
    elif isLevel_1(data)   and   isLevel_2(leftover(leftover(data,dict_1),dict_3))   and  isLevel_3(leftover(data,dict_1))  :
        return True
    elif isLevel_1(leftover(data,dict_2))   and   isLevel_2(data)   and  isLevel_3(leftover(leftover(data,dict_2),dict_1))  :
        return True
    elif isLevel_1(leftover(leftover(data,dict_2),dict_3))   and   isLevel_2(data)   and  isLevel_3(leftover(data,dict_2))  :
        return True
    elif isLevel_1(leftover(data,dict_3))   and   isLevel_2(leftover(leftover(data,dict_3),dict_1))   and  isLevel_3(data)  :
        return True
    elif isLevel_1(leftover(leftover(data,dict_3),dict_2))   and   isLevel_2(leftover(data,dict_3))   and  isLevel_3(data)  :
        return True
    else :
        return False
    
#function to check the data have 2 no. of levels
def have_2_levels(data :dict) :
    dict_1 = {'S':1, 'O':4, 'Na':1}
    dict_2 = {'S':1, 'O':3, 'Mg':1}
    dict_3 = {'O':2, 'Cl':3}
    if isLevel_1(data) and isLevel_2(leftover(data,dict_1)) :
        return True
    elif isLevel_1(leftover(data, dict_2)) and isLevel_2(data) :
        return True
    elif isLevel_2(data) and isLevel_3(leftover(data,dict_2)) :
        return True
    elif isLevel_2(leftover(data,dict_3)) and isLevel_3(data) :
        return True
    elif isLevel_1(data) and isLevel_3(leftover(data,dict_1)) :
        return True
    elif isLevel_1(leftover(data,dict_3)) and isLevel_3(data) :
        return True
    else :
        return False

#function to check the data which is belongs to level 4
def isLevel_4(data :dict) :
    if  have_3_levels(data)  or   have_2_levels(data)  :
        return True
    else :
        return False

#function to check the data which is belongs to level 0
def isLevel_0(data :dict) :
    if (not isLevel_3(data)) and (not isLevel_2(data)) and (not isLevel_1(data)) :
        return True
    else :
        return False
    
#function to find out the levels and return the level name
def find_out_Levels(datas :dict) :
    if isLevel_0(datas) == True :
        return "Level_0"
    elif isLevel_4(datas) == True :
        return "Level_4"
    elif isLevel_1(datas) == True :
        return "Level_1"
    elif isLevel_2(datas) == True :
        return "Level_2"
    elif isLevel_3(datas) == True :
        return "Level_3"

 
#function to write final outputs to the output files
def write_on_file(data_collections :dict) :
    file_0 = open("Level_0.txt",'w')
    file_1 = open("Level_1.txt",'w')
    file_2 = open("Level_2.txt",'w')
    file_3 = open("Level_3.txt",'w')
    file_4 = open("Level_4.txt",'w')
    for data in data_collections :
        value = data_collections[data]
        level = find_out_Levels(value)
        if level == "Level_0" :
            file_0.write(data + '\n')
        elif level == "Level_1" :
            file_1.write(data + '\n')
        elif level == "Level_2" :
            file_2.write(data + '\n')
        elif level == "Level_3" :
            file_3.write(data + '\n')
        elif level == "Level_4" :
            file_4.write(data + '\n')

    file_0.close()
    file_1.close()
    file_2.close()
    file_3.close()
    file_4.close()
        

#main programme to call the functions to run the code
INPUT_FILE_NAME = input()
write_on_file(read_file(INPUT_FILE_NAME))




################################################################################
# Do not change anything below this line.
evaluate_lab9()