#!/usr/bin/env python
# coding: utf-8

# # Final Capstone Projects
# 
# Please refer to the [**Final Capstone Projects**](http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/tree/master/Final%20Capstone%20Projects/) folder to get all the info on final capstone project ideas and possible solutions!

# In[1]:


import sys
import time
import keyboard
import playsound
from pynput import *


# In[2]:


key_count = 0
key_sentence = ''
quit = None



# In[3]:


def on_press(key):
    global key_count
    global key_sentence
    global quit
    print(key)

    
    if str(key) == 'Key.esc':
        quit = True
        print(quit)
        
    elif str(key) == 'Key.backspace':
        key_count += 1
        key_sentence = ''
    elif str(key) != 'Key.backspace':
        key_sentence = key_sentence + str(key).removeprefix("'").removesuffix("'")
    print(key_sentence)
    
         
    

def on_release(key):

    pass
    
    


# In[4]:


monitor = keyboard.Listener(on_press=on_press, on_release=on_release)


# In[5]:


def ocdmonitor():
    global key_count
    global quit
    monitor.start()
    
    while key_count <= 5:
        if quit == True:
            exit()
        if key_count == 5:
            print('Stop doing that, it is not you but the disease')
            playsound.playsound('mo.mp3')
            key_count = 0
            print(quit)

        time.sleep(2)

        print(key_count)
        print(quit)


    
    


# In[ ]:





# In[ ]:


ocdmonitor()


# In[ ]:




