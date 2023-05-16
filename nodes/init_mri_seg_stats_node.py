#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 12:02:33 2023

@author: leocs
"""

def init_mri_seg_stats_node(work_dir, name):
    
    import os 
    from itertools import product
    from nipype import MapNode
    from morphometry.interfaces.MRISegStats import MRISegStats  
    from morphometry.utils.get_niftis_bids import get_niftis_bids
    
    os.environ['SUBJECTS_DIR'] = work_dir

    mri_seg_stats_node = MapNode(MRISegStats(), iterfield=['annot','i','summ'], name=name)

    return mri_seg_stats_node