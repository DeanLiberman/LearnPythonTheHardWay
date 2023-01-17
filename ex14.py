
# Alright, so from what I understand, this imports argv which from what I know thus far means "a variable you type in when you run the code in the terminal."
from sys import argv
# below is the variable that I define in the script itself rather than in the terminal. For now, that seems to be how this all works. 
fortuna = 4

# So to recap... %s, %r, and %d all seem to work somewhat similarly. But %s can call the strings without single or double quotations. %r will put the strings in single quotations. And %d doesn't at this... stage seem to work at all when I try to plug in intergers from the terminal line. 

# The below code are the arg variables and they seem to define user_name and whatever I add after that as the argv. I do not quite know what the script value is, unless the script value is just the filename of the script?
script, user_name, dejanus = argv
# Below the variable prompt seems to be purely aesthetic. I can make the primpt a normal less than sign or a greater than sign. I think for the next run I'll make the prompt a kissy face.
prompt = ":3"

# below, the %s thingy seems to call the variables in order from left to right. I still don't fully understand the difference between %s, %d, and %r. I am told %r is what is used for debugging and is basically a super version of %s.
# When having multiple variables, it would seem I have to put the argv variables in brackets. I wonder if I can combine argv with regular variables(probably can).
print "Hi %s, remember your old pal %s? Or your hated enemy, %d? Anyways I'm the %s script." % (user_name, dejanus,  fortuna, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" %user_name
likes = raw_input(prompt)

print "Where do you live %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

# Alright, time to test my hypothethis. The idea here is that by using the %s... thingy instead of %r the input will be given in the terminal without single or double apostrophes. I prophecize that that will happen! ...Eventually. 
# BADDA BING! Seems to work, for now. I better be cognizant as fuck about how I'm doing object oriented programming and if the writer of this guide doesn't want me to move on to Python 3 then Python 1 might have precedence over Python 2 might mean Nancy Grace Hopper controls us all. NB: I've noticed that while typing python I've seen pythong be rendered. The g might come from my chubby little fingers but knowing how my father would add "PS I love you" to the emails of his co-workers I am somewhat apprehensive about typos. 

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is, or where anything is, WE LIVE IN THE MATRIX.
And you have a %r computer. Nice. """ %(likes, lives, computer)

# the raw input variables ought to be defined beneath the question, at least for now. 



