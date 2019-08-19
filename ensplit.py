from __future__ import print_function

import logging
import os.path
import string
import re
import numpy as np
import sys
# Main method, just run "python ensplit.py
if __name__ =='__main__':
    # Connnect each company name lines into one string)
    str1 = open("Comen.txt",'r').readlines()
    str2 =''
    for line in str1:
        str2 += line.strip() + " "

    # Split the long string into single words by using regular expressions with ',' & ' '
    l = filter(None,re.split(r', | ',str2))

    # Remove duplicate words and build the result list
    resultlist = list(set(l))
    wordcount = len(resultlist)
    compcount = len(open("Comen.txt",'r').readlines())

    # Initiate one zeros matrix with rows [company name lines] and columns [word count +1] 
    matrixbow = np.zeros((compcount,wordcount+1))

    # Main process as following
    lines = open("Comen.txt",'r').readlines()
    i = 0
    for line in lines:
        # Split each company name into words
        l = re.split(r', | ',line)
        for j in l:
            try:
               # Looping to look up the location of whole word list, 
               # if found, put the matrix[i][p] value to 1 till ending of words by each line split
               p = resultlist.index(j.upper())
               matrixbow[i][p] = 1
            except ValueError:
               # any exceptional happens, put the last column to 1
               p = -1
               matrixbow[i][p] = 1
        i = i + 1

    # Sum each columns values into one tempoary list
    colsum = np.sum(matrixbow,axis=0).tolist()

    # Define keyword extraction file
    splitoutp = open("splitoutp.txt",'w')

    # Find the minimun column number of each company splitting words
    for j in range(compcount):
        eachwordlist = [i for i, x in enumerate(matrixbow[j]) if x == 1]
        minl = 9999999999
        minsub = 0
        # get the minimun number and return the corresponding word
        for x in eachwordlist:
             if  colsum[x] < minl:
                    minl = colsum[x]
                    minsub = x
        if minsub < wordcount:
           print(j,resultlist[minsub])
           splitoutp.write(str(j) + " " + str(resultlist[minsub]) + '\n')
        else:
           print(j,'no keyword found')
           splitoutp.write(str(j) + ' no keyword found' + '\n')
    splitoutp.close

