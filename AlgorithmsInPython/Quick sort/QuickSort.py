def QictkSort(list1, start, end):
    '''Insertion Sort.

    this function will sort element of given list Insertion sort.
    '''
    if start < end:                             #if lower index is not equal fo higher index

         mid = partition(list1, start, end)     #seletion a pivot point to slip the list on
         QictkSort(list1, start, mid-1)         #first half of the list
         QictkSort(list1, mid+1, end)           #second half of the list
        # print list1[:mid-1]
         #print list1[mid:]
    else:
        return




def partition(List, List_start, List_end):
    '''Selecting pivot.

    this function will iterate through the List to arrange the list in such order that all the
    values greater then the pivot are on the right side and values less then the pivot point on
    the right side
    '''
    pivot = List[List_start]       #selection first index as pivot
    start = List_start+1;          #variable for starting index
    end=List_end                   # variable for last index
    while not(start>=end):           #do while the start index become equal to greater then the last index

        while not(start>=end) and not(List[start] >= pivot):    #continue pivot become less the or equal to start index
            start = start+1

        while not (start>end) and not (pivot >= List[end]): #continue while pivot become greater or equal to last index
            end = end-1

        #swaping element of start and last index variables
        tmp=List[start]
        List[start]=List[end]
        List[end]=tmp

    #undo last swap because the start and end index variables over flow
    tmp=List[start]
    List[start]=List[end]
    List[end]=tmp

    #swaping last index with pivot index
    tmp=List[List_start]
    List[List_start]=List[end]
    List[end]=tmp
    return end      #returning index of last index variable






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
    print "pecess start"
    start_time = datetime.now()
    QictkSort(listOrg)
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))

    print listOrg[:]