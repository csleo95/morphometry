#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 20:44:18 2023

@author: leocs
"""

def init_mris_anat_stats_node(subjects_dir, name):
    
    import os
    from nipype.pipeline.engine import MapNode
    from morphometry.interfaces.MRIsAnatStats import MRIsAnatStats
    
    os.environ['SUBJECTS_DIR'] = subjects_dir
        
    mris_anat_stats_node = MapNode(MRIsAnatStats(), iterfield=['annotation_file','subject_name','hemi','table_file'], name=name)
    mris_anat_stats_node.inputs.tabular_output = True
    mris_anat_stats_node.inputs.environ = {'SUBJECTS_DIR':subjects_dir}
    
    return mris_anat_stats_node