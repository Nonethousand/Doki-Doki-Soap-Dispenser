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
            ss angry "{b}Oh, I'll tell you what's happening. You've stolen my finger. And I need it back immediately."
            if (not hasFinger):
                mc "Oh... I, uh..."
                mc "I don't have it anymore. It disappeared."
    return