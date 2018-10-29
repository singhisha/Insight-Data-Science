#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 16:38:58 2018

@author: isha
"""

class Insight(object):
    def filter_certified(self, new_data):
        '''
        Returns a list of certified users only
        Args:
            new_data: Data extracted from the input file that is needed for analysis 
        Returns:
            certified_data: Data containing only certified users
        '''
        certified_data = list(filter(lambda row: row[0] == 'CERTIFIED', new_data))
        return certified_data
    def count_per_state(self, certified_data):
        '''
        Calculates the number of applications that have been certified for work in that state and
         saves the top 10 states to the output file
        Args:
            certified_data: Data containing only certified users from filter_certified() function
        Returns:
            this function does not return anything
        '''
        top_10_states = open("./output/top_10_states.txt", mode = "w")
        state_dictionary = dict()
        size = len(certified_data)
        for row in certified_data:
            key = row[2]
            if key in state_dictionary:
                state_dictionary[key] += 1
            else:
                state_dictionary[key] = 1
        dictlist = []
        for key, value in state_dictionary.items():
            percent = round((value/size)*100, 1)
            temp = [key, value, percent]
            dictlist.append(temp)
        dictlist.sort(key=lambda x: (-x[2], x[0]))
        top_10_states.write("{}\n".format("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE"))
        if len(dictlist) < 10:
            print_size = len(dictlist)
        else:
            print_size = 10
        for i in range(print_size):
            top_10_states.write("{};{};{}%\n".format(dictlist[i][0],dictlist[i][1],dictlist[i][2]))
    def count_per_occupation(self, certified_data):
        '''
        Calculates the number of applications that have been certified for work in that occupation and
         saves the top 10 occupation to the output file
        Args:
            certified_data: Data containing only certified users from filter_certified() function
        Returns:
            this function does not return anything
        '''
        top_10_occupations = open("./output/top_10_occupations.txt", mode = "w")
        state_dictionary = dict()
        size = len(certified_data)
        for row in certified_data:
            key = row[1]
            if key in state_dictionary:
                state_dictionary[key] += 1
            else:
                state_dictionary[key] = 1
        dictlist = []
        for key, value in state_dictionary.items():
            percent = round((value/size)*100, 1)
            temp = [key, value, percent]
            dictlist.append(temp)
        dictlist.sort(key=lambda x: (-x[2], x[0]))
        top_10_occupations.write("{}\n".format("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE"))
        if len(dictlist) < 10:
            print_size = len(dictlist)
        else:
            print_size = 10
        for i in range(print_size):
            top_10_occupations.write("{};{};{}%\n".format(dictlist[i][0],dictlist[i][1],dictlist[i][2]))
if __name__ == '__main__':
    data_path = 'input/h1b_input.csv'
    data = open(data_path, mode = "r")
    header_row = data.readline()
    headers = header_row.split(";")
    # If the file is empty, the code should exit 
    if len(headers) <= 1:
        print("File is empty")
        raise SystemExit
    data_dict = dict.fromkeys(headers, 0)
    data_list = list()
    for row in data:
        temp = row.split(";")
        i = 0
        for t, i in zip(temp, range(len(headers))):
            data_dict[headers[i]] = t
            i += 1
        temp_list = []
        if 'STATUS' in data_dict:
            temp_list.append(data_dict['STATUS'])
        else:
            temp_list.append(data_dict['CASE_STATUS'])
        if 'LCA_CASE_SOC_NAME' in data_dict:
            temp_list.append(data_dict['LCA_CASE_SOC_NAME'])
        else:
            temp_list.append(data_dict['SOC_NAME'])
        if 'LCA_CASE_WORKLOC1_STATE' in data_dict:
            temp_list.append(data_dict['LCA_CASE_WORKLOC1_STATE'])
        else:
            temp_list.append(data_dict['WORKSITE_STATE'])
        data_list.append(temp_list)
    insight = Insight()
    certified_data = insight.filter_certified(data_list)
    certified_data = list(map(lambda row: list(map(lambda x: x.replace("\"",""),row)),certified_data))
    insight.count_per_state(certified_data)
    insight.count_per_occupation(certified_data)
