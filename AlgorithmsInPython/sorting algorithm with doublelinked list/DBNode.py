class Node:
    '''Node class for defining Nodes that contain data and address of next element
    '''
    def __init__(self):
        '''constructor of Node Factory'''
        self.__data=0   #initializing private variable
        self.__Next=None    #private variable for holding address of next node
        self.__prev=None    #pointer to the previous element

    #getData  function will return value of current node
    def getData(self):
        return self.__data

    #getNext  function will return address of next node
    def getNext(self):
        return self.__Next


    #getprev  function will return address of previous node
    def getPrev(self):
        return self.__prev


    #setData function  will set value of current node
    def setData(self,data):
        self.__data=data

    #setNext function  will set address field of current node
    def setNext(self,Next):
        self.__Next=Next


    #setprev function  will set address field of current node
    def setPrev(self,prev):
        self.__prev=prev

#    def __str__(self):
#        return str(self.__data)





#-----------------------------------------------------Double link list class--------------------------------------------------#
class DoubleList:
    '''List
            this class will use Node class to create a link list
    '''
    def __init__(self):
        '''constructor of list class'''
        self.__headNode=Node()          #defining private head node which i indicator of start piont
        self.__headNode.setNext(None)   #set next to null
        self.__headNode.setPrev(None)   #prev address to null
        self.__Current=self.__headNode  #set current position to start of list
        self.__lastCurrent=None
        self.__length=0



    #function for adding element to the list
    def Add(self,object):   #this function will take one argument which is data for insertion
        newNode=Node()          #create new for holding new data
        newNode.setData(object) #insert data to newly created node
        self.__length=self.__length+1
        #if current is pionting to head that show is it is the first element in list
        if self.__Current==self.__headNode:
            newNode.setNext(None)   #set next pointer to null
            self.__headNode.setNext(newNode)#set next of field of headnode to newnode
            newNode.setPrev(self.__headNode)
            self.__lastCurrent=self.__Current   #moving last current to current position
            self.__Current=newNode              #move current pointer to to newnode

        #if current is not pointing to headnode list is not empty
        else:
            newNode.setPrev(self.__Current)
            newNode.setNext(self.__Current.getNext())
            self.__Current.setNext(newNode) #set the next field of current to new object
            self.__lastCurrent=self.__Current
            self.__Current=newNode          #move the current field to new node



    #remove function will remove current element of list list
    def remove(self):
        if self.__length>0:
            self.__lastCurrent.setNext(self.__Current.getNext())
            (self.__Current.getNext()).setPrev(self.__lastCurrent)
            self.__Current.setNext(None)
            self.__Current.setPrev(None)
            del self.__Current
           # print self.__Current.getData()
            self.__Current=self.__lastCurrent.getNext()
            self.__length=self.__length-1



    #this function will print length of link list
    def __len__(self):
         return self.__length



    #move current position to next element
    def next(self):
        if self.__Current.getNext()!=None:
            self.__lastCurrent=self.__Current
            self.__Current=self.__Current.getNext()

    def prev(self):
        if self.__Current.getPrev()!=None:
            self.__lastCurrent=self.__Current
            self.__Current=self.__Current.getPrev()


    #moving current position to start
    def start(self):
        self.__lastCurrent=self.__headNode
        self.__Current=self.__headNode.getNext()
        return self.__Current

    #this function is used to return current node data
    def get(self):
        return self.__Current.getData()

    #  isEmpty function is use to check weither function is empty or not
    def isEmpty(self):
        if self.__length==0:
            return True

    #function for displaying list
    def show(self):
        self.__Current=self.__headNode  #move current pointer to starting position
        while self.__Current.getNext()!=None:   #continue reading until the next field become empty
            self.__Current=self.__Current.getNext() #move current pionter to next element
            print str(self.__Current.getData()) ,#print data of current current element
    #geting last index of linked list
    def last(self):
        self.__Current=self.__headNode  #move current pointer to starting position
        while self.__Current.getNext()!=None:   #continue reading until the next field become empty
           # if self.__Current.getNext()!=None:
                self.__Current=self.__Current.getNext()
            #else:
        return self.__Current




    def __str__(self):
        return str(self.__Current.getData())
    #Deleting a node of a give value
    def delete(self,data):
         #   print "here"
            self.__lastCurrent=self.__headNode
            self.__Current=self.__headNode.getNext()
          #  print "here"
            for i in range(0,self.__length):
               # print self.__Current.getData()
                if self.__Current.getData() == data:
                    print self.__Current.getData()
                    self.__lastCurrent.setNext(self.__Current.getNext())
                    (self.__Current.getNext()).setPrev(self.__lastCurrent)
                    self.__Current.setNext(None)
                    self.__Current.setPrev(None)
                    del self.__Current
                    self.__Current=self.__lastCurrent.getNext()
                    self.__length=self.__length-1
                    break
                self.__lastCurrent=self.__Current
                self.__Current=self.__Current.getNext()

