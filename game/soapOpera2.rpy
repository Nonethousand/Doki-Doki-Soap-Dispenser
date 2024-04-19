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
        "Admire the model skeleton":
            call enterSamuel
    return

label enterSamuel:
    mc "..."
    if (admiredSecond):
        mc "No, I'm not doing this shit again."
        mc "There's no point in wasting time marveling over some nonexistent skeleton."
        $ ss_name = "???"
        show samuel neutral zorder 1 at f11
        ss "{b}Who are you calling nonexistent? I'm just as real as you are!{/b}"
        mc "..."
        mc "What the fuck."
        if (stoleFinger):
            $ ss_name = "Samuel B. Skeleton"
            ss "{b}I'm [ss_name], and I have a bone to pick with you, [player]!!!{/b}"
            mc "What the hell is happening?!"
            ss confused "{b}Oh, I'll tell you what's happening. You've stolen my finger. And I need it back immediately."
            mc "Oh... I, uh..."
            if (hasFinger):
                mc "Do you... really need it back? Are you sure I can't keep it?"
                ss angry "{b}Why are you asking me that? Of course I want it back!{/b}"
                mc "Whoa, chill. No need to point that at me. Here, just take it."
                "I toss the pinkie finger to the skeleton. He catches it and tries to reattach the joint, but fails."
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
            else:
                mc "I don't have it anymore. It disappeared."
                ss neutral "{b}...{/b}"
                ss angry "{b}YOU WHAT?!{/b}"
                mc "Wait, wait, wait! I think you're overreacting a bit, dude. It's just a dumb little finger. No need to pull out a fucking gun."
                ss "{b}Overreacting?! What if I took your finger and lost it, hm? I can guarantee you wouldn't be that happy about it.{b}"
                mc "Honestly I couldn't care less."
                ss "{b}...{/b}"
                ss "{b}You don't deserved to be merely shot by a gun.{/b}"
                ss veryangry "{cps=200}{b}YOU NEED TO BE BLASTED TO SMITHEREENS WITH THIS FUCKING ROCKET LAUNCHER!!!{b}"
                mc "What the fuck?! Where did you even get that?!"
                ss "{b}That doesn't matter! What matters is that I'm going to pull this trigger and there's nothing you can do about it!"
                mc "Wait-{nw}"
                stop music
                scene black
                $ movielength = 13.3 # https://www.reddit.com/r/RenPy/comments/oqwubr/how_do_you_make_it_so_that_the_user_cannot/
                $ movieplaying = "mod_assets/samuelMissileEnding.webm"
                call screen custommoviescreen with dissolve
    return