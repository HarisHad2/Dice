import random

dice = input("Vill du slå tärning?")
num = random.randrange(1, 7)   
while dice == "ja":
    num = random.randrange(1, 7)
    print(num)
    dice2 = input("Vill du slå tärning?")
    
 


