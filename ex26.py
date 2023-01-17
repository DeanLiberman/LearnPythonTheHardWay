prompt = '^_^'

print("How old are you?")
age = raw_input(prompt)
print("How tall are you?")
height = raw_input(prompt)
print("How much do you weigh?")
weight = raw_input(prompt)

print("So, you're %s old, %s tall and %s heavy.") % (age, height, weight)

from sys import argv

script, filename = argv


txt = open(filename)

print("Here's your file:")
print(txt.read())

print("Type the filename again:")
file_again = raw_input()

txt_again = open(filename)

print(txt_again.read())


print"""Let\'s practice everything you\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs."""

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - (2 + 3) 
print("This should be '5' %d") % (five)

def secret_formula(start_point):
    jelly_beans = start_point * 500
    jars = jelly_beans / 1000
    crates = jars * 100
    return jelly_beans, jars, crates
    print ("You have %d Jelly Beans, %d jars, and %d crates.") % (jelly_beans, jars, crates)


start_point = 10000
jelly_beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of %d.") % (start_point)
# it's just like with an f"" string
print("We'd have %d jelly beans, %d jars, and %d crates.") % (jelly_beans, jars, crates)

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("With a starting point of %d, We'd have {} beans, {} jars, and {} crates.".format(*formula)) % start_point






people = 20
cats = 30
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("Man's best friend reigns supreme.")

if people <= dogs:
    print("Man's best friend is rather pernicious.")

#In another universe, one less... sweet, did I remember the extra equals sign? Anyways in Python = is used for defining variables and == is used for like numerical stuff and junk
if people == dogs:
    print("The Doggy Dog World has reached an equilibrium with the world of man.")





