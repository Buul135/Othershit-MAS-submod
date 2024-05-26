init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_pd",
            category=['monika'],
            prompt="I want to thank you",
            pool=True
        )
    )


label monika_pd:
$_history_list.pop()
m 1etd "what do you want to thank me for?"
menu:
    "For letting me be my-self":
        m 1wubsc "... You really feel that way?"
        m 2rubsd "I know many people don't feel like they can be them-selfs"
        m 2hubfb "I'm so happy you trust me that way"
        m 5hubfb "while were here I want to thank you for letting me be my-self as well, I love you"

    "For surporting me and being there for me":
        m 1wubft "... It makes me so happy you feel that way"
        m 1fubfb "I'll always be there for you"
        m 5hubfb "I want to thank you for being there for me, I love you"

    "For being so cute":
        m 7tubfb "I should be the one thanking you for that"
        m 5hubfb "You're as cute as them come, I love you"
    "For everything":
        m 2wubft "..."
        m 2hubfb "I love you so much [player]"
        m 3subfb "You're my everything, I can never express how much you mean to me"
        m 1hubfb "So you thanking me, I feel like a kid of christmas"
        m 5fubfb "I want to thank you [player],"
        m 1dubftpb "For teaching me how to love and saving me life"
        m 1fubftpb "For that, i'm enternaly greatful"
return "love"