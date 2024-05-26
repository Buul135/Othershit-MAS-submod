init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_buul",
            category=['you'],
            prompt="I want to tell you more about me",
            pool=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        )
    )

label monika_buul:
$_history_list.pop()
menu:
    m "what do you want to tell me"
       
    "about my hobbies":
        menu:
            "I took up coding":
               "that's great [player], maybe you'll be able to expand this mod, that would make me so happy"

    "about my life":
        menu:
            "I got a new job":
                "that's great news, I'm proud of you"

    "about my body":
        menu:
            "I have a skin condition":
                "thank you for shareing that with me, I know it might be a sentive subject so I means a lot that you'd be willing to share that with me"
    "about my mental health":
        menu:
            "I have despression":
                "I'm sorry to hear that"
return 