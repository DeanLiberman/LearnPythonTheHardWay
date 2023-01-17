from sys import exit
from random import randint

##debugging notes -- curly brackets and regular brackets keep getting mixed up.


class Scene(object):

    def enter(self):
      print "This scene is not yet configured. Sublcass and implement enter()."
      exit(1)
        
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True: 
            print "\n--------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        
class Death(Scene):
    
    quips = [
    "You died. You kinda suck at this.",
    "Your mom would be proud... if she were smarter.",
    "Such a luser.",
    "I have a small puppy that's better at this."
    ]
    
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)
        
class CentralCorridor(Scene):
    def enter(self):
     print "The Gothons of Planet Percal 25 have invaded your ship and destroyed"
     print "your entire crew. You are the last surviving member and your last"
     print "mission is to get the neutron destruct bomb from the Weapons Armory,"
     print "put it in the bridge, and blow the ship up after getting into an "
     print "escape pod."
     print "\n"
     print "You're running down the central corridor to the Weapons Armory when"
     print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
     print "flowing around his hate filled body. He's blocking the door to the"
     print "Armory and about to pull a weapon to blast you."
     
     action = raw_input(">_ ")
     
     if action == "shoot!":
      print "Quick on the draw you yank out your blaster and fire it at the Gothon."
      print "His clown costume is flowing and moving about his body which throws"
      print "off your aim. Your laser hits his costume but misses his core entiretly. This"
      print "completely ruins his brand new costume his mother bought him, which"
      print "makes him fly into a rage and blast you repeatedly in the face until"
      print "you are dead. Then he eats you."
      return 'death'
    
     elif action == "go back":
      return 'central_corridor'
     
     elif action == "dodge!":
      print "Like a world class boxer you dodge, weave, slip and slide right"
      print "as the Gothon's blaster cranks a laser past your head."
      print "In the middle of your artful dodge your foot slips and you"
      print "bang your head on the metal wall and pass out."
      print "You wake up shortly after only to die as the Gothon stomps on"
      print "your head and eats you."
      return 'death'
     
     elif action == "tell a joke":
      print "Lucky for your they made you learn Gothon insults in the academy."
      print "You tell the one Gothon joke you knkw:"
      print "Lbhe zbgurevf sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr"
      print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
      print "While he's laughing you run up and shoot him square in the head"
      print "putting him down, then jump through the Weapon Armory door."
      return 'laser_weapon_armory'
      
     else:
      print "DOES NOT COMPUTE!"
      return 'central_corridor'
    
class LaserWeaponArmory(Scene):


    def enter(self):
         print "You do a dive roll into the Weapon Armory, crouch and scan the room"
         print "for more Gothons that might be hiding. It's dead quiet, too quite."
         print "You stand up and run to the far side of the room and find the"
         print "neutron bomb in its containiner. There's a keypad lock on the box"
         print "and you need the code to get the bomb out. If you get the code"
         print "wrong 10 times then the lock closes forever and you can't"
         print "get the bomb. The code was 3 digits."
         code = "%d" % (randint(1,9))
         cheat = "sixtynine"
         
         guess = raw_input("[keypad]> ")
         ##!!!!
         guesses = 0
         
         while guess != code and guess != cheat and guesses < 10 and guess != "go back":
          print "BZZZZED! WRONG!"
          guesses += 1
          guess = raw_input("[keypad]> ")
          
         if guess == code:
          print "The container clicks open and the seal breaks, letting gas out."
          print "You grab the neutron bomb and run as fast as you can to the"
          print "bridge where you must place it in the right spot."
          return 'the_bridge'
          
         elif guess == "go back":
          print "You decide to head back to the Central Corridor. Alas..."
          return 'central_corridor'
          
         elif guess == cheat:
          print "The container clickss open and the seal breaks, letting gas out."
          print "You grab the neutron bomb and run as fast as you can to the"
          print "bridge where you must place it in the right spot."
          return 'the_bridge'
         
         else:
          print "The lock buzzes one last time and you hear a sickening"
          print "melting sound as the mechanism is fused together."
          print "You decided to sit there and finally the Gothons blow up the"
          print "ship from their ship and you die."
          return 'death'
         
class TheBridge(Scene):
    
    def enter(self):
        print "You burst onto the bridge with the neutron destruct bomb"
        print "under your arm and suprise 5 gothons who are trying to"
        print "take control of the ship. Each of them has an even uglier"
        print "clown costume than the last. They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to see it off."
        
        action = raw_input("> ")
        
        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door. Right as you drop it a"
            print "Gothon shoots you right in the back killing you."
            print "As you die you see another Gothon frantically trying to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            return 'death'
            
        elif action == "go back":
         return 'central_corridor'
        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm."
            print "and the Gothons put their hands up and begin to sweat."
            print "You inch backwards to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off this tin can."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return 'the_bridge'
            
class EscapePod(Scene):
    
    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes. It seems like"
        print "hardly any Gothons remain on the ship, so your run is clear of"
        print "interference. You get to the chamber with the escape pods,  and"
        print "now need to pick one to take. Some of them could be damaged"
        print "but you do not have the luxury to examine them. A pristine mobius symbol"
        print "and a pristine 0 catches the corner of your eye."
        print "There's 5 pods, which one do you take?"
        
        cheat2 = "80"

        good_pod = randint(1,2)
        #my "partner" is clearly griefing me. 
        guess = raw_input("[pod #]> ")
        
        
        
        if guess == cheat2:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below. As it flies to the planet, you look"
            print "back and see your ship implode and then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time. You won!"
            exit(1)
            
        elif guess == "go back":
         return 'central_corridor'
         
         

            
            
class Map(object):

    scenes = {
       'central_corridor': CentralCorridor(),
       'laser_weapon_armory': LaserWeaponArmory(),
       'the_bridge': TheBridge(),
       'escape_pod': EscapePod(),
       'death': Death(),

    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
            
        
            
       
