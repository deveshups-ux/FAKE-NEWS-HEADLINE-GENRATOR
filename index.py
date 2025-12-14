# FAKE NEWS HEADLINE GENRATOR 
import random

def fakenews():
    subject = ["devesh" , "srk" , "salmon bhai" , "the group of dog" , "cow"]
    word1 = subject[random.randint(0,4)]
    # print(word1)


    actions = ["dancing" , "running" , "swimming" , "begging" , "fucking"]
    word2 = actions[random.randint(0,4)]
    #(word2)

    place = ["at delhi" , "in taj hotel" , "in home" , "on road" , "on bed"]
    word3 = place[random.randint(0,4)]

    print(f"{word1} is {word2} {word3}")

    news = input("SHOW YOU NEXT HRADLINE (YES AND NO): ")
    newheadline = news.lower()
    if(newheadline == "yes" ):
        fakenews()
    else:
        print("bye bye")    

fakenews()

    

    

