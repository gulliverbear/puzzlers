#!/usr/bin/python
'''
4/18/16
code like huffman

'''

import sys
import collections

class Node(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.is_root = False
    
def combine(left_child, right_child):
    '''
    creates a new node that is parent of the 2 children, returns the parent node
    '''
    left_child.side = 0 # interesting you can make a new object variable without it being in init...
    right_child.side = 1
    parent = Node('.' + left_child.name + right_child.name, left_child.value + right_child.value)
    left_child.parent = parent
    right_child.parent = parent
    return parent
    
def trace_path(leaf):
    '''
    given a leaf it traces the path up to the root
    appends a 0 if it is a left_child, a 1 if it is a right_child for each step
    '''
    current_node = leaf
    l = []
    while True:
        if current_node.is_root:
            l = map(str, l)
            return ''.join(l[::-1])
        l.append(current_node.side)
        current_node = current_node.parent

def huffman(s):
    '''
    given a string, print out huffman encoding for each char
    '''
    node_dict = {}
    q = []
    freq_dict = collections.Counter(s)
    for key, value in freq_dict.items():
        new_leaf = Node(key, value) # True to show it is a leaf
        q.append((key, value))
        node_dict[key] = new_leaf # so I can access the object by the name
    
    while True:
        if len(q) == 1:
            break

        # get the two with lowest value, prioritize node over leafs, then alphabetically
        left_child, right_child = sorted(q, key=lambda x:(x[1], x[0]))[:2]
        new_parent = combine(node_dict[left_child[0]], node_dict[right_child[0]])

        node_dict[new_parent.name] = new_parent
        q.remove(left_child)
        q.remove(right_child)
        q.append((new_parent.name, new_parent.value))
    
    node_dict[q[0][0]].is_root = True
    
    l = []
    for leaf_name in sorted(freq_dict):
        l.append(leaf_name + ':')
        l.append(trace_path(node_dict[leaf_name]) + ';')
    print ' '.join(l)


with open(sys.argv[1]) as FH:
    for line in FH:
        line = line.rstrip()
        huffman(line)
