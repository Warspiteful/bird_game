label start_seagull:
    hide misc newspaper with dissolve
    play music seagull
    $ notify_music()
    show bg docks with dissolve
    if seagull_return == True:
        jump cap_return

    "The briny perfume of the harbor infuses the air all around you. It's a smell like nowhere else in the world."
    "Waves thrum against the keels of ferries and yachts and antique man-o-wars lashed to the dock. Yet there is something... uneasy about this idyllic place."
    "Something you can't quite put your feather on..."

label seagull_visit_def:
    $ count = 0
    $ adv_mode.clear_actions()
    $ adv_mode.register_action("look", "Moored Ship", "cap_ship")
    $ adv_mode.register_action("look", "Diver", "cap_diver")
    $ adv_mode.register_action("look", "Coin-Op Tower Viewer", "cap_viewer")


label seagull_visit:
    show char menuBG with dissolve
    if get_choice_exhaust("cap_ship") and get_choice_exhaust("cap_viewer") and get_choice_exhaust("cap_diver"):
        $ adv_mode.clear_actions()
        $ adv_mode.register_action("talk", "Seagull", "cap_talk")

    call screen adv_menu

label cap_first:
    if count == 0:
        "A voice like a steel rake running over barnacles breaks the silence just above you."
        "You try to locate its source, but whatever it is seems to be flying about with too much maddening energy for you to pin."
        $ first = False
    if count == 3:
        show char lan happy with dissolve
        un "By Ahab's leg! The map is here!"
        "The blasting power of this seagull's arrival nearly throws you off your feet."
        "His wings flutter and flap madly as he turns and turns about on the wharf."
    $ count += 1
    return

label cap_ship:
    un "Where great ladies sleep..."
    call cap_first from _call_cap_first

    $ set_choice_exhaust("cap_ship")
    jump seagull_visit


label cap_diver:
    un  "Where banners are false..."
    call cap_first from _call_cap_first_1
    $ set_choice_exhaust("cap_diver")
    jump seagull_visit

label cap_viewer:
    un "Where the horizon greets ye as a friend..."
    call cap_first from _call_cap_first_2
    $ set_choice_exhaust("cap_viewer")
    jump seagull_visit

label cap_talk:
    show char lan happy with dissolve
    menu:
        "Who are you?":
            jump cap_who
        "...":
            show char lan neutral
            un "Aye! The strong, silent type! The trademark spirit of a true sailor!"
            un "Well, maybe not a lookout, but a deck-swabber, no doubt!"
        "Whoa! Chill out!":
            show char lan neutral
            un "Arr! Ye'd ask me to cool my blood when we stand at the cliffs of glory?!"
    menu:
        "Who are you?":
            jump cap_who

label cap_who:
    show char lan neutral
    l "Cap'n Quint Langwing, at yer service!"
    l "Scourge o' the Orkneys! Dread pirate-king of the Auster-lands!"
    l "Liberator and professional treasure-hunter extraordinaire!"
    menu:
        "Pleased to meet you!":
            l "Aye, shipmate. I speak of a mountain, made entirely..."
            menu:
                "What's a jonah?":
                    show char lan anger
                    l "A curse upon a vessel, cloaked in the flesh of its own crew!"
                    menu:
                        "I see...":
                            pass
                    jump cap_treasure
                "What's this about treasure?":
                    l "Aye, treasure! The finest riches yer avian mind can imagine!"
        "What's this about treasure?":
            l "Aye, treasure! The finest riches yer avian mind can imagine!"
        "Austerlands? What are those?":
            l "Never mind that now!"

label cap_treasure:
show char lan happy
l "The map is close... I can smell it. We're breathin' its same air says I, shipmate!"
menu:
    "Map to what?":
        pass
    "I only smell the ocean...":
        l "Arr! Forgive an ol' Cap'n 'is sailor-speak. Fifty years before the mast will add its share of salt to the sharpest o' noodles!"
    "Um, I don't think maps can breathe...":
        l "Dun' ye be daft now, shipmate! Fifty years before the mast and I've finally found it, so will ye help or hinder me?"
l "But before we go any farther, might I be askin' yer name, shipmate?"
menu:
    "Certainly! My name is [user].":
        l "Arr! A name like a northern gale! 'Tis the horn-call of adventure, says I!"
        l "A fine shipmate ye may yet be, if ye too be willing t'suffer the hunt for the Midderlode."
        menu:
            "The Midderlode?":
                jump cap_mid
    "What's it to you?":
        show char lan anger
        l "Dun' ye be daft now, shipmate! Fifty years before the mast and I've finally found it, so will ye help or hinder me?"
        menu:
            "The Midderlode?":
                jump cap_mid
            "Would you please stop speaking in riddles?":
                show char lan anger
                l "I speak the word o' the wind, shipmate! Or be ye a Jonah, with ears plugged to the truth o' the sails?"
                menu:
                    "I'm sorry. I didn't mean to be rude...":
                        l "I appreciate ye're magnanimity, shipmate. Now, will ye help me find the map to the Midderlode?"
                        jump cap_mid_cont
                    "Ugh, why do I always get the crazy ones?":
                        jump cap_badEnd
