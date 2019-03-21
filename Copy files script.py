#!/usr/bin/env python 

# This small Python script file : How to copy files from one location to another location / Copy a file with new name.

# The shutil module offers a number of high-level operations on files and collections of files. 
# In particular, functions are provided which support file copying and removal.

import shutil
 

# Main function is the entry point of any program. 
# But python interpreter executes the source file code sequentially and doesn’t call any method if it’s not part of the code. 
# But if it’s directly part of the code then it will be executed when the file is imported as a module.
# That’s why there is a special technique to define main method in python program, so that it gets executed only when the program is run directly and not executed when imported as a module. 

def main():
 
    # The shutil module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal.
    # Copy file to another directory
    newPath = shutil.copy('/Users/tommashuang/Desktop/01/01.jpg', '/Users/tommashuang/Desktop/02')
 
    print("Path of copied file : ", newPath)
 
    #Copy a file with new name
    newPath = shutil.copy('sample1.txt', '/Users/tommashuang/Desktop/sample2.txt')
 
    print("Path of copied file : ", newPath)
 
    # Copy a symbolic link as a new link
    newPath = shutil.copy('/Users/tommashuang/Desktop/link.csv', '/home/varung/test/sample2.csv')
 
    print("Path of copied file : ", newPath)
 
    # Copy target file pointed by symbolic link
    newPath = shutil.copy('/home/varung/test/link.csv', '/home/varung/test/newlink.csv', follow_symlinks=False)
 
    print("Path of copied file : ", newPath)
 
 
# '__main__' is the name of the scope in which top-level code executes. A module’s __name__ is set equal to '__main__' when read from standard input, a script, or from an interactive prompt.
# A module can discover whether or not it is running in the main scope by checking its own __name__, which allows a common idiom for conditionally executing code in a module when it is run as a script or with python -m but not when it is imported:

if __name__ == '__main__':
    main()