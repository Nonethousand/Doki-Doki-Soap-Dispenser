label soapOpera1:
    stop music fadeout 2.0
    scene bg class_day 
    with dissolve_scene_full
    play music t2
    $ restore_all_characters()

    pause 20.0
    mc "{i}Sigh...{/i}"
    "I can't help but feel like I have been doing nothing with my life."
    "It just feels like I'm stuck in an endless cycle of \"wake up, go to school, go home, and sleep.\""
    "Honestly, the only thing keeping my sanity intact because of my friends at the literature club. Okay, that may be an exaggeration, but still."
    "If Sayori never forced me to join, I probably wouldn't have any people to socially interact with. Besides Sayori, of course."
    play sound bell
    "My thoughts are interrupted by the bell, signaling the end of the school day."
    "I pick up my backpack and walk to the club."
    scene bg corridor
    with wipeleft
    "Hm."
    "Well shit. I forgot to write a poem for today. Oh well, that's a problem for future me. Which will probably be me in five minutes."
    scene bg club_day
    with wipeleft
    "I look around. It seems that I'm the first one here, which isn't really a common occurrence."
    "Usually when something like this happens, there is something going on that I don't know about."
    "I take out my phone to text the others to find out where they are, but then I remember that it's impossible due to the fact that I forgot to charge it overnight."
    "I would try charging it in this room but I never bring any of my chargers to school. So I just set my phone on a desk and think to myself."
    "Maybe I just got to the club faster than normal, as I don't really recall Monika or any of the others saying we were doing something else today."
    "Which gives me time to myself, at least for a little while. If they are coming to the club today, I probably should take a few minutes to do something while they're gone."
    menu:
        "Maybe I can take the time to quickly make a poem. It would be shitty, but it's better than having nothing to show for today. Or maybe I could do something else."
        "Make a poem":
            call makePoem from _call_makePoem
        "Admire the model skeleton":
            call samuelSkeleton from _call_samuelSkeleton
        "Exit the clubroom and dip":
            $ dipping = True
    if (dipping):
        call dipper from _call_dipper
    show sayori base cm zorder 1 at t21
    show natsuki cross happ cm zorder 2 at t22
    if (not dipping):
        "My thoughts are suddenly interrupted by Sayori and Natsuki entering the room at around the same time."
    show natsuki cross happ mc zorder 2 at f22
    n "See? I told you he would be here!"
    show natsuki cross happ cm
    mc "Eh?"
    "Yeah, I definitely missed out on something I was supposed to hear..."
    show natsuki cross happ cm zorder 1 at t22
    show sayori base mi zorder 2 at f21
    s "Hey, [player]! Why are you here? Didn't you get my text?"
    show sayori base cm
    mc "Text?"
    s 1c "Yeah! Text! I texted you during last period to meet us all in the courtyard instead of coming here!"
    mc "Well my phone is dead so I{nw}"
    show sayori base e2a shoc
    extend " had no idea you guys wanted me to do that."
    show sayori base b1b e4c rup fine ml lup zorder 2 at hf21
    s "Dead? No wonder! I thought you had broken all your fingers and you couldn't respond or something!"
    mc "Broken my fingers doing what?"
    s "..."
    s tap nerv uniform m1 awkw "I dunno. Just seems like something you would end up doing somehow."
    show sayori tap nerv uniform closed_mouth awkw
    mc "Uh... okay then."
    mc "So... did you both really need to come and get me? I feel like that should've been a one person job."
    show sayori base fine cm nobl zorder 1 at t21
    show natsuki base fine mh lhip zorder 2 at f22
    n "I forgot something in this room so I tagged along with Sayori since we were both heading here anyway."
    show natsuki base fine md lhip
    mc "Couldn't you just have come here yourself and done both?"
    n cross anno ml "Does it matter?"
    show natsuki cross anno mj
    mc "No, but-{nw}"
    n cross anno ml "Then shut your yap."
    show natsuki cross anno mj
    "She stands there for a few moments, before turning around and leaving{nw}"
    show natsuki cross anno mj zorder 2 at thide
    hide natsuki
    show sayori base fine cm zorder 1 at t11
    extend " presumably to get whatever she forgot here."
    mc "So I guess it's time for us to head to the courtyard now?"
    s base happ mb "Yeah, we should go. Natsuki will probably come down in a bit, so we can probably leave her here."
    # idk why i installed extra poses but i sure as hell am going to use them now.

    stop music fadeout 3.0

    scene bg corridor with wiperight_scene
    pause 0.8
    scene bg stairs with wiperight
    pause 0.8
    scene bg courtyard with wiperight

    play music t6

    show sayori base happ zorder 1 at t31
    show monika base happ uniform zorder 3 at t32
    show yuri base rup flus zorder 2 at t33
    "Sayori and I walk outside to find Monika and Yuri chatting away under a tree."
    show monika base rhip happ uniform mb zorder 3 at f32
    m "Well you finally decided to show up, [player]."
    show monika base rhip happ uniform cm
    mc "Yeah, yeah. Why did you suddenly decide to have the club meet outside today?"
    m base rhip anno uniform mi "It's a nice day today and I thought that it would be a good idea to spend the afternoon in the sunlight instead of being stuck in a classroom."
    m "You especially could use some sunlight anyway.{nw}"
    show sayori base vsur
    show yuri base b1f eyes_a mk
    extend " I bet once you get home from school each day you spend the rest of the night playing your weird little visual novels."
    m "Just... think of this as an opportunity to finally touch some grass."
    show monika base rhip anno uniform cm
    mc "..."
    mc "Huh??? What are you... What the hell is that supposed to mean???"
    "This sudden rudeness from Monika is a bit strange. She usually treats me pretty nicely, so it makes me wonder if I accidentally did something to piss her off."
    show monika base rhip anno uniform cm zorder 2 at t32
    show yuri base b1f eyes_a om lup zorder 3 at f33
    y "Monika... I don't think those remarks are really necessary."
    show yuri base b1f eyes_a mj lup zorder 1 at t33
    show sayori base e1a vsur mi zorder 3 at hf31
    s "Yeah, Monika. What's gotten into-{nw}"
    show yuri base b1f eyes_a mj lup zorder 1 at t44
    show monika base rhip anno uniform cm zorder 2 at t43
    show sayori base e1a vsur mi zorder 3 at t42
    show natsuki base happ oe mc lhip zorder 4 at l41
    n "Hey guys! I'm back!"
    n cross b1f mj "..."
    n cross b1f ml "Did, uh... something happen? What's with all your faces?"
    show natsuki cross b1f mj zorder 2 at t41
    show monika base rdown happ uniform mb lpoint zorder 4 at f43
    show sayori base e1a vsur mj
    m "Oh, nothing! Just a small disagreement between me and [player]. But you don't need to worry about it."
    show monika base rdown happ uniform cm lpoint zorder 4 at f43
    "I... wow. She did a complete 180 with her demeanor. That's Monika for you, I guess."

    stop music fadeout 2.0
    play music t7

    menu:
        "I could try calling her out but I don't think I'd get much out of doing that."
        "Call Monika out":
            call bullshitting from _call_bullshitting
        "Stay silent":
            call timid
        "Admire the model skeleton":
            call daveBones from _call_daveBones
        "Exit the situation and dip":
            call dipTheSecond from _call_dipTheSecond
    mc "{cps=200}{b}Oof!!!{/b}"
    "I tripped on... something, and fell on the ground. I've scraped my hands in the process."
    "They are bleeding a bit, so it looks like I have to go and clean them. I'm still on school grounds, so it would probably be fastest to just go in there and wash my hands."
    call soapOpera2
    return

