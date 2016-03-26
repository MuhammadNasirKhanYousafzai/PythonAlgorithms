import DBNode
def QuickSort(head,last):
     '''Quick sort

                    sort link list using quick sort algorithm

     '''
#     print head.getData(),last.getData()
     if head==None or head==last:
        return
     povit=partition(head,last)
     QuickSort(head,povit)
     QuickSort(povit.getNext(),last)




def partition(head,last):
    '''partition

            partition function return the povit node a it's sorted position in the list
            by moving node with greater walue to right and nodes with somaller walue to
            left side of povit
    '''
    povit=head.getData()    #povit of the linked ist
    sort=head               #data in sorted linked list
    head=head.getNext()     #moving current node to the second node
    less=[]                   #list for holding values of less then the povit node
    greater=[]                 #list for holding values greater then the povit of node
    while head!=last.getNext(): #loop thourgh the linked list
      if povit<head.getData():
          greater.append(head.getData())
      else:
          less.append(head.getData())
      head=head.getNext()

    for i in less:  #adding values less then povit
        sort.setData(i)
        sort=sort.getNext()

    sort.setData(povit) #povit point in linked list at it's sorted position
    seletedpovit=sort   #get the linked list not of povit piont
    sort=sort.getNext() #move the node to next next node
    for i in greater:   #adding values greater then the povit point of linked list
        sort.setData(i)
        sort=sort.getNext()

    return seletedpovit     #return povit node of linked list


