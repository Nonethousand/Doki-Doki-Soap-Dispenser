# based on script-poemresponses.rpy

label poemresponseDDSD:
    # These variables set the amount of poems read by the player and disables
    # the skip transition.
    $ poemsread = 0
    
    # This label loops the poem music and applies the screen transition of
    # the poem responses.
    label poemresponse_loop:
        # This variable disables skipping poems.
        $ skip_poem = False

        # This if statement checks if we are playing music and the track playing 
        # is not Okay Everyone.
        if renpy.music.get_playing() and not (renpy.music.get_playing() == audio.t5 or renpy.music.get_playing() == audio.t5c):
            $ renpy.music.play(audio.t5, fadeout=1.0, if_changed=True)
        if poemsread > 0:
            scene bg courtyard
            with wipeleft_scene

        # This if statement checks if no music is playing to play Okay Everyone.
        if not renpy.music.get_playing():
            play music t5

    label poemresponse_start2:
        $ skip_poem = False
        
        if poemsread == 0:
            $ menutext = "Who should I show my poem to first?"
        else:
            $ menutext = "Who should I show my poem to next?"

        ## Main Menu of the Poem Responses
        menu:
            "[menutext]"

            "Sayori" if not s_readpoem:
                $ s_readpoem = True
                call sayoriResponse

            "Natsuki" if not n_readpoem:
                $ n_readpoem = True
                call natsukiResponse

            "Yuri" if not y_readpoem:
                $ y_readpoem = True
                call yuriResponse

            "Monika" if not m_readpoem:
                $ m_readpoem = True
                call monikaResponse

        # This variable increases the poems read by 1.
        $ poemsread += 1
        
        # This if/else statement checks if we have not yet read 3 poems for Act 2 
        # or if we are in Act 1 and haven't read 4 poems.
        if poemsread < 3 or (persistent.playthrough == 0 and poemsread < 4):
            jump poemresponse_loop

    # These variables resets the read poem variables back to normal.
    $ s_readpoem = False
    $ n_readpoem = False
    $ y_readpoem = False
    $ m_readpoem = False
    $ poemsread = 0
    return

label sayoriResponse:
    scene bg courtyard
    show sayori base rup happ mj lup zorder 1 at f11
    with wipeleft_scene
    mc "[poemDialog[poemsread]]"
    pause 1.7
    s base rdown anno lup "..."
    s base rdown anno mi lup "[player]... Did you even try today?"
    show sayori base rdown anno mj lup
    mc "No.{nw}"
    show sayori base rdown lsur mk lup
    extend ""
    mc "I forgot to make a poem last night so this was the best I could do when I finally remembered about it.{nw}"
    show sayori base e2b rdown lsur mk lup
    extend ""
    s base e1a rdown lsur mh lup "Uh, okay then."
    s "But you probably would've been better off if you showed up with nothing."
    show sayori base e1a rdown lsur mj lup
    mc "Yeah, I already thought about that."
    mc "But whatever. I made it so I sure as hell am going to show it. Even if it is shitty compared to the things I usually come up with."
    if (poemsread < 3):
        "Well, time to show someone else."
    return

label natsukiResponse:
    scene bg courtyard
    show natsuki cross happ zorder 1 at f11
    with wipeleft_scene
    mc "[poemDialog[poemsread]]"
    pause 1.5
    n "..."
    mc "Are you not going to say anything?"
    n cross happ mc "I mean, what is there to say? It's just as bad as the poems you usually make!"
    show natsuki cross happ cm
    mc "What?"
    n cross b1a happ e4b mo "Come on. You know I'm just joking."
    mc "Oh."
    n base rhip doub e1d mc "So, what's the story behind whatever this shit is?"
    show natsuki base rhip doub e1d ma
    mc "Oh, I just forgot to make a poem last night. I had to throw this together last minute."
    n base b2a rhip laug mc "Yeah, I can tell."
    n "But I won't put it against you. I've forgotten to make poems a few times myself so I know what it feels like."
    show natsuki base b2a rhip laug ma
    mc "Thanks."
    if (poemsread < 3):
        "Well, time to show someone else."
    return

label yuriResponse:
    scene bg courtyard
    show yuri base e4b rup happ lup zorder 1 at f11
    with wipeleft_scene
    mc "[poemDialog[poemsread]]"
    pause 1.2
    y base rup curi mj ldown "..."
    y base e1b rup curi mk ldown "Um... I reckon this is just something you{nw}"
    show yuri base e1a rup curi mk
    extend " threw together in a few seconds?"
    show yuri base e1a rup curi mj
    mc "Yep. I forgot to make a poem last night. So I just made this garbage so I would at least have something to show."
    y base b1c e1a rdown fine mb "Well, I'm glad you decided to try and make something even though you probably would've saved a bit of time if you didn't."
    show yuri base b1c e1a rdown fine ma
    mc "I mean, I didn't exactly try..."
    y base b1a e1a rup fine mb lup "I'd still say it technically counts as your poem for the day.{nw}"
    show yuri base b1a e1b rup fine mb lup
    extend " Even though it isn't of the best quality,{nw}"
    show yuri base b1a e1a rup fine mb lup
    extend " a haiku is still a poem like any other."
    mc "I... guess that's true. Thanks."
    y shy e1 happ awkw "N-No problem."
    if (poemsread < 3):
        "Well, I guess it's time to show someone else."
    return

label monikaResponse:
    scene bg courtyard
    show monika base rhip happ uniform zorder 1 at f11
    with wipeleft_scene
    "Time to show Monika. I hope she's done being a bitch."
    mc "[poemDialog[poemsread]]"
    pause 1.3
    m base e1b rhip happ uniform "Hm..."
    m base e1a rhip happ uniform mb "I'm guessing you forgot to make a poem and just threw this together last minute?"
    show monika base e1a rhip happ uniform ma
    mc "Yep."
    m lean happ m3 "That's okay. It's not like it happens every single day, so I don't really mind."
    m lean happ e4 m3 "Just do your best not to forget again in the future."
    show monika lean happ e4 m1
    mc "Alright. I'll try, but no promises."
    "That went surprisingly well."
    if (poemsread < 3):
        "Anyway, time to show someone else."
    return