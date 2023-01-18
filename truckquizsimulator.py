def truckquiz():
      rightanswers = 0
      wronganswers = 0
      
      print "What is a truck?"
      answer = raw_input(">_<")
      if answer == "a truck" or answer == "truck" or answer == "atruck":
        print "correct!"
        rightanswers += 1
      else: 
        print "No, that is incorrect."
        wronganswers += 1
      
      
      
      if wronganswers >= 1:
        print "You've reached the maximum amount of wrong answers on this truck quiz."
        print "Better luck next time!"
        exit(1)
        
        
      if rightanswers >= 1:
        print "You have passed the truck quiz!"
        print "Congratulations!"
        exit(1)
        
        
      
truckquiz()
      
      
