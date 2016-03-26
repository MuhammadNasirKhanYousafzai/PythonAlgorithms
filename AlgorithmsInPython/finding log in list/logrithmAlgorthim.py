import math
def findLogrithm(list):
    #selecting a default base
    base=1
    for i in range(2,list[0]+1):    #finding log of smallest member in list
        j=1
        while math.pow(i,j)<=list[0]:   #check if element is power of current number
            if math.pow(i,j)==list[0]:
                    print "basic", i    #print value of base
                    base= i             #assign value of iterator to base
                    break               #break statement for while loop
            j=j+1                       #increment of iterator of while loop
        if(base>1):                     #if value of is change break from loop
            break
    lst=[]
    for j in range(0,list.__len__()):
        nmbr=1
       # print nmbr
        while math.pow(base,nmbr)<=list[j]:
            #print math.pow(base,nmbr)
            if math.pow(base,nmbr)==list[j]:
                #print math.pow(base,nmbr)
                lst.append(nmbr)
                break
            nmbr=nmbr+1
        if(math.pow(base,nmbr))>list[j]:
            number=nmbr
            while not (list[j]>=math.pow(base,number)):
                number=number-0.001
            lst.append(number)
    print lst[:]

    #list of element for finding logarithm list must be in sorted form

    #list of element for finding logarithm list must be in sorted form
findLog=[5*5*5*5*5*5*5*5*5*5,625,24,123,625*5]
findLogrithm(findLog)