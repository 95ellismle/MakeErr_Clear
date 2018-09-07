#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:32:58 2018

@author: mellis
"""

import re

class Parser(object):
    """
    Parses the Make error message and fills a dictionary (errs) with the 
    results. 
    
    Params:
        make_error_text = The raw text from the make error message.
        
    Methods:
        __init__                -> intialises
        error_message_combine   -> combines same error messages
        find_err_type           -> finds the type of error
        find_module             -> finds the module which is throwing an error
        find_line_num           -> find the line which is throwing an error
        clean_err               -> cleans the error message
        create_err_dict         -> parses the error messages into 1 dictionary
        find_subroutine_errors  -> finds any errors in subroutines
        find_function_errors    -> finds any errors in functions
        match_err_to_subroutine -> finds which subroutine the error is in
    """
    
    def __init__(self, make_error_text):
        self.errs = {}
        self.create_err_dict(make_error_text)
        self.match_err_to_subroutine()
        self.group_errs_by_subroutine()

    def create_err_dict(self, make_error_text):
        """
        Will create the err dictionary which contains info on the error message
        in a computer readable format (e.g. line numbers as integers etc...).
        
        Params: 
            * make_error_text  =  The error message outputted by make [str]       
        """
        
        self.find_subroutine_errors(make_error_text)
        self.find_function_errors(make_error_text)
        
    def find_subroutine_errors(self, make_error_text):
        """
        Will find all the errors attached to subroutines and fill the errs 
        dictionary with them.
        
        Params: 
            * make_error_text  =  The error message outputted by make [str]
        """
        # Find errors with subroutines
        self.err_count = 0
        s_lines = make_error_text.split('\n')
        for i, line in enumerate(s_lines):
            if 'error:' in line.lower() and 'at ' in line.lower():
                scount = str(self.err_count) + 's'
                self.errs[scount] = {}
                err_msg = s_lines[i-4:i+1]
        #        print err_msg, "\n\n"
                line_num, char_num = self.find_line_num(err_msg[0])
                if '-' in char_num:
                    char_num = [int(i) for i in char_num.split('-')]
                else:
                    char_num = int(char_num)
                bad_line = err_msg[2]
                err = err_msg[-1]
                err = self.clean_err(err)
                filepath, mod = self.find_module(err_msg[0])
                self.errs[scount]['Module'] = mod.strip()
                self.errs[scount]['Filepath'] = filepath
                self.errs[scount]['Error'] = err.strip()
                self.errs[scount]['Line'] = int(line_num)
                self.errs[scount]['Line_Excerpt'] = bad_line.strip()
                self.errs[scount]['char_num'] = char_num
                self.errs[scount]['type'] = self.find_err_type(err)
                self.err_count += 1
    
    def find_function_errors(self, make_error_text):
        """
        Will find all the make errors inside functions and add them to the errs
        dictionary. 
        
        Params:
            * make_error_text  = The error message outputted by make [str]
        """
        # Find errors with functions
        while make_error_text.find('In function') != -1:
            fcount = str(self.err_count) + 'f'
            self.errs[fcount] = {}
            check = make_error_text.find("In function ")
            make_error_text = make_error_text[check + len("In function "):]    
#            function = err_txt[1:err_txt.find('\n')-2]
            next_line = make_error_text.split('\n')[1]
            filepath, mod = self.find_module(next_line)
            line_num, char_num = self.find_line_num(next_line)
            err = next_line.split(':')[-1]
            
            self.errs[fcount]['Module'] = mod.strip()
            self.errs[fcount]['Filepath'] = filepath
            self.errs[fcount]['Error'] = err.strip()
            self.errs[fcount]['Line'] = int(line_num)
            self.errs[fcount]['Line_Excerpt'] = ''
            self.errs[fcount]['char_num'] = char_num
            self.errs[fcount]['type'] = self.find_err_type(err)
            self.err_count += 1

    def clean_err(self, err_msg):
        """
        Will remove unwanted parts of the error message from a string
        
        Params: 
            err_msg  =  The error message that requires cleaning [str]
        """
        at_part = re.findall("at \(\d*\)", err_msg)
        for i in at_part:
            err_msg = err_msg.replace(i, "")
        flag_part = re.findall('\[\D*\]',err_msg)
        for i in flag_part:
            err_msg = err_msg.replace(i,'')
        err_msg = err_msg.replace("Error:", "").replace("\xe2\x80\x99", "'").replace("\xe2\x80\x98","'")
        err_msg = err_msg.strip()
        return err_msg
    
    def find_line_num(self, err_msg):
        """
            Will find the line number a line of the error message.
            
            Params: 
                * err_msg  =  The error message with a line number in  [str]
        """
        line_num_char_num = re.findall(":\d*.\d*:|:\d*.\d*-\d*.:|:\d*.:",err_msg)    
        if len(line_num_char_num) == 1:
            line_num_info = line_num_char_num[0].strip(':')
            splitter_digit = [i for i in line_num_info if not i.isdigit() and i != '-']
            if len(splitter_digit) == 1:    
                return [i for i in line_num_info.split(splitter_digit[0]) if i]
            elif len(splitter_digit) == 0:
                return line_num_info, '0'
            else:
                print("Splitter digits = ",splitter_digit)
                raise SystemExit("The number of possible splitting digits is not 1. Look at find_line_num function.")
        else:
            raise SystemExit("""Sorry but I think the regex in the function 'find_line_num' needs fixing.
    The string that needs regexing is: 
        %s
    and the regex is:
        ':\d*.\d*:|:\d*.\d*-\d*.:'"""%(err_msg))
    
    def find_module(self, err_msg):
        """
        Will find the module in which there is a make error.
        
        Params:
            err_msg  =  The error message with the module in  [str]
        """
        filepath = re.findall('/.*\.F', err_msg)
        if len(filepath) == 1:
            filepath = filepath[0]
            return filepath, filepath[filepath.rfind('/')+1:]
        else:
            return "Unable to find Module!"
    
    def find_err_type(self, err_msg):
        """
        Will classify the type of error based on the error message
        
        Params:
            err_msg  =  The error message with the error explanation in  [str]
        """
        if 'unused variable' in err_msg.lower():
            return 'unused_var'
        elif 'unclassifiable statement' in err_msg.lower():
            return 'unclass_stat'
        elif 'Unused dummy argument' in err_msg:
            return 'unused_arg'
        elif 'Syntax error' in err_msg:
            return 'Syntax'
        elif 'not a DUMMY variable' in err_msg:
            return "too_many_vars"
        elif 'not a member of the' and 'structure' in err_msg:
            return 'missing_var_in_type'
        elif 'Symbol' in err_msg and 'has no IMPLICIT type' in err_msg:
            return "missing_var"
        elif 'Invalid character in name' in err_msg:
            return 'invalid_char'
        elif 'Unexpected' in err_msg and 'statement in' in err_msg:
            return 'unexpected_statement'
        elif 'Expecting END' in err_msg:
            return 'no_end'
        elif 'Missing kind-parameter' in err_msg:
            return "missing_kind"
        elif 'Allocate-object' in err_msg and  'also appears' in err_msg:
            return "$FIX$Remove some allocations"
        elif 'undefined reference to ' in err_msg:
            return "$FIX$Need to import (or create) the subroutine mentioned above."
        elif 'Rank mismatch' in err_msg:
           return "rank_mismatch"
        else:
            return "not_classified"
    
    def match_err_to_subroutine(self):
        """
        Will find which subroutine is causing the error.
        
        Params:
            None
        """
        all_files = list(set([(self.errs[err_code]['Filepath'], self.errs[err_code]['Module']) for err_code in self.errs if 's' in err_code]))
        self.SR_ranges = {}
        for f, module in all_files:
            with open(f, 'r') as ftxt:
                self.SR_ranges[module] = self.find_all_subroutines(ftxt)
        
        for err_code in self.errs:
            triggered = False
            for SR_details in self.SR_ranges[self.errs[err_code]['Module']]:
                if SR_details['start'] < self.errs[err_code]['Line'] < SR_details['end']:
                    self.errs[err_code]['SR_name'] = SR_details['name']
                    triggered = True
            if not triggered:
                self.errs[err_code]['SR_name'] = ''
        
    def find_all_subroutines(self, ftxt):
        """
        Will find the start and end index of each subroutine in a file
        
        Params:
            * ftxt               =  The file text in question [file object]
        """
        begin = False
        end = True
        subroutine_ranges = []
        count = 0
        for line_num, line in enumerate(ftxt):
            L = line.upper()
            if 'SUBROUTINE' in L and all(j not in L for j in ('END','CALL')) and not begin and end:
                begin = True
                end = False
                SR_name = line[L.find('SUBROUTINE')+len('SUBROUTINE'):line.find('(')].strip()
                subroutine_ranges.append({'name':SR_name, 'start':line_num+1})
            elif 'SUBROUTINE' in L and 'END' in L and 'CALL' not in L and not end and begin: 
                begin = False
                end = True
                subroutine_ranges[count]['end'] = line_num+1
                count += 1
            
            elif 'SUBROUTINE' in L and 'END' in L and 'CALL' not in L and begin and not end:
                print("\n#######################\n\nSubroutine '%s' has started before the previous subroutine has finished!\n\n#######################\n"%SR_name)
                
            elif 'SUBROUTINE' in L and 'END' in L and 'CALL' not in L and end and not begin: 
                print("\n#######################\n\nSubroutine '%s' has ended before it has begun!\n\n#######################\n"%SR_name)
        return subroutine_ranges

    def find_all_functions(self, ftxt):
        """
        Will find the start and end index of each function in a file
        
        Params:
            * ftxt               =  The file text in question [file object]
        """
        begin = False
        end = True
        function_ranges = []
        count = 0
        for line_num, line in enumerate(ftxt):
            L = line.upper()
            if 'FUNCTION' in L and 'END' not in L and not begin and end:
                begin = True
                end = False
                SR_name = line[L.find('FUNCTION')+len('FUNCTION'):line.find('(')].strip()
                function_ranges.append({'name':SR_name, 'start':line_num+1})
            elif 'FUNCTION' in L and 'END' in L and 'CALL' not in L and not end and begin: 
                begin = False
                end = True
                function_ranges[count]['end'] = line_num+1
                count += 1
            
            elif 'FUNCTION' in L and 'END' not in L and begin and not end:
                print("\n#######################\n\nFunction'%s' has started before the previous function has finished!\n\n#######################\n"%SR_name)
                
            elif 'FUNCTION' in L and 'END' in L and 'CALL' not in L and end and not begin: 
                print("\n#######################\n\nFunction '%s' has ended before it has begun!\n\n#######################\n"%SR_name)
        return function_ranges
    
    def group_errs_by_subroutine(self):
        """
        Will group the errors by the subroutine name stored in a list of 
        dictionaries.
        
        Params:
            None
        """
        all_SRs = list(set([self.errs[i]['SR_name'] for i in self.errs]))
        self.errs_grouped_by_SR = {i:[] for i in all_SRs}
        for err_code in self.errs:
            self.errs_grouped_by_SR[self.errs[err_code]['SR_name']].append(self.errs[err_code])

def error_message_combine(err_msg, strs_to_remove):
        """
        Will amalgamate the specified error into 1 list
        
        Params:
            err_msg        =  The unused variable error message  [str]
            strs_to_remove =  The substrings to remove from the error message before appending [list of str]
        """
        unused_vars, unused_lines = [], []            
        unused_var = err_msg['Error'][:] 
        for remove_str in strs_to_remove:
            unused_var = unused_var.replace(remove_str,"")
        str_line_no = str(err_msg['Line'])
        unused_vars.append(unused_var)
        unused_lines.append(str_line_no+(len(unused_var)-len(str_line_no))*" ")
        return unused_vars, unused_lines

