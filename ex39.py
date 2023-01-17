# Odd. In the manual, they suggested using "[", but "{" was the solution on the dvd and what this computer seems to accept. Maybe dict needs to use "{? It seems I can use '[' for other cities.
# Even practicing Python might be a bad idea. If I take what they did with my car keys as an example, I could be blasting some other angry incel's ears with loud music every time I try to print.
# But with that sort of logic, I should avoid having ever pressed any button anywhere. There's no gurantee that pressing the "I" key on my computer will NOT nuke the entire world. 
# I predict I shall die in despair, and my afterlife, if I get one, shall be miserable too. 
# Because in my gut I know. There's no beating the Golden Bitch or gaslighters. The only time they COULD have been beaten was back when one was a child.


states = {
  'Oregon': 'OR',
  'Florida': 'FL',
  'California': 'CA',
  'New York': 'NY',
  'Michigan': 'MI'
  
}

cities = {
  'CA': 'San Francisco',
  'MI': 'Detroit',
  'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Flordia's abbreviation is ", states['Florida']

#print '-' * 10
#print "Michigan's abbreviation is: ", states['Michigan']
#print "Florida's abbreviation is: ", states['Florida']

print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Flordia has: ", cities[states['Florida']]

print '-' * 10
for state, abbrev in states.items():
  print "%s is abbreviated %s" % (state, abbrev)
  
print '-' * 10
for abbrev, city in cities.items():
  print "%s has the city %s" % (abbrev, city)

print '-' * 10
for state, abbrev in states.items():
  print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
  
print '-' * 10
state = states.get('Texas', None)

if not state:
  print "Sorry, no Texas."
  
city = cities.get('TX", "Does Not Exist')
print "The city for the State 'TX' is: %s" % city
  


  
  

  
  
