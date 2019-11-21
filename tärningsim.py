import random
import time

def dicethrow():
    return random.randrange(1, 7)

list_of_throws = []

dice = input("Vill du slå tärning?")
time.sleep(1) 
while dice == "ja":
    x = dicethrow()
    print(x)
    list_of_throws.append(x)
    dice2 = input("Vill du slå igen?")
    time.sleep(1)
    if dice2 == "quit":
        quit()
    if dice2 == "mean":
        print(float(mean_of_throws(list_of_throws)))


def sum_of_throws(list_of_throws):
    result = 0
    for x in list_of_throws:
        result = result + x
    return result

def mean_of_throws(list_of_throws):
    result = 0 
    for x in list_of_throws:
        result = result + x
    return result / len(list_of_throws)
 


