#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 19:27:20 2020

@author: comtech
"""

import codecs
import numpy as np
import re

final_word_list = []

def handle_data():
    word_set = set()
    no_symbol_list = []
    for line in codecs.open('CompanyEN.txt', "r", encoding='utf-8').readlines():
        new_line = list(filter(None, re.split(r'[,();（）；，&\r\n| ]', line)))
        no_symbol_list.append(new_line)
        for word in new_line:
            word_set.add(word.upper())

    result_list = list(word_set)
  
    bow = np.zeros((len(no_symbol_list), len(result_list)))

    for line_number in range(0,len(no_symbol_list)):
        for word in no_symbol_list[line_number]:
            word_pos = result_list.index(word.upper())
            bow[line_number][word_pos] = 1

    sum_list = bow.sum(axis=0).tolist()
    
    for j in range(0,len(no_symbol_list)):
        original_company_index = [i for i, x in enumerate(bow[j]) if x == 1]
        lowest_frequency = float("inf")
        lowest_index = 0
        # get the minimun number and return the corresponding word
        for index in original_company_index:
             if  sum_list[index] < lowest_frequency:
                    lowest_frequency = sum_list[index]
                    lowest_index = index
      
        final_word_list.append(result_list[lowest_index])

def output_file():
    output = codecs.open('Output-review.txt', "w+", encoding='utf-8')
    for count in range(1, len(final_word_list) + 1):
        output.write(str(count) + " " + final_word_list[count-1] + "\n")


if __name__ == '__main__':
    handle_data()
    output_file()