label makePoem:
    "I glance around to make sure that no one snuck into the room while I was pondering what to do, then quickly grab a piece of lined paper and a pencil."
    "I'll just make a haiku, since those things can be made pretty easily and fast."
    $ madePoem = True
    $ show_poem (poem_SO1)
    "...yeah, maybe having nothing to show would be the better option. This is absolute garbage."
    return

label samuelSkeleton:
    mc "..."
    mc "Ah, the skeleton. An exquisite representation of the structure inside our human bodies. Each bone is like it's own masterpiece, carefully and meticulously crafted by nature."
    mc "What a marvelous thing it is. I wonder if I can pocket a finger from it."
    mc "..."
    mc "Yes, in fact I will. Such art shouldn't be kept in a place like this, with no one to observe it's glory."
    "I glance around to make sure that no one snuck into the room while I was admiring the skeleton, then snatch the pinkie finger from it's hand and stick it in my pocket for safekeeping."
    $ hasFinger = True
    $ stoleFinger = True
    mc "I feel like that should have been attached more securely on there. That was way easier to pull off than I thought."
    return

label dipper:
    "Hm. Yeah. It would probably be best to just dip and leave before anyone gets here. I could just text Sayori and tell them I wasn't feeling well or something."
    "I glance around to make sure that no one snuck into the room while I was pondering what to do, then quickly grab my things and leave."
    scene bg corridor
    with wiperight
    mc "Oh shit, I forgot my phone."
    "I quickly go back into the room to grab my phone, which takes like ten seconds to find."
    scene bg club_day
    with wipeleft
    pause 1.0
    scene bg corridor
    with wiperight
    "I start to walk away, but then I notice Sayori and Natsuki walking down the hallway. Well, I guess my plan to ditch the club has failed."
    "I decide to go back into the clubroom and just pretend I was standing in there the entire time just waiting."
    scene bg club_day
    with wipeleft
    "Then, I wait for them to enter the room."
    return

