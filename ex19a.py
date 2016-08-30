def apples_and_oranges(apple_count, orange_count):
	print "you have %d apples." % apple_count
	print "you have %d oranges." % orange_count
	print "i feel a fruit salad coming on."
	print "get a fork.\n"
	
print "give function direct numbers:"
apples_and_oranges(40, 50)

print "or, use variables:"
amount_of_apples = 20
amount_of_oranges = 30

apples_and_oranges(amount_of_apples, amount_of_oranges)

print "we could do math:"
apples_and_oranges(5 + 7, 9 - 5)

print "variables and math:"
apples_and_oranges(amount_of_apples +3, amount_of_oranges - 7)

print "ask for raw input"
amount_of_apples = int(raw_input("enter apples  "))
amount_of_oranges = int(raw_input("enter oranges  "))

apples_and_oranges(amount_of_apples, amount_of_oranges)

print "math with raw input"
amount_of_apples = int(raw_input("enter amount of apples  "))
amount_of_oranges = int(raw_input("enter amount of oranges  "))

apples_and_oranges(amount_of_apples + 5, amount_of_oranges - 2)

print "randomly generated amount"
import random
amount_of_apples = random.randrange(1, 50)
amount_of_oranges = random.randrange(1, 50)

apples_and_oranges(amount_of_apples, amount_of_oranges)

print "math and random generator"
import random
amount_of_apples = random.randrange(1, 50)
amount_of_oranges = random.randrange(1, 50)

apples_and_oranges(amount_of_apples / 2, amount_of_oranges * 2)

print "user input with random generator"
amount_of_apples = int(raw_input("enter apples to add  "))
amount_of_oranges = int(raw_input("enter oranges to add  "))

import random
generated_apples = random.randrange(1, 10)
generated_oranges = random.randrange(1, 10)

apples_and_oranges(amount_of_apples + generated_apples, amount_of_oranges + generated_oranges)

