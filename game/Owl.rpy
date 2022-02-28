label start_owl:
    hide misc newspaper with dissolve
    show UI
    $ adv_mode.clear_actions()
    "There's an owl perched atop a bench. It seems to be... holding a book?"
    "Well, there is a first time for everything. You can't tell what book it is, at least not from here."
    "Whatever it is, it must be tasty or really pretty to be keeping the owl's attention like that."
    "Maybe you could ask them about it."
    $ adv_mode.register_action("talk", "Owl", "owl_begin")
    $ adv_mode.register_action("move", "Seaside", "start_seagull")
    $ adv_mode.register_action("move", "Alleyway", "start_ostritch")

    call screen adv_menu


label owl_begin:
    show char bal neutral with dissolve
    "Trying to get their attention, you fly closer to the owl. It doesn't work. Their face is still buried in the book."
    menu:
        "\"What are you reading?\"":
            jump reading1
        "\"What is that?\"":
            jump what
        "Slap the book out of their wings":
            jump slap
        "Leave":
            jump main_start


# Reading Path
label reading1:
    show char bal anger
    "The owl nearly falls off the bench at the sound of your voice."
    "Once they realize who was speaking, they try and regain their composure."
label reading2:
    show char bal neutral
    un "I..."
    "They stop and clear their throat. Small bits of an owl pellet come flying out."
    un "Apologies. I am reading the collected works of the Bard of Avon"
label reading3:
    menu:
        "Who?":
            pass
label reading4:
    "They let out a long sigh."
    show char bal interested
    un "I am reading the works of William Shakespeare. Do you know whooo William Shakespeare is?"
    menu:
        "Of course I do!":
            jump readingA
        "Uh, no. Not really.":
            jump readingB
        "Willum Shake-what? I thought humans stopped using those things forever ago.":
            jump readingC

# Reading Path A
label readingA:
    show char bal happy
    un "Wonderful! It's so nice to meet someone familiar with the fine arts. I'm rereading Macbeth at the moment, we must discuss it at some point... Oh, I'm sorry but I think I missed your name..."
    menu:
        "I'm [user]":
            pass
    b "It is nice to make your acquaintance, [user]. I, am Balthazar the Owl."
    menu:
        "The pleasure is all mine.":
            b "Whoo whoo, you are too kind!"
        "It's nice to meet you too, Balthazar.":
            b "Yes indeed, we are both very lovely."
        "Put her there Bathtub!":
            b "Hmmm. That is not my name, but I do appreciate the enthusiasm."
    show char bal interested
    b "Anyways, I have a question for you, [user]."
    menu:
        "What is it?":
            pass
        "Yes?":
            pass
        "Shoot":
            pass
    jump bookClub

label readingB:
    show char bal neutral
    un "Oh my, that is fascinating. You, my friend, are very lucky!"
    menu:
        "Why is that?":
            pass
    un "Because..."
    "They stop for a moment, trying to remember a name they had never heard."
    show char bal interested
    un "I am sorry, what is your name?"
    menu:
        "I'm [user].":
            pass
    show char bal happy
    b "It's very nice to meet you, [user]. I am Balthazar the Owl. Where was I again?"
    menu:
        "Something about me being very lucky?":
            pass
    b "Ah yes! You are very lucky because you can still experience the ecstasy that is Shakespeare for the first time."
    menu:
        "And how would I go about that?":
            pass
    show char bal interested
    b "Well, you would need someone to provide you with the texts and someone to teach you how to read if you do not already know how... I think I know who can help, but first I must ask you a question."
    menu:
        "What is it?":
            pass
        "Yes?":
            pass
        "Shoot":
            pass
    jump bookClub

label readingC:
    show char bal anger
    "Balthazar slaps their own face with their wing in utter disbelief."
    show char bal neutral
    un "My, you have a lot to learn. William Shakespeare was British poet and playwright. Humans have been reading his work for hundreds of years."
    menu:
        "Reading, huh? How does one do that?":
            pass
    un "Well, it would be a little difficult to tell you. You would need someone to teach you."
    show char bal interested
    un "You know... Oh apologies, I did not catch you name."
    menu:
        "I am [user].":
            pass
    show char bal happy
    b "Ah yes, a beautiful name. It's nice to meet you [user]. I am Balthazar. Now where was I..."
    jump readingC2

