##############################################################
#########      finding series in a given list     ############
#########               Dec 2014                  ############
#########       Author: Muhammad Nasir            ############
##############################################################


import math
def series(list):
    length=list.__len__()
    #find series of list that contain powers of a number of a number in list
    if length>2:            #if length of list is greater then 2 element

        #if base is first element of
        #we can find this with if block of code
        #consider the first number as base
        if list[0]*list[0]==list[1]:
            if list[1]*list[0]==list[2]:
                for i in range(1,length-1):
                    if list[i]*list[0]!= list[i+1] :
                        print "this is not series"
                        print "condition fails at" ,list[i+1]
                        print "suggested series number is",list[i]*list[0]
                return  True





        #finding base of first number
        #second possible condition for series
        logof=1
        for base in range(2,list[0]):               #find base of first element
            power=1
            while math.pow(base,power)<=list[0]:   #check if element is power of current number
                if math.pow(base,power)==list[0]:
                    if(logof!=base):
                        logof= base                       #assign value of iterator to base
                power=power+1

        #finding sequence with first number base
        if list[0]*logof==list[1]:      #if first element *base is equal to second element
            if list[1]*logof==list[2]:
                for i in range(1,length-1):
                    if list[i]*logof!= list[i+1] :
                        print "this is not logo series"
                        print "condition fails at" ,list[i+1]
                        print "suggested series number is",list[i]*logof
                        return False
                return True




        #series can be made my adding previous two term of series
        #that condition will be handle by the following code
        #this part of code will check series for fibonacci series
        if list[0]+list[1]==list[2]:        #if sum of first last two term is equal to current
            if list[0]==2 and length >3:
                if list[1]+list[2]==list[3]:
                    for i in range(0,length-2):      #it hold fibonacci series in the start of series
                        if list[i]+list[i+1]!=list[i+2]:    #if it did not hold series condition at any point
                            print "this is not basic series"
                            print "condition fails at" ,list[i+2]
                            print "suggested series number is",list[i]+list[i+1]    #provide user with a suggested number
                            return False
                    return True
            elif list[0]!=2:
                    if length<4:
                        for i in range(0,length-2):      #it hold fibonacci series in the start of series
                            if list[i]+list[i+1]!=list[i+2]:    #if it did not hold series condition at any point
                                print "this is not 2 series"
                                print "condition fails at" ,list[i+2]
                                print "suggested series number is",list[i]+list[i+1]    #provide user with a suggested number
                                return False
                        return True
                    else:
                        if list[2]+list[3]==list[4]:
                            for i in range(0,length-2):      #it hold fibonacci series in the start of series
                                if list[i]+list[i+1]!=list[i+2]:    #if it did not hold series condition at any point
                                    print "this is not 2 series"
                                    print "condition fails at" ,list[i+2]
                                    print "suggested series number is",list[i]+list[i+1]    #provide user with a suggested number
                                    return False
                            return True



    #if list is not a series of power of integers
        incrementsList=[]           #list for getting difference b/t elements of list element
        diffInConsectiveInc=[]        #list for getting difference b/t incrementList element to find increasing factor

       #getting defference between consective number
        for i in range(0,length-1):
            incrementsList.append(list[i+1]-list[i])

        #increamantal factor if defference between consective element
        if incrementsList.__len__() >1:
            for i in range(0,incrementsList.__len__()-1):
                diffInConsectiveInc.append(incrementsList[i+1]-incrementsList[i])


        #if list increasement with a constant factor then
        #differnce b/t consective element will be zero
        if diffInConsectiveInc[0]==0:

            #get constant increament from increments list
            constInc=incrementsList[0]

            #check every element of list against the factor
            if list[0]+constInc==list[1]:
              if length>3:
               if list[2]+constInc==list[3]:
                        for i in range(1,length-1):
                            if list[i]+constInc !=list[i+1]:    #if any element is not expect in lis provide with suggested element
                                print "this is not const series"
                                print "condition fails at" ,list[i+1]
                                print "suggested series number is",list[i]+constInc
                           #     return False
                        return  True #return from the  function
               else:
                   if list[1]+constInc==list[2]:
                        for i in range(1,length-1):
                            if list[i]+constInc !=list[i+1]:    #if any element is not expect in lis provide with suggested element
                                print "this is not const series"
                                print "condition fails at" ,list[i+1]
                                print "suggested series number is",list[i]+constInc
                           #     return False
                        return  True #return from the  function


        #IF  list increament is factor is not constant
        if diffInConsectiveInc.__len__()>1 and diffInConsectiveInc[0]!=diffInConsectiveInc[1]:

            #get in increament element from increment list
            multBaseinc=incrementsList[0]
            #get factor by which increament elements increase
            factor=diffInConsectiveInc[1]-diffInConsectiveInc[0]
            #che if it means condition
            if list[0]+multBaseinc==list[1]:
                 for i in range(0,length-1):    #lolp throhgt every element if not in list provid with sugggestion
                    if list[i]+multBaseinc !=list[i+1]:
                           # print "this is not series"
                   #         print "condition fails at" ,list[i+1]
                    #        print "suggested series number is",list[i]*multBaseinc
                            complexSeries(list)        #checking for complext list
                            return
                    multBaseinc=multBaseinc*factor

        return False
        print " give list is not simple series"
    return False


def complexSeries(list):
    '''complex series

    a series that has different roles of increment for odd and even element will be slove by this function
    '''
    #print '-------------complex---------------'
    lenght=len(list)
    if lenght>4:
       #item at even number
       evenCounter=0
       evenList=[]
       oddCounter=1
       oddList=[]

        #store elements at even position in the list
       for i in range(0,lenght/2):
           evenList.append(list[evenCounter])
           evenCounter=evenCounter+2
       #store elements at the odd position of list
       for i in range(0,lenght/2):
           oddList.append(list[oddCounter])
           oddCounter=oddCounter+2

#       print "even part of list",evenList[:]
 #      print "odd part of list",oddList[:]
       #print "check for even number list"
       #print '------------------this is complex series result-----------------'
       first=series(evenList)
       #print "check for odd number list"
       second=series(oddList)

       if not(first) or not(second):
           genericSeries(list)
       else:

           print "this is complex list"

def genericSeries(list):
     print '------------------------generic series-----------------------'
     length=len(list)
     knowledge=[]
     knowledge.append(list[1]-list[0])
     knowledge.append(list[2]-list[1])
     knowledge.append(list[3]-list[2])
     for i in range(0,length-1):
        if not (knowledge.__contains__(list[i+1]-list[i])):
                knowledge.append(list[i+1]-list[i])



#     print "list with increasment",knowledge[:]
     print "next expected element",
     print list[length-1]+knowledge[0]," second ",list[length-1]+knowledge[0]+knowledge[1]

if __name__ == '__main__':
    #list list element must me be +ve
    #input sample data
    #list=[1,7,14,21,51]
    list=[1,3,9,5,67,7]
   # list=[1,1,2,3,3,4]
    #list=[1,2,3,5,8,8]
    #list=[1,7,14,21,26]
    #list=[1,3,2,5,3,8]

    series(list)
    #complexSeries(list)
    print list[:]
    #print "first 20 element of list"
    #for i in range(0,20);
