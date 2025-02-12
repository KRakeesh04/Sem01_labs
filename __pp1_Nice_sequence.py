input_sequence = list(map(int, input("Enter the sequence: ").split()))


# case 01
if 2 <= len(input_sequence) < 4 :
    for i in range(0, len(input_sequence)-2, 2) :
        is_niced = True
        if input_sequence[i] < input_sequence[i+1] and input_sequence[i+1] > input_sequence[i+2] :
            continue
        else :
            is_niced = False
            break

    if is_niced == True :
        print("Result: nice")
    else :
        print("Result: not nice")

# case 02
elif 4 <= len(input_sequence) <= 9 :
    for i in range(0, len(input_sequence), 2) :
        is_niced = True
        if input_sequence[i] < input_sequence[i+1] and input_sequence[i+1] > input_sequence[i+2] :
            continue
        else :
            is_niced = False
            break

    if is_niced == True :
        print("Result: nice")
    else :
        print("Result: not nice")
else :
    print("sequence length should be between 2 to 9")
    exit()


