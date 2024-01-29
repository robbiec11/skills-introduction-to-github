#add the below code to a function called play_game
# print 'welcome to rock, paper, scissors'
# print 'please enter paper, rock, or scissors'
# read the user's input
# store the user's input in a variable
# print the user's input
# generate a random number between 0 and 2
# store the random number in a variable
# print the random number
# if the random number is 0, set the computer's choice to paper
# if the random number is 1, set the computer's choice to rock
# if the random number is 2, set the computer's choice to scissors
# print the computer's choice
# if the user wins, increment the user's score
# if the computer wins, increment the computer's score
# print the user's score
# print the computer's score
# initialize a list to store the user's choice and the computer's choice
# append the user's choice to the list
# append the computer's choice to the list
# print the list
# if the user's score is 3, end the game
# if the computer's score is 3, end the game
# if the game has ended, print the winner
# if the game has ended, print the list of choices
# if the game has ended, print the user's score
# if the game has ended, print the computer's score
# if the game has ended, print 'game over'
# create a pythin function called play_game
# call the play_game function
# Path: app.py
# create a python function called play_game
# call the play_game function

# Path: app.py

user_score = 0

computer_score = 0

def play_game():
    print('welcome to rock, paper, scissors')
     # define  user_score and  computer_score
    global user_score
    global computer_score
    user_choice = input('please enter paper, rock, or scissors: ')
    print(user_choice)
    import random
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        computer_choice = 'paper'
    elif computer_choice == 1:
        computer_choice = 'rock'
    elif computer_choice == 2:
        computer_choice = 'scissors'
    print(computer_choice)

    if user_choice == computer_choice:
        print('it\'s a tie')    
    elif user_choice == 'paper' and computer_choice == 'rock':
        print('you win')
        user_score += 1
    elif user_choice == 'paper' and computer_choice == 'scissors':
        print('you lose')
        computer_score += 1
    elif user_choice == 'rock' and computer_choice == 'paper':
        print('you lose')
        computer_score += 1
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print('you win')
        user_score += 1
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print('you win')
        user_score += 1
    elif user_choice == 'scissors' and computer_choice == 'rock':
        print('you lose')
        computer_score += 1
    else:
        print('invalid choice')
        

    print('user score: ' + str(user_score))
    print('computer score: ' + str(computer_score))
    choices = []
    choices.append(user_choice)
    choices.append(computer_choice)
    print(choices)
    if user_score == 3:
        print('you win')
        print('game over')
    elif computer_score == 3:
        print('you lose')
        print('game over')
    else:
        play_game()

play_game()