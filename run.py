# Creator: Stephen Darcy
# Date:
# Project 3 - The code Institute

from functions import P_STAT, game_over, player_died
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

TIME_ELAPSED = 2

# Start the game and gives initial choices to the player


def start():
    """
    Starts the game, gives a narrative to set the scene and asks
    if the player would like to play or not. The function also asks
    the players name
    """
    print(Fore.RED + Back.YELLOW + Style.BRIGHT + "  The Great Castle Escape")
    time.sleep(TIME_ELAPSED)
    print(Fore.CYAN + '''
                                     T~~
                                     |
                                     /"\\
                             T~~     |'| T~~
                         T~~ |    T~ WWWW|
                         |  /"\   |  |  |/\T~~
                         /"\ WWW  /"\ |' |WW|
                         WWWWW/\| /   \|'/\|/"\\
                         |   /__\/]WWW[\/__\WWWW
                         |"  WWWW'|I_I|'WWWW'  |
                         |   |' |/  -  \|' |'  |
                         |'  |  |LI=H=LI|' |   |
                         |   |' | |[_]| |  |'  |
                         |   |  |_|###|_|  |   |
                         '---'--'-/___\-'--'---'
                     \n
                        Can you escape the castle!\n''')
    while True:
        """
        Set P-NAME to global variable
        """
        global P_NAME
        P_NAME = input(" Please enter a username: \n\n")
        print()
        if P_NAME == "":
            print(" You need to enter a username to continue...\n")
            continue
        else:
            break
    P_STAT(f" Welcome {P_NAME}, good luck, you will need it\n", 2)
    P_STAT(Fore.YELLOW + " You awake a little dazed and confused", 2)
    P_STAT(Fore.YELLOW + " You find yourself in a dimly lit room", 2)
    P_STAT(Fore.YELLOW + " You can hear the rain crashing down outside", 2)
    P_STAT(Fore.YELLOW + " You try to recall how you got here", 2)
    P_STAT(Fore.YELLOW + " You look around the room", 2)
    P_STAT(Fore.YELLOW + " Its big cold and damp, you notice a window", 2)
    P_STAT(Fore.YELLOW + " A large wooden door is in front of you", 2)
    P_STAT(Fore.YELLOW + " Not a lot to choose from", 2)
    print(Fore.BLUE + " So, do you have the guts to try and escape?(e or s)")
    # convert the player's input to lower_case
    answer = input("=> ").lower().strip()

    if answer == "escape" or answer == "e":
        small_window()
    elif answer == "stay" or answer == "s":
        P_STAT(Fore.RED + " Shame", 1)
        P_STAT(f" Enjoy the solitude and loneliness {P_NAME}", 2)
        play_again()
    else:
        P_STAT(Fore.RED + " Error, please enter a valid choice (e or s) ", 2)
        play_again()
# Player has the option to check the window or ignore it


def small_window():
    """
    Function called to let the player explore the
    small window in the room
    """
    P_STAT(Fore.BLUE + " You get up and walk towards the window", 1)
    P_STAT(Fore.BLUE + " You peer out and can only see darkness", 1)
    print(Fore.YELLOW + " Do you try open the window? (y or n)")

    try_window = input("=> ").lower().strip()
    if try_window == "y" or try_window == "yes":
        P_STAT(Fore.BLUE + " You try the window, nothing.", 1)
        P_STAT(Fore.BLUE + " Urggh its sealed shut", 1)
        try_door()
    else:
        P_STAT(Fore.BLUE + " You ignore the window", 1)
        P_STAT(Fore.BLUE + " and head for the door", 1)
        try_door()


