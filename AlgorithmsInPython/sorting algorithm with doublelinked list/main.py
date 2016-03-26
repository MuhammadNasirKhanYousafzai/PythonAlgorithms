import DBNode,selectionsort,bublesSort,insertionSort,mergeSort,quickSort


#getting nodes of list from user
def add(list):
        item=True
        #adding element of linked list
        while item==True:
            addItem=int(raw_input("add number to list   "))
            list.Add(addItem)
            print"----------------------------------------------"

            check=raw_input("Y or y to add an other number to list   ")
            if check!='y' and check!='Y':
                item=False


#function for applaying algorithms on the list
def performOperation(list):
    #while loop for perfoming operation on the linked list
    performOperation=True
    while performOperation==True:
        print "select operation on linked list"
        operation=int(raw_input("1 for seletion sort \n 2 for bubble sort \n 3 form insertion sort   \n 4 for merge sort  \n 5 for quick sort"))

        #performing operation on the linked list according to user input
        if operation==1:
            print "selection sort operation"
            selectionsort.selectionSort(list)
        elif operation==2:
            print "Bubble sort operation"
            bublesSort.BubbleSort(list)
        elif operation==3:
            print "Insertion sort operation"
            insertionSort.InsertionSort(list)
            list.show()
        elif operation==4:
            print "Merge  sort operation"
            mergeSort.MargeSort(list.start())
            list.show()
        elif operation==5:
            print "Quick sort operation"
            quickSort.QuickSort(list.start(),list.last())
            list.show()
        else:
            print "enter a valid option"
        check=raw_input("\nenter y or Y perform other operation ")
        if check!='y' and check!='Y':
            performOperation=False




def deleteNode(list):
    performOperation=True
    while performOperation==True:
        node=raw_input("\nenter element you want to delete ")
        list.delete(int(node))
        print "press y to delete other node"
        if check!='y' and check!='Y':
            performOperation=False



if __name__ == '__main__':
    '''Main function of the program'''


    listoperation=True
    #while loop for changing values of linked list
    while listoperation == True:
        list=DBNode.List()
        print "this is new linked list"
        add(list)
        performOperation(list)
        choice=int (raw_input("press 1 for adding element to list and 2 for deleting not any other key for"))
        if(choice==1):
            add(list)
        elif choice==2:
            deleteNode(list)

        check=raw_input("Y or y to perform operation on different  list    ")
        if check!='y' and check!='Y':
                listoperation=False

    print doctest.testmod(verbose=True)
