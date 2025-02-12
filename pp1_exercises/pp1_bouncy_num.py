def is_increasing(num) :
    for j in range(len(str(num))-1) :
        if num[j] <= num[j+1] :
            continue
        else :
            return False
    return True
            
def is_decreasing(num) :
    for j in range(len(str(num))-1) :
        if num[j] >= num[j+1] :
            continue
        else :
            return False
    return True



num_range = list(map(int, input().split()))
sum_of_bouncy_num = 0
for i in range(num_range[0] , num_range[1]+1) :
    if ( is_increasing(str(i)) == True ) or ( is_decreasing(str(i)) == True ) :
        continue
    else :
        sum_of_bouncy_num += i

print(sum_of_bouncy_num)