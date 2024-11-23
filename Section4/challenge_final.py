choice = -1
while choice != 0:
    if 1 <= choice <= 5:
        print(f"You have chosen option {choice}.")

    else:
        print(
            "Please choose your option from the list below: \
        \n1.\tLearn Python \
        \n2.\tLearn Java \
        \n3.\tGo swimming \
        \n4.\tHave dinner \
        \n5.\tGo to bed \
        \n0.\tExit"
        )
    choice = int(input())
else:
    print("Goodbye.")
