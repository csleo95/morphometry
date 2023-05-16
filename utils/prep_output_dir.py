#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 01:00:19 2023

@author: leocs
"""
import os

def prep_output_dir(dataset,output_dir,parcellations):
    
    os.makedirs(os.path.join(output_dir,'morpho_stats','regions'), exist_ok=True)
    
    for parcellation in parcellations:
        
        os.makedirs(os.path.join(output_dir,'morpho_stats','regions', parcellation), exist_ok=True)
        
    os.makedirs(os.path.join(output_dir,'qc_stats'), exist_ok=True)
    
    os.makedirs(os.path.join(output_dir,'MIND'), exist_ok=True)
    
    os.makedirs(os.path.join(output_dir,'samseg'), exist_ok=True)
    
    for i in range(0,dataset.shape[0]):
        
        if dataset['subjects_dir'][i] != 0:
            
            sub = dataset['subs'][i]
            os.makedirs(os.path.join(output_dir,'samseg',sub), exist_ok=True)
    
    return None
    
    