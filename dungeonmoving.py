##Simple skeleton code to simulate moving between "rooms" freely.


def centerroom():
    print "You are in the center room. You can go up to the upper room."
    print "Down to the lower room."
    print "Left to the left room."
    print "Or right to the right room."
    
    choice = raw_input(">_")
    
    if choice == "left" or "LEFT" or "Left":
        leftroom()
    if choice == "right" or "RIGHT" or "Right":
        rightroom()
    if choice == "up" or "UP" or "Up":
        upperroom()
    if choice == "down" or "DOWN" or "Down":
        lowerroom()
    
        
    else:
        centerroom()
    
def lowerroom():
    print "You are in the lower room."
    print "There seems to be nothing of note here."
    print "You can go back up to the center room."
    
    choice = raw_input(">_")
    
    if choice == "up" or "UP" or "Up":
        centerroom()
    else:
        lowerroom()
        
        
def upperroom():
    print "You are in the upper room."
    print "You can go back down to the center room."
    
    choice = raw_input(">_>")
    
    if choice == "down" or "DOWN" or "Down":
        centerroom()
    else:
        upperroom()
        
def rightroom():
    print "You are in the right room."
    print "You can go back left to the center room."
    
    choice = raw_input(">_>")
    
    if choice == "left" or "Left" or "LEFT":
        centerroom()
    else:
        rightroom()
        
def leftroom():
    print "You are in the left room."
    print "You can go back right to the center room."
    
    choice = raw_input(">_<")
    
    if choice == "right" or "Right" or "RIGHT":
        centerroom()
    else:
        leftroom()
    
centerroom()
    
    
