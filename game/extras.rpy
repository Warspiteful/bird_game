# MUSIC DISPLAY
init -5 python:
    class MusicItem:
        def __init__(self, name, file, length, about):
            self.name = name
            self.file = file
            self.length = length
            self.about = about
            self.refresh_audio()

        def refresh_audio(self):
            if not renpy.seen_audio(self.file):
                self.is_locked = True
            else:
                self.is_locked = False

    music_list= []
    music_list.append(MusicItem(_("A Seagull's Life for You{#song title}"),audio.seagull,1.04,_("Captain Langwing's theme.{#about the track}")))
    music_list.append(MusicItem(_("Rhymes from Kenneth the Crow{#song title}"),audio.crow,.57,_("Kenneth's theme.{#about the track}")))
    music_list.append(MusicItem(_("Chase!{#song title}"),audio.aus_escape,0.48,_("Aussie's escape theme.{#about the track}")))
    music_list.append(MusicItem(_("Stealth...{#song title}"),audio.aus,0.48,_("Aussie's stealth theme.{#about the track}")))
    music_list.append(MusicItem(_("An Owl's Book Club{#song title}"),audio.owl,1.12,_("Balthazar's theme.{#about the track}")))
    music_list.append(MusicItem(_("Fluttering Friends{#song title}"),audio.main,1.09,_("Main Game Theme.{#about the track}")))
    music_list.append(MusicItem(_("Harvard Birds{#song title}"),audio.main,6.12,_("Harvard Square Ambience.{#about the track}")))



init python:
    def notify_music():
        for i in music_list:
            if i.file == renpy.music.get_playing('music'):
                renpy.show_screen("notify_music",song=i.name[:-13])
    def notifyBack():
        for i in music_list:
            if i.file == renpy.music.get_playing('backing'):
                renpy.show_screen("notify_music",song=i.name[:-13])

#COUNTDOWN TIMER
screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
        ### ^this code decreases variable time by 0.01 until time hits 0, at which point, the game jumps to label timer_jump (timer_jump is another variable that will be defined later)

    bar value time range timer_range xalign 0.7 yalign 0.4 xmaximum 300 at alpha_dissolve
        # ^This is the timer bar.


#SOURCE: https://www.fortunusgames.com/post/timed-choices-code
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

init: ### just setting variables in advance so there are no undefined variable problems
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0
