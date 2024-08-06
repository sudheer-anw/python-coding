import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Calculates the score from the list of cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

while True:
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0:
        print("Blackjack! You win!")
        break
    elif computer_score == 0:
        print("Computer has Blackjack! You lose.")
        break
    elif user_score > 21:
        print("You went over. You lose.")
        break

    while input("Type 'y' to get another card, 'n' to pass: ") == 'y':
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")

        if user_score == 0:
            print("Blackjack! You win!")
            break
        elif user_score > 21:
            print("You went over. You lose.")
            break

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if computer_score > 21 or (user_score <= 21 and user_score > computer_score):
        print("You win!")
    elif user_score == computer_score:
        print("It's a draw.")
    else:
        print("You lose.")
    break

        
    

