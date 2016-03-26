import inspect
import weakref
class Node:
    '''

    Node class for defining Nodes that contain data and address of next element
    '''
    def __init__(self):
        '''constructor of Node Factory'''
        self.__data=0   #initializing private variable
        self.__Next=None    #private variable for holding address of next node

    #getData function function will return value of current node
    def getData(self):
        return self.__data

    #getNext function function will return address of current node
    def getNext(self):
        return self.__Next

    #setData function function will set value of current node
    def setData(self,data):
        self.__data=data

    #setNext function function will set address field of current node
    def setNext(self,Next):
        self.__Next=Next
    #    def __str__(self):
    #        return str(self.__data)





#-----------------------------------------------------Double link list class--------------------------------------------------#



class List:
    '''List
            this class will use Node class to create a link list
    '''
    def __init__(self):
        '''constructor of list class'''
        self.__headNode=Node()          #defining private head node which i indicator of start piont
        self.__headNode.setNext(None)   #set next to null
        self.Current=self.__headNode  #set current position to start of list
        self.lastCurrent=None
        self.length=0


    def headNode(self):
        return self.__headNode
    def lastCurrent(self):
        return self.lastCurrent

    #function for adding element to the list
    def Add(self,object):   #this function will take one argument which is data for insertion
        newNode=Node()          #create new for holding new data
        newNode.setData(object) #insert data to newly created node
        newNode.setNext(None)   #set next pointer to null
        self.length=self.length+1
        #if current is pionting to head that show is it is the first element in list
        if self.Current==self.headNode:
            self.__headNode.setNext(newNode)#set next of field of headnode to newnode
            self.lastCurrent=self.Current   #moving last current to current position
            self.Current=newNode              #move current pointer to to newnode

        #if current is not pointing to headnode list is not empty
        else:
            self.Current.setNext(newNode) #set the next field of current to new object
            self.lastCurrent=self.Current
            self.Current=newNode          #move the current field to new node



    #remove function will remove current element of list list
    def remove(self):
        if self.length>0:
            self.lastCurrent.setNext(self.Current.getNext())
            self.Current.setNext(None)
            del self.Current
           # print self.__Current.getData()
            self.Current=self.lastCurrent.getNext()
            self.length=self.length-1

    #Deleting a node of a give value
    def delete(self,data):
         #   print "here"
            self.lastCurrent=self.__headNode
            self.Current=self.__headNode.getNext()
          #  print "here"
            for i in range(0,self.length):
               # print self.__Current.getData()
                if self.Current.getData() == data:
                    print self.Current.getData()
                    self.lastCurrent.setNext(self.Current.getNext())
                    self.Current.setNext(None)
                    del self.Current
                    self.Current=self.lastCurrent.getNext()
                    self.length=self.length-1
                    break
                self.lastCurrent=self.Current
                self.Current=self.Current.getNext()


    #this function will print length of link list
    def __len__(self):
         return self.length



    #move current position to next element
    def next(self):
        if self.Current.getNext()!=None:
            self.lastCurrent=self.Current
            self.Current=self.Current.getNext()
            return self.Current
        else:
            return None



    #moving current position to start
    def start(self):
        self.lastCurrent=self.__headNode
        self.Current=self.__headNode.getNext()
        return self.Current
    def nstart(self):
        self.Current=self.__headNode

    #this function is used to return current node data
    def get(self):
        return self.Current.getData()

    #isEmpty function is use to check weither function is empty or not
    def isEmpty(self):
        if self.length==0:
            return True

    #function for displaying list
    def show(self):
        self.Current=self.__headNode  #move current pointer to starting position
        while self.Current.getNext()!=None:   #continue reading until the next field become empty
            self.Current=self.Current.getNext() #move current pionter to next element
            print str(self.Current.getData()) ,#print data of current current element
    #geting last index of linked list
    def last(self):
        self.Current=self.__headNode  #move current pointer to starting position
        while self.Current.getNext()!=None:   #continue reading until the next field become empty
           # if self.__Current.getNext()!=None:
                self.Current=self.Current.getNext()
            #else:
        return self.Current



    def __str__(self):
        return str(self.Current.getData())
