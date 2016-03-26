import Node
def selectionSort(list):
     '''selection sort algorithm

     selection sort algorithm for linked list with swaping pointer values
     '''
     currentpre=list.headNode() #node before current node
     current=currentpre.getNext()   #current pionter of linked list

     #outer loop for selection sort
     while current!=None:
        minimum=current       #selecting first node as minimum values node
        nextprev=current;       #previous node for nextinner pointer
        beforesort=nextprev     #previous not for the pointer with minimum value
        nextinner=current.getNext()     #node for next inner loop of selection sort

        #inner loop of  selection sort
        while nextinner!=None:

            if minimum.getData()>nextinner.getData():   #finding minimum value pointer
                beforesort=nextprev                     #setting values of pointer to minimum value pointer
                minimum=nextinner
            nextprev=nextinner
            nextinner=nextinner.getNext()


        #after the inner loop completion of cycle we will have all values in correnponding pointer
        #there are there condition of minimum value pointer
        #(i) current pointer is minimum value pointer in this case will do no swap
        #(ii) pointer pointed to minimum value pointer in this case if will be executed
        #(iii) pointer is some where else in the linked list in this case elif will be executed

        #case ii
        #pionter are next to each other in this we did not beforesort pointer because that is current pointer
        # and we did not next next pointer of current node here is code
        if current.getNext()==minimum :
            minimumNext=minimum.getNext()   #pointer to next node pointed my minimum node
            currentpre.setNext(minimum)     #nex pointer of pointer before the current node is to minimum node
            minimum.setNext(current)        #set minimum next pointer of minimum node to current
            current.setNext(minimumNext)    #set next pointer of current to next pointer pointed my my minimum pointer
            current=minimum                 #set current to minimum

        #case iii
        #in this case we need all four pointer we have created for swapping
        #i.e i) pre-pointer of current node  ii)nex pointer of current node
        #    iii)pre-pointer of sorted node    iv) pointer pointed my sorted node
        #here is code for swapping
        elif current.getNext()!=minimum and current!=minimum:
                 currentNext=current.getNext()            #pointer pointed my the current node
                 minimumNext=minimum.getNext()           #pointer to next node pointed my minimum node
                 currentpre.setNext(minimum)               #set pre-current to minimum pointer
                 minimum.setNext(currentNext)             #set next pointer of minimum node to currentNext pointer
                 beforesort.setNext(current)                #setting pre pointer of sorted node to current pointer
                 current.setNext(minimumNext)               #current pointer next pointer set to next of minimumNext
                 current=minimum                             #set current to minimum
        currentpre=current              #set pre-current to current
        current=current.getNext()       #set current to current ->next
     list.show()