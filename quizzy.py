def quiz():

    print "What is 1 + 2?"
    answer = raw_input(">_ ")
    answers = 0

    

    
    if answer == "3" or "Three" or "three":
        answers += 1
     
    
    
    print "What is the capital of New York?"
    answer = raw_input(">_ ")
    if answer == "Albany" or "albany" or "ALBANY":
        answers += 1
    
    print "What is the color red spelled backwards?"
    answer = raw_input(">_ ")
    if answer == "der" or "Der" or "DER":
        answers += 1
    
    print "What is the color of the sky?"
    answer = raw_input(">_ ")
    if answer == "blue" or "BLUE" or "Blue":
        answers += 1
    
    print "How many questions have I asked in this file including this one?"
    answer = raw_input(">_ ")
    if answer == "Five" or "5" or "five":
        answers += 1
    
    if answers >= 5:
        print "You got all answers correct!"
    
    else:
        print "You got %r answers out of 5 correct." % (answers)
    
quiz()
         
         
         