label daveBones:
    $ admiredSecond = True
    mc "..."
    mc "Ah, the skeleton, An exquisite..."
    show sayori base e1a curious lup
    mc "Wait, why the hell is the skeleton outside now?"
    show natsuki cross b1f lightly_amazed mj
    show sayori base e1a curious mi lup zorder 4 at f42
    show monika base rdown happ uniform cm lpoint zorder 3 at t43
    s "What skeleton?"
    show sayori base e1a curious mj lup
    mc "What do you mean what skeleton?"
    mc "Wait... where did the skeleton go?"
    mc "I swear there was a skeleton right here!"
    show natsuki cross b1f lightly_amazed ml zorder 4 at f41
    show sayori base e1a curious mj lup zorder 3
    show monika base rdown happ uniform cm lpoint zorder 2
    n "You good? I think you're probably just seeing things."
    show natsuki cross b1f lightly_amazed mj
    if (hasFinger):
        $ hasFinger = False
        "Seeing things? Is... is the skeleton not real? No, that couldn't be. I grabbed a finger from it. Unless..."
        "I reach into my pocket. Sure enough, the finger is gone."
        mc "What the..."
    else:
        "Seeing things? Is... is the skeleton not real? No, that couldn't be. Was I really... hallucinating?"
    mc "..."
    mc "I need some time to myself."
    show natsuki cross b1f lightly_amazed mj at thide
    show sayori base e1a curious mj lup at thide
    show monika base rdown happ uniform cm lpoint at thide
    show yuri base b1f eyes_a mj lup at thide
    hide natsuki
    hide sayori
    hide monika
    hide yuri
    "I run off in the other direction, contemplating this new information."
    "How could such immaculate artwork be nonexistent? How could I have even been imagining it? I saw it with my own two eyes up close!"
    "There is no way that I could've-{nw}"
    return

label dipTheSecond:
    mc "You know what, fuck this."
    mc "I need some time to myself."
    show yuri base b1f eyes_a mj lup at thide
    show natsuki cross b1f mj at thide
    show sayori base e1a vsur mj at thide
    show monika base rdown happ uniform cm lpoin at thide
    hide natsuki
    hide sayori
    hide monika
    hide yuri
    "I run off in the other direction, heading towards my house."
    "I contemplate everything that's happened so far. Why did Monika suddenly decide to be such a dipshit towards me?"
    "I genuinely don't recall doing anything to-{nw}"
    return

