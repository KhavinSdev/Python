#!/usr/bin/env python
# coding: utf-8

import random

dishes = ['Burger', 'Pizza', 'Paneer', 'Pasta', 'DumAloo', 'Maggi', 'Pav Bhaji', 'Ordering out']

try:
    with open('LastSelection.txt', mode = 'r') as fr:
        last_dish = fr.read()
        dishes.remove(last_dish)
        print(dishes)

except:
    pass

random_no = random.randint(0, len(dishes) - 1)

print(f'The special dish selected for this week is: {dishes[random_no]}')

with open('LastSelection.txt', mode = 'w') as fw:
    fw.write(dishes[random_no])








