import time
import random
items = []
enemies_list = ['wicked fairy', 'pirate', 'dragon', 'monster']
weapons_list = ['sword', 'trident', 'glaive']
current_enemy = random.choice(enemies_list)
current_weapon = random.choice(weapons_list)


def print_pause(enter_message, pause=2):
    print(enter_message)
    time.sleep(pause)


def intro():
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a dangerous enemy is somewhere around here,"
                " and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                " (but not very effective) dagger.")


def restart_game():
    items.clear()
    global current_enemy, current_weapon
    current_weapon = random.choice(weapons_list)
    current_enemy = random.choice(enemies_list)
    while True:
        option = input("Would you like to play again? (y/n)")
        if option == 'y':
            print_pause("Excellent! Restarting the game ...")
            play_game()
        elif option == 'n':
            print_pause("Thanks for playing! See you next time.")
            exit()


def fight_run():
    while True:
        choice2 = input("Would you like to (1) fight or (2) run away?")
        if choice2 == '1':
            if current_weapon in items:
                print_pause("As the " + current_enemy + " moves to attack,"
                            " you unsheathe your new " + current_weapon + ".")
                print_pause("The " + current_weapon + " of Ogoroth shines "
                            "brightly in your hand as you brace yourself"
                            " for the attack.")
                print_pause("But the " + current_enemy +
                            " takes one look at your shiny new"
                            " toy and runs away!")
                print_pause("You have rid the town of the "
                            + current_enemy + ". You are victorious!")
            else:
                print_pause("You feel a bit under-prepared for this,"
                            " what with only having a tiny dagger.")
                print_pause("You do your best...")
                print_pause("but your dagger is no match for the "
                            + current_enemy + "...")
                print_pause("You have been defeated!")
            restart_game()
        elif choice2 == '2':
            print_pause("You run back into the field."
                        " Luckily, you don't seem to have been followed.")
            start_game()


def house():
    print_pause("You approach the door of the house.", 3)
    print_pause("You are about to knock when the door"
                " opens and out steps a " + current_enemy + " .", 3)
    print_pause("Eep! This is the " + current_enemy + " house!")
    print_pause("The " + current_enemy + " attacks you!", 3)
    fight_run()


def cave():
    print_pause("You peer cautiously into the cave.", 3)
    if current_weapon in items:
        print_pause("You've been here before, and gotten "
                    "all the good stuff. It's just an empty cave now.", 3)
    else:
        print_pause("It turns out to be only a very small cave.", 3)
        print_pause("Your eye catches a glint of metal behind a rock.", 3)
        print_pause("You have found the magical "
                    + current_weapon + " of Ogoroth!", 3)
        print_pause("You discard your silly old dagger"
                    " and take the " + current_weapon + " with you.", 3)
        items.append(current_weapon)
    print_pause("You walk back out to the field.", 3)
    start_game()


def start_game():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    while True:
        choice1 = input("What would you like to do?\n(Please enter 1 or 2.)")
        if choice1 == '1':
            house()
        elif choice1 == '2':
            cave()


def play_game():
    intro()
    start_game()


if __name__ == "__main__":
    play_game()
