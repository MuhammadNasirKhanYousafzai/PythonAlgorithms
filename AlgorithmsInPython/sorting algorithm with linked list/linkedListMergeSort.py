import Node
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
     return marge(MargeSort(head),MargeSort(secondhalf))



def marge(firsthalf,secondhalf):
    list=List()
    curr=list.headNode()
    while firsthalf !=None and secondhalf!=None:

        if firsthalf.getData()<secondhalf.getData():
            curr.setNext(firsthalf)
            firsthalf=firsthalf.getNext()
        else:
            curr.setNext(secondhalf)
            secondhalf=secondhalf.getNext()
        curr=curr.getNext()
    #if first half is not Node add to list
    if firsthalf!=None:
        curr.setNext(firsthalf)
    else:
        curr.setNext(secondhalf)
    print '\n------------------------'
    list.show()
    resut=list.start()
    return resut

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


