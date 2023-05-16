#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 01:26:49 2023

@author: leocs
"""

def prep_work_dir(dataset,work_dir,parcellations,hemis):
    
    import os
    import shutil
    
    surfaces = ['white','pial','smoothwm','inflated','sphere','orig','orig.nofix','thickness','volume','area','curv','sulc']
    
    for i in range(0,dataset.shape[0]):
        
        if dataset['subjects_dir'][i] != 0:
            
            sub = dataset['subs'][i]
            subjects_dir = dataset['subjects_dir'][i]
            
            os.makedirs(os.path.join(work_dir, sub, 'label'), exist_ok=True) 
            os.makedirs(os.path.join(work_dir, sub, 'stats'), exist_ok=True) 
            os.makedirs(os.path.join(work_dir, sub, 'surf'), exist_ok=True) 
            
            for surface in surfaces:
                for hemi in hemis:
                    shutil.copy(os.path.join(subjects_dir, sub, 'surf',hemi+'.'+surface), os.path.join(work_dir, sub, 'surf',hemi+'.'+surface))
                    #shutil.copy(os.path.join(subjects_dir, sub, 'surf','rh.white'), os.path.join(work_dir, sub, 'surf','rh.white'))
                    #shutil.copy(os.path.join(subjects_dir, sub, 'surf','lh.white'), os.path.join(work_dir, sub, 'surf','lh.white'))
                    #shutil.copy(os.path.join(subjects_dir, sub, 'surf','rh.sulc'), os.path.join(work_dir, sub, 'surf','rh.sulc'))
                    #shutil.copy(os.path.join(subjects_dir, sub, 'surf','lh.sulc'), os.path.join(work_dir, sub, 'surf','lh.sulc'))                
    
    os.makedirs(os.path.join(work_dir, 'sulc'), exist_ok=True) 
    os.makedirs(os.path.join(work_dir, 'sulc_stats'), exist_ok=True)
    os.makedirs(os.path.join(work_dir, 'morpho_stats'), exist_ok=True)
    os.makedirs(os.path.join(work_dir, 'morpho_stats','regions'), exist_ok=True)
    
    if parcellations is not None:
        for parcellation in parcellations:
            os.makedirs(os.path.join(work_dir, 'morpho_stats','regions',parcellation), exist_ok=True)
    
    return None