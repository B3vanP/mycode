#!/usr/bin/env python3
# Author: RZFeeser RZFeeser@alta3.com

"""Script to search for a pattern match"""

import os
import fnmatch
import sys

EXCLUDE = ["/usr", "/home", "/var"]  # Don't search in these locations

def find(pattern, path):
    """Search through filesystem based on given path location"""
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        if root in EXCLUDE:  # if the root matches the exclude list
            dirs[:] = []  # remove the directory list for this iteration
            files[:] = []  # remove the file list for this iteration
        for name in files:  # always perform the nested loop, but it may be empty
            if fnmatch.fnmatch(name.lower(), pattern.lower()):  # if match, case-insensitive
                result.append(os.path.join(root, name))  # add to our list
    return result  # return the list

def main():
    """Runtime code"""
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <pattern> <path>")
        sys.exit(1)
    
    lookfor = sys.argv[1]
    lookwhere = sys.argv[2]
    print("Results: ", find(lookfor, lookwhere))  # call function

if __name__ == "__main__":
    main()

