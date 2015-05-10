import random

coin_sides = ('HEADS','TAILS')

bet = raw_input('What is your bet? HEADS or TAILS? ')

#coin flip
side = random.choice(coin_sides)

if side == bet:
	print "Well Done!, get 100$"
else:
	print "Too bad.., pay 100$"