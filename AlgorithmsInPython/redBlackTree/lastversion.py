class tree:
    def __init__(self):
        self.data=0
        self.left=None
        self.right=None
        self.parent=None
        self.color='r'


def rotate_right(node):
    newNode=node.left;
    nodeLeft=newNode.right;
    newNode.right=node
    node.left=nodeLeft
    newNode.parent=node.parent
    if node.parent!=None:
        if node==(node.parent).left:
       #     print "\nright parent is left",((node.parent).left).data
            (node.parent).left=newNode
      #      print "right parent is left",((node.parent).left).data
           # print newNode.data, (newNode.left).data,(newNode.right).data
        else:
     #       print " right parent is right"
            (node.parent).right=newNode
    node.parent=newNode
    if newNode.parent==None:
        root=newNode
    if nodeLeft!=None:
        nodeLeft.parent=node

    #print "node after",newNode.data,((newNode.parent).right).data
    return newNode



def rotate_left(node):
  #  print 'data',node.data
    newNode=node.right
    noderight=newNode.left
    newNode.left=node
    node.right=noderight
    newNode.parent=node.parent
    if node.parent!=None:
        if node==(node.parent).left:
           # print "parent is left"
            (node.parent).left=newNode
        else:
          #  print "parent is left"
            (node.parent).right=newNode
    node.parent=newNode
  #  if newNode.parent!=None:
   #     (newNode.parent).right=newNode
    if newNode.parent==None:
        root=newNode
    if noderight!=None:
        noderight.parent=node
   # print 'node',newNode.data
    return newNode



def insert(Root,data):
    newNode=tree()
    newNode.data=data

    parent=root=Root
 #   print  "Node",parent.getData(),"  data",data
    while parent.data!=data and root!=None:
        parent=root
#        print parent.data,data
        if  parent.data > data:
            root=parent.left
        else:
            root=parent.right

    if data == parent.data:
        print "data already exist"
        del newNode
        return
    elif data<parent.data:
        parent.left=newNode
      #  newNode.color='r'
        newNode.parent=parent
#        print  "left Node"
    else:
        parent.right=newNode
       # newNode.color='r'
        newNode.parent=parent
    #print newNode.data
#    print parent.data,newNode.data
    IsRootNode(newNode)
    while Root.parent!=None:
        Root=Root.parent
    #print "root",Root.data
    return Root
  #      print  "Right Node"


def grandparent(node):

 if (node != None) and node.parent != None: #IF     NODE and Parent IS NOT Node is not Node
    return (node.parent).parent             #return grandparent
 else:
  return  None          #return None


#this function is use to return uncle for current . sibling of parent node
def uncle(node):
 # print node.data
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
   # print 'cchekd',node.data
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
  #print 'here'
  Nodeuncle = uncle(node)       #get value of uncle node
  if Nodeuncle!=None and Nodeuncle.color =='r': # if uncle is red
  #    print "here"
      (node.parent).color = 'b'         #label uncle and parent with black
      Nodeuncle.color = 'b'
      grandp = grandparent(node)        #color of grandparent and node to red
      grandp.color = 'r'
   #   print grandp.data,grandp.parent
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
        node.parent=rotate_left(node.parent)
        node = node.left

        #if current node is rigt child of left child of grandparend
        #left rotate parent
    elif node == (node.parent).left and node.parent == grandp.right:
        node.parent=rotate_right(node.parent)
        node = node.right

    nodeRotation(node)  #else tree in LL and RR case

#in this function the case of left child of left subtree and right child of right
# is solved make making left roatation to right subtree and left rotation fo right subtree
def nodeRotation(node):
   #print node.data
   grandp = grandparent(node)       #geting grand parent
   (node.parent).color = 'b'        #set parent to black
   grandp.color = 'r'               #grand parent to red

   if node == (node.parent).left:   # if node is left child
        rotate_right(grandp)        #right rotate tree
   else:
     #    print 'must be here'
       #  print grandp.data
         rotate_left(grandp)        #left rotate  tree
    #     print 'after',node.data



