#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 10:19:29 2023

@author: leocs
"""

def init_aparcstats2table_node(work_dir, parcellations, hemis):
    
    import os
    from nipype import MapNode
    from itertools import product
    from morphometry.interfaces.AparcStats2Table import AparcStats2Table
    
    meas = ['area', 'volume', 'thickness', 'thicknessstd', 'meancurv', 'gauscurv', 'foldind', 'curvind']
    
    combinations = list(product(hemis, parcellations, meas))
    combinations = [(*t, os.path.join(work_dir,'morpho_stats','regions', f"{t[1]}",f"{t[0]}.{t[1]}.{t[2]}.csv")) for t in combinations]
    zip(*combinations)
        
    aparcstats2table_node = MapNode(AparcStats2Table(), iterfield=['hemi','parc','meas','table_file'], name='aparcstats2table')
    #aparcstats2table_node.inputs.subjects = subjects
    aparcstats2table_node.inputs.hemi, aparcstats2table_node.inputs.parc, aparcstats2table_node.inputs.meas, aparcstats2table_node.inputs.table_file = zip(*combinations)
    aparcstats2table_node.inputs.delimiter = 'comma'
    aparcstats2table_node.inputs.environ = {'SUBJECTS_DIR':work_dir}
    
    return aparcstats2table_node

