#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:33:18 2018

@author: mellis
"""

class Printer(object):
    """
    Will handle all the printing of the errors in a standard human readable way.
    
    Input:
        * parser  ->  a Parser object (see parsing.py)
    
    Methods:
        * print_err          ->  prints a single error
        * print_all_errs     ->  prints all the errors
        * print_list_errors  ->  print a list of errors  
    """
    
    def __init__(self, parser):
        self.width = 90
        self.print_all_errs(parser.errs_grouped_by_SR)
    
    
    def print_single_line(self, line):
        """
        Will print a single line keeping to the class's width.
        
        Params:
            * line  ->  the text to be printed
        """
        print(line + ' '*(self.width-len(line)) + '|')
        
    def print_err(self, err_dict):    
            """
            Will print the re-formatted error in a standard human readable way.
            
            Params:
                err_dict  =  The dictionary containing info on the error
            """
            line_num_line = "Line  :         %i'"%(err_dict['Line'])
            err_msg_line = "Error :         %s'"%(err_dict['Error'])
            
            self.print_single_line(line_num_line)
            self.print_single_line(err_msg_line)          
            if err_dict['Line_Excerpt']:
                line_excerpt = "Line Excerpt:  '%s''"%(err_dict['Line_Excerpt'])
                self.print_single_line(line_excerpt)
    #            print("            "+" "*err_dict['char_num']+"^")
            if err_dict['type'][:5] == '$FIX$':
                fix_line = "FIX   :         %s"%err_dict['type'][5:]
                self.print_single_line(fix_line)
            self.print_single_line("")
            self.print_single_line("")
    
    
    def print_all_errs(self, errs_grouped_by_SR):
        """
        Will print all the error messages in a human readable format.
        
        Params:
            * errs_grouped_by_SR  ->  The list of the error messages grouped by the 
                                      subroutine.
        """
        for sr_i, SR in enumerate(errs_grouped_by_SR):
            print("\n")
            self.print_single_line("-"*self.width)
            SR_title =           '                | Subroutine %i = %s |'%(sr_i+1, SR)
            SR_title_underline = "                -------------------"+"-"*len(SR)
            self.print_single_line(SR_title)
            self.print_single_line(SR_title_underline)
            self.print_single_line("")
            self.print_single_line("")
            for err_dict in errs_grouped_by_SR[SR]:
                self.print_err(err_dict)
            self.print_single_line("-"*self.width)
            print("\n\n")
    
    
    def print_list_errors(self, err_list, err_lines_list, title):
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