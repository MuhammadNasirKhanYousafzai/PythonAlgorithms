def bubbleSort(list1):
    '''Bubble sort.

    this function will sort element of given list using bubble sort
    '''
   #loop for selecting an index3
    for i in range(0,list1.__len__()-1):
       #seleting index for comparison
        for j in range(0,list1.__len__()-1-i):
       #compare the two indexes
            if list1[j]>list1[j+1]:
              #swap if condition satisfy
                tmp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=tmp
    #print list on screen
   # for i in list1:
    #    print  i,"    ",
    #print "with the help of for loop"
    #for i in range(0,list1.__len__()):
     #   print list1[i],"    ",


if __name__ == '__main__':
    '''Main

    program excution will start from here
    '''
    listOrg=[]
#    listOrg[0]=1000
    i=0

    try:
        f=open('nasir.txt')

    except IOError:
        print "not found"
        with open('nasir.txt', 'w+') as f:
            for i in range(1,1001):
                if (i%5==0):
                  #  listOrg[i]=-i
                    var=str(-i)+","
                    f.write(var)
                elif((i%2)==0):
                    var=str(i+((i*2)/10))+","
                    f.write(var)
                else:
                    var=str(i)+","
                    f.write(var)

        f.close();
    finally:
        with open('nasir.txt', 'r+') as f:
            values=f.read()
            i=0
            for item in values.split("\n"):
                if(item!=""):
                    listOrg.append(int((item)))
                    i=i+1

    #print listOrg[:]
    from datetime import datetime
    #print "pecess start"
    start_time = datetime.now()
    bubbleSort(listOrg)
    end_time = datetime.now()
    #print('Duration: {}'.format(end_time - start_time))

    print listOrg[:]