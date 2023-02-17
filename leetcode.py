from random import randint


storage = []

for i in range(10):
    dice = randint(1, 12)
    storage.append(dice)
    print(f"{dice}")