import random

lottery = []
for _ in range(100):
    number = str(random.randint(0, 88888)).zfill(5)
    lottery.append(number)
    
    
winners = random.sample(lottery, 1)
print("you are winner" ,winners)