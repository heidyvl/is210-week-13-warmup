#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring"""

import os
import json

DICTIONARY = {'A':100, 'B':90, 'C':80, 'D':70, 'F':60}

def get_score_summary(filename):

    fhandler = open('inspection_results.csv', 'rb')
    new_dict = {}
    rest_boro = {}
    final_dict = {}
    sum_q = 0
    sum_sc_q = 0
    sum_m = 0
    sum_sc_m = 0
    sum_bx = 0
    sum_sc_bx = 0
    sum_bk = 0
    sum_sc_bk = 0
    sum_si = 0
    sum_sc_si = 0
    for line in fhandler.readlines():
        data = line.split(',')[:-2]
        if data[0] not in new_dict:
            new_dict = {data[0]:(data[1], data[10])}
            for key, value in new_dict.iteritems():
                if new_dict[key][0] == 'QUEENS' and new_dict[key][1] != '' and new_dict[key][1] != 'P':
                    sum_sc_q += float(DICTIONARY[new_dict[key][1]])
                    sum_q += 1
                    rest_boro['QUEENS']=(sum_q, float(sum_sc_q/sum_q))
                if new_dict[key][0] == 'MANHATTAN' and new_dict[key][1] != '' and new_dict[key][1] != 'P':
                    sum_sc_m += float(DICTIONARY[new_dict[key][1]])
                    sum_m += 1
                    rest_boro['MANHATTAN']=(sum_m, float(sum_sc_m/sum_m))
                if new_dict[key][0] == 'BRONX' and new_dict[key][1] != '' and new_dict[key][1] != 'P':
                    sum_sc_bx += float(DICTIONARY[new_dict[key][1]])
                    sum_bx += 1
                    rest_boro['BRONX']=(sum_bx, float(sum_sc_bx/sum_bx))
                if new_dict[key][0] == 'BROOKLYN' and new_dict[key][1] != '' and new_dict[key][1] != 'P':
                    sum_sc_bk += float(DICTIONARY[new_dict[key][1]])
                    sum_bk += 1
                    rest_boro['BROOKLYN']=(sum_bk, float(sum_sc_bk/sum_bk))
                if new_dict[key][0] == 'STATEN ISLAND' and new_dict[key][1] != '' and new_dict[key][1] != 'P':
                    sum_sc_si += float(DICTIONARY[new_dict[key][1]])
                    sum_si += 1
                    rest_boro['STATEN ISLAND']=(sum_si, float(sum_sc_si/sum_si))
         
    return rest_boro
    fhandler.close()

#print get_score_summary('inspection_results.csv')

#get_market_density(filename):
dictio = {}
fhandler = json.load(open('green_markets.json'))
dictio = dict((item['idssss'], item) for item in fhandler.iteritems())

print dictio
    
    
