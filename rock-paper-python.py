# A little ROCK, PAPER, SCISSORS game in python.
# Nice ideas would be a randomized computer choice and a best of 3 mode, where you can restart afterwards and play again.

computer_choice = 'rock'
user_choice = raw_input("Enter rock, paper, or python:\n")
win_statement = "The computer chose " + computer_choice + ". You WIN! :D"

if computer_choice == user_choice:
    print("The computer chose " + computer_choice + " too! It's a TIE")
elif user_choice == "rock" and computer_choice == "python":
    print(win_statement)
elif user_choice == "paper" and computer_choice == "rock":
    print(win_statement)
elif user_choice == "python" and computer_choice == "paper":
    print(win_statement)
else:
    print("The computer always chooses " + computer_choice + ". You lose! :(")
