##############################################################
#########    red black tree data structure        ############
#########               Dec 2014                  ############
#########       Author: Muhammad Nasir            ############
##############################################################

class red_blackNode:
    def __init__(self):
        self.data=0
        self.left=None
        self.right=None
        self.parent=None
        self.color='r'

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

    if node.right !=None:
        (node.right).parent=node

    newParent.parent=node.parent

    node.parent=newParent
    return newParent



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
    if node.right !=None:
        (node.rght).parent=node

    newParent.parent=node.parent
    node.parent=newParent
    return newParent




def insert(root,data):
    newNode=red_blackNode()   #make a new
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
    newNode.parent=currentnode
    IsRootNode(newNode)
    return root

#grandparent function will return  grandparent if exist
#if grandparent did not exist i will return Node
def grandparent(node):

 if (node != None) and node.parent != None: #IF     NODE and Parent IS NOT Node is not Node
    return (node.parent).parent             #return grandparent
 else:
  return  None          #return None


#this function is use to return uncle for current . sibling of parent node
def uncle(node):
  grandp= grandparent(node)         #get grandparent node using function
  if grandp ==None:                 #if grandparent is  null return Node
    return None   # No grandparent means no uncle
  if node.parent == grandp.left:                #parent is left of grandparent
    return grandp.right                          #return right child of grandparent
  else:                                             #else return left child
    return grandp.left


#check the node. if it is root labeled with black color
def IsRootNode(node):
 if (node.parent == None):  #if parent is Node
    node.color = 'b'            #currnet node is root
 else:
    blackParent(node)       #check if root node parent is black


#this function is used to check parent of node.
#if node parent is black return tree is in RB form
def blackParent(node ):

 if ((node.parent).color == 'b'):   #if parent is red
  return #  Tree is still valid
 else:
    parentNuncleAreRed(node)     #check if uncle color is red


#this function will check uncle color.
#function will validate tree depend of color of uncle
def parentNuncleAreRed(node):

  Nodeuncle = uncle(node)       #get value of uncle node
  if Nodeuncle!=None and Nodeuncle.color =='r': # if uncle is red
      (node.parent).color = 'b'         #label uncle and parent with black
      Nodeuncle.color = 'b'
      grandp = grandparent(node)        #color of grandparent and node to red
      grandp.color = 'r'
      IsRootNode(grandp)                #check if tree is root node change color of black
  else: #if uncle color is not red
    LR_RLcase(node)

#LR =left child of right parent
#RL= right child of left parent
#this case same like AVL free LR RL rotation
def LR_RLcase(node):
    #get grandparend node
    grandp = grandparent(node)
    #if current node is left child of right child of grandparend
    #right rotate parent
    if node == (node.parent).right and (node.parent == grandp.left) :
        node.parent=leftRotation(node.parent)
        node = node.left

        #if current node is rigt child of left child of grandparend
        #left rotate parent
    elif node == (node.parent).left and node.parent == grandp.right:
        node.parent=rightRotation(node.parent)
        node = node.right
    nodeRotation(node)  #else tree in LL and RR case

#in this function the case of left child of left subtree and right child of right
# is solved make making left roatation to right subtree and left rotation fo right subtree
def nodeRotation(node):

   grandp = grandparent(node)       #geting grand parent
   (node.parent).color = 'b'        #set parent to black
   grandp.color = 'r'               #grand parent to red

   if node == (node.parent).left:   # if node is left child
        grandp=rightRotation(grandp)        #right rotate tree
   else:
         grandp=leftRotation(grandp)        #left rotate  tree






def delete(root,node):
    '''delete
    deletion from red black tree is same from BST but after deletion we have check redblack tree condition
    deletion from BST is done my recusive call so we can add the fixing condition of redblack tree to delete
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
        if deletenode.color=='b':
            if root.color=='r':
                root.color='b'
        del deletenode
        isLeafNode(root)    #validation red black tree
    return root

#function for finding sibling
def sibling(node):

 if node == (node.parent).left:         #if current node is left
     return (node.parent).right         #return right node
 else:
     return (node.parent).left          # return left node





def isLeafNode(node ):      #if current not is leaf node tree vali
 if node!=None and (node.parent != None):   #if node is not leaf
    siblingcolor(node)    #check color of sibling

#check color if sibling simple case if sible is red
def siblingcolor(node):

  siblng = sibling(node)    #get sibling node

  if (siblng.color == 'r') :    #if color is red
      (node.parent).color = 'r' #change parent color to red
      siblng.color = 'b'        #sibling color to black
      if (node == (node.parent).left):      #if node is
          leftRotation(node.parent) #left rotate parent
      else:
            rightRotation(node.parent)  #right rotate parent

  parentsiblingRblack(node)

#if parant sibling and sibling children have have color change color of sibling to red and perform balancing
def parentsiblingRblack(node ):

   siblng = sibling(node)   #getting sibling

   if (node.parent).color == 'b' and (siblng.color == 'b') and (siblng.left).color == 'b' and (siblng.right).color == 'b' :
      siblng.color = 'r'    #if all required node have black color label sibling with red color
      isLeafNode(node.parent)   #perform balancing of parent because color to black will change number of black nodes
   else:        #if parent is not black
       parentIsRed(node)

#handle case of deletion were sibling and sibling children are black and parent is red
def parentIsRed(node):

   siblng = sibling(node)

   if (node.parent).color == 'r' and siblng.color == 'b' and (siblng.left).color == 'b' and (siblng.right).color == 'b':
        siblng.color = 'r'  #if parent is change sibling to red
        (node.parent).color = 'b'   #change parent to black this changing will not volite any role
   else:
        siblingNOneChildIsRed(node)#if sibling is black but its child have different color


#function for handles volition occoured when sibling is red and on of its child black and other is red
def siblingNOneChildIsRed(node):

  siblng = sibling(node)    #getting sibling of current node

  if  siblng.color == 'b':  #if sibling color is black

      #if sibling is left child and it left child color is red
      if node == (node.parent).left and (siblng.right).color == 'b' and (siblng.left).color == 'r':
         siblng.color = 'r' #chang sibling color of black
         (siblng.left).color = 'b'  #change left child to black
         rightRotation(siblng)  #right rotate tree

         #if sibling is right child if parent and its right child is red
      elif node == (node.parent).right and (siblng.left).color == 'b' and (siblng.right).color == 'r':
          siblng.color = 'r'    #change sibling to red
          (siblng.right).color = 'b'    #change right child to black
          leftRotation(siblng)  #left rotate sibling

  LL_RRIsRed(node)
#left sibling left child or right sibling right chlid is red
def LL_RRIsRed(node):

    siblng = sibling(node) #get sibling node
    siblng.color = (node.parent).color #change color of parent and sibling
    (node.parent).color = 'b'       #set parent to black
    if node == (node.parent).left : #if sibling is red child
        (siblng.right).color = 'b' #chind sibling right color ro red
        leftRotation(node.parent)   #left rotate parent
    else :
        (siblng.left).color = 'b'      #change left child color to balck
        rightRotation(node.parent)      #right rotate tree




def sortTree(node):
    if node !=None:
        sortTree(node.left)
        print node.data," ",node.color,
        sortTree(node.right)

if __name__ == '__main__':
    root=red_blackNode()
    root.data=16
    root.color='b'
    root=insert(root,66)
    root=insert(root,44)
    #sortTree(root)
    print "root",root.data
    sortTree(root)
#    print "\n",(root.left).data
