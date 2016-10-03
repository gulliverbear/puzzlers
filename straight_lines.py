#!/usr/bin/python
'''
straight lines
12/15/15

i guess for each pair you generate a line
and then see if any other points fall on that line

I should make a dict where the key is a tuple of (m,b) and the
value is all the points on the line
'''

import sys
import collections

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '({}, {})'.format(self.x,self.y)
    def get_tuple(self):
        return (self.x, self.y)

def create_line(p1, p2):
    '''
    to do
    '''

with open(sys.argv[1]) as FH:
    for line in FH:
        line = line.rstrip()

        points = []
        l = line.split('|')
        for i in l:
            i = i.strip()
            x,y = i.split()
            x,y = map(int, [x,y])
            points.append(Point(x,y))

        line_dict = collections.defaultdict(set)
        # generate all possible lines
        for i in xrange(len(points)-1):
            for j in xrange(i+1, len(points)):
                new_line_tuple = create_line(points[i], points[j])
                line_dict[new_line_tuple].add(points[i].get_tuple())
                line_dict[new_line_tuple].add(points[j].get_tuple())
        
        total = 0
        for found_line in line_dict:
            if len(line_dict[found_line]) > 2:
                total += 1
        print total
