cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90

# cars_driven is minimum of cars and drivers
if cars <= drivers:
    cars_driven = cars
else:
    cars_driven = drivers

cars_not_driven = cars - cars_driven
carpool_capacity = cars_driven * space_in_a_car

# Convert to float to print appropriate average
if passengers <= carpool_capacity:
    passengers_travelling = passengers
else:
    passengers_travelling = carpool_capacity
 
average_passengers_per_car = (1.0 * passengers_travelling) / cars_driven 

print "Cars ", cars, " Drivers ", drivers, " Cars_Driven ", cars_driven, " passengers ", passengers
print " carpool_capacity ", carpool_capacity, " passengers_travelling", passengers_travelling
print " average_passengers_per_car ", average_passengers_per_car
