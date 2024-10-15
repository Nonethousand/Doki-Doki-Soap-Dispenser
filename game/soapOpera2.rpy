label soapOpera2:
    stop music fadeout 3.0
    play music t3

    scene bg corridor2 with wipeleft
    pause 0.7
    scene bg bathroom with wipeleft
    "I quickly walk over to the sink to wash my hands. I put one of my hands under the soap dispenser and use the other hand to press the button."
    "Except that I'm met with a smooth and cold wall rather than a soap dispenser button."
    mc "Wait, what?!"
    mc "Where's the dispenser?"
    "I look around frantically trying to find the dispenser, but it is to no avail. Where could it have gone?"
    menu:
        "Perhaps someone has stolen it? Maybe I should look around for clues..."
        "Look for clues":
            return
        "Try another bathroom":
            return
        "Admire the model skeleton":
            call enterSamuel
    return

label enterSamuel:
    mc "..."
    if (admiredSecond): # admired the second time
        mc "No, I'm not doing this shit again."
        mc "There's no point in wasting time marveling over some nonexistent skeleton."
        $ ss_name = "???"
        show samuel neutral zorder 1 at f11
        ss "{b}Who are you calling nonexistent? I'm just as real as you are!{/b}"
    else: # did not admire the second time
        mc "Ah, the skeleton... Uh... I can't really admire this thing in such a weird environment."
        show samuel neutral zorder 1 at f11
        ss "{b}BOOOOOOOO!!!!!{/b}" # I can't think of a better intro for him so im going with this for now
    mc "..."
    mc "What the fuck."
    if (stoleFinger): # admired the first time
        $ ss_name = "Samuel B. Skeleton"
        ss "{b}I'm [ss_name], and I have a bone to pick with you, [player]!!!{/b}"
        mc "What the hell is happening?!"
        ss confused "{b}Oh, I'll tell you what's happening. You've stolen my finger. And I need it back immediately."
        mc "Why the hell is there a talking skeleton?! I must be seeing things again. Maybe I got a concussion when I fell or something."
        ss "{b}That doesn't matter right now! What matters is you giving back my finger!"
        mc "Well, uh..."
        if (hasFinger):
            $ hasFinger = False
            mc "Do you... really need it back? Are you sure I can't keep it?"
            ss angry "{b}Why are you asking me that? Of course I want it back!{/b}"
            mc "Hey! Chill, man! No need to resort to violence! Just take the stupid thing!"
            "I toss the pinkie finger to the skeleton. He catches it and tries to reattach the joint, but repeatedly fails."
            ss ayo "{b}Now look what you've done! I can't even put it back on!{/b}"
            mc "Just try harder?"
            ss neutral "{b}Shut up! This never would have happened if you just never snatched my finger in the first place!{/b}"
            mc "How was I supposed to know the one skeleton I take a finger from is alive for some fucking reason?"
            ss "{b}Just don't steal fingers in general! What were you even trying to accomplish by taking it off of me?{/b}"
            mc "Nothing. I just wanted it."
            ss confused "{b}...{/b}"
            ss "{b}I'm not even going to question your logic any further.{/b}"
            mc "Uh, okay."
            show samuel neutral
            mc "So... why is there just a sentient model skeleton walking around?"
            ss "{b}Because.{/b}"
            mc "Because?"
            ss "{b}Yep.{/b}"
            ss "{b}Now, since you've damaged my hand permanently you're going to have to do something for me to make it up.{/b}"
            mc "Whatever. It's not like I have anything else to do anyway."
            mc "So... what is it that you need help with?"
            ss "{b}Okay, so you're probably wondering what I'm doing in this bathroom, right?{/b}"
            mc "Not really, no."
            ss "{b}Well, I came here to look for a certain object. A soap dispenser.{/b}"
            "Wait, what? He needs the soap dispenser too? What kind of devious scheme is he plotting that needs a soap dispenser?"
            ss "{b}However, when I came in here, I found nothing. How do you people even wash your hands in this school?{/b}"
            mc "Oh. Well, there are usually soap dispensers in the bathrooms, but it seems that the one here is missing."
            mc "Why do you even need a soap dispenser in the first place??"
            ss "{b}It is the last key item I need to execute my plan of WORLD DOMINATION.{/b}"
            mc "World domination? I've always wanted to do that."
            ss confused "Well, too bad. I'm doing it instead. And when I'm done, you'll just be known as the random dude that I forced to help me."
            mc "Whatever."
            scene bg corridor2 with wiperight_scene
            menu:
                "It seems this dumb skeleton is going to stay in the bathroom and look around. I might as well look for clues as well. Or I can dip and get the hell out of this place."
                "Look on wall":
                    call lookyonywally
                    return
                "Look in another bathroom":
                    return
                "Look in clubroom":
                    return
                "Exit the school and dip":
                    call bludstopdipping
                    return
        else:
            "What am I supposed to do? I stole it but when I looked at him the second time it just randomly disappeared!"
            "I guess I should come clean seeing how he's probably going to keep pestering me about it. What could possibly go wrong anyway?"
            mc "I, um, don't have it anymore. It disappeared. It was in my pocket but when I tried to take it out again it was gone."
            ss neutral "{b}...{/b}"
            ss angry "{b}IT DISAPPEARED?!{/b}"
            mc "Wait, wait, wait! I think you're overreacting a bit, dude. It's just a dumb little finger. No need to pull out a fucking gun."
            ss "{b}Overreacting?! What if I took your finger and lost it, hm? I can guarantee you wouldn't be that happy about it.{b}"
            mc "Honestly, I couldn't care less. I still have nine others."
            ss "{b}...{/b}"
            ss "{b}You don't deserve to be merely shot by a gun.{/b}"
            show ss veryangry at hf11
            ss "{cps=200}{b}YOU NEED TO BE BLASTED TO SMITHEREENS WITH THIS FUCKING ROCKET LAUNCHER!!!{b}"
            mc "What the fuck?! Where did you even get that?!"
            ss "{b}That doesn't matter! What matters is that I'm going to pull this trigger and there's nothing you can do about it!"
            mc "Wait-{nw}"
            stop music
            scene black
            $ movielength = 13.3 # https://www.reddit.com/r/RenPy/comments/oqwubr/how_do_you_make_it_so_that_the_user_cannot/
            $ movieplaying = "mod_assets/samuelMissileEnding.webm"
            call screen custommoviescreen with dissolve
    else: # did not admire the first time
        return
    return