label readingC2:
    show char bal interested
    b "Right! Are you interested in learning more about books and how to read?"
    menu:
        "Yes, that sounds very fun!":
            jump bookClub
        "Sorry, not right now. It was nice meeting you though.":
            show char bal sad
            b "Oh... Well that's a shame. Have a nice day, [user]."
            jump main_start

# What
label what:
    show char bal anger
    "The owl nearly falls off the bench at the sound of your voice."
    "Once they realize who was speaking, they try and regain their composure."
    show char bal neutral
    un "This..."
    un "They stop and clear their throat. Small bits of an owl pellet come flying out."
    un "Apologies. This is a book."
    menu:
        "Yes, I know that. Which one?":
            jump whatReading
        "What is that?":
            pass
    show char bal anger
    "They let out a long sigh."
label what2:
    show char bal neutral
    un "A book is a way of recording information using writing and images. It is made of many pages of paper bound together. They are usually used to tell stories or chronicle important information."
    menu:
        "I see...":
            pass
    show char bal interested
    b "You know... Oh apologies, I did not catch you name."
    menu:
        "I am [user].":
            pass
    show char bal happy
    b "Ah yes, a beautiful name. It's nice to meet you, [user]. I am Balthazar. Now where was I..."
    jump readingC2


label whatReading:
    b "I am reading the collected works of the Bard of Avon"
    menu:
        "Who?":
            jump reading2
        "Ah yes. I am familiar with Shakespeare's work.":
            jump readingA

#Slap
label slap:
    show char bal anger
    "You flap your wings and slap the book from the owl's hands. They start and jerk their head in every direction trying to figure out what just happened."
    "Their gaze lands on you as they begin to shoot daggers."
    un "What was the purpose of that you imbecile! Why would disturb me, and so aggresively nonetheless?"
    menu:
        "I was trying to get your attention!":
            un "Well why didn't you speak to me first? You know what, nevermind. What is it you need?"
            menu:
                "I wanted to know what you were reading.":
                    jump reading2
        "I wanted to know what you were reading and I couldn't see the cover.":
            un "You could have just asked you thug. There was no need to resort to physical violence."
            un "If you must know, I am reading the collected works of the Bard of Avon."
            jump reading3
        "I was trying to help you! That thing was eating you!":
            pass
    un "No it was not you simpleton! I was reading it. It's a book. It is not alive. I am in no danger!"
    menu:
        "What's a book?":
            "They let out a long sigh."
            jump what2
        "You should really thank me for saving your life. That thing clearly brainwashed you and you just don't know it.":
            un "My, you are a fool..."
            show char bal neutral
            un "This is a book. Humans make them. They cannot hurt us."
            menu:
                "Fine then. What exactly is a book?":
                    pass
            jump what2


label bookClub:
    show char bal interested
    $ adv_mode.clear_actions()
    b "Would you like to join my book club?"
    menu:
        "Of course.":
            show char bal happy
            b "Wonderful! Magnificent! Oh how resplendent! Meet me at the coffee shop and we can begin right away!"
        "I don't know how to read...":
            show char bal neutral
            b "That is quite alright my feathered friend! I can teach you! Meet me at the coffee shop and we can begin our lessons right away!"
        "I'm still not totally sure what a book is.":
            b "Still huh? Well I will change that. Meet me at the coffee shop and we will begin your lessons!"
    menu:
        "OK, I'll meet you there!":
            pass
    play music square
    $ owl_visit = True
    $ notify_music()
    $ adv_mode.register_action("move", "Coffee Shop", "coffee_start")
    $ adv_mode.register_action("move", "Seaside", "start_seagull")
    $ adv_mode.register_action("move", "Alleyway", "start_ostritch")
    show char menuBG with dissolve
    call screen adv_menu


label coffee_start:
    show bg cafe
    show char menuBG
    play music owl
    $ notify_music()
    "The coffee shop is sparsely populated, but still full of life. Humans are sitting in every nook drinking beverages and reading. It is not the full-bodied and eratic kind of life you're used to, but it is still life."
    "In one corner you see an owl with a book spread before it. You also see the baristas behind the counter making orders, a bookshelf filled to the brim, and a small cozy spot in the corner of the room."
    jump coffee_shop

