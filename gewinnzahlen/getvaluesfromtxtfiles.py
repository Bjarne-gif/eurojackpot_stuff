import os.path
import ast
for x in range(2011, 2021):
    print(x)
    yearofnumbers = str(x)
    filename = yearofnumbers+".txt"
    
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            lines = [x.strip() for x in lines]
            counter = 0
            for line in lines:
                counter += 1
                print("_______________count: "+str(counter))
                mylist = ast.literal_eval(line) # Converting string to list 
                print(mylist)
                if counter != 1:
                    if counter != 3:
                        y = 0
                        sumtogether = 0
                        arrayforpercentage = []
                        for y in range(1,51):
                            y = str(y) #int to str
                            #how often is a number in the list?
                            #print("Zahl: "+y+" -> "+ str(sum(x.count(y) for x in mylist)))
                            sumfromevvalue = str(sum(x.count(str(y)) for x in mylist))
                            print("Zahl: "+y+" -> "+sumfromevvalue)

                            #how many numbers are in the list?
                            sumtogether = int(sumtogether) + int(sumfromevvalue)

                            y = int(y)
                            arrayforpercentage.insert(y, sumfromevvalue)

                        print(arrayforpercentage)

                            #percentage of every number in the list in relation to all numbers

                        print("Gesamt: "+str(sumtogether))
                    else:
                        y = 0
                        sumtogether = 0
                        arrayforpercentage = []
                        for y in range(1,11):
                            y = str(y) #int to str
                            #how often is a number in the list?
                            #print("Zahl: "+y+" -> "+ str(sum(x.count(y) for x in mylist)))
                            sumfromevvalue = str(sum(x.count(y) for x in mylist))
                            print("Zahl: "+y+" -> "+sumfromevvalue)

                            #how much numbers are in the list?
                            sumtogether = int(sumtogether) + int(sumfromevvalue)

                            y = int(y)
                            print(y)
                            
                            arrayforpercentage.insert(y , sumfromevvalue)
                                
                        print(arrayforpercentage)

                            #percentage of every number in the list in relation to all numbers 

                        print("Gesamt: "+str(sumtogether))                           
                else:
                    exit
            f.close()
    else:
        print("file not existant")
        exit