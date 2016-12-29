# -*- coding: utf-8 -*-
cars = 100
#给cars赋值

space_in_a_car = 4.0
#给space_in_a_car赋值
drivers = 30
#给drivers赋值
passengers = 90
#给passengers赋值
cars_not_driven = cars - drivers
#给carr_not_driven赋值，为cars-drivers
cars_driven = drivers
#把drivers的值赋给cars_driven
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
# 把右边公式的值计算后赋给左边

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
#输出“”号内的文字，以及输出变量