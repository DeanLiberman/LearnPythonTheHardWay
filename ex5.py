name = 'Zed A Shaw.'
age = 35 # Not a lie, apparently
height = 74 # inches
weight = 180 # lbs
euro_height = height * 2.54
euro_weight = weight * 0.454
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
destiny = 'The King who heavily dislikes chess save for the horsies because the horsies confused the other players at the beginning and the horsies are pretty dang based.'

print "Let's talk about %s" % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# the below line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
  age, height, weight, age + height + weight)
print "Let's talk about %r." % destiny
print "I am %r centimeters tall." % euro_height
print "I weigh %r kilos." % euro_weight

