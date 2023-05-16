#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 01:18:05 2023

@author: leocs
"""

def get_sulc_stats(sulc_files, hemi, parcellation, work_dir):
    
    import os
    import pandas as pd

    n = 0
    if parcellation == "500.aparc" and hemi == "lh":
        n = 153
    elif parcellation == "500.aparc" and hemi == "rh":
        n = 157
    elif parcellation == "100.aparc" and hemi == "lh":
        n = 768
    elif parcellation == "100.aparc" and hemi == "rh":
        n = 767
    elif parcellation == "HCPMMP1" and hemi == "lh":
        n = 181
    elif parcellation == "HCPMMP1" and hemi == "rh":
        n = 181
    elif parcellation == "500.sym.aparc" and hemi == "lh":
        n = 160
    elif parcellation == "500.sym.aparc" and hemi == "rh":
        n = 160
    
    sulc_df = pd.DataFrame(columns = ['']*n)

    for file in sulc_files:
        
        if hemi in file and parcellation in file and 'sulc.sum' in file:
            
            with open(file, 'r') as f:
                lines = f.readlines()[-n:]
            
            if sulc_df.empty:
                sulc_df.columns = [line.split()[4] for line in lines]
             
            sulc_row = [line.split()[5] for line in lines]
            sulc_row = pd.DataFrame([sulc_row], columns=sulc_df.columns)
            sulc_df = pd.concat([sulc_df, sulc_row], ignore_index=False)
            
            index_name = os.path.basename(file).split('.')[0]
            
            if sulc_df.shape[0] == 1:
                sulc_df.index = [index_name]
            else:
                sulc_df.index = sulc_df.index.tolist()[:-1] + [index_name]
    
    table_file = os.path.join(work_dir,hemi+'.'+parcellation+'.sulc.csv')
    sulc_df.to_csv(table_file)

    return table_file

def init_get_sulc_stats_node(hemis, parcellations, work_dir):
    
    from nipype import Function
    from nipype.pipeline import MapNode
    from itertools import product
    
    get_sulc_stats_node = MapNode(
        Function(
            input_names=["sulc_files", "hemi", "parcellation", "work_dir"],
            output_names=["table_file"],
            function=get_sulc_stats
        ),
        name='get_sulc_stats',
        iterfield=['hemi', 'parcellation']
    )
    
    combinations = list(product(hemis, parcellations))
    
    get_sulc_stats_node.inputs.hemi, get_sulc_stats_node.inputs.parcellation = zip(*combinations)
    get_sulc_stats_node.inputs.work_dir = work_dir

    return get_sulc_stats_node

