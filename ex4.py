# the variable below represents the amount of vehicles present
cars = 100
#in the line below, reducing the number for space_in_a_car to 4 rather 4.0 results in the variable carpool going from being a floating variable to being more plain. I should try and play around with the drivers variable to see if numbers become floating if just one of their composite floats. Yup, seems to be.
#the variable below represents the space in a car
space_in_a_car = 4
# the variable below represents the amount of drivers present. I am reticent to use the word "this" because of some incredibly snotty intellectual joke my brother who can actually code knows. 
drivers = 30.0
# the variable below represents the passengers
passengers = 90
# the variable below is a composite variable based upon the difference between the variable of cars and the variable of drivers
cars_not_driven = cars - drivers
# the variable below carries the same value as drivers
cars_driven = drivers 
# had an error with the below line due to a missing "n" where "cars driven" should have been, but instead "cars drive" was typed instead Man I miss my family, I hope I'm not damned to eternal hellfire.
carpool_capacity = cars_driven * space_in_a_car
# the variable below is the quotient of two variables.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

