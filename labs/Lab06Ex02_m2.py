from datetime import datetime

def days_to_birthday(date):
    '''
    Calculates the number of days that have passed since the 1st of January 
    to the given date.

    :param date: A date string in the format of yyyy-mm-dd
    :return: The number of days to the date from 1st of January 
             (eg: date->2021-01-01, return->1)
    '''

    # Convert the date string to a datetime object
    datetime_object = datetime.strptime(date, "%Y-%m-%d")

    # Extract only the date and remove the timestamp
    date = datetime_object.date()

    # Find the number of days since the begining of the year
    num_days = date.timetuple().tm_yday

    return num_days


# Please do not edit anything above this line.
################################################################################ 

# Your code should be included here. 
# You may use the days_to_birthday(date) function in your solution.



#function to return the first 7 digits of the nic num if the details is given
def convert_to_nic(name_detail):
    name = name_detail.split(' ')
    global date_list            #to use this variable in the main programme with this same name
    date_list = name[1].split('-')

    day_count = days_to_birthday(name[1])   #calling the function to count the days  until the birthday from "jan 01"
    #adding 500 to the days count to birthday if the person is a female
    if name[2] == 'M':
        nic_num = date_list[0] + str(day_count).rjust(3,'0')
    elif name[2] == 'F' :
        day_count += 500
        nic_num = date_list[0] + str(day_count).rjust(3,'0')
    else :
        exit()
    
    nic_ = [name[0], nic_num]
    return nic_

#get user input of the file name and read the texts on the file
file_name = input()
file = open(file_name , "r")
file_details = file.readlines()
file.close()

Dict_year = { }     #dict to count the no. of people born in a year for the usage to form last 3 digits of the nic

#create a file to write the outputs and save
out_file = open("output.txt" , 'w')
for j in file_details :
    j = j.replace("\n", '')
    nic_detail = convert_to_nic(j)
    year = date_list[0]
    #creating last 3 digits of the nic using the above dictionary named "Dict_year"
    if year not in Dict_year :
        Dict_year[year] = 1
    else :
        Dict_year[year] += 1
    entry = nic_detail[0] + ' ' + nic_detail[1] + str(Dict_year[year]).rjust(3, '0') + '\n'
    out_file.write(entry)

out_file.close()




