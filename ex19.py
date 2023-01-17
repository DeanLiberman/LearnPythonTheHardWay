
# The textbook said a function is essentially a "mini-script." My brain almost understands this... ok, so um... what this "mini-script"(the mini-script meaning cheese_and_crackers) is doing is taking two variables, which are intergers, and printing those integers along with the text. What I don't get is where cheese_count and boxes_of_crackers come in and how they can be replaced by other variables.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    
print "We can just give the function numbers directly:"
cheese_and_crackers(1, 1)

print "OR, we can use variables from our script:"
amount_of_cheese = 1
amount_of_crackers = 2

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
