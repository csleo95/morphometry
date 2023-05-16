#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 20:54:04 2023

@author: leocs
"""

def get_sub(annot_files):
    return [annot_file.split('/')[-3] for annot_file in annot_files]

def get_hemi(annot_files):
    import os
    return [os.path.basename(annot_file).split('.')[0] for annot_file in annot_files]

def convert_to_stats(annot_files):
    return [annot_file.replace('label','stats').replace('annot','stats') for annot_file in annot_files]

def concatenate_list(in_list):
    
    if isinstance(in_list, str):
        in_list = [in_list]  # make it a list of strings
    elif isinstance(in_list, list) and all(isinstance(i, str) for i in in_list):
        pass  # it's already a list of strings, do nothing
    else:
        raise ValueError("in_lists must be a string or a list of strings")
    
    out_list = [item.split('/')[-3] for item in in_list]
    
    return out_list

def get_str_sub(input_files):
    return input_files[0].split('/')[-3] if input_files else None

def get_annot(annot_files):
    if isinstance(annot_files, str):
        annot_files = [annot_files]
    formatted_strings = []
    for file in annot_files:
        file_parts = file.split('/')
        sub = file_parts[-3]
        hemi = file_parts[-1].split('.')[0]
        parc = file_parts[-1].split('.')[1:-1]
        parc = '.'.join(parc)
        formatted_string = f"{sub} {hemi} {parc}"
        formatted_strings.append(formatted_string)
    return formatted_strings

def get_summ(annot_files):
    import re
    import os
    
    if isinstance(annot_files, str):
        annot_files = [annot_files]
    
    summ_files = []
    for annot_file in annot_files:
        path = re.sub(r'(?<=tmp/).*', "sulc", annot_file)
        sub = annot_file.split('/')[-3]
        spec = os.path.basename(annot_file).replace('annot','sulc.sum')
        summ_file = os.path.join(path,sub+'.'+spec)
        summ_files.append(summ_file)

    if len(summ_files) == 1:
        return summ_files[0]
    else:
        return summ_files


def get_in_vol(annot_files):
    import re

    if isinstance(annot_files, str):
        # if annot_files is a single string
        summ_file = annot_files.replace('label','surf')
        summ_file = re.sub(r'(?<=lh|rh).*$', '.sulc', summ_file)
        return summ_file

    elif isinstance(annot_files, list):
        # if annot_files is a list of strings
        summ_files = []
        for annot_file in annot_files:
            summ_file = annot_file.replace('label','surf')
            summ_file = re.sub(r'(?<=lh|rh).*$', '.sulc', summ_file)
            summ_files.append(summ_file)
        return summ_files

    else:
        raise ValueError("annot_files must be a string or a list of strings")

def get_str_summ(input_file):
    return input_file[0]



