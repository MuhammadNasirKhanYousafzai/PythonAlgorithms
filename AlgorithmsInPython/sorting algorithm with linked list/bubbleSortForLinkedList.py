import Node
def BubbleSort(list):
     '''


     Bubble sort algorithm
     loop is bubble sort will same as loop for build in data type
     '''
     listItem=list.__len__()    #getting length of list
     end =None                    #defining end of inner loop

     #out loop for loop which is used only for n iteration of bubble sort
     for iterator in range(0,listItem):

         lastcurrent=list.headNode()    #set last current to headnode of linked list
         current=lastcurrent.getNext()  #set current pointer to first node


         #while loop which perform swappin of pointer in the linked list
         while current.getNext()!=end:      #while it is not equal to end pointer

            #IF consecutive values are not in order make a swap
             if current.getData()> (current.getNext()).getData():

                nextnode=current.getNext()          #variable for holding next pointer
                nextpointer=nextnode.getNext()      #pointer variable for holding address pointed my next pointer

                lastcurrent.setNext(nextnode)       #set last current pointer to next node
                nextnode.setNext(current)           #set the next of next node pointer to current

                current.setNext(nextpointer)        #set next of current to nextpointer variable
                current=nextnode                    #make the new node as current

             lastcurrent=current                    #move lastcurrent node
             current=current.getNext()              #move current node

         end=current                                 #decrease inloop by one pointer each time
     list.show()

