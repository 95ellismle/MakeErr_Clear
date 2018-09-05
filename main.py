#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 14:43:32 2018

@author: mellis
"""
import numpy as np
import os
import re

s = """Discovering programs ...
Removing stale archives for sopt ... 
Resolving dependencies for sopt ... 
gfortran -c -I/scratch/mellis/flavoured-cptk/cp2k/tools/toolchain/install/include  -march=native -fno-omit-frame-pointer -g   -O3 -funroll-loops -ffast-math  -ffree-form -std=f2003 -fimplicit-none  -Werror=aliasing -Werror=ampersand -Werror=c-binding-type -Werror=intrinsic-shadow -Werror=intrinsics-std -Werror=line-truncation -Werror=tabs -Werror=target-lifetime -Werror=underflow -Werror=unused-but-set-variable -Werror=unused-variable -Werror=unused-dummy-argument -Werror=conversion -Werror=zerotrip -Werror=uninitialized -Wno-maybe-uninitialized -Wuse-without-only  -D__LIBXSMM   -D__HAS_smm_dnn  -D__LIBXC -D__LIBINT -D__LIBINT_MAX_AM=6 -D__LIBDERIV_MAX_AM1=5 -D__FFTW3    -D__QUIP  -D__COMPILE_ARCH="\"local\"" -D__COMPILE_DATE="\"Tue  5 Jun 14:38:52 BST 2018\"" -D__COMPILE_HOST="\"helford.phys.ucl.ac.uk\"" -D__COMPILE_REVISION="\"git:c70063e\"" -D__DATA_DIR="\"/scratch/mellis/flavoured-cptk/cp2k/data\"" -D__SHORT_FILE__="\"aom_initialization.F\"" /scratch/mellis/flavoured-cptk/cp2k/src/aom_initialization.F 
gfortran -c -I/scratch/mellis/flavoured-cptk/cp2k/tools/toolchain/install/include  -march=native -fno-omit-frame-pointer -g   -O3 -funroll-loops -ffast-math  -ffree-form -std=f2003 -fimplicit-none  -Werror=aliasing -Werror=ampersand -Werror=c-binding-type -Werror=intrinsic-shadow -Werror=intrinsics-std -Werror=line-truncation -Werror=tabs -Werror=target-lifetime -Werror=underflow -Werror=unused-but-set-variable -Werror=unused-variable -Werror=unused-dummy-argument -Werror=conversion -Werror=zerotrip -Werror=uninitialized -Wno-maybe-uninitialized -Wuse-without-only  -D__LIBXSMM   -D__HAS_smm_dnn  -D__LIBXC -D__LIBINT -D__LIBINT_MAX_AM=6 -D__LIBDERIV_MAX_AM1=5 -D__FFTW3    -D__QUIP  -D__COMPILE_ARCH="\"local\"" -D__COMPILE_DATE="\"Tue  5 Jun 14:38:52 BST 2018\"" -D__COMPILE_HOST="\"helford.phys.ucl.ac.uk\"" -D__COMPILE_REVISION="\"git:c70063e\"" -D__DATA_DIR="\"/scratch/mellis/flavoured-cptk/cp2k/data\"" -D__SHORT_FILE__="\"aom_main.F\"" /scratch/mellis/flavoured-cptk/cp2k/src/aom_main.F 
/scratch/mellis/flavoured-cptk/cp2k/src/aom_initialization.F:889:64:

      INTEGER :: i, j, k, l, m, d, c,  first_diabat, active_state, mat
                                                                1
Error: Unused variable ‘active_state’ declared at (1) [-Werror=unused-variable]
/scratch/mellis/flavoured-cptk/cp2k/src/aom_initialization.F:881:70:

      TYPE(atomic_kind_type), DIMENSION(:), POINTER  :: atomic_kind_set
                                                                      1
Error: Unused variable ‘atomic_kind_set’ declared at (1) [-Werror=unused-variable]
/scratch/mellis/flavoured-cptk/cp2k/src/aom_initialization.F:891:69:

      REAL(KIND=dp) :: cutoff_sites, cutoff_connect, scaling, deltatMD, deltatE
                                                                     1
Error: Unused variable ‘deltatmd’ declared at (1) [-Werror=unused-variable]
/scratch/mellis/flavoured-cptk/cp2k/src/aom_initialization.F:915:72:

      REAL(KIND=dp), DIMENSION(:), ALLOCATABLE     :: energy_conservation
                                                                        1
