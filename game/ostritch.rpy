label start_ostritch:
    hide misc newspaper with dissolve
    show bg alley with dissolve
    play music aus
    $ renpy.music.set_volume(0.0, delay=0, channel=u'backing')
    play backing aus_escape
    $ notify_music()
    $ adv_mode.clear_actions()
    "As you enter the alleyway you can hear a rustling come from deep inside this forgotten crevice."
    "Trash cans and dumpsters line the walk, and above you there a numerous fire escapes criss-crossing over the sides of apartments."
    $ adv_mode.register_action("look", "Trash Bags", "aus_trashBags")
    $ adv_mode.register_action("look", "Fire Escape", "aus_fireEscape")
    $ adv_mode.register_action("look", "Dumpster", "aus_dumpster")
    $ adv_mode.register_action("look", "Trash Can", "aus_trashCan")

label aus_start:

    call screen adv_menu

label aus_trashBags:
    "The stench from these bags is palpable at the entrance of the alley. Up close, it's almost unbearable."
    "As you approach them a rat scurries towards. You quickly fly back. Maybe stick to breadcrumbs..."
    $ set_choice_exhaust("aus_trashBags")

    jump aus_start

label aus_fireEscape:
    "You fly up to the first level on the fire escape to see what you can find."
    "To your surprise, your met with the maw of a house cat."
    "Just as the feline prepares to pounce, you take flight and avoid an unseemly demise."
    $ set_choice_exhaust("aus_fireEscape")

    jump aus_start

label aus_dumpster:
    "You fly up onto the lip of the dumpster, but one look makes your stomach churn."
    "Contrary to popular belief, you actually have some class. Unlike those trash pandas roaming about."
    "You decide it's best to leave the toxic waste to them."
    $ set_choice_exhaust("aus_dumpster")
    jump aus_start

label aus_trashCan:
    "You approach the covered trash can, but before you can land on it a large bird pops out of it."
    show char aus anger Can with dissolve
    un "Get away from me! I'm never going back! You can't make me!"
    menu:
        "Woah, what's wrong?":
            jump aus_trashCanA
        "Hey, I'm not going to hurt you!":
            "The big bird calms down for a moment and looks at you intently."
            un "You promise? How am I supposed to know you're not lying?"
            menu:
                "I don't even know what you're running from!":
                    pass
            un "Haha, that's fair. I'm trying to stay away from zookeepers."
            menu:
                "Why are you running from zookeepers?":
                    jump aus_ZooKeepers
        "Everything's going to be ok! Who's trying to hurt you?":
            un "It's the zookeepers! They're the reason I'm so jumpy all the time."
            menu:
                "Why are the zookeepers trying to hurt you?":
                    jump aus_ZooKeepers

label aus_trashCanA:
    show char aus neutral Can
    un "Huh? Oh, you're not one of them. You're not wearing their uniform. Plus you're way too small. And a bird. Unless you're a spy!"
    menu:
        "A spy for who?":
            show char aus sneak Can
            un "Don't play dumb, spy. You know you're working for those nasty zookeepers. I mean, look in the mirror. Classic zookeeper spy clothes!"
            menu:
                "Didn't you just say I wasn't dressed like them?":
                    pass
        "I'm not a spy, I don't even know what you're talking about.":
            un "That's exactly what a spy would say! You're even the right size to be a zookeeper. There's no fooling me!"
            menu:
                "Didn't you just say that I'm not big enough to be a zookeeper?":
                    pass
        "Why would I want to spy on you?":
            un "You know exactly why, spy! You can't fool me!"
            menu:
                "But I'm not a human, like you just said.":
                    pass
    show char aus neutral Can
    un "Oh, uh. Wait yeah, you aren't. You swear you aren't one?"
    menu:
        "I swear I'm not a zookeeper. I don't think they'd even hire me.":
            pass
    un "Haha, yeah that's a good point."
    menu:
        "Why are you running from zookeepers anyways?":
            jump aus_ZooKeepers

