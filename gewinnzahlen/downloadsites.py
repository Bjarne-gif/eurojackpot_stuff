#imports
import urllib
from urllib.request import Request, urlopen
from lxml import html
import requests
import os.path

#download all numbers from webpage https://www.lottozahlenonline.com/eurojackpot/archiv/"

def appendtxtfile(listnametog, listlottonumb, listeurojack, yearofnumber):

    listnametog = str(listnametog)
    listlottonumb = str(listlottonumb)
    listeurojack = str(listeurojack)

    filename = yearofnumber+".txt"
    if not os.path.isfile(filename):
        f = open(filename,"w")
        f.write(""+listnametog+"\n"+listlottonumb+"\n"+listeurojack)
        f.close()
        exit
    else:
        print("Data is existant")
        exit

def downloadnumbersoflastyears():
    
    #there is only 2012 to 2019 data
    for x in range(2011, 2021):

        print(x)
        yearofnumbers = str(x)

        page = requests.get("https://www.lottozahlenonline.com/eurojackpot/archiv/"+yearofnumbers+"/")
        tree = html.fromstring(page.content)
        numbers = tree.xpath('//text[@text-anchor="middle"]/text()')

#next step is to cut though the lists and get all lottonumbers(5) and all eurojackpotnumbers(2) separated

        if not numbers:
            print("Year doesn´t exist")
            exit
        else:            
            numbersstrip = []
            numbersstrip1 = []
            allnumbers = []

            #get nested list of lottonumbers only
            i = 0
            while i < len(numbers):
                numbersstrip.append(numbers[i:i+5])
                i +=7
            lottonumbers = numbersstrip

            #get nested list of eurojackpotnumbers only
            z = 5
            while z < len(numbers):
                numbersstrip1.append(numbers[z:z+2])
                z +=7
            eurojackpotnumbers = numbersstrip1

            #get nested list of all values lottonumbers and eurojackpotnumbers in the rigt order
            y = 1
            u = 0
            w = 0
            while y < len(numbers):          
                allnumbers.insert(u, numbersstrip[w])
                allnumbers.insert(y, numbersstrip1[w])
                w +=1
                u +=2
                if w == len(numbersstrip1):
                    break
                y +=2

            appendtxtfile(allnumbers, lottonumbers, eurojackpotnumbers, yearofnumbers)

        x = x+1

downloadnumbersoflastyears()