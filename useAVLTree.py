from bridges.bridges import *
from bridges.avl_tree_element import *
from AVLTree import AVLTree

def useAVLTree(filename):

    # get your_user_name and your_key from your profile at http://bridges-cs.herokuapp.com/profile
    bridges = Bridges(tree_id, "decker155", "732843077886")

    #avl = AVLTree("myTree.txt")
    avl = AVLTree('tree'+ str(tree_id) + '.txt')

    # add some visual attributes
    avl.root.visualizer.color = "magenta"
    avl.root.visualizer.opacity = 0.8

    # set visualizer type
    bridges.set_data_structure(avl.root)

    # visualize the tree
    bridges.visualize()

if __name__ == "__main__":

    for tree_id in range(1,5):
        useAVLTree(tree_id)
