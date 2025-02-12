dealer_input = input().split()
player_input = input().split()

card_val = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
four_suits = ['D', 'S', 'H', 'C']


# player's card details
P_card_val = 0
for j in range(len(player_input)) :
    if player_input[j][0]  in four_suits :
        P_card_val += card_val[player_input[j][1]]
    else :
        print('Check the cards shape of the input : ', j)
        exit()

# dealer's card details
# ['HA', 'D5', 'C5']
D_card_val = 0
for i in range(len(dealer_input)-1) :
    if dealer_input[i][0]  in four_suits :
        D_card_val += card_val[dealer_input[i][1]]
    else :
        print('Check the cards shape of the input : ', i)
        exit()

# Cases for won, lost and hit
if D_card_val == 21 and P_card_val == 21 :
    if dealer_input[2][0]  in four_suits :
        D_card_val += card_val[dealer_input[2][1]]
        if D_card_val == 31 :
            print('Hit')
        else:
            print('Won')
    else :
        print('Check the cards shape of the input : ', i)
        exit()

elif D_card_val != 21 and P_card_val == 21 :
    if dealer_input[2][0]  in four_suits :
        D_card_val += card_val[dealer_input[2][1]]
        if D_card_val == 31 or D_card_val == 21:
            print('Hit')
        else :
            print('Won')
    else :
        print('Check the cards shape of the input : ', i)
        exit()

elif D_card_val != 21 and P_card_val != 21 :
    if dealer_input[2][0]  in four_suits :
        D_card_val += card_val[dealer_input[2][1]]
        if D_card_val == 31 or D_card_val == 21 :
            print('Lost')
        elif D_card_val > 21 :
            print('Won')
        else :
            if D_card_val > P_card_val :
                print('Hit')
            else :
                print('Won')
    else :
        print('Check the cards shape of the input : ', i)
        exit()