def delete(Root,data):
    newNode=tree()
    newNode.data=data
    parent=root=Root
    me=root
 #   print  "Node",parent.getData(),"  data",data
    while parent.data!=data and root!=None:
        parent=root
      #  print parent.data,data
        if  parent.data > data:
            root=parent.left
        else:
            root=parent.right

    if data == parent.data and parent.left!=None and parent.right!=None:
            mnNode=minNode(parent.right)
            parent.data=mnNode.data
            parent=mnNode

    if parent.left==None and parent.right==None:
        isRootNode(parent)

    if parent==(parent.parent).left:
        (parent.parent).left=None
    else:
        (parent.parent).right=None
    while me.parent!=None:
        me=me.parent
    return me

#function for finding sibling
def sibling(node):

 if node == (node.parent).left:         #if current node is left
     return (node.parent).right         #return right node
 else:
     return (node.parent).left          # return left node

def leafNode(root):

    if root.left==None and root.right ==None:
        return True
    return False



def isRootNode(node):

    if  node.parent!=None and node.color=='r':
        siblingNode=sibling(node)
        if siblingNode==None or siblingNode.color=='r':
            return
    elif (node.parent).color=='r':
        parentIsRed(node)
    else:
        #print 'this is'
        parentIsBlack(node)

def parentIsRed(node):
    '''
    IF  parent is red and need to be deleted is black and sibling is also black.
    this condition can be handle by only one rotation.
    '''

    siblingNode=sibling(node)
    if siblingNode!=None and node.color=='b' and leafNode(siblingNode) :
            (node.parent).color='b'
            siblingNode.color='r'
            return

    #if node sibling is not leaf node
    elif siblingNode !=None and not(leafNode(siblingNode)):
        #if node to be deleted is leafNode.
        #node color is red .sibling color is black. where parent color is red
        #if we are deleting left node that full fill above conditions if block will execute
        if leafNode(node) and node==(node.parent).left and node.color=='b' and siblingNode.color=='b':
            #print 'herer'
            rotate_left(node.parent)    #left rotate parent of node
            ch=(node.parent).color      #get parent color
            (node.parent).color=((node.parent).parent).color    #exchange
            ((node.parent).parent).color=ch
          #  print "node ",(node.parent).data,((node.parent).right).data,((node.parent).parent).data
            grand=grandparent(node)
            if grand.color=='r':
                if grand.left!=None:
                    (grand.left).color='b'
                if grand.right!=None:
                    (grand.right).color='b'
            if (node.parent).color=='r':
                ((node.parent).right).color='b'

         #if we are deleting right subtree  this will decrease one black node in right tree.
         #To fix violation of red black node we will right rotate parent node exchange color of
         #node's parent and grand parent node.
        elif leafNode(node) and node==(node.parent).right and node.color=='b' and siblingNode.color=='b':
            rotate_right(node.parent)    #left rotate parent of node
            ch=(node.parent).color      #get parent color
            (node.parent).color=((node.parent).parent).color    #exchange
            ((node.parent).parent).color=ch

            grand=grandparent(node)
            if grand.color=='r':
                if grand.left!=None:
                    (grand.left).color='b'
                if grand.right!=None:
                    (grand.right).color='b'
            if (node.parent).color=='r':
                ((node.parent).left).color='b'


