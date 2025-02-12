U_range = int(input("Enter Input: "))

rewards = []
for nGS in range(1,U_range+1) :
    is_rewarded = True 
    for i in range(2,11) :
        if nGS%i != 0 :
            continue
        else :
            is_rewarded = False
            break
    if is_rewarded == True :
        rewards.append(nGS)
    else :
        continue
    
print("Number of rewards:", len(rewards))









