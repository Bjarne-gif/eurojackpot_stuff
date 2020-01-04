#imports
import urllib
from urllib.request import Request, urlopen
from lxml import html
import requests

#download all numbers from webpage https://www.lottozahlenonline.com/eurojackpot/archiv/"
def downloadnumbersoflastyears():
    
    #there is only 2012 to 2019 data
    for x in range(2011, 2020):

        print(x)
        yearofnumbers = str(x)

        page = requests.get("https://www.lottozahlenonline.com/eurojackpot/archiv/"+yearofnumbers+"/")
        tree = html.fromstring(page.content)
        numbers = tree.xpath('//text[@text-anchor="middle"]/text()')

#next step is to cut though the lists and get all lottonumbers(5) and all eurojackpotnumbers(2) separated

        if not numbers:
            print("Year doesn´t exists")
            exit
        else:            
            numbersstrip = []
            numbersstrip1 = []
            i = 0
            z = 5

            while i < len(numbers):
                numbersstrip.append(numbers[i:i+5])
                i +=7

            while z < len(numbers):
                numbersstrip1.append(numbers[z:z+2])
                z +=7

            print(numbersstrip)
            print(numbersstrip1)

            # Hier müssen die nested lists zusammengebastelt werden.

            #Rohdaten werden in Dateien gespeichert, es muss noch eingebaut werden das Daten gespeichert werden nur wenn sie nicht schon bestehen.
            
            numbers = str(numbers)
            filename = yearofnumbers+".txt"
            f = open(filename,"w")
            f.write(""+numbers)
            f.close()
        x = x+1

downloadnumbersoflastyears()