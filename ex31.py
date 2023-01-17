print "You enter a dark room with two doors. Do you go through the left or right?"

door = raw_input(">_")

if door == "left":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off."
        print "Do you stand still, or run away?"
        print "1. Stand still."
        print "2. Run away."
        facial = raw_input("> ")
        if facial == "1":
          print "The bear eats your face and goes back to sleep."
        elif facial == "2":
          print "You try to run away, but such a cowardly act don't let you save face."
        else:
             print "You try to do %s, but it just doesn't work out." % facial
           
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
        
elif door == "right":
    print "You stare into the endless abyss at Cthulu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
         print "The insanity rots your eyes into a pool of muck. Good job!"
         
elif door == "3":
    print "Monty Hall laughs manically as he reveals that switching the doors don't actually increase your odds of getting the prize"
    
elif door == "Moonwalk backwards out of the room.":
    print "You thought for yourself?! We can't have that. You are gangstalked and tortured to death. END" 
 
else:
    print "You stumble around and fall on a knife and die. Good job!"
    # When I copy Zed Shaw's code exactly, I do not seem to be griefed. Well, not exactly true, I am griefed before as well.
