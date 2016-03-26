##############################################################
#########       AVL tree data structure           ############
#########               Dec 2014                  ############
#########       Author: Muhammad Nasir            ############
##############################################################

#class for making nodes of avl tree
class avlTreeNode:
    def __init__(self):     #constructor
        self.data=0     #da,ta of node
        self.left=None  #pointer to left child
        self.right=None #pointer to right child
        self.height=0    #height of node


#function for getting balance
#difference of left and right subtree
def getBalance(node):
        return height(node.left) - height(node.right)

#return max of the heights of nodes
def max(a,b):
    if a<b:
        return  b
    return a

#getting height of node
def height(node):
    if node==None:
        return 0;
    return node.height


#left rotation function of avl tree
def leftRotation(node):
    '''leftRotation

        get right subtree of node.let say it is newparent. move rightsubtree
        of newparent to right subtree of node.set node to left subtree of newparent. return
        newparent
    '''
    newParent=node.right    #getting right child tree node as new parent node
    rightchild=newParent.left   #getting left subtree of new parent
    newParent.left=node     #set node to left subtree of new parent
    node.right=rightchild           #set right of newparent to node
    node.height=max(height(node.right),height(node.left))+1   #set height of node
    newParent.height=max(height(newParent.right),height(newParent.left))+1#set height of new node
    return newParent            #return new node



def rightRotation(node):
    '''right rotation

        get left subtree of node.let say it is newparent. move leftsubtree
        of newparent to right subtree of node.set node to left subtree of newparent. return
        newparent
    '''
    newParent=node.left    #getting left child tree node as new parent node
    righttchild=newParent.right   #getting right subtree of new parent
    newParent.right=node     #set node to left subtree of new parent
    node.left=righttchild           #set right of newparent to node#
    node.height=max(height(node.right),height(node.left))+1   #set height of node
    newParent.height=max(height(newParent.right),height(newParent.left))+1#set height of new node
    return newParent            #return new node



#insertion function of AVL is same as BST but we have check AVL property after insertion
#and if tree is not in AVL form rotate it
def insert(root,data):
    newNode=avlTreeNode()   #make a new
    newNode.data=data       #assign data to it's data part

   # print "here",data
    currentnode=nextnode=root               #make two for iteration throght the tree

    while currentnode.data !=data and nextnode!=None:   #if next node is not None and data is not equal to current node data
        currentnode=nextnode                #move current node ot nextnode

        if currentnode.data<data:           #get next
      #      print "here",data
            nextnode=currentnode.right

        else:
            nextnode=currentnode.left

    if currentnode.data==data:      #if data already exist
        print "data is already in list"
        del newNode             #do not add to list
        return

    elif currentnode.data<data:         #if node is greater add to right side
        currentnode.right=newNode
    else:                               #else add to left side of node
        currentnode.left=newNode

    root=fixInsertion(root,data)    #fixing up variation that occoured with insertion

    return root


#fixInsertion will check the tree and if there is any variation made it correct
def fixInsertion(root,data):
    '''fixInsertion

    this is a recursive function for checking the avail property a every node starting from last inserted node to root if
     there is any variation call the appropiate rotation
    '''
    #this control statement is use for moving recursively to last add nod
    if root.data<data:
        root.right = fixInsertion(root.right,data)
    elif root.data>data:
      root.left =  fixInsertion(root.left,data)
    else:
        root.height=max(height(root.left),height(root.right))+1
        return root
    #when the recently add node is reached start checking for AVL properties
    #if its hold move to parent if not make rotation
    #get height of current node
    root.height=max(height(root.left),height(root.right))+1
    #check difference between left and right child of tree
    blnce=getBalance(root)

    #case 1
   #if new node is added to left of child of root left subtree
    if blnce>1 and data<(root.left).data:
       return rightRotation(root)
    #case 2
    #if new node is added to right child of root left subtree
    elif blnce>1 and data>(root.left).data:
            root.left=leftRotation(root.getLeft())
            return rightRotation(root)

    #case 3
    #if new node is added to right child of root right subtree
    elif blnce<-1 and data>(root.right).data:
            return leftRotation(root)

    #case 4
    #if new node is add to left child of root right subtree
    elif blnce<-1 and data<(root.right).data:
            root.right=rightRotation(root.right)
            return leftRotation(root)

   #if root is in avl form return root with any rotation
    return root


#delete function is used to delete a node from current current tree
def delete(root,node):
    '''delete
    deletion from avl is same from BST but after deletion we have check avl tree condition
    deletion from BST is done my recusive call so we can add the fixing condition of avl to delete
    function without making a new function call
    '''

    if node<root.data:              #if node is less the root then node will be deleted from left subtree
        leftnode=delete(root.left,node)
        root.left=leftnode

    elif node > root.data:          #if node is greater then root the node to be deleted will be in right subtree
        rightnode=delete(root.right,node)
        root.right=rightnode


    #else if root is same node then there are two main condition for deletion
    #case 1
    #if root == node and its left and right subtree is not Node
    #find the node with with minimum will in right subtree and replay with with root
    #node in the right subtree find that node and delete from tree
    elif node==root.data and(root.left!=None and root.right!=None):
        minnode=min(root.right)
        root.setData(minnode.data)
        delnode=delete(root.right,minnode.data)
        root.right=delnode

    #case 1
    #if one of both subtree of root is Node
    #this is simple case if deletion replace root with subtree or None
    else:
        deletenode=root         #get pointer of root node
        if(root.right==None):       #if right subtree is Node replace root with left subtree

           root=root.left
        elif root.left==None:           #else replace with right subtree
            root=root.right
        else:                            #if both are None replay roo wih Node
            root=None
        del deletenode
        return root                     #return root

    #get balance of root node and check for avl condition
    #there is 4 cases for deletion too
    blnce=getBalance(root)

    #case 1
    #if node is deleted from left child of left subtree of root
    if blnce>1 and getBalance(root.left)>=0:
       return rightRotation(root)

    #case 2
    #if node is deleted from right child of left subtree of root
    elif blnce>1 and getBalance(root.left)<0:
            root.left=leftRotation(root.getLeft())
            return rightRotation(root)


    #case 3
    #if node is deleted from right child of right subtree of root
    elif blnce<-1 and getBalance(root.right)<=0:
            return leftRotation(root)


    #case 4
    #if node is deleted from left child of right subtree of root
    elif blnce<-1 and getBalance(root.right)>0:
            root.right=rightRotation(root.right)
            return leftRotation(root)

    #if root is satisfy avl tree condition return root
    return root



#function for returning subling of node
def sibling(node):
 if node == (node.parent).left:
  return (node.parent).right;
 else:
  return (node.parent).left;




def sortTree(node):
    if node !=None:
        sortTree(node.left)
        print node.data,
        sortTree(node.right)



if __name__ == '__main__':
    root=avlTreeNode()
    root.data=33
    #print root.height
    #root=insert(root,55)
    #root=insert(root,56)
   # root=insert(root,58)


    #sortTree(root)
  #  delete(root,58)
    rights=root.right
    print '\n root',root.data
    sortTree(root)
