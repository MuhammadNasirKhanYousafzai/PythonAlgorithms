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
        print "right",root.data
        minnode=min(root.right)
        root.data=(minnode.data)
        delnode=delete(root.right,minnode.data)
        root.right=delnode

    #case 1
    #if one of both subtree of root is Node
    #this is simple case if deletion replace root with subtree or None
    else:
        deletenode=root         #get pointer of root node
        if(root.right==None):       #if right subtree is Node replace root with left subtree
        #   print "\nif",root.data
           newnode=root.left

           if (root.color == 'b'):
                if newnode!=None and newnode.color == 'r':
                    (root.left).color='b'
                else:
                    delete_case1(root);
           root=root.left
       #    print 'root', root

        elif root.left==None:           #else replace with right subtree
           newnode=root.right
           if (root.color == 'b'):
                if newnode!=None and newnode.color == 'r':
                    (root.right).color='b'
                else:
                    delete_case1(root)
           root=root.right
        del deletenode

   # if root !=None:
    #   print 'here is ' ,root.data
       # pass     isLeafNode(root)    #validation red black tree
    return root

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



def delete_case1(node ):

    if node.parent != None:
        delete_case2(node)

def delete_case2( node):

    siblng = sibling(node)

    if (siblng.color == 'r'):
        (node.parent).color = 'r'
        siblng.color = 'b'
        if (node == (node.parent).left):
            rotate_left(node.parent)
        else:
            rotate_right(node.parent)

    delete_case3(node)

def delete_case3(node):

    sbling = sibling(node)

    if (node.parent).color == 'b' and (sbling.color == 'b') and (sbling.left).color == 'b' and (s.right).color == 'b':
        sbling.color = 'r'
        delete_case1(node.parent)
    else:
       # print "parent is red"
        delete_case4(node)


def delete_case4(node ):

    sblng= sibling(node)

    if (node.parent).color == 'r' and sblng.color == 'b' and (sblng.left).color == 'b' and (sblng.right).color == 'b':

        sblng.color ='r'
        (node.parent).color = 'b'
    else:
        delete_case5(node)



def delete_case5(node ):
    sbling = sibling(node)
    if sbling.color == 'b':
        if sbling.right!=None and node == (node.parent).left and (sbling.right).color == 'b' and (sbling.left).color == 'r':

            sbling.color = 'r'
            (sbling.left).color = 'b'
            rotate_right(sbling)

        elif node == (node.parent).right and  (sbling.left).color == 'b' and (sbling.right).color == 'r':
            sbling.color = 'r'
            (sbling.right).color = 'b'
            rotate_left(sbling)

    delete_case6(node)

def delete_case6(node ):
    siblng = sibling(node)
    print "\nthis is wi "
    siblng.color = (node.parent).color;
    (node.parent).color = 'b'
    #print (node.parent).data,siblng.data
    if node == (node.parent).left:
        if siblng.right==None:
            print "sibling" ,siblng.data
            siblng= rotate_right(siblng)
            (siblng.right).color = 'b'
            print "right",siblng.data,(siblng.right).data,(siblng.parent).data
            rotate_left(siblng.parent)
            print siblng.data,siblng.left


    else :
        (siblng.left).color = 'b'
        rotate_right(node.parent)
#Have you created bots using Python






#sorting free element
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
    root=insert(root,15)
   # print root.data
    #insert(root,2)
 #   print "root",root.data
    root=insert(root,6)
#    root=insert(root,4)
  #  (root.right).right=rotate_right(root,(root.right).right)
   # root.right=rotate_left(root,root.right)
    #print root.right, 'root',((root.right).left).parent,((root.right).right).parent
  #  print '\n-------------------------------------------------------------------'
    #print "root",root.data
   # sortTree(root)
    #insert(root,5)
    root=insert(root,5)
    #print "root",root.data
    root=insert(root,8)
   # print "root",root.data
    root=insert(root,7)
    #print "root",root.data
   # root=insert(root,9)
    #print "root",root.data,root.parent
    #root=insert(root,10)
    #root=insert(root,-11)

    sortTree(root)
  #  delete(root,7)
  #  print '\ndeleting 7'
  #  sortTree(root)
  #  delete(root,8)
  #  print '\ndeleting 8'
  #  sortTree(root)
    delete(root,5)
    print '\ndeleting 5'
    sortTree(root)
 #   delete(root,6)
 #   print '\ndeleting 6'
  #  sortTree(root)
#    delete(root,15)
  #  print '\ndeleting 15'
    #sortTree(root)