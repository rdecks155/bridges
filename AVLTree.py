'''
@author: Robbie Decker
'''

from bridges.avl_tree_element import *

class AVLTree():
    def __init__(self, filename):
        self.nodes = []

        # read keys from txt file
        File = open(filename)
        for key in File:
            # create an AVL tree elements
            self.nodes.append(AVLTreeElement(int(key), key))
        File.close()
        # initialize the root as empty
        self.root = None

        # build the tree
        self.build()

    # build the tree
    def build(self):
        # insert node to the tree one by one
        for node in self.nodes:
            self.root = self.insert(node, self.root)

    # insert one node to current tree
    def insert(self, node, root):
        if not root:
            root = node
        # go to the left
        elif node.key < root.key:
            root.left = self.insert(node, root.left)
        # go to the right
        else:
            root.right = self.insert(node, root.right)

        #Calculate balance for each root in tree
        root.balance_factor = self.height(root.left) - self.height(root.right)

        #additional feature that shows balance factor on bridges
        root.label = str(root.balance_factor)

        #Check if balance factor is greater than 1 or less than -1
        if root.balance_factor > 1:
        
            #right rotation
            if node.key < root.left.key:
                root = self.right_rotation(root)
            else:
                #Left-Right Rotation
                root.left = self.left_rotation(root.left)
                root = self.right_rotation(root)

        elif root.balance_factor < -1:
            #left rotation
            if node.key > root.right.key:
                root = self.left_rotation(root)
            else:
                #Right-Left Rotation
                root.right = self.right_rotation(root.right)
                root = self.left_rotation(root)
        # recursively return root of current subtree
        return root

    # rotate to the left
    def left_rotation(self, root):
        #steps of pseudo-code given
        #Step 1
        temp = root
        newRoot = root.right
        #step 3
        if newRoot.left:
            temp.right = newRoot.left
        else:
            temp.right = None
        #step 2
        newRoot.left = temp

        #step 4
        return newRoot


    # rotate to the right
    def right_rotation(self, root):
        #Steps of pseudo-code given
        #step 1
        temp = root
        newRoot = root.left

        #step 3
        if newRoot.right:
            temp.left = newRoot.right
        else:
            temp.left = None
        
        #step 2
        newRoot.right = temp

        #step 4
        return newRoot



    def height(self, node):
        if not node:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1
        
    #changed name of method to bypass variable and method name matchup error
    def getRoot(self):
        return self.root