Error: Unused variable ‘energy_conservation’ declared at (1) [-Werror=unused-variable]
/scratch/mellis/flavoured-cptk/cp2k/src/aom_initialization.F:889:50:

      INTEGER :: i, j, k, l, m, d, c,  first_diabat, active_state, mat
                                                  1
Error: Unused variable ‘first_diabat’ declared at (1) [-Werror=unused-variable]
/scratch/mellis/flavoured-cptk/cp2k/src/aom_initialization.F:910:85:

      CHARACTER(LEN=default_string_length)         :: keyword_init, keyword_basis_repr, &
                                                                                     1
Error: Unused variable ‘keyword_basis_repr’ declared at (1) [-Werror=unused-variable]
/scratch/mellis/flavoured-cptk/cp2k/src/aom_initialization.F:910:65:

      CHARACTER(LEN=default_string_length)         :: keyword_init, keyword_basis_repr, &
                                                                 1
Error: Unused variable ‘keyword_init’ declared at (1) [-Werror=unused-variable]
/scratch/mellis/flavoured-cptk/cp2k/src/aom_initialization.F:903:62:

      INTEGER                                      :: new_state , ELsteps   
                                                              1
Error: Unused variable ‘new_state’ declared at (1) [-Werror=unused-variable]
/scratch/mellis/flavoured-cptk/cp2k/src/aom_initialization.F:914:67:

      INTEGER                                      :: nparticle_kind
                                                                   1
Error: Unused variable ‘nparticle_kind’ declared at (1) [-Werror=unused-variable]
/scratch/mellis/flavoured-cptk/cp2k/src/aom_initialization.F:911:68:

                                                      prop_wf_keyword
                                                                    1
Error: Unused variable ‘prop_wf_keyword’ declared at (1) [-Werror=unused-variable]
/scratch/mellis/flavoured-cptk/cp2k/src/aom_initialization.F:891:59:

      REAL(KIND=dp) :: cutoff_sites, cutoff_connect, scaling, deltatMD, deltatE
                                                           1
Error: Unused variable ‘scaling’ declared at (1) [-Werror=unused-variable]
/scratch/mellis/flavoured-cptk/cp2k/src/aom_initialization.F:888:25:

      INTEGER :: coord, t2
                         1
Error: Unused variable ‘t2’ declared at (1) [-Werror=unused-variable]
/scratch/mellis/flavoured-cptk/cp2k/src/aom_initialization.F:904:62:

      REAL(KIND=dp)                                :: dR, times 
                                                              1
Error: Unused variable ‘times’ declared at (1) [-Werror=unused-variable]
/scratch/mellis/flavoured-cptk/cp2k/src/aom_initialization.F:397:62:

                                   adiab_section, my_bo_keyword,  &
                                                              1
