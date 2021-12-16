# bst representation from GeeksforGeeks
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

lst = []
def find2ndBiggest(root):
    try:
        find2ndBiggest(root.right)
        lst.append(root.val)
        return lst[1]
    except:
        print("")





# Let us create the following BST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 5)
r = insert(r, 80)
r = insert(r, 90)

print(find2ndBiggest(r))
