# -*- coding: utf-8 -*-
from sys import argv

def print_all_lines(fp):
    print fp.read()

def print_one_line(fp):
    print fp.readline()

def seek(position):
    fp.seek(position)

if __name__ == "__main__":
    scripts, filename = argv
    fp = open(filename)
    print "print all lines:"
    print_all_lines(fp)
    print "print one line:"
    seek(0)
    for line in range(4):
        print_one_line(fp)
    fp.close()