def try_door():
    """
    The function offers the player the choice of
    opening the door or not in the first room.
    """
    P_STAT(Fore.BLUE + " Reaching the door you try the handle", 2)
    P_STAT(Fore.BLUE + " It opens, thats odd you think", 2)
    P_STAT(Fore.YELLOW + " Do you take a look outside? (y or n)", 2)

    look_outside = input("=>").lower().strip()

    if look_outside == "y" or look_outside == "yes":
        P_STAT(Fore.BLUE + " You open the door as silently as you can", 2)
        P_STAT(Fore.BLUE + " Looking outside you see a door at either end", 2)
        P_STAT(Fore.BLUE + " of a long corridor", 2)
        take_items()

    else:
        P_STAT(Fore.BLUE + " You are too terrified to go on, shame", 1)
        P_STAT(f" Enjoy the solitude and loneliness {P_NAME}", 2)
        play_again()


def take_items():
    """
    The function gives the player the option to check a discovered drawer
    """
    P_STAT(Fore.BLUE + " A table outside catches your eye, it has a drawer inset", 2)
    print(Fore.YELLOW + " Do you try the drawer in the table? (y or n)")

    open_drawer = input("=> ").lower().strip()

    if open_drawer == "y" or open_drawer == "yes":
        P_STAT(Fore.BLUE + " You pull out the drawer and find a key and a knife", 2)
        P_STAT(Fore.BLUE + " You reach in quickly and pick up both items", 2)
        P_STAT(Fore.BLUE + " You stuff them in your pockets and close the drawer", 2)
        P_STAT(Fore.BLUE + " You think maybe the knife will open the window", 3)
        back_to_window()

    elif open_drawer == "n" or open_drawer == "no":
        P_STAT(Fore.BLUE + " Probably best not to disturb anything", 2)
        direction_choice_two()

    else:
        print(Fore.RED + " Error, please enter a valid choice (y or n) ")


def return_to_table():
    """
    Player returns to the table from the locked door
    """
    P_STAT(Fore.BLUE + " You go back to the table and pull drawer open", 2)
    P_STAT(Fore.BLUE + " Result, a key and a knife?", 2)
    P_STAT(Fore.BLUE + " You stuff them in your pockets and close the drawer", 2)
    P_STAT(Fore.BLUE + " You quickly get back to the right hand door", 2)
    go_right_back()


def back_to_window():
    """
    Brings the player back into the start room to the locked
    window
    """
    P_STAT(Fore.RED + "\n You return to the first room", 2)

    P_STAT(Fore.BLUE + " You look out the window again", 2)
    print(Fore.YELLOW + " Do you try the window with the knife? (y or n)")

    open_window = input("=> ").lower().strip()

    if open_window == "y" or open_window == "yes":
        P_STAT(Fore.BLUE + " You jam the knife into the gap of the windowpane", 2)
        P_STAT(Fore.BLUE + " the timber comes loose and the window pops open", 2)
        P_STAT(Fore.BLUE + " Success, you climb up and outside", 2)
        P_STAT(Fore.BLUE + " You peer through the dark and the rain and can ", 2)
        P_STAT(Fore.BLUE + " just make out the sloping roof. You jump and to your horror ", 2)
        P_STAT(Fore.BLUE + " the tile gives way and you fall to your death.", 3)

        player_died()
        game_over()
        play_again()

    else:
        P_STAT(Fore.BLUE + " Looking down into the dark bleak night", 2)
        P_STAT(Fore.BLUE + " you decide its best not to try and make your", 2)
        P_STAT(Fore.BLUE + " way back to the large door opening", 2)
        direction_choice()


def direction_choice():
    """
    Player will make a choice to go left or right
    out of the doorway and they will have the 
    objects from the drawer
    """
    P_STAT(Fore.BLUE + " Standing in the doorway you need to make a choice", 1)
    print(Fore.YELLOW + " Do you go left or go right? (l or r)")

    player_choice = input("=> ").lower().strip()

    if player_choice == "l" or player_choice == "left":
        go_left()
    elif player_choice == "r" or player_choice == "right":
        go_right()
    else:
        print(Fore.RED + "That it not a valid option, please enter l or r")


