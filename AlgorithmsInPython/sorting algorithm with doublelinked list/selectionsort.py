import DBNode
def selectionSort(list):
     '''selection sort algorithm
     '''
     node = list.start()        #getting first node of link list

     while node is not None:    #while not is not None
        minNode=node.getData()  #get save value of current node in minNode
        nextnode=node.getNext() #getting next node
        #print minNode,nextnode.getData()
        while nextnode is not None:     #looping from get node to end of list

            if nextnode.getData() < minNode:    #if minNode is greater then any of other node swap values
                temp=nextnode.getData()
                nextnode.setData(minNode)
                minNode=temp

            nextnode=nextnode.getNext()     #getting next node for inner while loop
        node.setData(minNode)               #setting the minNode value to current code
        node = node.getNext()               #getting next node for outer while loop
     list.show()                             #display list in sorted form

