#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 01:41:23 2023

@author: leocs
"""
    
def init_morphometry_stats_both_wf(dataset, 
                                   parcellations,
                                   reconall_dir,
                                   freesurfer_dir,
                                   hemi,
                                   work_dir,
                                   output_dir):
    
    import os    
    from nipype import Workflow
    from morphometry.nodes.init_processed_subs_node import init_processed_subs_node
    from morphometry.nodes.init_mri_surf2surf_node import init_mri_surf2surf_node
    from morphometry.nodes.init_datasink_label_node import init_datasink_label_node
    from morphometry.nodes.init_mris_anat_stats_node import init_mris_anat_stats_node
    from morphometry.nodes.init_aparcstats2table_node import init_aparcstats2table_node
    from morphometry.nodes.init_merge_node import init_merge_node
    from morphometry.nodes.init_join_node import init_join_node
    from morphometry.nodes.init_mri_seg_stats_node import init_mri_seg_stats_node
    from morphometry.nodes.init_get_sulc_stats_node import init_get_sulc_stats_node
    from morphometry.nodes.init_qc_stats_node import init_qc_stats_node
    from morphometry.nodes.init_mind_node import init_mind_node
    from morphometry.nodes.init_samseg_node import init_samseg_node
    from morphometry.utils.handler_functions import get_sub
    from morphometry.utils.handler_functions import get_hemi
    from morphometry.utils.handler_functions import convert_to_stats
    from morphometry.utils.handler_functions import get_str_sub
    from morphometry.utils.handler_functions import get_annot
    from morphometry.utils.handler_functions import get_summ
    from morphometry.utils.handler_functions import get_in_vol
    from morphometry.utils.handler_functions import get_str_summ
    
    # define reconall_dir nodes
    processed_subs_reconall_dir_node = init_processed_subs_node(dataset, reconall_dir, 'processed_subs_reconall_dir_node')
    mri_surf2surf_reconall_dir_node = init_mri_surf2surf_node(reconall_dir, parcellations, hemi,'mri_surf2surf_reconall_dir_node')
    datasink_label_reconall_dir_node = init_datasink_label_node(work_dir, 'sinker_reconall_dir_node')
    mris_anat_stats_reconall_dir_node = init_mris_anat_stats_node(reconall_dir, 'mris_anat_stats_reconall_dir_node')
    join_subs_reconall_dir_node = init_join_node('join_subs_reconall_dir_node','processed_subs_reconall_dir_node')
    mri_seg_stats_reconall_dir_node = init_mri_seg_stats_node(work_dir, 'mri_seg_stats_reconall_dir_node')
    join_sulc_summ_reconall_dir_node = init_join_node('join_sulc_summ_reconall_dir_node','processed_subs_reconall_dir_node')
    mind_reconall_dir_node = init_mind_node(work_dir,parcellations,os.path.join(output_dir,'MIND'),'mind_reconall_dir_node')
    samseg_reconall_dir_node = init_samseg_node(os.path.join(output_dir,'samseg'),'samseg_reconall_dir_node')

    
    # define freesurfer_dir nodes
    processed_subs_freesurfer_dir_node = init_processed_subs_node(dataset, freesurfer_dir, 'processed_subs_freesurfer_dir_node')
    mri_surf2surf_freesurfer_dir_node = init_mri_surf2surf_node(freesurfer_dir, parcellations, hemi,'mri_surf2surf_freesurfer_dir_node')
    datasink_label_freesurfer_dir_node = init_datasink_label_node(work_dir, 'sinker_freesurfer_dir_node')
    mris_anat_stats_freesurfer_dir_node = init_mris_anat_stats_node(freesurfer_dir, 'mris_anat_stats_freesurfer_dir_node')
    join_subs_freesurfer_dir_node = init_join_node('join_subs_freesurfer_dir_node','processed_subs_freesurfer_dir_node')
    mri_seg_stats_freesurfer_dir_node = init_mri_seg_stats_node(work_dir, 'mri_seg_stats_freesurfer_dir_node')
    join_sulc_summ_freesurfer_dir_node = init_join_node('join_sulc_summ_freesurfer_dir_node','processed_subs_freesurfer_dir_node')
    mind_freesurfer_dir_node = init_mind_node(work_dir,parcellations,os.path.join(output_dir,'MIND'),'mind_freesurfer_dir_node')
    samseg_freesurfer_dir_node = init_samseg_node(os.path.join(output_dir,'samseg'),'samseg_freesurfer_dir_node')
   
    # define global nodes
    merge_subs_node = init_merge_node('merge_subs_node')
    aparcstats2table_node = init_aparcstats2table_node(work_dir, parcellations, hemi)
    merge_sulc_summ_node = init_merge_node('merge_sulc_summ_node')
    get_sulc_stats_node = init_get_sulc_stats_node(hemi, parcellations, os.path.join(work_dir, 'sulc_stats'))
    qc_stats_node = init_qc_stats_node(work_dir,hemi,os.path.join(output_dir,'qc_stats'))
   
    # Create a workflow
    morphometry_stats_wf = Workflow(name='morphometry_stats_wf', base_dir=work_dir)

    # Connect the nodes
    morphometry_stats_wf.connect([
                                    (processed_subs_reconall_dir_node, mri_surf2surf_reconall_dir_node, [('subs', 'target_subject')]),
                                    (mri_surf2surf_reconall_dir_node, datasink_label_reconall_dir_node, [('out_file', '@out_file')]),
                                    (datasink_label_reconall_dir_node, mris_anat_stats_reconall_dir_node, [('out_file', 'annotation_file')]),
                                    (datasink_label_reconall_dir_node, mris_anat_stats_reconall_dir_node, [(('out_file',convert_to_stats),'table_file')]),
                                    (datasink_label_reconall_dir_node, mris_anat_stats_reconall_dir_node, [(('out_file',get_sub),'subject_name')]),
                                    (datasink_label_reconall_dir_node, mris_anat_stats_reconall_dir_node, [(('out_file',get_hemi),'hemi')]),
                                    (mris_anat_stats_reconall_dir_node, join_subs_reconall_dir_node, [(('stats_file',get_str_sub), 'input')]),
                                    (datasink_label_reconall_dir_node, mri_seg_stats_reconall_dir_node, [(('out_file',get_annot), 'annot')]),
                                    (datasink_label_reconall_dir_node, mri_seg_stats_reconall_dir_node, [(('out_file',get_summ), 'summ')]),
                                    (datasink_label_reconall_dir_node, mri_seg_stats_reconall_dir_node, [(('out_file',get_in_vol), 'i')]),
                                    (mri_seg_stats_reconall_dir_node, join_sulc_summ_reconall_dir_node, [(('out_file',get_str_summ), 'input')]),
                                    (datasink_label_reconall_dir_node, mind_reconall_dir_node, [(('out_file',get_str_sub), 'sub')]),
                                    (processed_subs_reconall_dir_node, samseg_reconall_dir_node, [('niftis', 'input')]),
                                    (processed_subs_reconall_dir_node, samseg_reconall_dir_node, [('subs', 'output')]),
                                    
                                    (processed_subs_freesurfer_dir_node, mri_surf2surf_freesurfer_dir_node, [('subs', 'target_subject')]),
                                    (mri_surf2surf_freesurfer_dir_node, datasink_label_freesurfer_dir_node, [('out_file', '@out_file')]),
                                    (datasink_label_freesurfer_dir_node, mris_anat_stats_freesurfer_dir_node, [('out_file', 'annotation_file')]),
                                    (datasink_label_freesurfer_dir_node, mris_anat_stats_freesurfer_dir_node, [(('out_file',convert_to_stats),'table_file')]),
                                    (datasink_label_freesurfer_dir_node, mris_anat_stats_freesurfer_dir_node, [(('out_file',get_sub),'subject_name')]),
                                    (datasink_label_freesurfer_dir_node, mris_anat_stats_freesurfer_dir_node, [(('out_file',get_hemi),'hemi')]),
                                    (mris_anat_stats_freesurfer_dir_node, join_subs_freesurfer_dir_node, [(('stats_file',get_str_sub), 'input')]),
                                    (datasink_label_freesurfer_dir_node, mri_seg_stats_freesurfer_dir_node, [(('out_file',get_annot), 'annot')]),
                                    (datasink_label_freesurfer_dir_node, mri_seg_stats_freesurfer_dir_node, [(('out_file',get_summ), 'summ')]),
                                    (datasink_label_freesurfer_dir_node, mri_seg_stats_freesurfer_dir_node, [(('out_file',get_in_vol), 'i')]),
                                    (mri_seg_stats_freesurfer_dir_node, join_sulc_summ_freesurfer_dir_node, [(('out_file',get_str_summ), 'input')]),
                                    (datasink_label_freesurfer_dir_node, mind_freesurfer_dir_node, [(('out_file',get_str_sub), 'sub')]),
                                    (processed_subs_freesurfer_dir_node, samseg_freesurfer_dir_node, [('niftis', 'input')]),
                                    (processed_subs_freesurfer_dir_node, samseg_freesurfer_dir_node, [('subs', 'output')]),
                                    
                                    (join_subs_reconall_dir_node, merge_subs_node, [('input', 'in1')]),
                                    (join_subs_freesurfer_dir_node, merge_subs_node, [('input', 'in2')]),
                                    (merge_subs_node, aparcstats2table_node, [('out', 'subjects')]),
                                    (join_sulc_summ_reconall_dir_node, merge_sulc_summ_node, [('input', 'in1')]),
                                    (join_sulc_summ_freesurfer_dir_node, merge_sulc_summ_node, [('input', 'in2')]),
                                    (merge_sulc_summ_node, get_sulc_stats_node, [('out', 'sulc_files')]),
                                    (merge_subs_node, qc_stats_node, [('out', 'subs')]),
                                    #(merge_subs_node, split_subs_node, [('out', 'subs')]),
                                    #(split_subs_node, mind_node, [('subs', 'subs')])

                                ])
    
    return morphometry_stats_wf


