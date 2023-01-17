# The line below defines the variable x. From my limited understanding, the %d function basically gives the number on the right.
# Ok, now I know(knock on wood) that %d gives a number. %s gives a string. %r gives both but is for debugging for some reason. Why use %s over %r? Well, apparently %s will give a string without single quotation marks.
x = "There are %d types of people." % 10
# I think the line belows defines the variable binary as a text string, "binary."
binary = "binary"
# I think the variable below, do_not, is assigned the value of itself as a contraction.
do_not = "don't"
# The below code seems to assign the variables binary and do_not to the %s. 
y = "Those who know %s and those who %s." % (binary, do_not)

# The below code prints the variable x
print x
# The below code prints the variable y
print y
# From my limited understanding, the variable of x is assigned to the function %r
print "I said: %r." % x
# From my limited understanding, the variable of y is assigned to the function %y.
print "I also said: '%s'." % y
# This seems to be a joke
hilarious = False
# I am not sure what %r is doing in the code below, but the program does not work without it. Upon further inspection, it seems that %r will attach to the next % variable it can latch on to.
joke_evaluation = "Isn't that joke so funny?! %r"
# Below is the case in point
print joke_evaluation % hilarious
#Originally the lack of space with these two variables of strings was jarring
w = "This is the left side of..."
e = " a string with a right side."
# The code below seems to combine the two variables above to print out a longer string. And yet, due to my potty mouth and loner tendencies, I could still be being taught wrong as a joke. Take my comments with the most dire skepticism, as I am a reprobate. 
print w + e

# WARNING WARNING WARNING My Brain which is being toyed with skipped over the number 6 and went straight to 7 when doing this exercise. All seems like fun and games for now, but I must be cautious. WARNING WARNING WARNING


