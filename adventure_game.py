"""Text based word game about killing a bad guy."""
import time
import random
choose_bad_guy = random.choice(['nazi', 'pirate', 'trump supporter',
                                'facist'])
bad_guy = choose_bad_guy
choose_weapon = random.choice(['Viking Sword', 'Hammer of Thor',
                              'Holy Hand Grenade', 'Katana'])
weapon = choose_weapon


def print_pause(message_to_print):
    """Function so messages display with a delay."""
    print(message_to_print)
    time.sleep(2)


def house(items):
    """Simulation of walking in the house."""
    print_pause("You get a strange feeling right as the door "
                "opens and out steps a " +
                bad_guy.title() + ".")
    print_pause("Shit! You knew you had a bad feeling about this one!")
    print_pause("The " + bad_guy.title() + " makes a lunge at you.")
    fight = input("Would you like to (1) fight or (2) run away?\n")
    if fight == "1":
        if "weapon" in items:
            print_pause("As the " + bad_guy.title() + " moves to "
                        "attack, you side step him and draw your "
                        + weapon.title() + ".")
            print_pause("The " + weapon.title() + " shines brightly "
                        "has a nice weight to it. This will be fun.")
            print_pause("The " + bad_guy.title() + " takes one look at "
                        + weapon + "and screams like a new born child!!")
            print_pause("As the dust settles, you start to breath easier "
                        "knowing that's one less " + bad_guy.title()
                        + "in the world.")
            print_pause("You search the kitchen for a celebratory drink and "
                        "you think to yourself....did I lock my car??")
            print_pause("Congratulations, you have won! "
                        "+9000 points to Gryffindor!!")
            user_retry(items)
        elif "weapon" not in items:
            print_pause("You try your best...")
            print_pause("but your pocket knife couldn't cut an apple "
                        "let alone a " + bad_guy.title() + ".")
            print_pause("The " + bad_guy.title() + "is too quick and makes "
                        "easy work of you.")
            print_pause("As you lay dying in the hot sun, you think...."
                        "did I lock my car?")
            print_pause("::dead::")
            user_retry(items)
    elif fight == '2':
        print_pause("You run back into the field. Luckily, you "
                    "don't seem to have been followed.")
        valid_input(items)
    else:
        print_pause("That's not a valid response....need a refresher?")
        house(items)


def tool_shed(items):
    """Simulation of checking the tool shed."""
    print_pause("You peer cautiously through a dusty window.")
    print_pause("It turns out to be a very small, run down tool shed.")
    if "weapon" in items:
        print_pause("You've been here before, and gotten all the good stuff.")
        print_pause("It's just a pile of junk now.")
        print_pause("You walk back out to the field.")
        valid_input(items)
    elif "weapon" not in items:
        print_pause("Your eye catches a glint of metal behind a box.")
        print_pause("You have found a absolutly beautiful "
                    + weapon + "!")
        print_pause("You discard your silly old pocket knife and "
                    "take the weapon with you.")
        print_pause("You walk back out to the field.")
        items.append("weapon")
        valid_input(items)


def user_retry(items):
    """See if user would like to play again."""
    retry = input("Would you like to play again? (y/n)\n").lower()
    if retry == 'y':
        print_pause("Excellent! Restarting the game..")
        play_game()
    elif retry == 'n':
        print_pause("Fine...be like that...come back soon though?")
    else:
        print_pause("Yaaaa, that's not going to work for an answer."
                    "Please try again, this time a 'y' or 'n' please.")
        user_retry(items)


def valid_input(items):
    """User picks what they want to enter, house or cave."""
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to investigate the tool shed.")
    decision = input("(Please enter 1 or 2.)\n")
    if decision == '1':
        print_pause("You walk towards the house")
        house(items)
    elif decision == '2':
        print_pause("You walk towards the tool shed")
        tool_shed(items)
    else:
        print_pause("Ummm, no...that's not a 1 or 2. Try again...")
        valid_input(items)


def intro():
    """Gives the setting for our video game."""
    print_pause("As you desend the south face of Mt. Python,")
    print_pause("You can faintly see what looks like civilization.")
    print_pause("You pick up the pace in hopes to reach whatever "
                "lies ahead before dark.")
    print_pause("You stop to drink the last of the water in your canteen,")
    print_pause("and you can clearly make out a small rundown house, "
                " with a small tool shed behind it.")
    print_pause("In your hand you have a small rusted out pocket knife.")
    print_pause("As you make your approach, "
                "you decide which to check first...")


def play_game():
    """Combines the functions necissary to run the game."""
    items = []
    intro()
    valid_input(items)

if __name__ == "__main__":
  play_game()