label coffee_shop:
    $ adv_mode.clear_actions()
    $ adv_mode.register_action("move", "Seaside", "start_seagull")
    $ adv_mode.register_action("move", "Alleyway", "start_ostritch")
    $ adv_mode.register_action("move", "Harvard Square", "main_start")
    if owl_return == False:
        $ adv_mode.register_action("look", "Coffee Bar", "coffeeBar")
        $ adv_mode.register_action("look", "Bookshelf", "coffeeBookshelf")
        $ adv_mode.register_action("look", "Cozy Spot", "coffeeSpot")
        $ adv_mode.register_action("look", "Owl", "coffeeOwl")
    else:
        $ adv_mode.register_action("talk", "Balthazar", "bal_secret")

label coffee_action:
    show char menuBG with dissolve
    call screen adv_menu

label coffeeBar:
    "You flutter over to the counter where people are ordering and picking up drinks."
    "Behind it, a group of baristas are hard at work. They are skillfully making drinks of all kind."
    "There are supplies to make various coffees, teas, hot-chocolates, and other assorted beverages."
    "The baristas move with speed and familiarity, quickly slinging drinks to the thirsty masses."
    jump coffee_action
label coffeeBookshelf:
    "Flying over to the bookshelf grants you a view of the coffe shop's amazing collection."
    "It has literary classics and contemporary award winners. It spans numerous genres and eras."
    "It would be difficult to find only books you dislike in the mess of colorful spines."
    jump coffee_action
label coffeeSpot:
    "You flap your wings and land in what is quite possibly the coziest spot in the entire coffe shop."
    "If you were to rest here, you may never wake up. Too bad that's not really an option right now."
    "You're on a mission to make friends!"
    jump coffee_action
label coffeeOwl:
    $slight = True
    "You approach Balthazar, and as you do they look up."
    show char bal happy with dissolve
    b "Hello, [user]! I'm so glad you could join me. Shall we start your lessons?"
    menu:
        "Hello! Yes let's begin.":
            pass
        "Not right now. In a little bit.":
            show char bal neutral
            b "Ah, OK. Let me know when you are ready."
            jump coffee_action
    show char bal neutral
    b "Wonderful, wonderful! We'll start with this."
    "Balthazar pulls out a workbook and lays it flat on the table. They launch into a lesson about the basics of reading. They speak passionately, but still give you space to ask questions."
    "To your surprise, you understand what they're saying! As the lesson continues you begin to understand the human language more and more. Eventually, everything clicks and you can read!"
    show char bal interested
    b "OK, now that you have a grip on the language, we can see how well you do on your own. Please read the following sentence and speak it aloud."

label coffeeOwlA1:
    menu:
        "The squirrel climbed the tree while holding a nut.":
            jump coffeeOwlA2
        "The screw chinned the bee well rolling a hut." if slight:
            show char bal interested
            b "Well, that's not right. Why don't you try again?"
            $slight = False
            jump coffeOwlA1
        "The tree climber the squirrel while hiding the nut.":
            show char bal neutral
            jump coffeeOwlA3
label coffeeOwlA2:
    show char bal happy
    b "Hoooowee, you got it right! Way to go friend. How about this one?"
    jump coffeeOwlAB

label coffeeOwlA3:
    b "Close, but that is not what it says exactly. The squirrel is actually the one climbing the tree in this sentence. How about we try another?"
    jump coffeeOwlAB

label coffeeOwlAB:
    $slight = True

label coffeeOwlB:
    menu:
        "The bird trilled the man feeder with bees and otter scrambled flights." if slight :
            $slight = False
            show char bal interested
            b "Well that didn't make much sense at all... let's try that one again!"
            jump coffeeOwlB
        "The man filled the bird feeder with seeds and other scrumptious delights.":
            show char bal happy
            b "Ohohoh, you're smarter than I thought my feathered friend! Let's try one more."
        "The bird feeder was a man who filled birds with seeds and other aviary treats.":
            show char bal interested
            b "I mean, I suppose that one makes sense but that's not quite what we're looking for."
            b "You see, the bird feeder in this case is an actual seed dispenser, not the man himself."
            b "We can try one more. Maybe you will get the hang of it!"
    show char bal neutral
    jump coffeeOwlBC