def direction_choice_two():
    """
    Second direction choice if player takes nothing from the drawer
    """
    P_STAT(Fore.BLUE + " Standing in the doorway you need to make a choice", 1)
    print(Fore.YELLOW + " Do you go left or go right? (l or r)")
    
    player_choice_two = input("=> ").lower().strip()

    if player_choice_two == "l" or player_choice_two == "left":
        go_left()
    elif player_choice_two == "r" or player_choice_two == "right":
        P_STAT(Fore.BLUE + " You reach the door to the right and try open it", 2)
        P_STAT(Fore.BLUE + " Its locked, damn it, you remember the drawer, maybe?", 2)
    else:
        print(Fore.RED + " That it not a valid option, please enter l or r")
    return_to_table()


def direction_choice_three():
    """
    Function for the player to return to the right hand door
    if they decide to return after going left
    """
    P_STAT(Fore.BLUE + " You reach the door to the right and try open it", 2)
    P_STAT(Fore.BLUE + " Its locked, damn it, you remember the drawer, maybe?", 2)
    return_to_table()


def go_left():
    """
    The player goes left and will have to makes choices
    in the next room
    """
    P_STAT(Fore.BLUE + " You decide to turn left and head towards the door", 2)
    P_STAT(Fore.BLUE + " as you approach the door you slow down", 2)
    P_STAT(Fore.BLUE + " you push at the door and it creaks open", 2)
    P_STAT(Fore.BLUE + " as your eyes adjust you make out a single candle light.", 2)
    P_STAT(Fore.BLUE + " You walk inside, at the far end there is an opening", 2)
    P_STAT(Fore.BLUE + " You approach the opening and see a staircase going down", 2)
    P_STAT(Fore.BLUE + " You look around the room", 2)
    print(Fore.YELLOW + " Do you explore ,proceed downstairs or go back? (e - p - g")

    decision = input("=> ").lower().strip()

    if decision == "explore" or decision == "e":
        explore_room()
    elif decision == "proceed" or decision == "p":
        proceed_down_stairs()
    else:
        P_STAT(Fore.BLUE + " You decide it would be better to check the other door", 2)
        direction_choice_three()


def explore_room():
    """
    Player decides to explore room
    """
    P_STAT(Fore.BLUE + " As you look around the room the idea you are in a castle", 2)
    P_STAT(Fore.BLUE + " still leaves you feeling confused", 2)
    P_STAT(Fore.BLUE + " You see a bowl with fruit in it, you are starving so", 2)
    P_STAT(Fore.BLUE + " pick it up and eat while continuing to explore", 2)
    P_STAT(Fore.BLUE + " You find a belt, ", 2)
    P_STAT(Fore.BLUE + " you wrap it around you and slip the knife in", 2)
    P_STAT(Fore.BLUE + " As there is nothing else left to check ", 2)
    P_STAT(Fore.BLUE + " you decide to go downstairs", 2)

    proceed_down_stairs()


def proceed_down_stairs():
    """
    Player proceeds down the spiral stairs
    """
    P_STAT(Fore.BLUE + " You enter the doorway", 2)
    P_STAT(Fore.BLUE + " Hugging the wall you make your way down", 2)
    P_STAT(Fore.BLUE + " You reach the bottom and as you listen", 2)
    P_STAT(Fore.BLUE + " you can hear what appears to be two voices", 2)
    P_STAT(Fore.BLUE + " You take a breath and peek around the corner and see", 2)
    P_STAT(Fore.BLUE + " two large men with what looks like swords?", 2)
    P_STAT(Fore.BLUE + " Their backs are to you", 2)
    P_STAT(Fore.YELLOW + " Hmmm attack or sneak? Your choice - (a or s)", 2)

    attack = input("=> ").lower().strip()

    if attack == "attack" or attack == "a":
        P_STAT(Fore.BLUE + " You charge at the men who are surprised", 2)
        P_STAT(Fore.BLUE + " but alas, one fouls swipe and you are....", 1)

        player_died()
        game_over()
        play_again()

    else:
        P_STAT(Fore.BLUE + " You put your back against the wall", 2)
        P_STAT(Fore.BLUE + " and sneak as quietly as you can passed them", 2)
        bottom_floor()


