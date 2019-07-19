import random
import os
import sys

while True:
    selection = input("U: To Play\nQ: To Quit\nYour Choice: ")
    if selection is "Q" or selection is "q":
        print("Quitting")
        sys.exit()
    if selection is "U" or selection is "u":
        print("Playing")
    elif selection != "U" or "u" or "Q" or "q":
        print("Not valid input")
    def calc_hand(hand):

        non_aces = [card for card in hand if card != 'A']
        aces = [card for card in hand if card == 'A']

        sum = 0

        for card in non_aces:
            if card in 'JQK':
                sum += 10
            else:
                sum += int(card)          

        for card in aces:
                if sum <= 10:
                    sum += 11
                else:
                    sum += 1
        return sum
        
    while True: # While Loop is true, need random shuffled cards from the LIST
        cards = [
        '2','3','4','5','6','7','8','9','10','J','Q','K','A',
        '2','3','4','5','6','7','8','9','10','J','Q','K','A',
        '2','3','4','5','6','7','8','9','10','J','Q','K','A',
        '2','3','4','5','6','7','8','9','10','J','Q','K','A',
        ]

        random.shuffle(cards) # The lists that the program will use to store the info for Dealer and Player

        dealer = []
        player = []

        player.append(cards.pop())
        dealer.append(cards.pop())
        player.append(cards.pop())
        dealer.append(cards.pop())

        # Variable for the stop of adding or removing cards
        standing = False
        # Variable if the users first hand is 21, then its blackjack
        first_hand = True

        # While Loop for the main function of playing the BJ Hands, calculating score, and user inputs
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            player_score = calc_hand(player)
            dealer_score = calc_hand(dealer)

            if standing:
                print('Dealer Cards: [{}] ({})'.format(']['.join(dealer), dealer_score))
            else:
                print('Dealer Cards: [{}][?]'.format(dealer[0]))
            print ('Your Cards:    [{}] ({})'.format(']['.join(player), player_score))
            print ('')

            if standing:
                if dealer_score > 21:
                    print('Dealer busted, you won!')
                elif player_score == dealer_score:
                    print('You Pushed')
                elif player_score > dealer_score:
                    print('You beat the dealer, winnnnnnner winner!')
                else:
                    print('You are a loser')
                print('')
                input('Play again? Hit enter to continue')
                break

            if first_hand and player_score == 21:
                print('Blackjack! 21!')
                print('')
                input('Play again? Hit enter to continue')
                break

            if player_score > 21:
                print('You busted, you are a loser!')
                print('')
                input('Play again? Hit enter to continue')
                break

            print('What would you like to do?')
            print(' [1] Hit')
            print(' [2] Stand')

            print('')
            choice = input('Your choice: ')
            print('')

            first_hand = False

            if choice == '1':
                player.append(cards.pop())
            elif choice == '2':
                standing = True
                while calc_hand(dealer) <= 16:
                        dealer.append(cards.pop())