Error: Unused dummy argument ‘my_bo_keyword’ at (1) [-Werror=unused-dummy-argument]
f951: some warnings being treated as errors
/scratch/mellis/flavoured-cptk/cp2k/makefiles/Makefile:448: recipe for target 'aom_initialization.o' failed
make[3]: *** [aom_initialization.o] Error 1
make[3]: *** Waiting for unfinished jobs....
/scratch/mellis/flavoured-cptk/cp2k/makefiles/Makefile:129: recipe for target 'all' failed
make[2]: *** [all] Error 2
/scratch/mellis/flavoured-cptk/cp2k/makefiles/Makefile:118: recipe for target 'sopt' failed
make[1]: *** [sopt] Error 2
Makefile:113: recipe for target 'all' failed
make: *** [all] Error 2
"""

#s = raw_input("")

s = '/scratch/mellis/flavoured-cptk/cp2k/makefiles/make.log'
s = open(s, 'r').read()
#print(s)


flags = """-fall-intrinsics -fbackslash -fcray-pointer -fd-lines-as-code  
-fd-lines-as-comments   
-fdec -fdec-structure -fdec-intrinsic-ints -fdec-static -fdec-math  
-fdefault-double-8 -fdefault-integer-8 -fdefault-real-8  
-fdefault-real-10 -fdefault-real-16 -fdollar-ok -ffixed-line-length-n  
-ffixed-line-length-none -ffree-form -ffree-line-length-n  
-ffree-line-length-none -fimplicit-none -finteger-4-integer-8  
-fmax-identifier-length -fmodule-private -ffixed-form -fno-range-check  
-fopenacc -fopenmp -freal-4-real-10 -freal-4-real-16 -freal-4-real-8 
-freal-8-real-10 -freal-8-real-16 -freal-8-real-4 -std= 
-ftest-forall-temp -A-question 
-Aquestion= -C -CC -Dmacro 
-H -P 
-Umacro -cpp -dD -dI -dM -dN -dU -fworking-directory 
-imultilib dir 
-iprefix file -iquote -isysroot dir -isystem dir -nocpp  
-nostdinc  
-undef -Waliasing -Wall -Wampersand -Wargument-mismatch -Warray-bounds 
-Wc-binding-type -Wcharacter-truncation -Wconversion 
-Wdo-subscript -Wfunction-elimination -Wimplicit-interface 
-Wimplicit-procedure -Wintrinsic-shadow -Wuse-without-only -Wintrinsics-std 
-Wline-truncation -Wno-align-commons -Wno-tabs -Wreal-q-constant 
-Wsurprising -Wunderflow -Wunused-parameter -Wrealloc-lhs 
-Wrealloc-lhs-all -Wfrontend-loop-interchange -Wtarget-lifetime 
-fmax-errors= -fsyntax-only -pedantic -pedantic-errors -fbacktrace -fdump-fortran-optimized -fdump-fortran-original 
-fdump-parse-tree -ffpe-trap= -ffpe-summary  -I  -J -fintrinsic-modules-path dir -static-libgfortran -fconvert= -fmax-subrecord-length= 
-frecord-marker= -fsign-zero -fc-prototypes 
-faggressive-function-elimination -fblas-matmul-limit=  
-fbounds-check -fcheck-array-temporaries  
-fcheck= 
-fcoarray -fexternal-blas -ff2c 
-ffrontend-loop-interchange 
-ffrontend-optimize 
-finit-character= -finit-integer= -finit-local-zero 
-finit-derived 
-finit-logical= 
-finit-real= 
-finline-matmul-limit= 
-fmax-array-constructor= -fmax-stack-var-size= 
-fno-align-commons  
-fno-automatic -fno-protect-parens -fno-underscoring  
-fsecond-underscore -fpack-derived -frealloc-lhs -frecursive  
-frepack-arrays -fshort-enums -fstack-arrays 
""".replace('\n','').split(' ')
flags = [i.replace(" ", "").lower() for i in flags if i]

bad_words = ['Removing', 'Resolving','Discovering', 'f951:', 'make',] + flags


def find_line_num(err_msg):
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

def clean_err(err_msg):
    at_part = re.findall("at \(\d*\)", err_msg)
    for i in at_part:
        err_msg = err_msg.replace(i, "")
    flag_part = re.findall('\[\D*\]',err_msg)
    for i in flag_part:
        err_msg = err_msg.replace(i,'')
    err_msg = err_msg.replace("Error:", "").replace("\xe2\x80\x99", "'").replace("\xe2\x80\x98","'")
    err_msg = err_msg.strip()
    return err_msg

def find_module(err_msg):
    s = re.findall("/\D*.F",err_msg)
    if len(s) == 1:
        s = s[0]
        return s[s.rfind('/')+1:]
    else:
        return "Unable to find Module!"

def find_err_type(err_msg):
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

# Parsing the Error message
errs = {}
count = 0
s_lines = s.split('\n')
for i, line in enumerate(s_lines):
    
    if 'error:' in line.lower() and 'at ' in line.lower():
        errs[count] = {}
        err_msg = s_lines[i-4:i+1]
#        print err_msg, "\n\n"
        line_num, char_num = find_line_num(err_msg[0])
        if '-' in char_num:
            char_num = [int(i) for i in char_num.split('-')]
        else:
            char_num = int(char_num)
        bad_line = err_msg[2]
        err = err_msg[-1]
        err = clean_err(err)
        mod = find_module(err_msg[0])
        errs[count]['Module'] = mod.strip()
        errs[count]['Error'] = err.strip()
        errs[count]['Line'] = int(line_num)
        errs[count]['Line_Excerpt'] = bad_line.strip()
        errs[count]['char_num'] = char_num
        errs[count]['type'] = find_err_type(err)
        count += 1

err_txt = s[:]
while err_txt.find('In function') != -1:
    errs[count] = {}
    check = err_txt.find("In function ")
    err_txt = err_txt[check + len("In function "):]    
    function = err_txt[1:err_txt.find('\n')-2]
    next_line = err_txt.split('\n')[1]
    mod = find_module(next_line)
    line_num, char_num = find_line_num(next_line)
    err = next_line.split(':')[-1]
    
    errs[count]['Module'] = mod.strip()
    errs[count]['Error'] = err.strip()
    errs[count]['Line'] = int(line_num)
    errs[count]['Line_Excerpt'] = ''
    errs[count]['char_num'] = char_num
    errs[count]['type'] = find_err_type(err)
    count += 1

# If there are errors procede
if len(errs) > 0:
    line_nums = []
    err_nums = []
    mods = []
    for i in errs:
        line_nums.append(errs[i]['Line'])
        err_nums.append(i)
        mods.append(errs[i]['Module'])
    
    
    tol = 7 # Can improve by simply grouping all errors in same subroutine
    
    line_nums_and_err_nums = np.array(sorted(zip(line_nums, err_nums,mods)))
    sorted_err_nums = line_nums_and_err_nums[:,1].astype(int)
    line_num_diffs = np.diff(line_nums_and_err_nums[:,0].astype(int))
    err_groups = {i:{0:[]} for i in set(line_nums_and_err_nums[:,2])}
    counts = {i:0 for i in set(line_nums_and_err_nums[:,2])}
    for i, diff in enumerate(line_num_diffs):
        mod_nam = line_nums_and_err_nums[i,2]
        err_groups[mod_nam][counts[mod_nam]].append(int(line_nums_and_err_nums[i,1]))
        if diff > tol: # This is currently the check to see whether things belong to different subroutines.
            counts[mod_nam] += 1
            err_groups[mod_nam][counts[mod_nam]] = []
    err_groups[line_nums_and_err_nums[-1,2]][counts[line_nums_and_err_nums[-1,2]]].append(int(line_nums_and_err_nums[-1,1]))
    

    cols = ['255;255;0','0;255;0','255;0;255']
    
    def print_err(err_dict, SR_i):    
        print("Line  :         %i\n'"%(err_dict['Line']))
        print("Error :         %s\n'"%(err_dict['Error']))
        if err_dict['Line_Excerpt']:
            print("Line Excerpt:  '%s'\n'"%(err_dict['Line_Excerpt']))
#            print("            "+" "*err_dict['char_num']+"^")
        if err_dict['type'][:5] == '$FIX$':
            print("FIX   :         %s"%err_dict['type'][5:])
        print("\n")
    
    def unused_var_sort(err_msg, unused_vars, unused_lines):
        unused_var = err_msg['Error'].replace("Unused variable ","").replace(" declared",'').replace("Unused dummy argument","")
        str_line_no = str(err_msg['Line'])
        unused_vars.append(unused_var)
        unused_lines.append(str_line_no+(len(unused_var)-len(str_line_no))*" ")
    
    def print_unused_var_info(unused_vars, unused_lines, title):
        if unused_vars:
            print("\n\n"+"-"*15+"\n\n")
            print("Bulk Info:")
            print("\t%s: "%title)
            print("\t\t"+',\t'.join(unused_vars))
            print("\t\t"+',\t'.join(unused_lines))
            
    for mod_i, mod_name in enumerate(err_groups):
        col = cols[mod_i%len(cols)]
        os.system("printf '\e[38;2;%sm'"%(col))
        print("\t\t\t__________"+("_"*(len(mod_name)+2)))
        print("\t\t\t|"+" "*(len(mod_name)+10)+" |")
        print("\t\t\t| MODULE = %s |"%mod_name)
        print("\t\t\t|__________"+("_"*len(mod_name))+"_|\n\n\n")
        
        for group_i in err_groups[mod_name]:
            if group_i > 0:
                col = ';'.join([str(int(int(i)*0.9)) for i in col.split(';')])
            os.system("printf '\e[38;2;%sm          (possible) Sub Routine %i:\n\n'"%(col,group_i+1))        
            err_num_inds = err_groups[mod_name][group_i]
            unused_vars      = []
            unused_var_lines = []
            unused_args      = []
            unused_arg_lines = []
            for err_ind in err_num_inds:
                err_msg = errs[err_ind]
                if err_msg['type'] == 'unused_var':
                    unused_var_sort(err_msg, unused_vars, unused_var_lines)
                if err_msg['type'] == 'unused_arg':
                    unused_var_sort(err_msg, unused_args, unused_arg_lines)
                print_err(err_msg, group_i)
            print_unused_var_info(unused_vars, unused_var_lines, "Unused Variables")
            print_unused_var_info(unused_args, unused_arg_lines, "Unused Arguments")
            print("\n\n"+"-"*60+"\n\n")
            
        os.system("printf '\e[38;2;%sm\n'"%('255;255;255'))
            
            
