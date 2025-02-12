def shifting(list :list, x :str, y :str, index :int = 0) :
    try :
        X_index = list.index(x,index)
        Y_index = list.index(y,index)
        list[X_index+1], list[Y_index] = list[Y_index], list[X_index+1]
        return shifting(list,x,y,Y_index+1)
    except :
        return list

lst = ['5','3','6','4','6','4','9','5']
print(lst)
print(shifting(lst,'4','5'))



