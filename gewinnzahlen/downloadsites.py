#imports
import urllib
from urllib.request import Request, urlopen
from lxml import html
import requests

#download all numbers from webpage https://www.lottozahlenonline.com/eurojackpot/archiv/"
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
            print("Year doesn´t exists")
            exit
        else:            
            numbersstrip = []
            numbersstrip1 = []
            numbersstriptog = []

            #get nested list of lottonumbers only
            i = 0
            while i < len(numbers):
                numbersstrip.append(numbers[i:i+5])
                i +=7

            #get nested list of eurojackpotnumbers only
            z = 5
            while z < len(numbers):
                numbersstrip1.append(numbers[z:z+2])
                z +=7

            #get nested list of all values lottonumbers and eurojackpotnumbers in the rigt order
            y = 1
            w = 0
            while y < len(numbers):          
                numbersstrip.insert(y, numbersstrip1[w])
                w +=1
                if w == len(numbersstrip1):
                    numbersstriptog = numbersstrip
                    break
                y +=2
            print(numbersstriptog)

            #safe nested list numbersstriptog in files
            numbersstriptog = str(numbersstriptog)
            filename = yearofnumbers+".txt"
            f = open(filename,"w")
            f.write(""+numbersstriptog)
            f.close()

            #numbers can be insert to files (raw data)
            #numbers = str(numbers)
            #filename = yearofnumbers+".txt"
            #f = open(filename,"w")
            #f.write(""+numbers)
            #f.close()
        x = x+1

downloadnumbersoflastyears()