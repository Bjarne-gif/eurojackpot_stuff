import random

mylottonumbers= []

for x in range (7):
    randnumb = random.randint(1, 49)
    if randnumb not in mylottonumbers:
       mylottonumbers.append(randnumb)
    else:
        randnumbifexi = random.randint(1, 49)
        mylottonumbers.append(randnumbifexi)
    mylottonumbers.sort()
print(mylottonumbers)