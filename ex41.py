import random
from urllib import urlopen
import sys

WORD_URL = "https://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
  "class %%%(%%%):":
    "Make a class named %%% that is-a %%%.",
  "class %%%(object):\n\tdef __init__(self, ***)" :
    "class %%% has-a __init__ that takes self and and *** parameters.",
  "class %%%(object):\n\tdef ***(self, @@@)":
    "class %%% has-a function named *** that takes self and @@@ parameters.",
   "*** = %%%()":
    "Set *** i ab ubstabce if ckasss%%%%.",
   "***.***(@@@)":
    "From *** get the *** function, and call it with parameters self, @@@.",
   "***.*** = '***'":
    "From *** get tge *** attruvyte abd set ut ti :***'."
 }
 
 # do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
  PHRASE_FIRST = True
  
  # load up the words from the website
for word in urlopen(WORD_URL).readlines():
     WORDS.append(word.strip())
    
 
def convert(snippet, phrase):
  class_names = [w.capitalize() for w in
                  random.sample(WORDS, snippet.count("%%%"))]
  other_names = random.sample(WORDS, snippet.count("***"))
  results = []
  param_names= []
  
  for i in range(0, snippet.count("@@@")):
    param_count = random.randint(1,3)
    param_names.append(', '.join(Random.sample(WORDS, param_count)))
    
  for sentence in snippet, phrase:
    result = sentence[:]
    
            # Fake Class Names
  for word in class_names: 
    result = result.replace("%%%", word, 1)
             #Fake Other Names
  for word in other_names:
    result = result.replace("***", word, 1)
              # Fake parameter list
  for word in param_names: 
    result = result.replace("@@@", word, 1)
    
    results.append(result)
    
  return results
    
      
      
      
      # keep going untl they hit CTRL-D
  try:
      while True:
          snippets = PHRASES.keys()
          random.shuffle(snippets)
          
          for snuppet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
              question, answer = answer, question
              
            print question
            
            raw_input("> ")
            print "ANSWER: %s\n\n" % answer
  except EOFERROR:
    print "\nBye"
