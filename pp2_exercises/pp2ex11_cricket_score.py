with open('pp2ex11_input.txt','r') as input :
    data = []
    for line in input:
        data.append(line.split())
    # Name          Dots    Ones    Twos    Threes  Fours   Sixes
    # SureshRaina   720     521     120        5    25      62
    with open('pp2ex11_output.txt', 'w') as output_val :
        for i in range(1,len(data)):
            name = data[i][0]
            score = 0
            for j in range(2,len(data[i])) :
                #print(j,score)
                if j == 6 :
                    score += int(data[i][j]) * j
                else :
                    score += (int(data[i][j])* (j-1))
            
            output = f"{name} {score}"
            output_val.write(output + '\n')
            print(output)

