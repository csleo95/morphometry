#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 20:26:21 2023

@author: leocs
"""

def init_datasink_label_node(base_directory, name):
    
    import nipype.pipeline.engine as pe
    import nipype.interfaces.io as nio
    
    datasink_label = pe.Node(nio.DataSink(), name=name)
    datasink_label.inputs.base_directory = base_directory
    datasink_label.inputs.regexp_substitutions = [
    (r'(?<=tmp/).*(?=/[^/]*$)', ''),
    #('(.*/)([lr]h\\.(500\\.aparc|500\\.sym\\.aparc|100\\.aparc|HCPMMP1)\\.)(.*)(\\.annot)', r'\1\4/\2\5')
    ('(.*[/\\\\])([lr]h\\.(500\\.aparc|500\\.sym\\.aparc|100\\.aparc|HCPMMP1)\\.)(.*)(\\.annot)', r'\1\4/label/\2\5'),
    #(r'(.*)(lh\.(500\.aparc|500\.aparc\.sym|100\.aparc|HCPMMP1)\.)(.*)(\.annot)', '')
    (r'\.\.', '.')
    ]
    #datasink_label.inputs.substitutions = [
    #('my_workflow/', ''),
    #('/mri_surf2surf/mapflow/_mri_surf2surf', ''),
    #('_subject_id_', '')
    #]

    #datasink_label.inputs.regexp_substitutions = [
    # Remove node number 
    #(r'/_mri_surf2surf\d', '/label'),
    
    # Remove the long alphanumeric string in the path
    #(r'/morphometry_stats_wf/[a-zA-Z0-9]*/', '/'),
    
    # Isolate the subject identifier and move it to the proper position in the path
    #(r'(_mri_surf2surf_reconall_dir_node[0-9]*/)(lh|rh).(500.aparc|500.aparc.sym|500.sym.aparc|100.aparc|HCPMMP1).(.*)(.annot)', r'\4/label/\2.\3.annot'),
    
    # Remove additional '.' 
    #(r'\.\.', '.'),
    
    # Remove the session id from the filename
    #(r'(?<=aparc\.)[^.]+(?=\.annot)', ''),  
    #(r'(?<=HCPMMP1\.)[^.]+(?=\.annot)', '')
    #]




    #datasink_label.inputs.substitutions = [('my_workflow/', ''),
    #                                       ('/mri_surf2surf/mapflow/_mri_surf2surf', ''),
    #                                       ('_subject_id_', '')]
    #datasink_label.inputs.regexp_substitutions = [
    #                                            (r'(?<=aparc\.)[^.]+(?=\.annot)', ''),  
    #                                            (r'(?<=HCPMMP1\.)[^.]+(?=\.annot)', ''),
    #                                            (r'\.\.', '.'),
    #                                            (r'/_mri_surf2surf\d', '/label'),
    #                                            (r'(/morphometry_stats_wf/[a-zA-Z0-9]*/mri_surf2surf_freesurfer_dir_node[0-9]*/)(lh|rh).(500.aparc|500.aparc.sym|100.aparc|HCPMMP1).(.*)(.annot)', r'/\4/\2.\3.annot')
    #                                            ]
    
    return datasink_label

