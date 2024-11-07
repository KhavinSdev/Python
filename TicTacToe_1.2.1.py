#!/usr/bin/env python
# coding: utf-8

# In[13]:


def XO():
    def display(r1,r2,r3):
        print( ' ' + r1[0] + ' | ' + r1[1] + ' | ' + r1[2])
        print('-----------')
        print( ' ' + r2[0] + ' | ' + r2[1] + ' | ' + r2[2])
        print('-----------')
        print( ' ' + r3[0] + ' | ' + r3[1] + ' | ' + r3[2])

    r1 = [' ', ' ', ' ']
    r2 = [' ', ' ', ' ']
    r3 = [' ', ' ', ' ']
    
    GEnd = False
    moves_played = []
    name1 = input("What is player1's name? ")
    name2 = input("What is player2's name? ")
    turn = 1
    
    
    while not GEnd:
    
        if turn == 1:
            display(r1,r2,r3)
            print("Format your move in the format(row no <no space> column number)")
            usr = tuple(input(f'What is your move {name1}?'))
            
            #print(usr)
            
            
            
            if usr in moves_played:
                print("That place is filled, please make another move")
                continue
            else:
                (x,y) = usr
                if int(x) == 1:
                    r1[int(y) - 1] = 'X'
                elif int(x) == 2:
                    r2[int(y) - 1] = 'X'
                elif int(x) == 3:
                    r3[int(y) - 1] = 'X'
            
                moves_played.append(usr)
            
            display(r1,r2,r3)
            print()
        
            if r1[0] == r1[1] == r1[2] == 'X' or r2[0] == r2[1] == r2[2] == 'X' or r3[0] == r3[1] == r3[2] == 'X' :
                print('You win ' + name1)
                break
            if r1[0] == r2[0] == r3[0] == 'X' or r1[1] == r2[1] == r3[1] == 'X' or r1[2] == r2[2] == r3[2] == 'X':
                print('You win ' + name1)
                break
            if r1[0] == r2[1] == r3[2] == 'X' or r1[2] == r2[1] == r3[0] == 'X':
                print('You win ' + name1)
                break
    
            turn = 2

            #print(moves_played)
            if len(moves_played) == 9:
                print("The Game is a Draw")
                break
        
    
        
        if turn == 2:
            print("Format your move in the format(row no <no space> column number)")
            usr = tuple(input(f'What is your move {name2}?'))
            
            #print(usr)
            
            
            
            if usr in moves_played:
                print("That place is filled, please make another move")
                continue
            else:
                (x,y) = usr
                if int(x) == 1:
                    r1[int(y) - 1] = 'O'
                elif int(x) == 2:
                    r2[int(y) - 1] = 'O'
                elif int(x) == 3:
                    r3[int(y) - 1] = 'O'
            
                moves_played.append(usr)
            
            display(r1,r2,r3)
            print()
        
            if r1[0] == r1[1] == r1[2] == 'O' or r2[0] == r2[1] == r2[2] == 'O' or r3[0] == r3[1] == r3[2] == 'O' :
                print('You win ' + name2)
                break
            if r1[0] == r2[0] == r3[0] == 'O' or r1[1] == r2[1] == r3[1] == 'O' or r1[2] == r2[2] == r3[2] == 'O':
                print('You win ' + name2)
                break
            if r1[0] == r2[1] == r3[2] == 'O' or r1[2] == r2[1] == r3[0] == 'O':
                print('You win ' + name2)
                break
    
            turn = 1
        
            if input('Do you want to end the game (y/n) ') == 'y':
                GEnd = True
                

        





    
    




        
        
        
        





# In[ ]:


XO()

