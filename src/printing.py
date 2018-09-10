#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:33:18 2018

@author: mellis
"""
import numpy as np

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
        self.width = 100
        self.max_error_print = 10
        self.Parser = parser
        self.print_all_errs()
    
    
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
            err_msg_line =         "Error :         %s'"%(err_dict['Error'])
            self.print_single_line(line_num_line)
            self.print_single_line(err_msg_line)          
            if err_dict['Line_Excerpt']:
                line_excerpt = "Line Excerpt:  '%s''"%(err_dict['Line_Excerpt'])
                self.print_single_line(line_excerpt)
    #            print("            "+" "*err_dict['char_num']+"^")
            if err_dict['type'][:5] == '$FIX$':
                fix_line = "FIX   :         %s"%err_dict['type'][5:]
                self.print_single_line(fix_line)
            self.print_single_line("Module:         %s"%err_dict['Module'])
            self.print_single_line("")
            self.print_single_line("")
    
    
    def print_all_errs(self):
        """
        Will print all the error messages in a human readable format.
        
        Params:
            * errs_grouped_by_SR  ->  The list of the error messages grouped by the 
                                      subroutine.
        """
        count = 0
        try:
            for sr_i, SR in enumerate(self.Parser.errs_grouped_by_SR):
                if count >= self.max_error_print:
                    self.print_single_line("                                .")
                    self.print_single_line("                                .")
                    self.print_single_line("                                .")
                    break
                print("\n")
                self.print_single_line("-"*self.width)
                SR_title =           '                | Subroutine %i = %s |'%(sr_i+1, SR)
                SR_title_underline = "                -------------------"+"-"*len(SR)
                self.print_single_line(SR_title)
                self.print_single_line(SR_title_underline)
                self.print_single_line("")
                self.print_single_line("")
                for err_dict in self.Parser.errs_grouped_by_SR[SR]:
                    if count >= self.max_error_print:
                        self.print_single_line("                                .")
                        self.print_single_line("                                .")
                        self.print_single_line("                                .")
                        break
                    count += 1
                    self.print_err(err_dict)
                self.print_single_line("-"*self.width)
                print("\n\n")
        except AttributeError:
            try:
                for sr_i, SR in enumerate(self.Parser.errs_grouped_function):
                    if count >= self.max_error_print:
                        self.print_single_line("                                .")
                        self.print_single_line("                                .")
                        self.print_single_line("                                .")
                        break
                    print("\n")
                    self.print_single_line("-"*self.width)
                    SR_title =           '                | Subroutine %i = %s |'%(sr_i+1, SR)
                    SR_title_underline = "                -------------------"+"-"*len(SR)
                    self.print_single_line(SR_title)
                    self.print_single_line(SR_title_underline)
                    self.print_single_line("")
                    self.print_single_line("")
                    for err_dict in self.Parser.errs_grouped_by_SR[SR]:
                        if count >= self.max_error_print:
                            print("\t\t.")
                            print("\t\t.")
                            print("\t\t.")
                            break
                        self.print_err(err_dict)
                        count += 1
                    self.print_single_line("-"*self.width)
                    print("\n\n")
            except AttributeError:
                for sr_i, err_code in enumerate(self.Parser.errs):
                    if count >= self.max_error_print:
                        self.print_single_line("                                .")
                        self.print_single_line("                                .")
                        self.print_single_line("                                .")
                        break
                    print("\n")
                    self.print_single_line("-"*self.width)
                    SR_title =           '                | Error %i |'%(sr_i+1)
                    SR_title_underline = "                ----------"+"-"*int(np.log10(99))
                    self.print_single_line(SR_title)
                    self.print_single_line(SR_title_underline)
                    self.print_single_line("")
                    self.print_single_line("")
                    self.print_err(self.Parser.errs[err_code])
                    self.print_single_line("-"*self.width)
                    print("\n\n")
                    count += 1
    
    
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