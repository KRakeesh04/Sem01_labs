alph_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

def text_balanced(text :str) :
    for j in range(len(text)) :
        if text[j].isalpha() == True :
            #sum of the weight of left side
            L_sum = 0
            for i in range(len(text[:j])) :
                L_sum += ( alph_dict[text[i].lower()] * (i+1) )
                
            #sum of the weight of right side
            R_sum = 0
            for k in range(len(text[j+1:])) :
                R_sum += ( alph_dict[text[k+j+1].lower()] * (k+j) )
            
            if L_sum == R_sum :
                return j, L_sum
            else :
                continue
        else :
            print("check the text")
            exit()
    return False 


text_input = input("Enter the input word: ").strip()

if text_balanced(text_input) == False :
    print("Cannot be balanced!")
else : 
    letter, weight = text_balanced(text_input)
    print("Balance point letter:", '"'+text_input[letter]+'"', "weight=" + str(weight))