def parentIsBlack(node):
    siblingNode=sibling(node)
    if siblingNode !=None and not(leafNode(siblingNode)):

        #if parent is has only one black node left and we want to delete that node.  this operation
        #will violate  red black tree because we are deleting black node from left subtree. this will
        #decrease number of black nodes on left side we. for fixing this problem we left rotate parent
        #of tree node.after rotation we will check parent again.If parent right side has one node if not we have to perform
        #left rotation rotation again
        if leafNode(node) and node==(node.parent).left and node.color=='b' and siblingNode.color=='r':
            #rotating left parent of node
            rotate_left(node.parent)
            grand=grandparent(node)
            #exchanging colors
            ch=(node.parent).color
            (node.parent).color=grand.color
            grand.color=ch

            #getting new sibling
            siblingNode=sibling(node)
           #after rotation node sibling has only left child we will do a right  rotation and then left rotation to fix from
           #if sibling node has only left child. first we have to rotate right  sibling node .right rotation will made possible left
           #rotation. because node ha no left child. if we try to right rotate parent node i will give exception
            if not(leafNode(siblingNode)) and siblingNode.left==None and leafNode(node):
                rotate_right(siblingNode)
                ch=siblingNode.color
                siblingNode.color=(siblingNode.parent).color
                (siblingNode.parent).color=ch

            #if left subtree is not leaf node right rotate
            if not(leafNode((node.parent).left)) and leafNode(node):
                rotate_left(node.parent)
                grand=grandparent(node)
                ch=(node.parent).color
                (node.parent).color=grand.color
                grand.color=ch
                #get grand parent of node and parent is red make its left and right child red
                if grand.color=='r':
                    (grand.left).color='b'
                    (grand.right).color='b'
                #if grand parent of node is black make its left and right child black
                if grand.color=='b':
                    (grand.left).color='r'
                    (grand.right).color='r'



        #if parent is has only one black node right and we want to delete that node.  this operation
        #will violate  red black tree because we are deleting black node from right subtree. this will
        #decrease number of black nodes on right side we. for fixing this problem we right rotate parent
        #of tree node.after rotation we will check parent again.If parent left side has one node if not we have to perform
        #right rotation rotation again
        elif leafNode(node) and node==(node.parent).right and node.color=='b' and siblingNode.color=='r':
           # print 'color',(node.parent).data
            rotate_right(node.parent)
          #  print 'color',(node.parent).data
            grand=grandparent(node)
            ch=(node.parent).color
            (node.parent).color=grand.color
            grand.color=ch


            siblingNode=sibling(node)
           #after rotation node sibling has only right child we will do a left  rotation and then right rotation to fix from
           #if sibling node has only right child. first we have to rotate left  sibling node .left rotation will made possible right
           #rotation rotation because node ha no right child. if we try to right rotate parent node i will give exception
            if not(leafNode(siblingNode)) and siblingNode.left==None and leafNode(node):
                rotate_left(siblingNode)
                ch=siblingNode.color
                siblingNode.color=(siblingNode.parent).color
                (siblingNode.parent).color=ch

            #if left subtree is not leaf node right rotate
            if not(leafNode((node.parent).left)) and leafNode(node):
                rotate_right(node.parent)
                grand=grandparent(node)
                ch=(node.parent).color
                (node.parent).color=grand.color
                grand.color=ch
                #get grand parent of node and parent is red make its left and right child red
                if grand.color=='r':
                    (grand.left).color='b'
                    (grand.right).color='b'
                #if grand parent of node is black make its left and right child black
                if grand.color=='b':
                    (grand.left).color='r'
                    (grand.right).color='r'


        #if node to be deleted is is leaf node.
        #node is right child of parent node and node color is black
        #child color is black.if sibling node is not leaf . the are two cases of rotation for fixing violation
        #accour by such deletion can be handle by left-right rotation or simple right rotation.
        elif leafNode(node) and node==(node.parent).right and node.color=='b' and siblingNode.color=='b':

            if not(leafNode(siblingNode)) and siblingNode.left==None:
                siblingNode=rotate_left(siblingNode)
                ch=siblingNode.color
                siblingNode.color=(siblingNode.left).color
                (siblingNode.left).color=ch
            rotate_right(node.parent)
            grand=grandparent(node)
            ch=grand.color
            grand.color=(node.parent).color
            (grand.left).color=ch
            (grand.right).color=ch

        elif leafNode(node) and node==(node.parent).left and node.color=='b' and siblingNode.color=='b':
            if not(leafNode(siblingNode)) and siblingNode.right==None:
                siblingNode=rotate_right(siblingNode)
                ch=siblingNode.color
                siblingNode.color=(siblingNode.left).color
                (siblingNode.left).color=ch
            rotate_left(node.parent)
            grand=grandparent(node)
            ch=grand.color
            grand.color=(node.parent).color
            (grand.left).color=ch
            (grand.right).color=ch



def minNode(root):
        if root ==None:
            return

        while root.left!=None:
            root=root.left
        return  root







def sortTree(node):
    if node !=None:
        sortTree(node.left)
        print node.data,node.color,
        sortTree(node.right)






if __name__ == '__main__':
    root=tree()
    root.data=14
    root.parent=None;
    root.color='b'
    root=insert(root,8)
    root=insert(root,16)
    root=insert(root,17)
    root=insert(root,18)
    root=insert(root,19)
    root=insert(root,20)
    root=insert(root,2)
    #sortTree(root)
    print ''
    sortTree(root)