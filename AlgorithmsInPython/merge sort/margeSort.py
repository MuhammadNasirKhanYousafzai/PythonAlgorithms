import os
def MargeSort(list1):
    '''Insertion Sort.

    this function will sort element of given list Insertion sort.
    '''
    if list1.__len__() == 1: #if list length equal to 1 return
        return
    #else do following work
    mid=list1.__len__()/2   #divide list length by 2 to get mid point
    blist=list1[:mid]   #first half of list
    clist=list1[mid:]   #second half of list
    #print list1[mid]
    #recursion call
    MargeSort(blist)    #recursion for first half
    MargeSort(clist)    #recurstion for second half
    Merge(list1, blist, clist)  #marging the half




def Merge(mainlist, sublist, sblist):
    '''Merge

    this function will merge the two sublists in sorted order
    '''
    #initialization of local variables
    i=0     #for sublist sub list
    j=0     #for sblist sublist
    k=0     #for loooping throught the elements of both lists

    #while sublists are not empty or list variable are not pointing to last element
    while (i < sublist.__len__()) and (j < sblist.__len__()):

        if sublist[i] < sblist[j]: #if sublist value is the sblist
            mainlist[k]=sublist[i]   #add sublist to main list
            i=i+1                    #increment iterator of sublist by one

         #else sblist element is less
        else:
            mainlist[k]=sblist[j] #add sublist to mainlist
            j=j+1                   #increment sublist iterator variable
        k=k+1           #increment mainlist iterator


    #if sublist element is at last position
    if i==sublist.__len__():
        for a in range(j,sblist.__len__()):#it show sblist is not empty
            mainlist[k]=sblist[a]   #add sblist element to mainlist
            k=k+1                   #increment mainlist iterator

    #else sblist iterator is at last position
    else:
        for a in range(i,sublist.__len__()):#add sublist element to main list
            mainlist[k]=sublist[a]           # add sublist element to mainlist
            k=k+1                 #increment mainlist iterator



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
    MargeSort(listOrg)
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))

    print listOrg[:]