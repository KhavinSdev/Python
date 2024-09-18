#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

dishes = {
    'B': 'Burger',
    'Pizza': 'Pizza',
    'Pn': 'paneer',
    'Pa': 'pasta',
    'DA': 'DumAloo',
    'Ma': 'Maggi',
    'PB': 'Pav Bhaji',
    'Order': 'Ordering out'
}

high = ['B', 'Ma', 'Pa', 'Pn']
medium = ['Pizza', 'PB']
low = ['Order']
selected_list = None
random_int = random.randint(1, 100)

if random_int <= 50:
    selected_list = high 
elif random_int <= 85:
    selected_list = medium 
elif random_int <= 100:
    selected_list = low


#print(selected_list)

try:
    with open('LastSelection.txt', mode = 'r') as fr:
        last_dish = fr.read()

        if last_dish in selected_list:
            selected_list.remove(last_dish)
            #print(selected_list)
except:
    pass


random_no = random.randint(0, len(selected_list) - 1)

print(f'The special dish selected for this week is: {dishes[selected_list[random_no]]}')

with open('LastSelection.txt', mode = 'w') as fw:
    fw.write(selected_list[random_no])


# In[ ]:




