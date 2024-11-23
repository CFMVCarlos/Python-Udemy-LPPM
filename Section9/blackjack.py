import random
import tkinter


def load_images(card_image):
    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]

    if tkinter.TkVersion >= 8.6:
        extension = "png"
    else:
        extension = "ppm"

    # For each suit, retrieve the image for the cards
    for suit in suits:
        # First the number cards 1 to 10
        for card in range(1, 11):
            name = f"Section9/cards/{card}_{suit}.{extension}"
            image = tkinter.PhotoImage(file=name)
            card_image.append(
                (
                    card,
                    image,
                )
            )

        # Next the face cards
        for card in face_cards:
            name = f"Section9/cards/{card}_{suit}.{extension}"
            image = tkinter.PhotoImage(file=name)
            card_image.append(
                (
                    10,
                    image,
                )
            )


def _deal_card(frame):
    # Pop the next card off the top of the deck
    next_card = deck.pop()
    # And add it to the back of the pack
    deck.insert(0, next_card)
    # Add the image to a label and display the label
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    # Now return the card's face value
    return next_card


def score_hand(hand):
    # Calculate the total score of all cards in the list
    # Only one ace can have the value 11, and this will be reduced to 1 if the hand would bust
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # If we would bust, check for an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    global player_stay_decision
    player_stay_decision = True
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(_deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
    else:
        result_text.set("Draw!")


def deal_player():
    if player_stay_decision:
        return
    player_hand.append(_deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer wins!")

    # global player_score, player_ace
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     card_value = 11
    #     player_ace = True
    # player_score += card_value
    # # If we would bust, check for an ace and subtract 10
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Dealer wins!")


def initial_deal():
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def new_game():
    global dealer_card_frame, player_card_frame, dealer_hand, player_hand, player_stay_decision
    player_stay_decision = False
    # Embedded frame to hold the results
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    result_text.set("")

    # Create the list to store the dealer's and player's hands
    dealer_hand = []
    player_hand = []

    initial_deal()


def shuffle_deck():
    random.shuffle(deck)


def play_blackjack():
    global deck, card_frame, dealer_card_frame, player_card_frame, result_text, dealer_score_label, player_score_label, player_stay_decision

    main_window = tkinter.Tk()

    # Set up the screen and frames for the dealer and player
    main_window.title("Blackjack")
    main_window.geometry("640x480")
    main_window.configure(background="green")

    result_text = tkinter.StringVar()
    result = tkinter.Label(main_window, textvariable=result_text)
    result.grid(row=0, column=0, columnspan=3)

    card_frame = tkinter.Frame(
        main_window, relief="sunken", borderwidth=1, background="green"
    )
    card_frame.grid(row=1, column=0, sticky="ew", rowspan=2, columnspan=3)

    dealer_score_label = tkinter.IntVar()
    tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(
        row=0, column=0
    )  # Dealer label
    tkinter.Label(
        card_frame, textvariable=dealer_score_label, background="green", fg="white"
    ).grid(
        row=1, column=0
    )  # Dealer score

    # Embedded frame to hold the results
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)
    player_score_label = tkinter.IntVar()
    # player_score = 0
    # player_ace = False
    player_stay_decision = False
    tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(
        row=2, column=0
    )  # Player label
    tkinter.Label(
        card_frame, textvariable=player_score_label, background="green", fg="white"
    ).grid(
        row=3, column=0
    )  # Player score

    # Embedded frame to hold the card images
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    button_frame = tkinter.Frame(main_window)
    button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

    tkinter.Button(button_frame, text="Stay", command=deal_dealer).grid(row=0, column=0)

    tkinter.Button(button_frame, text="Hit", command=deal_player).grid(row=0, column=1)

    tkinter.Button(button_frame, text="New Game", command=new_game).grid(
        row=0, column=2
    )

    tkinter.Button(button_frame, text="Shuffle", command=shuffle_deck).grid(
        row=0, column=3
    )

    # Load cards
    cards = []
    load_images(cards)

    # Create a new deck of cards and shuffle them
    number_of_decks = 3
    deck = list(cards) * number_of_decks
    shuffle_deck()

    # Create the list to store the dealer's and player's hands
    dealer_hand = []
    player_hand = []

    new_game()

    main_window.mainloop()


if __name__ == "__main__":
    play_blackjack()
