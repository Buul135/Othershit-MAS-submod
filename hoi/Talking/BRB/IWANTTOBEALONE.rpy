
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_idle_alone",
            prompt="I want to be alone for a bit",
            category=['be right back'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label monika_idle_alone:
    if mas_isMoniNormal(higher=True):
        if (
            mas_isMoniHappy(higher=True)
            and random.randint(1,5) == 1
        ):
            m 2eud "Are you okay?, If you want to talk about what I'm always here"
        else:
            m 2eud "I understand, see you later"

    elif mas_isMoniUpset():
              m 2tsc "bye"

    elif mas_isMoniDis():
           m 2rfp "... go then"
    
$ persistent._mas_idle_data["monika_idle_writing"] = True

return "idle"

label monika_idle_alone_callback:
     
    if mas_isMoniNormal(higher=True):    
        m 1eua "welcome back, I missed you"

    else:
       call mas_brb_generic_low_aff_callback 