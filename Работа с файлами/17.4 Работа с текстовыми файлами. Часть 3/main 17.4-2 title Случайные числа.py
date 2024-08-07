import random

with open("random.txt","w") as file:
    for i in range(25):
        number = random.randint(111, 777)
        file.write(f"{str(number)}\n")
