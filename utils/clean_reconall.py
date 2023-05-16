#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 16:51:25 2023

@author: leocs
"""

def clean_reconall(freesurfer_dir):
    
    from nipype.interfaces.io import DataFinder
    import os 
    
    paths = DataFinder()
    paths.inputs.root_paths = freesurfer_dir
    paths.inputs.match_regex = '.*\/IsRunning\.lh\+rh$'
    
    try:
        result = paths.run(raise_on_empty=True)
    except AttributeError:
        # No IsRunning.lh+rh files found
        return
    
#    incomplete_dirs = ['/'.join(sub.split('/')[:-2]) for sub in result.outputs.out_paths]
    isrunning_files = result.outputs.out_paths
    
    if not isrunning_files:
        # No incomplete directories found
        return
    
    for isrunning_file in isrunning_files:
        os.remove(isrunning_file)
