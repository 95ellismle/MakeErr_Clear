#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:33:18 2018

@author: mellis
"""



def print_err(err_dict):    
        """
        Will print the re-formatted error in a standard human readable way.
        
        Params:
            err_dict  =  The dictionary containing info on the error
        """
        width = 90
        line_num_line = "Line  :         %i'"%(err_dict['Line'])
        err_msg_line = "Error :         %s'"%(err_dict['Error'])
        
        
        print(line_num_line + ' '*(width-len(line_num_line)) + '|')
        print(err_msg_line + ' '*(width-len(err_msg_line)) + '|')
        
        if err_dict['Line_Excerpt']:
            line_excerpt = "Line Excerpt:  '%s''"%(err_dict['Line_Excerpt'])
            print(line_excerpt + ' '*(width-len(line_excerpt)) + '|')
#            print("            "+" "*err_dict['char_num']+"^")
        if err_dict['type'][:5] == '$FIX$':
            print("FIX   :         %s"%err_dict['type'][5:])
        print(" "*width + "|")
        print(" "*width + "|")

def print_all_errs(errs_grouped_by_SR):
    """
    Will print all the error messages in a human readable format.
    
    Params:
        * errs_grouped_by_SR  ->  The list of the error messages grouped by the 
                                  subroutine.
    """
    for sr_i, SR in enumerate(errs_grouped_by_SR):
        width = 90
        print("\n")
        print("-"*width)
        SR_title =           '                | Subroutine %i = %s |'%(sr_i+1, SR)
        SR_title_underline = "                -------------------"+"-"*len(SR)
        print(SR_title + ' '*(width-len(SR_title))+'|' )
        print(SR_title_underline + ' '*(width-len(SR_title_underline))+'|' )
        print(" "*width+'|')
        print(" "*width+'|')
        for err_dict in errs_grouped_by_SR[SR]:
            print_err(err_dict)
        print("-"*width)
        print("\n\n")

def print_list_errors(err_list, err_lines_list, title):
        """
        Will print a list of errors in a human-readable standard way.
        
        Params:
            err_list        =  The errors to print in a list
            err_lines_list  =  The line number of the corresponding index error
            title           =  The title of the group of errors (e.g. unused variables)
        """
        if err_list:
            print("\n\n"+"-"*15+"\n\n")
            print("Bulk Info:")
            print("\t%s: "%title)
            print("\t\t"+',\t'.join(err_list))
            print("\t\t"+',\t'.join(err_lines_list))