def go_right_back():
    """
    Return to the righthand door with the key
    """
    P_STAT(Fore.BLUE + " Using the key you push the door open and enter", 2)
    P_STAT(Fore.BLUE + " Looking around this lavish room you notice what looks like", 2)
    P_STAT(Fore.BLUE + " three levers on the wall", 2)
    P_STAT(Fore.BLUE + " You decide to try the levers", 1)

    try_lever = input("=> Pick a number from '1', '2' and '3':  ").lower().strip()

    if try_lever == "1":
        P_STAT(Fore.BLUE + " You pull the first lever, you hear a groan", 1.2)
        P_STAT(Fore.BLUE + " looking around a large object comes at you ...", 2)

        player_died()
        game_over()
        play_again()

    elif try_lever == "2":
        P_STAT(Fore.BLUE + " You pull the first lever, you hear a groan", 1.2)
        P_STAT(Fore.BLUE + " looking around a large object comes at you ...", 2)

        player_died()
        game_over()
        play_again()

    elif try_lever == "3":

        P_STAT(Fore.BLUE + " You pull the third lever ", 1.2)
        P_STAT(Fore.BLUE + " you hear a creaking and a concealed door opens", 2)
        P_STAT(Fore.BLUE + " You look around the room and ", 1.2)
        P_STAT(Fore.BLUE + " see a candle on the side table, picking it up", 2)
        P_STAT(Fore.BLUE + " You crouch down and make your way into the opening", 2)
        P_STAT(Fore.BLUE + " Holding the candle up the passage looks long and unused", 2)

        P_STAT(Fore.BLUE + " You proceed forward carful as it is sloping down", 2)
        P_STAT(Fore.BLUE + " You eventually reach the end and reappear in a room", 2)

        P_STAT(Fore.BLUE + " You hear voices, but they are coming from behind you", 2)
        bottom_floor()

    else:
        print(Fore.RED + " That it not a valid option, please pick '1', '2' or '3'")


def go_right():
    """
    Player returns to the corridor and goes to the right
    hand door from the starting room. This will also be the go right from the
    room the player initially makes.
    """
    P_STAT(Fore.BLUE + " You reach the door to the right and try open it", 2)
    P_STAT(Fore.BLUE + " You then remember the key and try it, it works", 2)
    P_STAT(Fore.BLUE + " You push the door open and enter", 2)
    P_STAT(Fore.BLUE + " Looking around this lavish room you notice what looks like", 2)
    P_STAT(Fore.BLUE + " three levers on the wall", 2)
    P_STAT(Fore.BLUE + " You decide to try the levers", 1)

    try_lever = input("=> Pick a number from '1', '2' and '3':  ").lower().strip()

    if try_lever == "1":
        P_STAT(Fore.BLUE + " You pull the first lever, you hear a groan", 1.2)
        P_STAT(Fore.BLUE + " looking around a large object comes at you ...", 2)

        player_died()
        game_over()
        play_again()

    elif try_lever == "2":
        P_STAT(Fore.BLUE + " You pull the first lever, you hear a groan", 1.2)
        P_STAT(Fore.BLUE + " looking around a large object comes at you ...", 2)

        player_died()
        game_over()
        play_again()

    elif try_lever == "3":

        P_STAT(Fore.BLUE + " You pull the third lever ", 1.2)
        P_STAT(Fore.BLUE + " you hear a creaking and a concealed door opens", 2)
        P_STAT(Fore.BLUE + " You look around the room and ", 1.2)
        P_STAT(Fore.BLUE + " see a candle on the side table, picking it up", 2)
        P_STAT(Fore.BLUE + " You crouch down and make your way into the opening", 2)
        P_STAT(Fore.BLUE + " Holding the candle up the passage looks long and unused", 2)

        P_STAT(Fore.BLUE + " You proceed forward carful as it is sloping down", 2)
        P_STAT(Fore.BLUE + " You eventually reach the end and reappear in a room", 2)

        P_STAT(Fore.BLUE + " You hear voices, but they are coming from behind you", 2)
        bottom_floor()

    else:
        print(Fore.RED + " That it not a valid option, please pick '1', '2' or '3'")


