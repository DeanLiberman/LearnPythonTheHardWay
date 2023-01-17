##Simple skeleton code to simulate moving between "rooms" freely.


def centerroom():
    print "You are in the center room. You can go up to the upper room."
    print "Down to the lower room."
    print "Left to the left room."
    print "Or right to the right room."
    
    choice = raw_input(">_")
    
    if choice == "left":
        leftroom()
    if choice == "right":
        rightroom()
    if choice == "up":
        upperroom()
    if choice == "down":
        lowerroom()
    
        
    else:
        centerroom()
    
def lowerroom():
    print "You are in the lower room."
    print "There seems to be nothing of note here."
    print "You can go back up to the center room."
    
    choice = raw_input(">_")
    
    if choice == "up":
        centerroom()
    else:
        lowerroom()
        
        
def upperroom():
    print "You are in the upper room."
    print "You can go back down to the center room."
    
    choice = raw_input(">_>")
    
    if choice == "down":
        centerroom()
    else:
        upperroom()
        
def rightroom():
    print "You are in the right room."
    print "You can go back left to the center room."
    
    choice = raw_input(">_>")
    
    if choice == "left":
        centerroom()
    else:
        rightroom()
        
def leftroom():
    print "You are in the left room."
    print "You can go back right to the center room."
    
    choice = raw_input(">_<")
    
    if choice == "right":
        centerroom()
    else:
        leftroom()
    
centerroom()
    
    
