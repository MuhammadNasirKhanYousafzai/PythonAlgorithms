def selectionSort(list1):
    '''Selection Sort.

    this function will sort element of given list using Selection sort.
    '''
    for i in range(0,list1.__len__()-1):#loop for selecting index
        mins=i #let i is index with minimum value
        for j in range(i+1,list1.__len__()):#loop through the list to get minimum if exist
            if(list1[mins]>list1[j]):#check for minimum value index
                mins=j
        #swap minimum index with the selected index
        tmp=list1[i]
        list1[i]=list1[mins]
        list1[mins]=tmp
    #printing sorted element on screen



#main function
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
            for item in values.split(","):
                if(item!=""):
                    listOrg.append(int((item)))
                    i=i+1

    print listOrg[:]
    from datetime import datetime
    print "process start"
    start_time = datetime.now()
    selectionSort(listOrg)
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))

    print listOrg[:]