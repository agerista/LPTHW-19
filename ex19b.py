def apples_and_oranges(apple_count, orange_count):
	print "you have %d apples." % apple_count
	print "you have %d oranges." % orange_count
	print "i feel a fruit salad coming on."
	print "get a fork."
	
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

print "we could get user input:"
raw_input("Enter apples")
raw_input("Enter oranges")

apples_and_oranges((int(raw_input), (int(raw_input))