label aus_ZooKeepers:
    show char aus sneak Can at imagebox
    un "They want to take me back to that cell they call a home! But I won't go back. No I can't go back!"
    show char aus neutral Can
    un "So I've been hiding here for a while. They're looking all over for me and I'm scared they'll find me."
    menu:
        "I can help you hide from them! No one should have to go where they don't want to.":
            show char aus happy Can
            un "Really? Thank you so much-"
            show char aus neutral Can
            "The big bird stops, unsure of what to call you."
            un "I'm sorry, what's your name?"
            menu:
                "I'm [user].":
                    pass
            show char aus happy Can
            a "Nice to meet you, [user]. I'm Aussie, Aussie the Ostrich."
            menu:
                "It's nice to meet you too!":
                    pass
            jump aus_escape
        "I'm sorry to hear that. I wish you the best of luck!":
            show char aus happy Can
            un "Thank you! Good luck with... Whatever you're doing!"
            jump main_start

label aus_escape:
        a "So, if the zookeepers come this way looking for me, I'll need you to-"
        show char aus neutral Can at imagebox
        "Before Aussie can finish her thought, you hear someone at the mouth of the alleyway. You turn and see a pair of zookeepers."
        $  renpy.music.set_volume(0, delay=3, channel=u'music')
        $ renpy.music.set_volume(1, delay=3, channel=u'backing')
        $ notifyBack()

        show char aus sneak Can

        "The flashlight wielding weirdos are closing in quickly. You need to act quickly if you want to save Aussie!"
        $ time = 15                                    ### set variable time to 3
        $ timer_range = 15                             ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'aus_escape_fail'                   ### set where you want to jump once the timer runs out
        show screen countdown
        menu:
            "Aussie, stay in there and hide! I'll divert their attention.":
                hide screen countdown
                jump aus_escape1A
            "Aussie, get your big dumb body over in those trash bags! They'll never be able to tell the difference.":
                hide screen countdown
                jump aus_escape1B
            "Stay here dummy! I'll try and draw them away.":
                hide screen countdown
                jump aus_escape1C
label aus_escape_fail:
    scene black with dissolve
    "You're not fast enough to help Aussie! You freeze up in the moment and end up getting Aussie caught. Before you know it she's being taken away by the zookeepers. If only you could try again..."
    scene bg alley at bgbox
    show char aus happy Can at imagebox
    show UI
    $  renpy.music.set_volume(1, delay=3, channel=u'music')
    $ renpy.music.set_volume(0, delay=3, channel=u'backing')
    $ notify_music()
    jump aus_ZooKeepers

label aus_escape1A:
    show char aus sneak Can
    a "Understood!"
    a "Aussie quickly folds back into the trash can, making the alleyway inconspicuous once again."
    jump aus_escape2

label aus_escape1B:
    show char aus anger noCan
    "Aussie opens her beak to protest, but decides against it. She listens to your rude command and gets into the pile of garbage bags."
    show char aus sneak noCan
    "She blends right in with the bags, but it's unclear whether it will stand up to the scrutiny of the zookeepers."
    jump aus_escape2

label aus_escape1C:
    show char aus anger Can
    a "He- Hey that wasn't very nice!"
    show char aus sneak Can
    "Aussie tries to protest her mistreatment but returns to the cover of the trash can anyways."
    "Trying to draw the zookeepers' attention, you dash out of the alleyway, screaming and squaking the entire time."


label aus_escape2:
    "The two zookeepers are close. What do you do?"
    $ time = 15                                     ### set variable time to 3
    $ timer_range = 15                             ### set variable timer_range to 3 (this is for purposes of showing a bar)
    $ timer_jump = 'aus_escape_fail'                   ### set where you want to jump once the timer runs out
    show screen countdown

    menu:
        "Act nonchalant and sit on the trash can's lid.":
            hide screen countdown
            "You perch on the trash can, doing your best impression of your normal self. The zookeepers continue to draw closer. Maybe they won't notice?"
            "Apparently not. The zookeepers close in on the trash can and push you away."
            jump aus_escape3
        "Fly out of the alleyway to draw their attention away.":
            hide screen countdown
            "You fly out of the alleyway, slightly startling the zookeepers. They keep pushing, but maybe they won't find Aussie?"
            jump aus_escape3
        "Hop on the can to get the zookeepers' attenion, revealing Aussie.":
            hide screen countdown
            show char aus anger Can
            "The zookeepers close in on you like a pack of dogs. They force you out of their way and rip the top off the trash can, revealing Aussie."
            "She screams in surprise as the zookeepers wrestle her out of the makeshift home."
            "It doesn't take long for the zookeepers to get a hold on Aussie. As they do, she calls out to you."
            jump aus_badEnd


