class TreeNode:
    def __init__(self):     #constructor
        self.__data=0       #data element
        self.__left=None    #left subtree address
        self.__right=None   #right subtree addess


    def getData(self):  #function for returning data of Node
        return self.__data  #return value of node


    def getLeft(self):  #function for returning left child address
        return self.__left


    def getRight(self): #function for returning right child address
        return  self.__right


    def setData(self,data):  #setting data of node
        self.__data=data


    def setLeft(self,left): #set address of left subtree
        self.__left=left

    def seRight(self,right):    #set address of right subtree
        self.__right=right



#----------------------------------------------------tree class---------------------------------------------#
#class CreateTree:

#    def __init__(self,node):#constructor of tree
 #       self.__root=TreeNode()
  #      self.__root.setData(node)
   #     self.__root.setLeft(None)
    #    self.__root.seRight(None)

def insert(Root,data):
    newNode=TreeNode()
    newNode.setData(data);
   # root=TreeNode()
    #parent=TreeNode()
    root=Root
    parent=Root
 #   print  "Node",parent.getData(),"  data",data
    while parent.getData()!=data and root!=None:
        parent=root
          #  print parent.getData()
        if  parent.getData() > data:
            root=parent.getLeft()
        else:
            root=parent.getRight()

    if data == parent.getData():
        print "data already exist"
        del newNode

    elif data<parent.getData():
        parent.setLeft(newNode)
#        print  "left Node"
    else:
        parent.seRight(newNode)
  #      print  "Right Node"



#sorting free element
def sortTree(node):
    if node !=None:
        sortTree(node.getLeft())
        print node.getData(),
        sortTree(node.getRight())

def delete(root,node):

    if node<root.getData():

        leftnode=delete(root.getLeft(),node)
        root.setLeft(leftnode)

    elif node > root.getData():
        rightnode=delete(root.getRight(),node)
        root.seRight(rightnode)
    elif node==root.getData() and(root.getLeft!=None and root.getRight()!=None):
        minnode=min(root.getRight())
        root.setData(minnode.getData())
        delnode=delete(root.getRight,minnode.getData())
        root.setRight(delnode)
    else:
        deletenode=root
        if(root.getRight()==None):

           root=root.getLeft()
        elif root.getLeft()==None:
            root=root.getRight()
        else:
            root=None
        del deletenode
    return root


    def min(root):
        if root ==None:
            return
        elif root.getLeft()==None:
            return  root
        min(root.getLeft())


#--------------------------------------------------------------------------------------------------------------#
def buildTree(root):
    addnext=True
    while addnext==True:
        data=int(raw_input("add data to tree"))
        insert(root,data)
        choice=int(raw_input("pree y to add an other node to tree"))
        if choice!='y' or choice!='Y':
            addnext=False


def deleteTree(root):
    addnext=True
    while addnext==True:
        data=int(raw_input("delete data to tree"))
        delete(root,data)
        choice=int(raw_input("pree y to delete an other node to tree"))
        if choice!='y' or choice!='Y':
            addnext=False



if __name__ == '__main__':
    '''Main function of the program'''
    testTree=True

    while testTree==True:
        root=TreeNode()
        rootData=int(raw_input("enter root of tree"))
        root.setData(rootData)
        buildTree(root)
        sortTree(root)
        deleteTree(root)
        sortTree(root)
        choice=int(raw_input("pree y to delete an other node to tree"))
        if choice!='y' or choice!='Y':
            testTree=False