def bottom_floor():
    """
    The player is in the place they sneak to from
    the stairs and from the secret tunnel and has a choice of 3 paths
    """
    P_STAT(Fore.BLUE + " Looking ahead you can see three paths", 2)
    P_STAT(Fore.BLUE + " There is a straight path, left and right path", 2)
    print(Fore.YELLOW + " Do you go s - l - r")

    path_choice = input("=> ").lower().strip()

    if path_choice == "s" or path_choice == "straight":
        P_STAT(Fore.BLUE + " You decide to proceed straight ahead", 2)
        P_STAT(Fore.BLUE + " Oh sugar.., a group of very angry men approach...", 2)

        player_died()
        game_over()
        play_again()

    elif path_choice == "l" or path_choice == "left":
        P_STAT(Fore.BLUE + " You decide to take the left path ahead", 2)
        P_STAT(Fore.BLUE + " You are in a small room with a vent on the wall", 2)
        print(Fore.YELLOW + " Do you open the vent? (y or n)")

        open_vent = input("=> ").lower().strip()

        if open_vent == "y" or open_vent == "yes":
            P_STAT(Fore.BLUE + " You pry the vent open and enter", 2)
            P_STAT(Fore.BLUE + " You crawl forward and can ", 2)
            P_STAT(Fore.BLUE + " see another vent in the distance", 2)
            P_STAT(Fore.BLUE + " as you reach the next vent ", 2)
            P_STAT(Fore.BLUE + " you can see below you a guard on his own", 2)
            print(Fore.YELLOW + " Try kill the guard? (y or n)")

        elif open_vent == "n" or open_vent == "no":
            return_to_paths()

        else:
            print(Fore.RED + " That it not a valid option, please pick y or n")
            play_again()

        kill_guard = input("=> ").lower().strip()

        if kill_guard == "y" or kill_guard == "yes":
            P_STAT(Fore.BLUE + " You pry the vent open and ready your knife", 2)
            P_STAT(Fore.BLUE + " You jump down surprising the guard", 2)
            P_STAT(Fore.BLUE + " With one stroke you cut his throat", 2)
            outside()

        elif kill_guard == "n" or kill_guard == "no":
            P_STAT(Fore.BLUE + " You decide to spare his life... for now.", 2)
            return_to_paths()

        else:
            print(Fore.RED + " That it not a valid option, please pick y or n")
            play_again()

    elif path_choice == "r" or path_choice == "right":
        P_STAT(Fore.BLUE + " You veer right to an empty room", 2)
        P_STAT(Fore.BLUE + " more doors, two of them", 2)
        print(Fore.YELLOW + " Left or Right? (l or r)")

        way_forward = input("=> ").lower().strip()

        if way_forward == "left" or way_forward == "l":
            P_STAT(Fore.BLUE + " You open the lefthand door", 2)
            P_STAT(Fore.BLUE + " You walk right into a room that is full of guards", 2)

            player_died()
            game_over()
            play_again()

        elif way_forward == "right" or way_forward == "r":

            P_STAT(Fore.BLUE + " You open the right hand door", 2)
            P_STAT(Fore.BLUE + " Dogs? and guard dogs..", 2)

            player_died()
            game_over()
            play_again()

        else:
            print(Fore.RED + " That it not a valid option, please pick 'l', 'r' or 's'")
