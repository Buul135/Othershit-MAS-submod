init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_pp",
            category=['monika'],
            prompt="Fuck",
            random=True
        )
    )

label monika_pp:
    m 3eub "hey [player]?"
    menu:
         "Yes Monika?":
            if persistent.gender == "M":
                m 1hubsb "You're the most handsome boy I've ever met"

            if persistent.gender == "F":
                m 1hubsb"You're the most beautiful girl I've ever met"

            if persistent.gender == "X":
                m 1hubsb"You're the most attractive person I've ever met"

            menu:
                "Look in a mirror and you'll see the prettest girl ever":
                    m 5fubsb "Awww, you're so sweet [player]"

                "Thank you!":
                    m 5fubsb "You deserve to be showered with compliments"

                "I disagree":
                    m 1ekblb "[player], You might not love your-self, but you are the: sweetest,kindest, most beautiful [boy] I've ever met"
                    m 5ekbfb "You've given me the word, I'll never be able to repay that, so please accept the compliment"
              
return

  
