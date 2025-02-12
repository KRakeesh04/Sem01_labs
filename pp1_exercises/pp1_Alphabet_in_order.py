def is_order(text :str) :
    for i in range(len(text)-1) :
        if text[i].isalpha() == False :
            print("check the input text")
            exit()
        elif text[i].isalpha() == True :
            if ord(text[i].lower()) <= ord(text[i+1].lower()) :
                continue
        else :
            return False
    return True

def is_reverse(text :str) :
    for i in range(len(text)-1) :
        if text[i].isalpha() == False :
            print("check the input text")
            exit()
        elif text[i].isalpha() == True :
            if ord(text[i].lower()) >= ord(text[i+1].lower()) :
                continue
        else :
            return False
    return True


text_input = input("Enter word: ").strip()

if is_order(text_input) == True :
    print(text_input, "IN ORDER")
elif is_reverse(text_input) == True :
    print(text_input, "IN REVERSE ORDER")
else :
    print(text_input, "NOT IN ORDER")