label bullshitting:
    mc "Bullshit.{nw}"
    show monika base b1c ed rhip angry uniform
    extend " \"Small disagreement?\" Your shitass just started being rude to me out of nowhere. I haven't even done anything annoying to you yet!"
    m base b1c e1d rhip angr uniform mi "You haven't done anything? Don't you remember yesterday?"
    show monika base b1c ed rhip angry uniform
    mc "I genuinely don't know what you are going on about right now. Are you on something?"
    m base b1c e1d rhip angr uniform mi "Don't you remember when you..."
    m base b1d e1b rhip uniform mh "{i}Sigh...{/i} Never mind. It makes sense as why you wouldn't remember."
    show monika base b1d e1b rhip uniform
    mc "Huh? Are you saying I have a bad memory or something?"
    m base b1d e1a rhip uniform mh "Well, no. It's just that..."
    m base b1d e1a rdown uniform mh lpoint "First of all, have you ever had a feeling that you've been stuck in an endless cycle of doing the same thing over and over again?"
    show monika base b1d e1a rdown uniform cm lpoint
    mc "What? I... How'd you know?"
    m base b1d e1a rdown uniform mh lpoint "Hm... I see. Well, you'll find out what I'm talking about soon enough."
    show monika base b1d e1a rdown uniform cm lpoint
    mc "What does that even..."
    mc "Actually, I'm not even going to ask what you're yapping about right now."
    mc "..."
    mc "You know what, I'm not even feeling like participating in club activities anymore, so I'm just going to go home."
    mc "I need some time to myself."
    show yuri base b1f eyes_a mj lup at thide
    show natsuki cross b1f mj at thide
    show sayori base e1a vsur mj at thide
    show monika base b1d e1a rdown uniform cm lpoint at thide
    hide natsuki
    hide sayori
    hide monika
    hide yuri
    "I run off in the other direction, heading towards my house."
    "I contemplate everything that's happened so far. What was she talking about? How did she know that I felt like I was just doing the same thing each day?"
    "I am genuinely confused as to what-{nw}"
    return

label timid:
    $ timidMC = True
    stop music fadeout 3.5
    play music t5

    "Whatever. I should probably drop it instead of escalating this situation even further."
    "So I decide to stay silent."
    show monika base rdown happ uniform cm lpoint zorder 2 at t43
    show natsuki cross b1c mc zorder 4 at f41
    n "Well, if you say it's fine then I won't question it."
    show natsuki cross b1c ma zorder 2 at t41
    show monika base rhip happ uniform mb lpoint zorder 4 at f43
    show sayori base rdown happ ma
    show yuri base b1c e1d rdown ma ldown
    m "Well now that we're all here, now would be a good time to start out club activities for the day by sharing our poems!"
    show monika base rhip happ uniform ma lpoint

    if (madePoem):
        "Well, I knew this would come eventually. Honestly though, I might be better off just showing nothing instead of showing whatever this shit is."
        "But I spent the time making it, so I might as well use it. I know it was only like fifteen seconds but still."
        mc "Let's just get this shit over with..."
        scene bg courtyard
        with wipeleft_scene
        call poemresponseDDSD from _call_poemresponseDDSD
        mc "Well, I've showed everyone this shit now. I don't really need this anymore."
        "I rip the paper in half, then crumple it up and throw it as far as I can in a random direction."
        $ madePoem = False
    else:
        "Well, I knew this would come eventually. But knowing myself, I'm glad I didn't try to come up with anything last minute."
        "I'm better off showing up with nothing than giving them whatever half-assed poem I would have came up with."
        mc "Yeah, uh, about that..."
        show monika base rhip curi uniform me ldown
        show natsuki cross b1f cm
        show sayori base b1a e1a rdown ma lup
        show yuri base b1c ea me
        mc "I forgot to make a poem last night, so..."
        m base b1b rhip uniform mb "Oh, did you?"
        m base b1a e4b rdown uniform mb lpoint "That's okay. It's not like it happens every single day, so I don't really mind."
        show natsuki cross b1c ma
        show sayori base b1a e4b rup ma lup
        show yuri base b1c eb cm
        m base b1a ea rdown uniform mb ldown "Just... do your best and make sure not to forget in the future, or else I'll really have a problem!"
        show monika base b1a ea rdown uniform ma ldown
        mc "Uh, okay. I guess I'll try, but I won't make any promises."
        "Well, that went surprisingly well."

    scene bg courtyard
    with wipeleft_scene
    "We finish our club activities for the day and say our goodbyes to each other."
    "I start running straight home, as I really need to finish this damn visual novel I have on my PC for some reason."
    "The story is quite engaging so far. It's about the MC stuck in an endless time loop. Each iteration he slowly realizes that he's stuck in an unending cycle and eventually-{nw}"
    return