label cap_mid:
    l "Aye, the Midderlode!"

label cap_mid_cont:
    show char lan neutral
    l "'Tis a mountain, north o' nowhere, which in its vast belly holds a trove of treasure no creature of our ilk can deny!"
    l "Aye, shipmate. I speak of a mountain, made entirely..."
    show char lan happy
    l "...of bread crumbs!"
    menu:
        "Amazing":
            pass
        "You must be joking...":
            pass
    l "Aye! That's exactly what I said to the old gull who first told me the tale o' the Midderlode."
    l "He spoke in deeper riddles than I, says... I!"
    show char lan neutral
    l "But the one riddle... aye, he made certain I heard that one. And its words've been branded in mine head ever since:"
    l '"Seek ye the place where banners are false..."'
    l '"Where great ladies sleep..."'
    l '"And where the horizon greets ye as a friend."'
    l '"Lay ye then down \'neath the stone sky..."'
    show char lan happy
    l '"And there, within the vessel of the lost, ye\'ll find the map!"'
    menu:
        "Fascinating!":
            pass
    show char lan neutral
    l "Aye! But the last bit still needs solvin'."



label cap_return:
    show char lan neutral
    l "Will ye help me find the map, shipmate?"
    menu:
        "Of course, I'll do what I can.":
            l "Arr! No cap'n could ask more o' their crew!"
            l "Now, if we search the clues the old gull spoke of, we may yet find that map just lying about, says I!"
            $ adv_mode.clear_actions()
            $ adv_mode.register_action("look", "Moored Ship", "cap_ship_search")
            $ adv_mode.register_action("look", "Diver", "cap_diver_search")
            $ adv_mode.register_action("look", "Coin-Op Tower Viewer", "cap_viewer_search")
        "I can't right now, but I will if I can return in time!":
            l "Make haste, shipmate! The Midderlode waits for no bird!"
            $ seagull_return = True
            jump main_start

label cap_search:
    show char menuBG
    "You recall the riddle Captain Langwing told you, remembering the \"stone sky\" and the \"vessel of lost souls.\" Maybe you have an idea?"
    call screen adv_menu
label cap_ship_search:
    menu:
        "Maybe that ship there is the vessel of lost souls?":
            pass
    show char lan happy
    l "Aye, shipmate! I'll search it myself!"
    "Captain Langwing waddles awkwardly down the gangway onto the nearby vessel. He searches for a long while, but still returns dejected."
    show char lan sad
    l "Nary a map in sight mine eyes ain't lain upon before, shipmate. Perhaps somewhere else?"
    $ set_choice_exhaust("cap_ship_search")
    jump cap_search
label cap_diver_search:
    menu:
        "What about under the wharf?":
            pass
    show char lan happy
    l "Ah yes, I see a hole nearby for going belowdecks!"
    "Captain Langwing slips beneath an open grate."
    "You hear his fluttering echo below, followed by boisterous, joyful caws. The Captain emerges... with the map!"
    l "We did it, shipmate! The map to the Midderlode is ours!"
    menu:
        "Where was it?":
            jump cap_where
        "I'm sorry, we? I figured it out.":
            show char lan anger
            l "Aye... and ye're old Cap'n crawled through the bilge o' the Charles River to get it, says I."
            menu:
                "Where was it?":
                    jump cap_where
                "Ugh. Seems like far too much dirty work for me.":
                    jump cap_midEnd
                "Oh please. I bet you've never even been to the Orkneys, you old sea-rat.":
                    jump cap_badEnd

label cap_viewer_search:
    menu:
        "Maybe you can use the viewfinder to look around?":
            pass
    show char lan happy
    l "Not a bad idea, shipmate!"
    "Captain Langwing flutters over to the viewfinder and peers through it. But though he is able to see far in all directions, he returns downcast."
    show char lan sad
    l "I see nothing but the wind and the rain, shipmate. Perhaps somewhere else?"
    $ set_choice_exhaust("cap_viewer_search")
    jump cap_search

label cap_where:
    l "'Neath the stone sky of this very wharf, shipmate! Tucked in an ol' used bottle o' rum."
    l "A message in a bottle... 'tis the oldest medium o' the lost, says I!"
    l "Now... where is that mountain?"
    "Captain Langwing opens the map and pores over it, inspecting every inch."
    "Curiously, you don't see the awe or epiphanic ecstasy you were expecting. Instead, the Captain begins grinding his beak..."
    show char lan sad
    l "Oh dear. By the ill January wind, all is lost, says I..."
    menu:
        "What's wrong?":
            pass
    l "The Midderlode... I was told it was a mountain. And so it is, says I."
    l "But it's a mountain that lies nearly a thousand nautical miles away... on an island."
    menu:
        "What's so bad about it being on an island?":
            pass
    l "Oh dear. Oh I'd hoped it wouldn't come to this... But nay."
    l "A Cap'n can't right well lie to their crew on the eve of adventure. It's time I came clean with ye, shipmate."
    l "Ol' Langwing, yer Cap'n..."
    l "...is a'feared of the ocean."
    menu:
        "What makes it so scary?":
            show char lan neutral
            l "I once followed the Labrador wind too far north. For eight days I saw nary a hint of land or beast or fish."
            l "Nearly starved! Ever since... just the thought of open water..."
        "Wait...really?":
            call cap_fear from _call_cap_fear
        "You've got to be kidding me.":
            call cap_fear from _call_cap_fear_1

    menu:
        "Well no wonder... that sounds terrifying!":
            show char lan sad
            l "Aye. But 't'wasn't the starvin' or the dyin' o' thirst that was so haunting..."
            l "It was the feeling of being so immensely alone. "
            l "The sea is a powerful god, shipmate. But one grace it has no power to give is company."
        "But you still call yourself a Captain?":
            "Aye! This bewitchment may have me yet, but I was still a force of the waves in my prime, says I!"
    jump cap_companyChoice

