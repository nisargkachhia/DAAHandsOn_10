# main.py
from bst import BinarySearchTree
from avl import AVLTree
from rbt import RedBlackTree

def run_cli(tree, name):
    while True:
        print(f"\n{name} Operations:")
        print("1. Add Element")
        print("2. Remove Element")
        print("3. Search Element")
        print("4. In-order Traversal")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter value to add: "))
            tree.add(value)
            print(f"{value} added to the {name}.")
        elif choice == 2:
            value = int(input("Enter value to remove: "))
            tree.delete(value)
        elif choice == 3:
            value = int(input("Enter value to search: "))
            found = tree._find_node(value)
            print(f"{value} {'found' if found else 'not found'} in the {name}.")
        elif choice == 4:
            print("In-order Traversal:", tree.inorder_traversal())
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    print("Select Tree Type:")
    print("1. Binary Search Tree")
    print("2. AVL Tree")
    print("3. Red-Black Tree")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        run_cli(BinarySearchTree(), "Binary Search Tree")
    elif choice == 2:
        run_cli(AVLTree(), "AVL Tree")
    elif choice == 3:
        run_cli(RedBlackTree(), "Red-Black Tree")
    else:
        print("Invalid selection.")
