# I am going to attempt to write a string based version of the cheese_and_crackers function.

def tortillas_and_avocado (type_of_tortilla, type_of_avocado) :
    print "You have a %s tortilla!" % type_of_tortilla
    print "You have a %s avocado!" % type_of_avocado
    print "Ever think of going vegan?"
    print "Seemingly irrelevant non-sequitor."
    
tortillas_and_avocado ("whole wheat", "hass")

# Okie Dokie, so it would seem that I kinda understand how to use a print function. If the function itself prints, then there's no need to add a print line. So this is a string based version of the the interger script in ex19.py. Let me see if I can replicate the rest of that but accomdate it for strings.

tortilla_dea = "White grain"
avocado_modo = "Rainbow" 

tortillas_and_avocado (tortilla_dea, avocado_modo)
# Might be my imagination but someone is stealing my "t" 

tortillas_and_avocado ("whole" + " wheat", "rain" + "bow")



# Up til now I have made a string based version of exercise 19. I wonder if I can combine string variables and math without changing the function's %s to %r. (I don't think I can)

tortillas_and_avocado ( tortilla_dea + 100, avocado_modo + 69.)


