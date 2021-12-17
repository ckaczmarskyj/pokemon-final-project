"""This code is a wishing simulator that allows the user to get pokemon through wishing. Users can get more wishes by answering math questions correctly!"""

import random

print("Welcome to the pokemon wishing simulator! You have 3 wishes. You may choose to get more!")
#welcome statement

pokemon_list_rare: list[str] = ["Chansey", "Tapu Fini", "Dracovish","Quagsire", "Rillaboom","Yveltal", "Dragapult", "Necrozma", "Toxapex", "Calyrex", "Galarian Darmanitan", "Lapras", "Swampert", "Urshifa Rapid-Strike Style", "Celesteela", "Regieleki", "Dragonite", "Grimmsnarl"]
#defined list of rare pokemon

pokemon_list_ultra_rare: list[str] = ["Landorus", "Cinderace", "Mimikyu", "Tyranitar", "Ditto", "Porygon2", "Ferrothorn", "Kyogre", "Hippowdon"]
#defined list of ultra rare pokemon

pokemon_list_legendary: list[str] = ["Zapdos", "Zacian", "Urshifu Single-Strike"]
#defined list of legendary pokemon

pokemon_list_all: list[str] = ["Chansey", "Tapu Fini", "Dracovish","Quagsire","Rillaboom","Yveltal", "Dragapult", "Necrozma", "Toxapex", "Calyrex", "Galarian Darmanitan", "Lapras", "Swampert", "Urshifa Rapid-Strike Style", "Celesteela", "Regieleki", "Dragonite", "Grimmsnarl","Landorus", "Cinderace", "Mimikyu", "Tyranitar", "Ditto", "Porygon2", "Ferrothorn", "Kyogre", "Hippowdon","Zapdos", "Zacian", "Urshifu Single-Strike" ]
#defined list of all pokemon


def main():
    #main function

    wish = input("\nWould you like to wish? Input 'y' for yes, and 'n' for no: ")
    #user input to ask if they would like to wish

    continue_play = True
    #boolean continue game
    
    if wish != 'y':
        continue_play = False

    wish_count = 3
    user_pokemon_list: list[str] = []
    #defined current wish count and list of user's pulled pokemon

    while continue_play == True:
        
        pokemon_choice = random.choices(pokemon_list_all, weights=(40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 25, 25, 25, 25, 25, 25, 25, 25, 25, 20, 20, 20), k=1)
        pokemon_choice_str = pokemon_choice[0]
        #chooses a random pokemon from the total list using weights for probability. 6% chance for legendary, 21% chance for ultra rare, 73% chance for legendary
        
        if pokemon_choice_str in pokemon_list_rare: 
            print("You got RARE pokemon", pokemon_choice_str)
            pokemon_choice_str = "[RARE] " + pokemon_choice_str
            user_pokemon_list += [pokemon_choice_str]
            #return for rare pokemon

        elif pokemon_choice_str in pokemon_list_ultra_rare:
            print("You got ULTRA RARE pokemon", pokemon_choice_str)
            pokemon_choice_str = "[ULTRA RARE] " + pokemon_choice_str
            user_pokemon_list += [pokemon_choice_str]
            #return for ultra rare pokemon

        elif pokemon_choice_str in pokemon_list_legendary: 
            print("WOW! You got LEGENDARY pokemon", pokemon_choice_str)
            pokemon_choice_str = "[LEGENDARY] " + pokemon_choice_str
            user_pokemon_list += [pokemon_choice_str]
            #return for legendary pokemon
        
        
        wish_count -= 1
        #takes one wish away when user wishes
        
        wish = input("\nWould you like to wish again? Input 'y' for yes, and 'n' for no: ")
        if wish != 'y':
            continue_play = False

        if continue_play == False:
            print("\nHave a nice day! Here is your pokemon list: ", user_pokemon_list)
            break
            #if user does not want to continue, prints out list

        if wish_count == 0:

            math_question = input("\nuh oh! you have no wishes left :( would you like to answer a math question to solve it? Enter 'y' for yes and 'n' for no: ")
            #if user is out of wishes, they can answer a math question to get another

            if math_question == 'y':
                a = random.randint(0, 20)
                b = random.randint(0, 20)
                print("\na =", a, ", b =", b)
                math_answer = int(input("a * b = "))

                if math_answer == a * b:
                    wish_count += 1
                    print("\nCorrect! Good job :) You now have 1 wish")
                    wish = input("\nWould you like to wish again? Input 'y' for yes, and 'n' for no: ")
                    #user is correct => option to continue game
                    
                    if wish != 'y':
                        print("\nHave a nice day! Here is your pokemon list: ", user_pokemon_list)
                        break
                    
                else:
                    print("\nUh oh! Your answer is incorrect. Here is your pokemon list: ")
                    print(user_pokemon_list)
                    break
                    #user is incorrect => game over

            else:
                print("\nHave a nice day! Here is your pokemon list: ", user_pokemon_list)
                break
                #if user does not want to answer a math question, program ends, and they get their list of pokemon

main()