label lookyonywally:
    scene bg corridor_forward
    with wipeleft_scene
    "..."
    "Well, this is definitely a wall."
    "Wait, what? \"Free soap dispensers in this direction, follow red arrow to find.\" Hm, seems like a trustworthy sign. Even Monika approved it, apparently."
    "I might as well follow it. Don't have any other leads anyway."
    return

label bludstopdipping:
    "..."
    "Man, what the hell is wrong with me?"
    "I must be tired or something. Skeletons aren't even real!"
    "Screw this, I'm leaving."
    scene bg corridor_forward with wiperight_scene
    pause 0.7
    scene bg stairs with wiperight
    # if submitted to monika and showed a poem instead of escalating the situation, you get to go home!!! if not you have to deal with four crazy ass bitches LMFAO good luck
    if (timidMC):
        pause 0.7
        scene bg courtyard with wiperight
        pause 0.7
        scene bg residential_day with wiperight
        pause 0.7
        scene bg kitchen with wiperight
        mc "Oh my god, I'm finally home. No more skeletons, and best of all, no more annoying bitches to deal with."
        mc "I can finally finish playing the visual novel I was yapping about earlier as well. The one I was talking about before I fell."
        mc "...Oh yeah. I fell."
        "I look down at my hands. Still bleeding. I never got to wash my hands."
        mc "Well, it's not like I can get infected from such a small injury. Right?"
        mc "...Right?"
        "I shake the thought out of my head, and go straight to my room to relax."
        scene bg bedroom with wipeleft
        mc "Time to get this shitty game over with..."
        "I turn on my gaming console and boot up the visual novel."
        scene bg bedroom_gameon
        mc "...You know what, now that, I look at the title screen more closely, the four FMCs look very similar to me for some reason."
        mc "Ah, I know. That one with the purple hair looks like Fern. Or maybe Raiden Shogun."
        mc "The one in the front and the one with the red bow look like characters from some random anime I forgot the name of."
        mc "But I don't know who the fuck that pink haired one is. Doesn't remind me of any character or person I know in real life."
        mc "Anyway, on with the game."
        scene black with wipeleft
        pause 0.7
        scene bg bedroom_night with wipeleft
        "After a few hours of playing, I finally finish the visual novel. Tears almost fall from my eyes but I manage to hold everything in."
        mc "Goddamn. That was a rollercoaster. I didn't think the MC would've had to sacrifice himself in order to stop the time loop."
        mc "And at the end, where all the other characters... actually, I can reminisce about this later. I need to go to sleep."
        stop music fadeout 1.0
        scene black with wipeleft
        play sound sleep
        pause 3
        scene bg bedroom with wipeleft
        "I sit up on my bed once I awake, stretching my arms."
    return