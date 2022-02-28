define un = Character("???")
define b = Character("Balthazar")
define a = Character("Aussie")
define l = Character("Captain Langwing")
define pc = Character("[user]")

init -6 python:
    audio.seagull = "audio/A Seagull_s Life for You.wav"
    audio.aus_escape = "audio/Aussie the Ostrich - Chase.wav"
    audio.aus = "audio/Aussie the Ostrich - Stealth.wav"
    audio.main = "audio/Fluttering Friends.wav"
    audio.crow_rap = "audio/Kenneth the Crow - Rap.wav"
    audio.crow = "audio/Kenneth the Crow.wav"
    audio.owl = "audio/Owl_s Book Club.wav"
    audio.main_amb = "audio/Ambient SFX/BirdsChirpingAMB_TitleScreen.wav"
    audio.square = "audio/Ambient SFX/CitySquareAMB_MainArea.wav"
    audio.button = "audio/FlutteringFriendsSFX.wav"
    renpy.music.register_channel("ambient", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix=u'', file_suffix=u'', buffer_queue=True, movie=False, framedrop=True)
    renpy.music.register_channel("backing", "music", True)
    renpy.music.register_channel("first", "sfx", False)
    renpy.music.register_channel("second", "sfx", False)
    renpy.music.set_volume(0.1,0,"first")
    renpy.music.set_volume(0.1,0,"second")

if (renpy.music.is_playing("second")):
    while (renpy.music.is_playing("second")):
        pause 1.0
image bg black:
    "images/black_background.png"

image bg cafe:
    zoom 0.35
    "images/Backgrounds/001_cafe.png"

image bg square:
    zoom 0.35
    "images/Backgrounds/002_square.png"

image misc newspaper:
    zoom 0.35
    "images/Backgrounds/002_square_newspaper.png"

image bg alley:
    zoom 0.35
    "images/Backgrounds/003_alleyway.png"

image bg yard:
    zoom 0.35
    "images/Backgrounds/004_yard.png"

image bg docks:
    zoom 0.35
    "images/Backgrounds/005_docks.png"


image UI = "gui/100_UI.png"


image char menuBG = "images/102_nocharbackground.png"
image char aus neutral noCan = "images/Character Sprites/Aussie the Ostrich/Neutral.png"
image char aus anger noCan  = "images/Character Sprites/Aussie the Ostrich/Angry.png"
image char aus happy noCan  = "images/Character Sprites/Aussie the Ostrich/Happy.png"
image char aus sad noCan  = "images/Character Sprites/Aussie the Ostrich/Sad.png"
image char aus neutral Can = "images/Character Sprites/Aussie the Ostrich/Neutral_TrashCan.png"
image char aus anger Can  = "images/Character Sprites/Aussie the Ostrich/Angry_TrashCan.png"
image char aus happy Can  = "images/Character Sprites/Aussie the Ostrich/Happy_TrashCan.png"
image char aus sad Can  = "images/Character Sprites/Aussie the Ostrich/Sad_TrashCan.png"
image char aus sneak Can = "images/Character Sprites/Aussie the Ostrich/Sneaky_Trashcan.png"
image char aus sneak noCan = "images/Character Sprites/Aussie the Ostrich/Sneaky.png"


image char bal neutral = "images/Character Sprites/Balthazar the Owl/Neutral.png"
image char bal anger = "images/Character Sprites/Balthazar the Owl/Angry.png"
image char bal sad = "images/Character Sprites/Balthazar the Owl/Sad.png"
image char bal interested = "images/Character Sprites/Balthazar the Owl/Interested.png"
image char bal happy = "images/Character Sprites/Balthazar the Owl/Happy.png"

image char ken neutral = "images/Character Sprites/Kenneth the Crow/Neutral.png"
image char ken anger = "images/Character Sprites/Kenneth the Crow/Anger.png"
image char ken sad = "images/Character Sprites/Kenneth the Crow/Sad.png"
image char ken happy = "images/Character Sprites/Kenneth the Crow/Happy.png"
image char ken thinking = "images/Character Sprites/Kenneth the Crow/Thinking.png"
image char ken passion = "images/Character Sprites/Kenneth the Crow/Passion!.png"
image char ken wings = "images/Character Sprites/Kenneth the Crow/Clipped Wings.png"

image char lan neutral = "images/Character Sprites/Langwing the Seagull/Neutral.png"
image char lan anger = "images/Character Sprites/Langwing the Seagull/Angry.png"
image char lan sad = "images/Character Sprites/Langwing the Seagull/Sad.png"
image char lan happy = "images/Character Sprites/Langwing the Seagull/Happy.png"
