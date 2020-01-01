#optimized best eurojackpot gen eu west
from random import sample

mylottonumbers2 = []
myeurojacknumbers2 = []

mylottonumbers2 = sample(range(1, 49),5)
mylottonumbers2_sortet = sorted(mylottonumbers2)
print(mylottonumbers2_sortet)

myeurojacknumbers2 = sample(range(1, 10),2)
myeurojacknumbers2_sortet = sorted(myeurojacknumbers2)
print(myeurojacknumbers2_sortet)