label cap_fear:
    show char lan neutral
    l "Aye. Been a'feared of it since I followed the Labrador wind too far north."
    l "For eight days I saw nary a hint of land or beast or fish. Nearly starved!"
    l "Ever since... just the thought of open water..."
    return

label cap_companyChoice:
    menu:
        "Of course not, Captain. You need a friend to have good company.":
            jump cap_goodEnd
        "Even still... a Captain should be able to withstand a little loneliness...":
            l "Ye may say so, shipmate. But until ye've floated in solitude upon the womb of that endless watery grave, ye'll never know what it means to truly be alone."
            menu:
                "But you don't have to be alone, Captain. I'll sail with you.":
                    jump cap_goodEnd
                "Oh c'mon. Now you're just being melodramatic.":
                    jump cap_midEnd
        "Right...sure":
            jump cap_midEnd
        "Oh please. I bet you've never even been to the Orkneys, you old sea-rat.":
            jump cap_badEnd

label cap_goodEnd:
    show char lan happy
    l "Aye... aye, ye're right, shipmate! What's a Cap'n without a crew?"
    l "'Tis a keel with no rudder, says I! A mast with no sail!"
    l "I'll get me a crew. We'll lash ourselves to the westerlies and hunt that horizon."
    l "The very bones of Davy Jones' locker will quake at our passing!"
    l "The Midderlode will be ours, friend! Yours and mine! I'll share it with ye and any other beast of the air with the tuft t'fly with me!"
    "The Captain puffs out his chest, and you can practically hear the stove of his heart humming with a newfound, passionate flame."
    l "We return here on the morrow, shipmate! Nay, first mate! Gather what companions ye may."
    l "At first light, we sail east, to glory! To bread!"
    scene black with dissolve
    "As you leave the frenetic Captain behind, a rush of unbidden and wholly welcome light fills your heart."
    "You may have little or no money in your purse, and nothing particular to interest you on shore, but these things no longer matter."
    "No longer will you remain grim about the mouth. No longer shall the damp, drizzly November of your soul hold sway."
    "No longer shall you pause involuntarily before coffin warehouses, or bring up the rear of every funeral you meet."
    "You are bound for adventure; bound for the sea!"
    "And sure, the Captain you sail under might be afraid of water, but nothing cures fear like a friend holding steady before the mast."
    "And that, at least, you know you can do quite well."
    return


label cap_midEnd:
    show char lan neutral
    l "Aye, mate."
    l "I smell a smell o' spirit in ye, an' 't'may yet be steered 'way towards adventurin,' but it's clear now yer soul's unfit for the life o' the gale, says I."
    l "Mine own expeditions be needin' hardier mates than ye. Fare ye well wherever ye fare."
    l "Perhaps I'll raise a grog t'ye on a still and cloudless day."
    "The Captain flies off, away towards the sun."
    scene black with dissolve
    "You can't be sure, but something inside tells you that you have either just dodged the world's biggest bullet... or missed out on the opportunity of a lifetime."
    return
label cap_badEnd:
    show char lan anger
    "The Captain's eyes narrow to black slits. Something mad rustles in the darkness behind them. Is that... thunder?"
    l "Ye bilge-scrapin' scabrous dog! Ye canker on the keel o' the sea itself!"
    l "Aye, ye curse 'pon the dreams of Triton an' Neptune an' all the gods o' the deeps! "
    l "Ye foul-retched gale o' the green easterlies, crawlin' o'er the reek of rotted seal meat too sickly for the likes of barnacles!"
    l "May ye ne'er see home o'er the other side of the sun, ye Jonah!"
    l "May the great fish that comes t'swallow ye keep ye tendin' the fires o' its belly 'til the sea gives up her dead!"
    l "May the salt-spouse what waits for ye abandon all delusion, and leave their tower-walk bare..."
    l "...that no eye may ever again call upon the horizon for sight of ye, ye plank-destined regurgitation of a sickly flounder, ye --"
    scene black with dissolve
    "The force of it all is too much. If you don't leave now, this \"captain\" may never stop."
    "He may be afraid of water -- he may be a complete fraud, for all you know -- but one thing is certain: he could bellow a ship hard against a headwind, if the sails offended him."
    return
