#!/usr/bin/env python3

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

print("I said: %r." % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke funny?! %r."
print(joke_evaluation % hilarious)

l = "This is the left side of ..."
r = "a string with a right side."

print(l + r)
