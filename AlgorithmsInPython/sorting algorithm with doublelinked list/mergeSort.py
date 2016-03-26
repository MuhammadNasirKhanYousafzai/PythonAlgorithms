import DBNode
def MargeSort(head):
     '''Merge sort

                    this function is used to merge linked list
     '''

     if head == None or head.getNext() == None:
        return head

     midnode=middleNode(head)    #get midpiont of linked list
     secondhalf=midnode.getNext()   #set start piont of second of half
     midnode.setNext(None)          #dividing linked list in 2 halfs
    #function for merging two half of linked list
     head= marge(head,midnode,MargeSort(head),MargeSort(secondhalf))
     return head



def marge(head,midnode,firsthalf,secondhalf):
   # news=Node()
    midnode.setNext(secondhalf) #marging the two halfs
    news=head       #linked list for sorting elements
    midns=secondhalf    #mindpiont of linked list
    list=[]             #list for holding sorted data
   #loop for sorting element
    while firsthalf !=midns and secondhalf!=None:
        if firsthalf.getData()<=secondhalf.getData():
            list.append(firsthalf.getData())
            firsthalf=firsthalf.getNext()
        else:
            list.append(secondhalf.getData())
            secondhalf=secondhalf.getNext()
    #if first half is not Node add to list
    if  firsthalf!=midns:
         while firsthalf!=midns:
             list.append(firsthalf.getData())
             firsthalf=firsthalf.getNext()
   #add second half to list
    else:
        while secondhalf!=None:
            list.append(secondhalf.getData())
            secondhalf=secondhalf.getNext()

    #add element of list to linked list
    for i in list:
        news.setData(i)
        news=news.getNext()
    return head

def middleNode(node):
    '''middle Node
            this function will return the middle node of linked list
    '''
    if node==None:
        return node
    mid=node
    end=node
    while end.getNext()!=None and mid.getNext()!=None and (end.getNext()).getNext()!=None:
        mid=mid.getNext()
        end=(end.getNext()).getNext()

    return mid


