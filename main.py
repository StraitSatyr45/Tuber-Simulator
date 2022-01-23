import random
import time
print("Welcome to your Tuber Simulator!")

array_succes_chance = random.choice([True , False , False , False , False , False , False])

suc = 1
while suc < 5:
    if suc == 1 and array_succes_chance:
        print(str(random.randrange(500 , 1000)) + " In one day!")
    elif suc == 1:
        print(str(random.randrange(1 , 10)) + " In one day!")
    
    if suc == 2 and array_succes_chance:
        print(str(random.randrange(1000 , 7000)) + " In a week!")
    elif suc == 2:
        print(str(random.randrange(1 , 20)) + " In a week")
    
    if suc == 3 and array_succes_chance:
        print(str(random.randrange(7000 , 15000)) + " In a month!")
    elif suc == 3:
        print(str(random.randrange(1 , 50)) + " In a month!")
    
    if suc == 4 and array_succes_chance:
        print(str(random.randrange(15000 , 100000)) + " In a year!")
    elif suc == 4:
        print(str(random.randrange(1 , 200)) + " In a year!")

    if suc == 5 and array_succes_chance:
        print(str(random.randrange(100000 , 10000000)) + " In a decade!")
    elif suc == 5:
        print(str(random.randrange(1000 , 50000)) + " In a decade!")
    
    suc += 1
    
