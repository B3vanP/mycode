#!/usr/bin/env python3
# A simple script to move two files into ceph_storage

# standard library imports
import shutil
import os

def main():
    # verify script will start in correct directory
    os.chdir('/home/student/mycode/')

    # use shutil to move file or folder to new path destination
    # Warning this will overwrite an existing file with the same name
    shutil.move('raynor.obj', 'ceph_storage/')

    # prompt for new file name
    xname = input('What is the new name for kerrigan.obj? ')

    # rename file with input
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

# call for main function
main()
