"""This code is a wishing simulator that allows the user to get pokemon through wishing. Users can get more wishes by answering math questions correctly!"""

import random

print("Welcome to the pokemon wishing simulator! You have 3 wishes. You may choose to get more!")
#welcome statement

pokemon_list_rare: list[str] = ["Zapdos", "Zacian", "Urshifu Single-Strike"]
#defined list of rare pokemon

pokemon_list_ultra_rare: list[str] = ["D", "E", "F"]
#defined list of ultra rare pokemon

pokemon_list_legendary: list[str] = ["G", "H", "I"]
#defined list of legendary pokemon

pokemon_list_all: list[str] = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

def main():
    #main function
    wish = input("Would you like to wish? Input 'y' for yes, and 'n' for no: ")

    wish_count = 3
    user_pokemon_list: list[str] = []
    #defined list of user's pulled pokemon

    while wish == 'y':
        
        pokemon_choice = random.choices(pokemon_list_all, weights=(70, 70, 70, 20, 20, 20, 10, 10, 10), k=1)
        print(pokemon_choice)
        
        if pokemon_choice in pokemon_list_rare: 
            print("You got RARE ", pokemon_choice)

        elif pokemon_choice in pokemon_list_ultra_rare:
            print("You got ULTRA RARE ", pokemon_choice)

        elif pokemon_choice in pokemon_list_legendary: 
            print("You got LEGENDARY ", pokemon_choice)
        
        user_pokemon_list += [pokemon_choice]
        wish_count -= 1
        #ISSUE: user_pokemon+list and wish_count not referenced before assignment. Figure out how to fix it.

        wish = input("Would you like to wish again? Input 'y' for yes, and 'n' for no: ")

        if wish_count == 0:
            math_question = input("uh oh! you have no wishes left :( would you like to answer a math question to solve it? Enter 'y' for yes and 'n' for no: ")
            
            if math_question == 'y':
                a = random.randint(0, 20)
                b = random.randint(0, 20)
                print("a =", a, ", b =", b)
                math_answer = int(input("a * b = "))

                if math_answer == a * b:
                    wish_count += 1
                    print("Correct! Good job :) You now have 1 wish")
                    wish = input("Would you like to wish again? Input 'y' for yes, and 'n' for no: ")
                else:
                    print("Uh oh! Your answer is incorrect. Here is your pokemon list: ")
                    return(user_pokemon_list)
            else:
                return(user_pokemon_list)

main()
