the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']


for number in the_count:
    print "This is count %d" % number


for x in fruits:
    print "A fruit of type: %s" % x
    


for i in change:
    print "I got %r" % i
    

elements = []


for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)
    
 # now we can print them out too
for i in elements:
    print "Element was :%d" % i
    
    
    
