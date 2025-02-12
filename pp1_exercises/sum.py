def add(list) :
    if len(list[1:]) == 1 :
        total = list[0] + list[1]
        return total
    else:
        total = list[0] + add(list[1:])
        return total



list = [0,1,2,3,4,5,6,7,8,9]

print(add(list))
