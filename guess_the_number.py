design= """
  /$$$$$$                                                 /$$     /$$                                                         /$$                          
 /$$__  $$                                               | $$    | $$                                                        | $$                          
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$       /$$$$$$  | $$$$$$$   /$$$$$$        /$$$$$$$  /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/      |_  $$_/  | $$__  $$ /$$__  $$      | $$__  $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$         | $$    | $$  \ $$| $$$$$$$$      | $$  \ $$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$        | $$ /$$| $$  | $$| $$_____/      | $$  | $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/        |  $$$$/| $$  | $$|  $$$$$$$      | $$  | $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      
 \______/  \______/  \_______/|_______/|_______/          \___/  |__/  |__/ \_______/      |__/  |__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/      
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
"""
import random
import os

lives=0
end_game= False
count=0
while not end_game:
    print("I'm thinking of a number between 1 and 100.")
    number= random.randint(0, 100)
    level= input("choose a deficulty level 'easy' or 'hard'")
    if level == 'easy':
        lives= 10
        print("You have 10 attempts remaining to guess the number.")
    elif level == 'hard':
        lives= 5
        print("You have 5 attempts remaining to guess the number.")
    for i in range(lives):
        guess= int(input("Make a guess"))
        if guess==number:
             
            count= 1
            break
        elif guess>=number:
            print(f'''Too High.
Guess again.
You have {lives-i-1} attempts remaining to guess the number.''')
        else:
            print(f'''Too low.
Guess again.
You have {lives-i-1} attempts remaining to guess the number.''')
    if count==1:
        print(f"You got it! The answer was{number}.")
    else:
        print("you lose")
        end_game= True
    
