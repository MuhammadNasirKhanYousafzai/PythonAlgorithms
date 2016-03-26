def Buildheap(list1):
    '''Build heap
    this is partially sorted list that contain element with greatest priority at the first index
    assumption -> list first element is at 1 index
    '''

    #getting midpiont of list due to the data is contain structure like tree
    iterator=list1.__len__()/2
 #   print "after",list1[iterator]

    while iterator>0: #continue iteration from mid of list to first element

        notheap=True   #boolean variable for checking heap status
        j=iterator      #start building heap from current value of iterator
       # print "after",list1[iterator]

        #continue iteration till the end or notheap become false
        while(notheap==True and j*2<(list1.__len__())):
            j=2*j       #geting left child
      #      print list1[j],"before",list1[iterator]

            #if right child is in the heap and greater then right chiled
            if (j+1<list1.__len__()) and (list1[j]<list1[j+1]):
                j=j+1       #get the left child

            if(list1[j]>list1[iterator]):   #compare it with parent
                tmp=list1[iterator]        #if greater swap parent with child
                list1[iterator]=list1[j]
                list1[j]=tmp
     #           print "after",list1[iterator]

            else:       #if bigest child is not greater the parent
                notheap=False   #it is a heap

        iterator=iterator-1     #continue iteration to first element






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
    Buildheap(listOrg)
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))

    
    #printing heap element on the screen according to priority
 #   while i>0:
  #      print listOrg[1]
   #     del listOrg[1]
    #    Buildheap(listOrg)
     #   i=i-1
