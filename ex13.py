from sys import argv

## Basicaly, what this seems to do is have the one running the code give the first six variables in the terminal, and then asks for the seventh variable. Of course in this case all the values come from the one rnning the code

# I don't quite understand what exactly is going on below. The variables have to be listed, but the purpose is for them to be changed in the terminal... kind of. I am beyond certain that I can just write first second third fourth fixth and sixth in the terminal and not change them.

script, first, second, third, fourth, fifth, sixth = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth
print "Your fifth variable is:", fifth
print "Your sixth variable is:", sixth


# Below is a simple string that will ask for an input for the seventh variable

print "Your seventh variable is:?",
seventh = raw_input();
print "So your seventh variable is %r." % ( seventh)









