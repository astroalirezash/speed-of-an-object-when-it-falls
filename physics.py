# Thanks to sir Guido van Rossum

# LETS START AFTER 3 MONTH


from math import sqrt  # radical
import random  # for random number
from time import sleep  # to refresh the resault

nums = '1234567890'
m = float(input('import mass of the object (kg): '))  # getting from user (kg)

while True:
    # getting height of object from sensor (meter) but here we use random nums
    h1 = float(''.join(random.sample(nums, 2)))
    g = 9.8  # default is 9.8

    v = sqrt((m * g * h1) / (m / 2))  # calculating Instantaneous speed
    print(f'{v} m/s')

    sleep(0.5)
