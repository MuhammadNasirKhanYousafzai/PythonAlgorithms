import DBNode
def InsertionSort(list):
     '''


     Insertion Sort algorithm
     '''

     node = list.start()        #getting first node of link list

     while node is not None:    #while not is not None
        sortedNode=list.start()  #get save value of current node in minNode
       # print sortedNode," last",node
        while sortedNode !=node:     #looping from get node to end of list

            if sortedNode.getData() > node.getData():    #if minNode is greater then any of other node swap values
                temp=sortedNode.getData()
                sortedNode.setData(node.getData())
                node.setData(temp)

            sortedNode=sortedNode.getNext()     #getting next node for inner while loop
        node = node.getNext()               #getting next node for outer while loop

     list.show()        #display list in sorted form
