def is_leapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def convert_to_nic(name_detail) :
    name = name_detail.split(' ')
    name[1] = name[1].split('-')
    # name = ['Saman', ['1990', '05', '03'], 'M']
    months = {1:'31', 2:'28', 3:'31', 4:'30', 5:'31', 6:'30', 7:'31', 8:'31', 9:'30', 10:'31', 11:'30', 12:'31'}
    gender = {"M":'001', "F":'002'}
    
    day_count = 0
    for i in range(1,int(name[1][1])) :
        day_count += int(months[i])

    if is_leapYear(int(name[1][0])) :
        day_count += 1  

    if name[2] == 'M':
        day_count += int(name[1][2])
        nic_num = name[1][0] + str(day_count).rjust(3,'0') + gender['M']
    elif name[2] == 'F' :
        day_count += (int(name[1][2]) + 500)
        nic_num = name[1][0] + str(day_count).rjust(3,'0') + gender['F']
    else :
        print(name_detail)
        exit()

    print(name[0], nic_num)



file = open("name_details.txt", "r")
file_details = file.readlines()
file.close()

for j in file_details :
    j = j.replace("\n", '')
    convert_to_nic(j)

print('''Saman 1990123001
Aruni 1990596002
Kumaran 1988065001
Nazar 1997267001
''')
