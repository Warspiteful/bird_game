# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")



# The game starts here.

init:
    $ imagebox = Position(xpos=0.142, ypos=0.694)
    $ namebox = Position(xpos=0.123, ypos=0.687)
    $ bgbox = Position(xpos=0.65, ypos=0.708)

label before_main_menu:
   play music main noloop
   play ambient main_amb loop
   return


label start:
    $ seagull_return = False
    $ owl_visit = False
    $ owl_return = False

    call init_module_adv from _call_init_module_adv
    scene bg black
    show char menuBG at imagebox
    show UI
    play music square
    $ notify_music()
    $ user = renpy.input("What is your name?")
    $ user = user.strip()
    if not user:
        $ user = "Chrys Anthem"
    show bg square at bgbox with dissolve
    hide UI
    show UI
    "It's a lovely Autumn afternoon and you're a peckish pigeon off to make some friends."
    "It might be tough but you've spent the past couple days building up courage."
    show misc newspaper at bgbox with dissolve
    "There's a old, human man throwing down bread crumbs in this city square."
    "Birds like bread, right? You suppose this is a good a place as any to start off."
    $ adv_mode.clear_actions()
    jump main_start

label main_start:
    show bg square with dissolve
    play music square
    $ notify_music()

    show char menuBG
    $ adv_mode.clear_actions()
    if owl_visit == False:
        $ adv_mode.register_action("look", "Owl", "start_owl")
    else:
        $ adv_mode.register_action("move", "Coffee Shop", "coffee_start")
    $ adv_mode.register_action("move", "Seaside", "start_seagull")
    $ adv_mode.register_action("move", "Alleyway", "start_ostritch")


    call screen adv_menu

define t = Character("Tipsy")
# Creation of the room menu
label example_room_menu:
    # First we clear all old ADV actions
    $ adv_mode.clear_actions()

    # Now we register the new ADV menu interactions
    $ adv_mode.register_action("look", "Around", "example_room_look_room")
    $ adv_mode.register_action("look", "Information board", "example_room_look_board")
    $ adv_mode.register_action("look", "Students", "example_room_look_students")
    $ adv_mode.register_action("look", "Street Lamps", "example_room_look_lamp")
    $ adv_mode.register_action("talk", "Crow", "start_crow")
    $ adv_mode.register_action("talk", "Seagull", "start_seagull")




    $ adv_mode.register_action("think", "Self", "example_room_think_self")

    $ adv_mode.register_action("use", "Street Lamps", "example_room_use_lamp")

    $ adv_mode.register_action("move", "Club Rooms", "example_room2_enter")

    # After we registered all ADV actions, we call the ADV menu
    call screen adv_menu


# The labels the menu jumps to
label example_room_look_room:
    "This is an example to show you the potential and the features of the ADV menu."
    $ set_choice_exhaust("example_room_look_room")
    jump example_room_menu


label example_room_look_board:
    "Hello and welcome to the presentation of the Japanese Style Adventure Menu."
    "When you are done familiarizing yourself with the menu, move to the Club Rooms and talk with Tipsy for an in-depth explanation."
    $ set_choice_exhaust("example_room_look_board")
    jump example_room_menu


label example_room_think_self:
    if get_choice_repeat("example_room_think_self") == 0:
        "Hm... I don't have any idea who I am..."
    elif get_choice_repeat("example_room_think_self") == 1:
        "Come on, you have to get yourself together, THINK!"
        "..."
        "Still nothing."
    elif get_choice_repeat("example_room_think_self") == 2:
        "Maybe if I try to remember REALLY REALLY hard, something will come to my mind."
        "*concentrate*"
        "*CONCENTRATE*"
        "... No use... there is nothing inside my head..."
        $ set_choice_exhaust("example_room_think_self")
    else:
        "I don't think that thinking any harder will change anything at this point."
    jump example_room_menu


label example_room_look_students:
    if get_choice_repeat("example_room_look_students") == 0:
        "A bunch of students are running around."
    elif get_choice_repeat("example_room_look_students") == 1:
        "Hey, one of them has a very nice jacket!"
    else:
        "They are just students."
        if get_choice_repeat("example_room_look_students") == 2:
            "Wait... maybe I am a teacher?"
            $ set_choice_exhaust("example_room_look_students")
    jump example_room_menu


label example_room_look_lamp:
    "Electric lamps in the style of an old gas lamps are decorating the path."
    $ set_choice_exhaust("example_room_look_lamp")
    jump example_room_menu


label example_room_use_lamp:
    if get_choice_repeat("example_room_use_lamp") == 0:
        "How do you find the light switch? This is a street lamp."
    else:
        "As hard as you try to look, you can not find a switch for the lamp."
        $ set_choice_exhaust("example_room_use_lamp")
    jump example_room_menu




####### ROOM 2 ########
label example_room2_enter:
    scene bg club
    jump example_room2_menu


label example_room2_menu:
    # First we clear all old ADV actions
    $ adv_mode.clear_actions()

    # Now we register the new ADV menu interactions
    $ adv_mode.register_action("look", "Around", "example_room2_look_room")

    $ adv_mode.register_action("talk", "Tipsy", "example_room2_talk_tipsy")

    # This is a demonstration how you can enable or disable a action based on its state
    if not get_choice_exhaust("example_room2_use_tipsy"):
        $ adv_mode.register_action("use", "Tipsy", "example_room2_use_tipsy")

    $ adv_mode.register_action("move", "Club Rooms", "example_room_enter")

    # After we registered all ADV actions, we call the ADV menu
    call screen adv_menu


label example_room2_look_room:
    "This is an example to show you the potential and the features of the ADV menu."
    "Here you can find Tipsy, who can provide you with more information."
    $ set_choice_exhaust("example_room2_look_room")
    jump example_room2_menu


label example_room2_talk_tipsy:
    show tipsy
    t "Hey, I am Tipsy and I am here to help you with the Adventure Menu."
    t "I hope on your way to me you already got a small impression for what this module can do."
    hide tipsy
    jump example_room2_menu


label example_room2_use_tipsy:
    show tipsy
    if get_choice_repeat("example_room2_use_tipsy") == 0:
        t "Of course you have to \"use\" the NPC. Great Job."
    if get_choice_repeat("example_room2_use_tipsy") == 1:
        t "Hey, stop using me, once was enough!"
    if get_choice_repeat("example_room2_use_tipsy") == 2:
        t "I said, stop using me!"
    if get_choice_repeat("example_room2_use_tipsy") == 3:
        t "..."
        t "Are you finished? Good, because I now remove this option!"
        $ set_choice_exhaust("example_room2_use_tipsy")
    hide tipsy
    jump example_room2_menu
