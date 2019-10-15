# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:54:11 2019

@author: MSCProcessor1
"""

import shutil;
print("enter 'x' for exit");
filename1 = input("please enter 1st file name to merge: ")

if filename1 == 'x':
    exit();

else:
    filename2 = input("please enter 2nd file name to merge: ")
    filename3 = input("please enter NewFileName to merge content: ")
    print();
    print("MERGING THE CONTENT OF 2 FILES IN",filename3,"please be patient");
    with open(filename3, "wb") as wfd:
        for f in[filename1,filename2]:
            with open(f,"rb") as fd:
                shutil.copyfileobj(fd,wfd,1024*1024*10);
    print("Content merged succesfully!");
    print("want to see? (y/n):");
    check = input();
    if check == 'n':
            exit();
    else:
        print();
        c = open(filename3,"r");
        print(c.read());
        c.close();
