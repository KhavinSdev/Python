import mysql.connector
import random
import getpass
import time

dbconnect = mysql.connector.connect(
    host='localhost',
    user='root',
    password=getpass.getpass(prompt='Enter db password: '),
    database="cellgame"
)

cursor = dbconnect.cursor()

# cursor.execute('use cells')
cursor.execute('select * from cells')

for i in cursor:
    print(type(i[0]))


class Cell:
    def __init__(self, name, health = int, age = float, count = int):
        self.name = name
        self.health = health
        self.age = age
        self.count = count

    def __str__(self):
        return f"Immune Cell:{self.name}"
    
    def cell_death(self, severity: float):

        self.count = self.count - severity
        print(f"cell {self.name} is no more")


class Macrophage(Cell):
    def __init__(self, name, health, age, count):
        super().__init__(name, health, age, count)

    def phagocytose(self, chance = float, level = float):
        if(random.randint(1, 1000) < chance/100 * 1000):
            Salmonella.count = Salmonella.count - Macrophage_cell.count*(contactr/1000)*(2+level)
            #print(f"Salmonella cell destroyed \n new count is {Salmonella.count}")
        

class TCell(Cell):
    def __init__(self, name, health, age, count):
        super().__init__(name, health, age, count)

class BCell(Cell):
    def __init__(self, name, health, age, count):
        super().__init__(name, health, age, count)

class Neutrophils(Cell):
    def __init__(self, name, health, age, count):
        super().__init__(name, health, age, count)

class DentriticCell(Cell):
    def __init__(self, name, health, age, count):
        super().__init__(name, health, age, count)

class BacterialCell(Cell):
    def __init__(self, name, health, age, count, divrate = float):
        super().__init__(name, health, age, count)
        self.divrate = divrate
    
    def infect(self, cell_name, chance):
        if random.randint(1, 1000) < (chance/100) * 1000:
            print(f"Cell {cell_name} ordered to commit suicide!")
            cell_name.cell_death(Salmonella.count*0.05)
    
    def multiply(self):
        self.count = self.divrate * self.count 
        
'''
Macrophage_cell = Macrophage('Macrophage', 100, 1, 200)
T_cell = TCell('TCell', 100, 1, 5000000 )
B_cell = BCell('BCell', 100, 1, 3000000)
Neutrophil = Neutrophils('Neutrophils', 100, 1, 1000000)
Dentritic_cell = DentriticCell('DentriticCell', 100, 1, 100000)
Salmonella = BacterialCell('Salmonella', 0, 1, 1, 2)

listofcells = [Macrophage_cell, T_cell, B_cell, Neutrophil, Dentritic_cell, Salmonella]


def contactrisk(pathogen_count: float, icell_count: float):
    return (pathogen_count / (icell_count + pathogen_count))  


first_contact = 0
cycle_count = 0.0
critical_max = False
level = 1


while True:

    if(Salmonella.count <= 0):
        print("All pathogens eliminated")
        break
    elif(Salmonella.count > 500):
        critical_max = True
    iscontact = False;
    # if(cycle_count % 5 == 0 and cycle_count > 5):
    for i in listofcells:
        print(f"{i.name} has a count of {i.count}")
    
    print("\n")
    
    contactr = contactrisk(Salmonella.count, Macrophage_cell.count) * 1000

    if(random.randint(1, 1000) < contactr):
        iscontact = True
        print("Pathogens detected \n")
    
    if(iscontact and critical_max):
        if(Salmonella.count > 10*Macrophage_cell.count):
            level += 10
        Macrophage_cell.phagocytose(95, level)
        Salmonella.infect(Macrophage_cell, 5)
        first_contact +=1

    

    if(Macrophage_cell.count < 500 and first_contact !=0):
        Macrophage_cell.count += 100
    Salmonella.multiply()

    if(random.randint(1,1000) <100):
        Salmonella.count += 10000



    cycle_count += 1
    time.sleep(1.0)
    

    
'''




