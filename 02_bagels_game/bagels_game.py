import random
# Set up the ruser_number_listes of the game
def description():
    print("""Bagels, a deductive logic game.
From Al Sweigart's Big book of small projects - My version of code.
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
Pico         One digit is correct but in the wrong position.
Fermi        One digit is correct and in the right position.
Bagels       No digit is correct.""")

# Generate the secret number the user needs to guess
def number_generator():
    secret_number=random.randint(100,999)
    print('''I have thought up a number.
You have 10 guesses to get it.''')
    return(str(secret_number))

# Get input (user's guess number)
def get_input():
    user_number=input('Type your guess: ')
    return(user_number)

# Split a given 3-digit number on individual digits
# Take care of input with one or two digits by converting it in 3 digit format
def number_parsing(n):
    l=[]
    k=len(n)
    while k<3:
        l.append('0')
        k=k+1
    for symbol in n:
        l.append(symbol)
    return(l)  

# Compare digits in the user input vs digits in the secret number
def input_analyser(user_number_list,secret_number_list):
    match_list=[]
    for n in range (0,3):
        for m in range(0,3):
            if user_number_list[n]==secret_number_list[m] and n==m:
                a='Yes'
            elif user_number_list[n]==secret_number_list[m]:
                a='Just about'
            else:
                a='No'
            match_list.append(a)
    return(match_list)

# Give user a hint (Fermi/Pico/Bagels)
def hint_generator(l):
    n=0
    while n<=6:
        if 'Yes' in l[n:n+3]:
            print('Fermi', end=' ')
        elif 'Just about' in l[n:n+3]:
            print('Pico', end=' ')
        n=n+3  
    if len(set(l))==1:
        print('Bagels', end=' ')

# Ask user if he wants to play another game
def new_game_starter():
    ng=input('Wouser_number_listd you like to start a new game? y/n: ')
    if ng.lower().strip()=='y':
        return True
    else:
        print("It was fun to play with you!")
        return False

description()
new_game=True
while new_game==True:
    secret_number=number_generator()
    secret_number_list=number_parsing(secret_number)
    correct_guess='False' 
    attempts=10
    while attempts>0:
        print(f"\nGuess number {11-attempts}")
        user_number=get_input()
        user_number_list=number_parsing(user_number)
        if user_number_list==secret_number_list:
            print('You got it!')
            correct_guess='True'
            break
        else:
            match_list=input_analyser(user_number_list,secret_number_list)
            hint_generator(match_list)
            attempts=attempts-1
        
    if correct_guess=='False':
        print('\nGame over')

    print(f'The secret number is {secret_number}')
    new_game=new_game_starter()

