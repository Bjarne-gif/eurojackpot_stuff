import random

mylottonumbers= []
eurozahlen= []

for x in range (5):
    randnumb = random.randint(1, 49)
    if randnumb not in mylottonumbers:
       mylottonumbers.append(randnumb)
    else:
        randnumbifexi = random.randint(1, 49)
        mylottonumbers.append(randnumbifexi)
    mylottonumbers.sort()
print(mylottonumbers)

for x in range (2):
    randnumb = random.randint(1, 10)
    if randnumb not in eurozahlen:
       eurozahlen.append(randnumb)
    else:
        randnumbifexi = random.randint(1, 10)
        eurozahlen.append(randnumbifexi)
    eurozahlen.sort()
print(eurozahlen)