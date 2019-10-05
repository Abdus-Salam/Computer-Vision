#import ecommerce.shipping
#from ecommerce.shipping import shipping_calculate
from pathlib import Path
from ecommerce import shipping as sh
import random

"""
    Modules
====================================================================
"""


"""
    Packages
====================================================================
Package is a container or file system modules.
Package = direcotory name যেখানে __init__.py নামে একটি ফাইল থাকবে। এটি দিয়ে বুঝাবে যে এটি package.
"""
# ecommerce.shipping.shipping_calculate()
# shipping_calculate()
sh.shipping_calculate()


"""
    Files & Directories
====================================================================

"""
path = Path('ecommerce')  # current directory
# path.mkdir()
# path.rmdir()

for file in path.glob('*.py'):
    print(file)

'''
Random number
=========================================================
'''

for i in range(0, 3):
    # print(random.random())
    print(random.randint(10, 20))

members = ["Abc", "xyz", "mno", "pqr"]

leader = random.choice(members)
print(leader)

# design a dice class which return tuple of dice throw!


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return (first, second)


dice = Dice()
print(dice.roll())
