import DBNode
def BubbleSort(list):
     '''


     Bubble sort algorithm
     loop is bubble sort will same as loop for build in data type
     '''
     listItem=list.__len__()    #getting length of list

     for iterator in range(0,listItem-1):       #outer loop
        node = list.start()         #getting start of list
        node2=node.getNext()        #getting second element of list
        #        print node.getData()," ",node2.getData()    #test for start values

        for innerlop in range(0,listItem-iterator-1):   #inner loop

            if node.getData()>node2.getData():          #if node greater then node2 swape values
                temp=node.getData()
                node.setData(node2.getData())
                node2.setData(temp)

            node=node2              #move mode to next node
            node2=node2.getNext()   #move node2 to next next node

     list.show()        #display list in sorted form





