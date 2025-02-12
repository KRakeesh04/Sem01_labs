def is_positive(list :list) :
    for num in list :
        if num >= 0 :
            continue
        else :
            print("check the values")
            return False
    return True


val_input = list(map(float, input("Input stock prices of the week: ").split()))

if is_positive(val_input) == True :
    average_val = sum(val_input) / len(val_input)
    n = 0
    for values in val_input :
        if values > (10 + average_val) :
            n += 1

    print("Number of valued days: ", n)

    if n >= 3 :
        print("RECOMMENDED")
    else :
        print("NOT RECOMMENDED")

else :
    exit()







