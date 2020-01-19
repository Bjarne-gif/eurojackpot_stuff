#optimized best eurojackpot gen eu west
from random import sample

def randomeurojackpotnmbrs():
    firstfive = []
    lasttwo = []
    #first five lotto numbers
    firstfive = sample(range(1, 51),5)
    firstfive_sortet = sorted(firstfive)

    #last two bonus numbers
    lasttwo = sample(range(1, 11),2)
    lasttwo_sortet = sorted(lasttwo)

    #combine all numbers to one var and print
    randomeurojackpotnmb_sortet = firstfive_sortet + lasttwo_sortet
    print(randomeurojackpotnmb_sortet)

#start function and generate numbers
randomeurojackpotnmbrs()