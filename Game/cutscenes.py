import sys
import time
import os

# Cutscene based functions-----------------------
cutscenes_state = {
    1: 'Incomplete',
    2: 'Incomplete',
    3: 'Incomplete',
    4: 'Incomplete',
}
display_scene = {
    1: 'Spawn',
    2: 'City',
    3: 'Forest',
    4: 'Cave',
}


def check(scene_number):  # given scene no.
    if scene_number in cutscenes_state:  # checks if the given scene no. is in the cutscenes_state dictionary 
        if cutscenes_state[scene_number] == 'Incomplete':  # if it's incomplete, continue the scene
            pass
        else:
            return False  # Scene is already completed, return False to stop the cutscene
    else:
        print("Scene does not exist.")  # if the scene doesn't exist, print a message
        return False  # Return False to avoid running a non-existent scene

    return True  # Return True to continue the cutscene


def update(scene_number):
    cutscenes_state[scene_number] = 'Completed' # just updates the dictionary to complete once the dialogue has completely finished.
    # New code*****
    print(f"{scene_number}: {cutscenes_state[scene_number]}!")


# Text based functions-------------------------
def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def preset_city():
    print(r"""
                           _ _.-'`-._ _
                ;.'________'.;
     _________n.[____________].n_________
    |''_''_''_''||==||==||==||''_''_''_''']
    |'''''''''''||..||..||..||'''''''''''|
    |LI LI LI LI||LI||LI||LI||LI LI LI LI|
    |.. .. .. ..||..||..||..||.. .. .. ..|
    |LI LI LI LI||LI||LI||LI||LI LI LI LI|
 ,,;;,;;;,;;;,;;;,;;;,;;;,;;;,;;,;;;,;;;,;;,,
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
===============================================
""")
    
def preset_village():
    print(r"""
          ~         ~~          __
       _T      .,,.    ~--~ ^^
 ^^   // \                    ~
      ][O]    ^^      ,-~ ~
   /''-I_I         _II____
__/_  /   \ ______/ ''   /'\_,__
  | II--'''' \,--:--..,_/,.-{ },
; '/__\,.--';|   |[] .-.| O{ _ }
:' |  | []  -|   ''--:.;[,.'\,/
'  |[]|,.--'' '',   ''-,.    |
  ..    ..-''    ;       ''. '
================================
          """)


# Actual Cutscenes-------------------------------

def unknown_scene():
    os.system("cls;clear")
    slow_print("All cutscenes are completed.")
    time.sleep(1)
    display_hub()

def spawn():
    id_ = 1
    check(id_)
    os.system("cls;clear")
    slow_print("You woke up in a strange cave...\n")
    time.sleep(1)
    os.system("cls;clear")
    slow_print("You looked around, and see a light..\n")
    time.sleep(1)
    os.system("cls;clear")
    slow_print("You're in the forest. You can see trees all around you and the sun is shining.\n")
    time.sleep(1.5)
    os.system("cls;clear")
    slow_print("You start walking and soon you see a small village in the distance.\n")
    time.sleep(1)
    os.system("cls;clear")
    preset_village()
    slow_print("You go to the village and hear a villager screaming\n")
    time.sleep(1)
    os.system("cls;clear")
    preset_village()
    slow_print("You walk up to them and see a villager hysterically \n")
    time.sleep(1)
    os.system("cls;clear")
    preset_village()
    slow_print("'AHHHHH!!! SOMEONE PLEASE HELP US. PLEASE SAVE MY CHILD IN THE FOREST!!'\n")
    time.sleep(1)
    os.system("cls;clear")
    preset_village()
    slow_print("You agree to help and start your journey to defeat the monster.(obviously)\n")
    time.sleep(1)
    update(id_)

def city_first():
    id_ = 2
    if not check(id_):  # If check() returns False, stop the cutscene
        return
    os.system("cls;clear")
    preset_city()
    slow_print("\x1b[3mYou are in the city of Luterra. You can see the bustling streets and tall buildings around you.\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    preset_city()
    slow_print("\x1b[3mYou found an enormous building named 'Guild'\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    preset_city()
    slow_print("\x1b[3mYou decided to enter, and went to the receptionist.\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mRin: Welcome to the guild! is there anything we can help?\033[0m\n")
    time.sleep(1)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mYou: I'd like to register as an Adventurer.\033[0m\n")
    time.sleep(1)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mRin: Sure thing! What's your name?\033[0m\n")
    time.sleep(1)
    os.system("cls;clear")
    preset_city()
    slow_print("\x1b[3mYou sign in your information...\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    preset_city()
    slow_print(f"\033[1mRin: Congratulations! You've have become an adventurer. You'll need to do guild quests to become a full fledged adventurer!\033[0m\n")
    time.sleep(1)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mRin: There are 6 tier, G>F>D>C>B>A. You'll need to complete 3 quests to move to the next tier. You can choose your quest from the guild quest board\033[0m\n")
    time.sleep(0.5)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mRin: Here's your Guild Card, stay safe adventurer!\033[0m")
    time.sleep(1)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mYou: Thank you!\033[0m\n")
    time.sleep(1)
    os.system("cls;clear")
    slow_print("\x1b[3mYou walked back to the city...\x1b[23m\n")
    time.sleep(1)
    update(id_)


def forest():
    id_ = 3
    if not check(id_):  # If check() returns False, stop the cutscene
        return
    os.system("cls;clear")
    slow_print("\x1b[3mYou're in Heart Forest... It's so dark you can barely see a thing.\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    slow_print("\x1b[3mYou wander around trying to find monsters...\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    slow_print("\x1b[3mYou heard a big stomp.. and a munching sound..\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    slow_print("\x1b[3mYou slowly go towards the sound...\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    slow_print("\x1b[3m...You are terrified, a huge monster is munching down Red Wraith so easily..\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    slow_print("\x1b[3mThey are so hopeless, they're being eaten alive.\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    slow_print("\x1b[3mAfter the monster is done feasting, it goes away..\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    slow_print("\x1b[3mYou are safe for now.\x1b[23m\n")
    time.sleep(1)
    update(id_)

def cave():
    id_ = 4
    if not check(id_):  # If check() returns False, stop the cutscene
        return
    os.system("cls;clear")



if __name__ == "__main__":
    spawn()
    city_first()
