# load packages
from random import randint

# random dice roll
def roll_attack_dice():
	d1 = randint(1, 6)
	d2 = randint(1, 6)
	d3 = randint(1, 6)
	return sorted([d1, d2, d3], reverse=True)

def roll_defend_dice():
	d1 = randint(1, 6)
	d2 = randint(1, 6)
	return sorted([d1, d2], reverse=True)


def battle(btype='2v1'):
	'''
	battle types can be either 2v1 or 3v2
	'''
	if btype == '2v1':
		defend = 1
		attack =  
	if roll_attack_dice()[0] > roll_defend_dice()[0]:


