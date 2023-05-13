import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def blackJack():
    is_blackjack_finished = False
    computer = [random.choice(cards),random.choice(cards)]
    person = [random.choice(cards),random.choice(cards)]
    score_person = sum(person)
    print(f"This is your cards : {person} , your current score = {score_person}")
    print(f"And computer's first card : {computer[0]}")
    if score_person > 21:
        score_person = 21
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    while not is_blackjack_finished:
        ask = input("Type 'y' to get another card, type 'n' to pass: ")
        if ask == 'y':
            person.append(random.choice(cards))
            score_person = sum(person)
            score_computer = sum(computer)
            print(f"This is your cards : {person} and your final hand = {score_person}")
            print(f"Computer's cards: {computer} and computer's final hand = {score_computer}")
            if score_person > 21:
                print("You went over, you lose ")
                is_blackjack_finished = True
                return 0
            elif score_computer < 21:
                computer.append(random.choice(cards))
            elif score_person == score_computer:
                print("It is Draw")
            elif score_person > score_computer:
                print("Congratulations...You won :D") 
            elif score_computer > score_person: 
                print("Computer wins...")
            elif score_computer > 21:
                print("Computer went over.. You won :D") 

        elif ask == 'n':
            score_person = sum(person)
            score_computer = sum(computer)
            print(f"This is your cards : {person} and your final hand = {score_person}")
            print(f"Computer's cards: {computer} and computer's final hand = {score_computer}")
            is_blackjack_finished = True
            if score_person > score_computer:
                print("Congratulations...You won :D") 
            elif score_computer > 21:
                print("Computer went over.. You won :D")

            elif score_computer == score_person:
                print("It is Draw")
            else: 
                print("Computer wins... You lose.. Better luck next time)") 
            
        else:
            print("You have entered invalid symbol. Sorry :(")

blackJack()