# Player choices for outside the castle


def return_to_paths():
    """
    Function returns palyers to path choices
    """
    P_STAT(Fore.BLUE + " You decide to return to the secret tunnel opening", 2)
    bottom_floor()


def outside():
    """
    Players choices for outside the castle
    """
    P_STAT(Fore.BLUE + " Quickly you search him and find keys and a sword.", 2)
    P_STAT(Fore.BLUE + " Looking up there is a door ahead.", 2)
    print(Fore.YELLOW + " Proceed through door? (y or n)", 2)

    go_to_door = input("=> ").lower().strip()

    if go_to_door == "yes" or go_to_door == "y":
        P_STAT(Fore.BLUE + " You fumble through the keys and find the right one", 2)
        P_STAT(Fore.BLUE + " You open the door and find yourself outside", 2)
        P_STAT(Fore.BLUE + " Pitch black and raining heavily you walk forward", 2)
        P_STAT(Fore.BLUE + " you go to the front of the building", 2)
        P_STAT(Fore.BLUE + " you can make out", 2)
        P_STAT(Fore.BLUE + " a gate ahead , guarded by two men", 2)
        P_STAT(Fore.BLUE + " There are high railings all around but", 2)
        P_STAT(Fore.BLUE + " you think you could climb them", 2)
        print(Fore.YELLOW + " Distract or Climb? (d or c)", 2)

    new_choice = input("=> ").lower().strip()

    if new_choice == "d":
        P_STAT(Fore.BLUE + " You look around for something to distract them", 2)
        P_STAT(Fore.BLUE + " picking up a stone you throw it towards the railing", 2)
        P_STAT(Fore.BLUE + " perfect shot, it makes a loud bang alerting them", 2)
        P_STAT(Fore.BLUE + " The two guards leave their post and go investigate", 2)
        P_STAT(Fore.BLUE + " This is your chance, you move as quickly", 2)
        P_STAT(Fore.BLUE + " and quietly as you can. You are out, you run!!!", 2)

        P_STAT(Fore.BLUE + '''
      __   __           _____                              _ 
      \ \ / /          |  ___|                            | |
       \ V /___  _   _ | |__ ___  ___ __ _ _ __   ___  __ | |
        \ // _ \| | | | |  __/ __|/ __/ _` | '_ \ / _ \/ _` |
        | | (_) | |_| | | |__\__ \ (_| (_| | |_) |  __/ (_| |
        \_/\___/ \__,_| \____/___/\___\__,_| .__/ \___|\__,_|
                                           | |               
                                           |_|               
                           ''', 2)
        play_again()

    elif new_choice == "c":
        P_STAT(Fore.BLUE + " You decide to climb the railings", 2)
        P_STAT(Fore.BLUE + " You put one foot up and pull yourself up to the", 2)
        P_STAT(Fore.BLUE + " top of them, you raise your other foot but", 2)
        P_STAT(Fore.BLUE + " to your surprise it slips, and you impale yourself", 2)
        P_STAT(Fore.BLUE + " You let out an anguished cry", 2)
        P_STAT(Fore.BLUE + " which alerts the guards", 2)
        P_STAT(Fore.BLUE + " AS they approach, weapons readied, one slice and ..", 2)

        player_died()
        game_over()
        play_again()

    else:
        print(Fore.RED + " That it not a valid option, please pick d or c'")


# Play again function called at end of game or when player dies
def play_again():
    """
    Asks the player if they would like to play again
    """
    print(Fore.YELLOW + " Would you like to play again? (Y or N)")

    answer = input("=> \n").lower().strip()

    if answer == "y" or answer == "yes":
        start()
    elif answer == "n" or answer == "no":
        print(f" Sorry to see you go {P_NAME}")
        print(Fore.YELLOW + " Please do comeback again")
    else:
        start()


start()
