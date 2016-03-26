import Node

def InsertionSort(list):
     '''


     Insertion Sort algorithm
     '''

     currentpre=list.headNode() #node before current node
     current=currentpre.getNext()   #current pionter of linked list

     #outer loop for insertion sort
     while current!=None:
        sortedLastCurrent=list.headNode()       #selecting first node as minimum values node
        sortedCurrent=sortedLastCurrent.getNext()     #node for next inner loop of selection sort

        #inner loop of  selection sort
        while sortedCurrent!=current:


        #there are there condition of minimum value pointer
        #(i) current pointer is minimum value pointer in this case will do no swap
        #(ii) pointer pointed to minimum value pointer in this case if will be executed
        #(iii) pointer is some where else in the linked list in this case elif will be executed

            if sortedCurrent.getData()>current.getData():

                #case ii
                #pionter are next to each other in this we did not beforesort pointer because that is current pointer
                # and we did not next next pointer of current node here is code
                if sortedCurrent.getNext()==current:

                     nextpointer=current.getNext()          #storing next pointer of of current node
                     sortedLastCurrent.setNext(current)     #set the current to next of sorted last current
                     current.setNext(sortedCurrent)         #set next of current to sorted current
                     sortedCurrent.setNext(nextpointer)     #set next of sorted current to nextpointer
                     sortedCurrent=current                   #set sorted current to current


                     #case iii
                     #in this case we need all four pointer we have created for swapping
                     #i.e i) pre-pointer of current node  ii)nex pointer of current node
                     #    iii)pre-pointer of sorted node    iv) pointer pointed my sorted node
                     #here is code for swapping
                elif sortedCurrent.getNext()!=current:

                     nextpointer=current.getNext()              #storing next pointer of of current node
                     sortednext=sortedCurrent.getNext()         #storing next of sorted current node
                     sortedLastCurrent.setNext(current)         #set current to next of sorted last current node
                     current.setNext(sortednext)                #set next of current to sorted next
                     currentpre.setNext(sortedCurrent)          #set next of currentpre to sorted current
                     sortedCurrent.setNext(nextpointer)         #set next of sorted current to next pointer
                     sortedCurrent=current                      #set sorted current to current pointer

            sortedLastCurrent=sortedCurrent                 #set sorted last current to current
            sortedCurrent=sortedCurrent.getNext()           #set sorted current to current ->next
        currentpre=current                          #set currentpre to current
        current=current.getNext()                   #set current to getNext
     #list.show()



