from __future__ import print_function

import logging
import os.path
import string
import re
import numpy as np
import sys
# Main method, just run "python ensplit.py
if __name__ =='__main__':
    compcount = len(open("Comen.txt",'r').readlines())

    f = open("Comstr.txt",'r')
    str = f.read()
    l = filter(None,re.split(r', | ',str))
    resultlist = list(set(l))
    wordcount = len(resultlist)

    matrixbow = np.zeros((compcount,wordcount+1))

    lines = open("Comen.txt",'r').readlines()
    i = 0
    for line in lines:
        l = re.split(r', | ',line)
        for j in l:
            try:
               p = resultlist.index(j.upper())
               matrixbow[i][p] = 1
            except ValueError:
               p = -1
               matrixbow[i][p] = 1
        i = i + 1

    colsum = np.sum(matrixbow,axis=0).tolist()
    for j in range(compcount):
        filtered = [i for i, x in enumerate(matrixbow[j]) if x == 1]
        s = 0
        minl = 9999999999
        minsub = 0
        for x in filtered:
             if  colsum[x] < minl:
                    minl = colsum[x]
                    minsub = x
             s = s + 1
        if minsub < wordcount:
           print(j,resultlist[minsub])
        else:
           print(j,'no keyword found')
