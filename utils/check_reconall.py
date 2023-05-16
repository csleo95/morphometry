#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 00:57:44 2023

@author: leocs
"""

def check_reconall(dataset,subjects_dir):
    
    import os 
    import re
    
    if not os.path.exists(subjects_dir):
        raise ValueError(f"Recon-all directory does not exist: {subjects_dir}")
    
    for i in range(0,dataset.shape[0]):
        
        if dataset['FS_version'][i] == '0' or \
           float('.'.join(dataset['FS_version'][i].split('.')[0:2])) < 7.1 or \
           dataset['FS_version'][i] == '7.1.0' or \
           dataset['FS_errors'][i] == '' or \
           dataset['FS_errors'][i] == 'with errors':
                     
               if dataset['subs'][i] in os.listdir(subjects_dir):
                   
                   recon_all_log_path = os.path.join(subjects_dir, dataset['subs'][i],'scripts', 'recon-all.log')
                   
                   # Read log file in reverse order
                   with open(recon_all_log_path, 'r') as log_file:
                       log_lines = log_file.readlines()[::-1]
                       
                   # Extract the version
                   version_pattern = re.compile(r'build-stamp.txt')
                   version = None
                   for line in log_lines:
                       if version_pattern.search(line):
                           version = re.search(r'[0-9](\.[0-9]){1,2}', line).group()
                           break
                   if version is not None:
                       dataset['FS_version'][i] = version
                   
                   # Extract whether errors occured
                   error_pattern = re.compile(r'recon-all .*(finished|exited)')
                   error = None
                   for line in log_lines:
                       if error_pattern.search(line):
                           if 'without error' in line.lower():
                               error = 'without errors'
                           elif 'with errors' in line.lower():
                               error = 'with errors'
                           break
                   if error is not None:
                       dataset['FS_errors'][i] = error
                     
                   if dataset['FS_version'][i] != '0' and \
                      (float('.'.join(dataset['FS_version'][i].split('.')[0:2])) > 7.1 or \
                      dataset['FS_version'][i] == '7.1.1') and \
                      dataset['FS_errors'][i] == 'without errors':
                          
                          dataset['subjects_dir'][i] = subjects_dir                                                           
                       
    return dataset
