def selectionSort(listsort):
    '''Insertion Sort.

    this function will sort element of given list Insertion sort.
    '''
    for i in range(0,listsort.__len__()):#selecting index for selection
        v=listsort[i]
        j=i-1
        #swaping value of selected index in the presorted list
        while (j>=0) and (v<listsort[j]) :
            #move value forward by one index
            listsort[j+1]=listsort[j]
            j=j-1#decreament walue of presorted subarry index
        listsort[j+1]=v #inserting value on the index






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