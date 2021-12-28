import time
import random

weapon = []
list_of_enemies = ["pirate", "wicked fairie", "gorgon",
                   "troll", "monster", "dragon", "lion", "tiger"]
enemy = random.choice(list_of_enemies)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere "
                "around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.")


while True:
    weapon = []
    list_of_enemies = ["pirate", "wicked fairie", "gorgon",
                       "troll", "monster", "dragon", "lion", "tiger"]
    enemy = random.choice(list_of_enemies)
    intro()
    while True:
        while True:
            while True:
                print_pause("\nEnter 1 to knock on the door of the house.")
                print_pause("Enter 2 to peer into the cave.")
                response = input("What would you like to do?\n"
                                 "(Please enter 1 or 2.)\n")
                if response == "1":
                    if "sword" not in weapon:
                        print_pause("You approach the door of the house.")
                        print_pause(f"You are about to knock when the "
                                    f"door opens and out steps a {enemy}.")
                        print_pause(f"Eep! This is the {enemy}'s house!")
                        print_pause(f"The {enemy} attacks you!")
                        print_pause("You feel a bit under-prepared for this, "
                                    "what with only having a tiny dagger.")
                        break
                    else:
                        print_pause("You approach the door of the house.")
                        print_pause(f"You are about to knock when the door "
                                    f"opens and out steps a {enemy}.")
                        print_pause(f"Eep! This is the {enemy}'s house!")
                        print_pause(f"The {enemy} attacks you!")

                        break
                elif response == "2":
                    if 'sword' in weapon:
                        print_pause("You peer cautiously into the cave.")
                        print_pause("You've been here before, and "
                                    "gotten all the good stuff. "
                                    "It's just an empty cave now.")
                        print_pause("You walk back out to the field.")

                    else:
                        print_pause("You peer cautiously into the cave.")
                        print_pause("It turns out to be only a "
                                    "very small cave.")
                        print_pause("Your eye catches a glint of metal "
                                    "behind a rock.")
                        print_pause("You have found the magical "
                                    "Sword of Ogoroth!")
                        print_pause("You discard your silly old dagger "
                                    "and take the sword with you.")
                        print_pause("You walk back out to the field.")
                        weapon.append("sword")

                else:
                    print_pause("Please enter a valid input!")

            player_response = input(
                "Would you like to (1) fight or (2) run away?\n")
            if player_response == '1':
                if "sword" not in weapon:
                    print_pause("You do your best...")
                    print_pause(f"but your dagger is no match "
                                f"for the {enemy}.")
                    print_pause("You have been defeated!")
                    break

                else:
                    print_pause(f"As the {enemy} moves to attack, "
                                "you unsheath your new sword.")
                    print_pause("The Sword of Ogoroth shines brightly in your "
                                "hand as you brace yourself for the attack.")
                    print_pause(f"But the {enemy} takes one look at "
                                "your shiny new toy and runs away!")
                    print_pause(f"You have rid the town of the {enemy}. "
                                "You are victorious!")
                    break

            elif player_response == '2':
                print_pause("You run back into the field. Luckily, "
                            "you don't seem to have been followed.")
                continue

            else:
                print_pause("Please enter a valid input!")
        while True:
            play_game_again = input("Would you like to play "
                                    "again? (y/n)\n").lower()
            if play_game_again == 'y':
                print_pause("Excellent! Restarting the game ...")
                break
            elif play_game_again == 'n':
                print_pause("Thanks for playing! See you next time.")
                break

            else:
                print_pause("Please enter a valid input!")

        if play_game_again == 'n':
            break
        if play_game_again == 'y':
            break
    if play_game_again == 'n':
        break