label coffeeOwlBC:
    $slight = True

label coffeeOwlC:
    menu:
        "Making the Ibiza a smart fleece by beast, the cat reflowered the delerious cry from your sky." if slight:
            $slight = False
            b "I-"
            show char bal interested
            b "I have no clue what you just said, but that is alright. Let's try again!"
            jump coffeeOwlC
        "Taking the rat apart piece by piece, the pizza devoured the delicous guy from down below.":
            show char bal sad
            b "That was one of the scariest things I have ever heard. Why is the pizza alive and eating a rat?"
            show char bal neutral
            b "You know what, nevermind. You were close, but not perfect."
            b "You have still made a lot of progress, which is amazing! I am so proud of you."
        "Taking the pizza apart piece by piece, the rat devoured the delicious pie from on high.":
            b "Wow! You learn quick friend. You have come a long way in this short amount of time, and I could not be more proud of you!"
    menu:
        "Thanks Balthazar. It was a lot of fun for me as well!" :
            pass
    show char bal happy
    b "Of course, of course. The honor was all mine."

label bal_secret:
    $ owl_return = True
    show char bal happy
    b "You know, can I let you in on a little secret of mine?"
    menu:
        "Certainly!":
            pass
        "Of course Balthazar, anything for you my friend.":
            pass
        "Normally I would say yes, but I really need to get going. Sorry.":
            b "Oh, yes of course. Don't let me hold you for too long. Enjoy your day, friend!"
            $ adv_mode.clear_actions()
            $ adv_mode.register_action("move", "Seaside", "start_seagull")
            $ adv_mode.register_action("move", "Alleyway", "start_ostritch")
            $ adv_mode.register_action("move", "Harvard Square", "main_start")

            $ adv_mode.register_action("talk", "Balthazar", "bal_secret")
            jump coffee_action
    show char bal neutral
    b "I have always wanted to be a teacher. Since I came out of that egg, it has been the only thing I want to do with my life."
    show char bal happy
    b "So thank you. Thank you for being a great friend and letting me live that dream."
    b "I was unsure of myself for so long, but now I think I have what it takes."
    menu:
        "I think you're an amazing teacher. Pursue that dream and help more birds learn about the magic of books!":
            jump owlEndingA
        "I think you'd do alright. You might not be perfect, but you could certainly learn how to help others learn.":
            jump owlEndingB
        "I don't think that's a good idea Balthazar. You're not exactly stellar at this whole teaching thing.":
            jump owlEndingC

label owlEndingA:
    show char bal happy
    b "Really? Thank you so much, [user]. That makes me feel so much better."
    b "In fact, I think I'll begin making plans for a school right now!"
    show char bal neutral
    b "The only problem is that I cannot do it by myself. I need someone to work with me, to help me help others."
    show char bal interested
    b "What if that bird was you [user]? What do you say, will you be my teaching assitant?"
    menu:
        "Of course!":
            pass
    scene black with dissolve
    "You join Balthazar as a teaching assitant in their new school for birds."
    "The two of you work hard, and soon everyone in the city square is literate! Not only have you made a new friend, but you have also elevated bird society."
    return
    #ENDING

label owlEndingB:
    show char bal neutral
    b "You're right, [user]. I still have some growing to do, but one day I'll make a damn fine teacher. Thanks for letting me try it out on you!"
    scene black with dissolve
    "Balthazar spent the next couple of months researching teaching styles. Eventually, they opened up a school for birds, which was wildly successful."
    "Balthazar became overworked, but slowly taught every bird in the square how to read."
    "You didn't become very close to them, but at least you helped elevate bird society."
    return
    #ENDING
label owlEndingC:
    show char bal sad
    "Balthazar begins to cry, tears dripping onto their beautiful feathers."
    b "How could you say that to me, [user]? I helped you and tried to be a friend, but you still insult me like that? What did I ever do to you?"
    show char bal anger with dissolve
    b "I cannot stand to look at you any longer. Leave now, before I make you."
    scene black
    "After seeing Balthazar burst into tears, you leave the coffee shop, never to return. After the incident they spent many months inside, all on their lonesome."
    "It was quite some time until you saw them return to the square to read. Sadly, they never started that school for birds."
    return
    #ENDING
