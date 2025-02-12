def is_shuffle(word, word_03) :
    count = 0
    for i in word :
        is_shuffled = True
        while len(word_03) > count :
                if i == word_03[count] :
                    is_shuffled = True
                    break
                else :
                    is_shuffled = False
                    count += 1
                    continue
        if is_shuffled == True :
            continue
        else:
            return is_shuffled

    return is_shuffled


word_01 = input('Enter word 01 : ').strip()
word_02 = input('Enter word 02 : ').strip()
word_03 = input('Enter word 03 : ').strip()


if word_01.isalpha() and word_02.isalpha() and word_03.isalpha() :
    if (word_01 in word_03) and (word_02 in word_03) :
        print("NOT A SHUFFLE")
    elif ( is_shuffle(word_01, word_03) == True ) and ( is_shuffle(word_02, word_03) == True ) :
        print("SHUFFLE")
    else :
        exit()
else :
    print("words should be alphabets")




