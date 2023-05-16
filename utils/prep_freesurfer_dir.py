#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 16:52:32 2023

@author: leocs
"""
def prep_freesurfer_dir(dataset,freesurfer_dir,reconall_dir=''):
    
    import os
    import shutil
    
    for i in range(0,dataset.shape[0]):
        
        if dataset['FS_version'][i] != '0' and \
           (float('.'.join(dataset['FS_version'][i].split('.')[0:2])) > 7.1 or \
           dataset['FS_version'][i] == '7.1.1') and \
           dataset['FS_errors'][i] == 'without errors':
               
               nifti = os.path.splitext(os.path.splitext(os.path.basename(dataset['NIfTIs'][i]))[0])[0]
               
               if not os.path.exists(os.path.join(freesurfer_dir,nifti)):
                   os.makedirs(os.path.join(freesurfer_dir,nifti))
                   os.makedirs(os.path.join(freesurfer_dir,nifti,'label'))
                   os.makedirs(os.path.join(freesurfer_dir,nifti,'stats'))
                   
    if reconall_dir != '' and not os.path.exists(os.path.join(reconall_dir,'fsaverage_img.trs')):
        shutil.copytree('/media/leocs/PortableSSD/DRIVE/analysis/enigma-ocd/fsaverage_img.trs', os.path.join(reconall_dir,'fsaverage_img.trs'))
