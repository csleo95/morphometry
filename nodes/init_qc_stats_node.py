#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 21:29:22 2023

@author: leocs
"""

def get_qc_stats(subs,subjects_dir,hemis,output_dir):
    
    import pandas as pd
    import os
    from nipype import  MapNode
    from nipype.interfaces.freesurfer import EulerNumber
    
    surfaces = ['white', 'pial', 'smoothwm', 'inflated', 'sphere', 'orig', 'orig.nofix']
    
    columns = [f'{hemi}.{surface}' for hemi in hemis for surface in surfaces]
    defects_df = pd.DataFrame(columns=columns)
    euler_df = pd.DataFrame(columns=columns)
    
    for sub in subs:
        
        in_file = [os.path.join(subjects_dir, sub, 'surf', f'{hemi}.{surface}') for hemi in hemis for surface in surfaces]

        euler_node = MapNode(EulerNumber(), iterfield=['in_file'], name='euler_node') 
        euler_node.inputs.in_file = in_file
        euler_node.inputs.environ = {'SUBJECTS_DIR':subjects_dir}
        res = euler_node.run()
        
        defects_list = res.outputs.defects
        euler_list = res.outputs.euler
        
        defects_df.loc[sub] = defects_list
        euler_df.loc[sub] = euler_list
    
    defects_df.to_csv(os.path.join(output_dir,'defects_df.csv'))
    euler_df.to_csv(os.path.join(output_dir,'euler_df.csv'))
    
    return None

def init_qc_stats_node(subjects_dir,hemis,output_dir):
    
    from nipype import  Node, Function
 
    qc_stats_node = Node(Function(input_names=['subs','subjects_dir','hemis','output_dir'],
                                  output_names=[],
                                  function=get_qc_stats),
                         name='qc_stats_node')
    
    qc_stats_node.inputs.subjects_dir = subjects_dir
    qc_stats_node.inputs.hemis = hemis
    qc_stats_node.inputs.output_dir = output_dir
    
    return qc_stats_node
        
        
        
