#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 01:48:35 2023

@author: leocs
"""

def init_mri_surf2surf_node(subjects_dir, parcellations, hemis, name):
    
    import os
    from nipype import Node, Function, MapNode

    os.environ['SUBJECTS_DIR'] = subjects_dir
    
    hemi = [hemi for hemi in hemis for parcellation in parcellations]
    source_annot_file = [os.path.join(subjects_dir, 'fsaverage_img.trs', 'label', hemi+'.'+parcellation+'.annot') for hemi in hemis for parcellation in parcellations]

    # Create mri_surf2surf node
    from nipype.interfaces.freesurfer import SurfaceTransform

    mri_surf2surf_node = MapNode(SurfaceTransform(),iterfield=['source_annot_file','hemi'], name=name) 
    mri_surf2surf_node.inputs.source_subject = 'fsaverage_img.trs'
    mri_surf2surf_node.inputs.source_annot_file = source_annot_file
    mri_surf2surf_node.inputs.hemi = hemi
    mri_surf2surf_node.inputs.environ = {'SUBJECTS_DIR':subjects_dir}
    
    return mri_surf2surf_node