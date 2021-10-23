from shipping import calc_shipping
calc_shipping()

import random 

from pathlib import Path


members = ['John', 'Smith', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second
    
dice = Dice()
print(dice.roll())



path = Path()
for file in path.glob('*.py'):
    print(file)



#for i in range(3):
 #   print(random.randint(10, 20))


#shipping.calc_shipping()