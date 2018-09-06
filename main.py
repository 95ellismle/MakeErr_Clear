#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 14:43:32 2018

@author: mellis
"""
import numpy as np
import os

from src import parsing 
from src import printing

###################      READING THE ERROR FILE      ##########################
""" Reading the make.log file (should have the error) """

filepath = raw_input("")

s = filepath# '/scratch/mellis/flavoured-cptk/cp2k/makefiles/make.log'
s = open(s, 'r').read()


""" Definitions """
script_file = os.path.realpath(__file__)
script_dir = script_file[:script_file.rfind('/')]
flags = list(np.load(script_dir+"/make_flags.npy"))

bad_words = ['Removing', 'Resolving','Discovering', 'f951:', 'make',] + flags
###############################################################################


    
###################     PARSING THE ERROR MESSAGE     #########################



""" Parsing the Error Message """

#print(s)
Errs = parsing.Parser(s)

printing.print_all_errs(Errs.errs_grouped_by_SR)


## If there are errors proceed
#if len(Err_msg.errs) > 0:
#    line_nums = []
#    err_nums = []
#    mods = []
#    for i in Err_msg.errs:
#        line_nums.append(Err_msg.errs[i]['Line'])
#        err_nums.append(i)
#        mods.append(Err_msg.errs[i]['Module'])
#    
#    
#    tol = 7 # Can improve by simply grouping all errors in same subroutine
#    
#    line_nums_and_err_nums = np.array(sorted(zip(line_nums, err_nums,mods)))
#    sorted_err_nums = line_nums_and_err_nums[:,1].astype(int)
#    line_num_diffs = np.diff(line_nums_and_err_nums[:,0].astype(int))
#    err_groups = {i:{0:[]} for i in set(line_nums_and_err_nums[:,2])}
#    counts = {i:0 for i in set(line_nums_and_err_nums[:,2])}
#    for i, diff in enumerate(line_num_diffs):
#        mod_nam = line_nums_and_err_nums[i,2]
#        err_groups[mod_nam][counts[mod_nam]].append(int(line_nums_and_err_nums[i,1]))
#        if diff > tol: # This is currently the check to see whether things belong to different subroutines.
#            counts[mod_nam] += 1
#            err_groups[mod_nam][counts[mod_nam]] = []
#    err_groups[line_nums_and_err_nums[-1,2]][counts[line_nums_and_err_nums[-1,2]]].append(int(line_nums_and_err_nums[-1,1]))
#    
#
#    cols = ['255;255;0','0;255;0','255;0;255']  
#            
#    for mod_i, mod_name in enumerate(err_groups):
#        col = cols[mod_i%len(cols)]
#        os.system("printf '\e[38;2;%sm'"%(col))
#        print("\t\t\t__________"+("_"*(len(mod_name)+2)))
#        print("\t\t\t|"+" "*(len(mod_name)+10)+" |")
#        print("\t\t\t| MODULE = %s |"%mod_name)
#        print("\t\t\t|__________"+("_"*len(mod_name))+"_|\n\n\n")
#        
#        for group_i in err_groups[mod_name]:
#            if group_i > 0:
#                col = ';'.join([str(int(int(i)*0.9)) for i in col.split(';')])
#            os.system("printf '\e[38;2;%sm          (possible) Sub Routine %i:\n\n'"%(col,group_i+1))        
#            err_num_inds = err_groups[mod_name][group_i]
#            unused_vars      = []
#            unused_var_lines = []
#            unused_args      = []
#            unused_arg_lines = []
#            for err_ind in err_num_inds:
#                err_msg = Err_msg.errs[err_ind]
#                if err_msg['type'] == 'unused_var':
#                    unused_vars, unused_var_lines = parsing.error_message_combine(err_msg, ['Unused variable ',' declared', 'Unused dummy argument'])
#                if err_msg['type'] == 'unused_arg':
#                    unused_args, unused_arg_lines = parsing.error_message_combine(err_msg, ['Unused variable ',' declared', 'Unused dummy argument'])
#                printing.print_err(err_msg)
#            printing.print_list_errors(unused_vars, unused_var_lines, "Unused Variables")
#            printing.print_list_errors(unused_args, unused_arg_lines, "Unused Arguments")
#            print("\n\n"+"-"*60+"\n\n")
#            
#        os.system("printf '\e[38;2;%sm\n'"%('255;255;255'))
#            
#            
