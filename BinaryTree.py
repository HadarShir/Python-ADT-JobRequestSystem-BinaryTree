## This file contains functions for the representation of binary trees.
## used in class Binary tree / search tree's __repr__
## Written by a former student in the course (at TAU) - thanks to Amitai Cohen
from ADTs import Stack
import copy
def printree(t, bykey=True):
    """Print a textual representation of t
    bykey=True: show keys instead of values"""
    # for row in trepr(t, bykey):
    #        print(row)
    return trepr(t, bykey)


def trepr(t, bykey=False):
    """Return a list of textual representations of the levels in t
    bykey=True: show keys instead of values"""
    if t == None:
        return ["#"]

    thistr = str(t.key) if bykey else str(t.val)

    return conc(trepr(t.left, bykey), thistr, trepr(t.right, bykey))


def conc(left, root, right):
    """Return a concatenation of textual represantations of
    a root node, its left node, and its right node
    root is a string, and left and right are lists of strings"""

    lwid = len(left[-1])
    rwid = len(right[-1])
    rootwid = len(root)

    result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

    ls = leftspace(left[0])
    rs = rightspace(right[0])
    result.append("".join([ls * " ", (lwid - ls) * "_", "/",
                           rootwid * " ", "\\", rs * "_", (rwid - rs) * " "]))

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i]
        else:
            row += lwid * " "

        row += (rootwid + 2) * " "

        if i < len(right):
            row += right[i]
        else:
            row += rwid * " "

        result.append(row)

    return result


def leftspace(row):
    """helper for conc"""
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    i = len(row) - 1
    while row[i] == " ":
        i -= 1
    return i + 1


def rightspace(row):
    """helper for conc"""
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    i = 0
    while row[i] == " ":
        i += 1
    return i


class TreeNode():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.key) + ":" + str(self.val)

    def is_Leef(self):
        return self.left is None and self.right is None


class BinaryTree():
    def __init__(self):
        self.root = None

    def __repr__(self):
        # no need to understand the implementation of this one
        out = ""
        # need printree.py file or make sure to run it in the NB
        for row in printree(self.root):
            out = out + row + "\n"
        return out

    def root_to_leaf_path_rec(self):
        result = []
        # Find all root to leaf paths
        self.wrapped_func_root_to_leaf_path_rec(self.root, [], result)
        return result

    def wrapped_func_root_to_leaf_path_rec(self, root, path, result):
        # A recursive wrapped function
        if root is None:
            return

        # Append the current node's key to the current path
        path_copy = path.copy()
        path_copy.append(root.key)

        # If the current node is a leaf,the current path added to the list
        if root.left is None and root.right is None:
            result.append(list(path_copy))
        else:
            # Recursively traverse left and right subtrees
            self.wrapped_func_root_to_leaf_path_rec(root.left, path_copy, result)
            self.wrapped_func_root_to_leaf_path_rec(root.right, path_copy, result)

    def root_to_leaf_path_iter(self):
        if self.root is None:
            return []

        # Stack to store nodes and their paths from root
        stack = Stack()
        stack.push((self.root, []))
        result = []

        while not stack.is_empty():
            node, path = stack.pop()
            # Update path with current node's key
            path.append(node.key)

            if node.left is None and node.right is None:
                # If leaf node, add path to result
                result.append(path)

            else:
                if node.right:
                    stack.push((node.right, list(path)))  # Add right child and its path
                if node.left:
                    stack.push((node.left, list(path)))  # Add left child and its path

        return result

    def print_all_neighbors(self, node):
        # In order to find the neighbors we have to perform several actions.
        # Find a member that is at the same height as the input and check if it comes from the same root.
        # I built several functions that will help me give the solution

        if not self.root or not node:
            return

        stack = Stack()
        stack.push((self.root, 0))  # Push the root node and its level to the stack
        result = Stack()
        parent_node = self.search_parent_rec(self.root,node)  # check if it comes from the same root
        distance_from_root = self.distance_from_root(node)  # Find a member that is at the same height

        while not stack.is_empty():
            current_node, level = stack.pop()

            # Check if the current node is at the same distance as the given node
            if level == distance_from_root:
                # Check if the current node is not the given node or its direct descendants of its parent
                if current_node != node and current_node != parent_node:
                    result.push(current_node.val)

            # Add right child first so that left child gets processed first
            if current_node.right and not self.is_descendant(parent_node, current_node.right):
                stack.push((current_node.right, level + 1))
            if current_node.left and not self.is_descendant(parent_node, current_node.left):
                stack.push((current_node.left, level + 1))

        # Print the contents of the stack without a newline
        while not result.is_empty():
            print(result.pop(), end=' ')
        print()

    def distance_from_root(self, node):
        distance = 0
        current = node
        while current != self.root:
            distance += 1
            current = self.search_parent_rec(self.root,current)
        return distance

    def search_parent_rec(self, root, target):
        if not root:
            return None
        if root.left == target or root.right == target:
            return root
        left_search = self.search_parent_rec(root.left, target)
        right_search = self.search_parent_rec(root.right, target)
        return left_search if left_search else right_search

    def is_descendant(self, ancestor, descendant, stack=None):
        # check if they come from the same root
        if not ancestor or not descendant:
            return False

        if stack is None:
            stack = Stack()

        stack.push(ancestor)

        while not stack.is_empty():
            current_node = stack.pop()
            if current_node == descendant:
                return True

            # Add the left and right children to the stack
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)

        # If the descendant node is not found during the traversal, return False
        return False

    def is_symmetric_tree(self):
        if self.root is None:
            return True
        return self.rec_is_symmetric_tree(self.root.left, self.root.right)

    def rec_is_symmetric_tree(self, left, right):
        # Checks for symmetry on both sides of the tree
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return self.rec_is_symmetric_tree(left.left, right.right) and self.rec_is_symmetric_tree(left.right, right.left)


