import random #this imports the random number module

def guessing_game():
    while True:
        player_input = input("Would you like to play a number guessing game?(y/n) ").lower() #this is menu and asks the player if they would like to play a number guessing game
        if player_input == "n":
            print("Okay. Good bye!")
            return #this will exit the game via menu
        elif player_input == "y":
            random_number = random.randint(1,100)  # this calls on the random number module generating a number between 1 and a 100
            counter_left = 0  # this marks (resets) the initial number of player's tries
            #print(random_number) #this line is for testing only

            while True:
                if counter_left == 3: #when the number of tries reaches 3, it will go back to the beginning and ask to start a new round
                    print("Believe it or not George isn't at home, please leave message at the beep. I must be out, or I'd pick up the phone. Where could I be? Believe it or not, I'm not home. \nThat's means you're done, if it wasn't obvious enough.")
                    break

                try:
                    player_input_1 = int(input("Guess a number between 1 and 100: ")) #this is game start and asks the player for numerical input
                except ValueError:
                    print("Numerics only, please. This will not count as a try") #this will notify the player than only numerical input is valid
                    continue

                if player_input_1 == random_number: #in case player guesses the random number, it goes back to menu
                    print("Congrats! That's it")
                    break
                elif player_input_1 < random_number: #if the player is off it tells them whether the number is lower or higher (lower)
                    counter_left += 1
                    print(f"Almost. The number is actually higher than {player_input_1}. Three tries and you're out. Try number {counter_left}.")
                    continue
                elif player_input_1 > random_number: #if the player is off it tells them whether the number is lower or higher (higher)
                    counter_left += 1
                    print(f"Almost. The number is actually smaller than {player_input_1}. Three tries and you're out. Try number {counter_left}.")
                    continue
