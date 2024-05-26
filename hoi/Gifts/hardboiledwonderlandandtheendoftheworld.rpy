init 5 python: 
    addReaction("mas_reaction_hardboiledwonderland", "hardboiledwonderland", is_good=True, exclude_on=["d25g"]) 

label mas_reaction_hardboiledwonderland: 
    m 1eub "[player], this is so sweet"
    m 1sub "you remembed my favourite book"
    m 3eub "I can read books here," 
    m 5lud "but only thought a pdf type file, and that's just doesn't feel the same"
    m 6fublb "thank you [player] for letting hold these books again"
    m 1fublb "this means so much to me"
    m 1sublb ".. it's even got that new book smell" 
    $ mas_receivedGift("mas_reaction_wonder") 
    $ store.mas_filereacts.delete_file(mas_getEVLPropValue("mas_reaction_hardboiledwonderland", "category")) 
    $ mas_gainAffection(modifier=2.0)
    return 