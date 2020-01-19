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
                if counter is not 1:
                    if counter is not 3:
                        y = 0
                        summeinsgesamt = 0
                        for y in range(1,51):
                            y = str(y) #int to str
                            #how often is a number in the list?
                            #print("Zahl: "+y+" -> "+ str(sum(x.count(y) for x in mylist)))
                            summevonzahlinliste = str(sum(x.count(str(y)) for x in mylist))
                            print("Zahl: "+y+" -> "+summevonzahlinliste)

                            #how much numbers are in the list?
                            summeinsgesamt = int(summeinsgesamt) + int(summevonzahlinliste)
                            
                            #percentage of every number in the list in relation to all numbers


                        print("Gesamt: "+str(summeinsgesamt))
                    else:
                        y = 0
                        summeinsgesamt = 0
                        for y in range(1,11):
                            y = str(y) #int to str
                            #how often is a number in the list?
                            #print("Zahl: "+y+" -> "+ str(sum(x.count(y) for x in mylist)))
                            summevonzahlinliste = str(sum(x.count(y) for x in mylist))
                            print("Zahl: "+y+" -> "+summevonzahlinliste)

                            #how much numbers are in the list?
                            summeinsgesamt = int(summeinsgesamt) + int(summevonzahlinliste)

                            #percentage of every number in the list in relation to all numbers
                            

                        print("Gesamt: "+str(summeinsgesamt))
                            
                else:
                    exit
            f.close()
    else:
        print("file not existant")
        exit