label aus_escape3:
    $ time = 15                                     ### set variable time to 3
    $ timer_range = 15                             ### set variable timer_range to 3 (this is for purposes of showing a bar)
    $ timer_jump = 'aus_escape_fail'                   ### set where you want to jump once the timer runs out
    show char aus anger noCan
    "You watch, powerless, as the zookeepers open the trash can and reveal Aussie. She pops out of the can surprised, and begins to run down the alleyway."
    menu:
        "Fly after her!":
            hide screen countdown
            "You catch up to Aussie quickly and hop onto her back."
            jump aus_escape4
        "Leave Aussie to her own devices":
            hide screen countdown
            "Aussie runs as far and as fast as she can, but she's not very familiar with her surroundings."
            "It doesn't take long for the zookeepers to catch her. As they do, she calls out to you."
            jump aus_badEnd

label aus_escape4:
    show char aus neutral noCan
    a "I don't know where I'm going here, so you have to tell me where I should head to!"
    $ time = 15                                     ### set variable time to 3
    $ timer_range = 15                             ### set variable timer_range to 3 (this is for purposes of showing a bar)
    $ timer_jump = 'aus_escape_fail'                   ### set where you want to jump once the timer runs out
    menu:
        "We have to take four left turns! (Betray Aussie)":
            hide screen countdown
            a "OK, [user], I'm trusting you here!"
            "Aussie takes four left turns, just like you said to. Your devious directions land her right back where she started: in the hands of the zookeepers."
            "It doesn't take long for the zookeepers to get a hold on Aussie. As they do, she calls out to you."
        "Take a left, cross the street, and then turn down the alleyway on the right. They'll never find us!":
            hide scren countdown
            a "OK, [user] I'm trusting you!"
            "Aussie follows your diligently laid directions, and eventually you reach an even more secluded alleyway. She quickly finds a new trash can to hide in."
            $ renpy.music.set_volume(0.0, delay=3, channel=u'backing')
            $ renpy.music.set_volume(1.0, delay=3, channel=u'music')
            $ notify_music()
            show char aus happy Can
            a "Thank you so much. [user]. I never would've made it out of there without you. I really owe you a lot."
            menu:
                "It was nothing.":
                    pass
                "I'm always to help those in need!":
                    pass
            a "Y'know, because of you, I might be able to see my family."
            menu:
                "Oh? Your family isn't at the zoo?":
                    pass
            show char aus neutral Can
            a "No, they're not. I'm not from around here. I was brought here from my home."
            show char aus sad Can
            a "I don't necessarily mind being here either, I just miss my family. The zoo was a nice enough place to live, I just miss the people I love."
            menu:
                "I'm so sorry to hear that, Aussie. What are you going to do now?":
                    pass
            show char aus neutral Can
            a "Honestly? I'm not sure. I don't know if I can make it back to my family, and even if I could, I don't know where I would start."
            menu:
                "I believe in you, Aussie. I know you have it in you to get back home!":
                    pass
            a "Really? Do you think it's possible?"
            menu:
                "Absolutely! And I'll even help you out.":
                    pass
            show char aus happy Can
            a "Thanks [user], it really means a lot that you would do so much for me."
            scene black with dissolve
            "With your help, Aussie begins to search for a way back home. It takes many months, but the two of you are able to avoid the zookeepers and find out where Aussie comes from."
            "She eventually finds passage back to her homeland, and invites you to join her! The two of you travel all the way to Australia, where Aussie is able to reunite with her family."
            return

label aus_badEnd:
    show char aus sad noCan
    a "How could you do this to me, [user]! Why would you betray me like this?"
    scene black with dissolve
    "Tears stream down Aussie's face as she is forced into the back of the van."
    "Who knows what she'll face back at the zoo. It was clearly something she wanted to stay away from..."
    return
