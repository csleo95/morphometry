#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:04:10 2023

@author: Leonardo Cardoso Saraiva
"""

"""
Define arguments and parsing
"""
import os
import argparse

# Create an ArgumentParser object to handle command-line arguments
parser = argparse.ArgumentParser(
                                 prog="morphometry",
                                 description="This is a wrapper script \
                                             that performs T1-weighted MRI data \
                                             preprocessing for the morphometric \
                                             similarity analyses proposed by \
                                             Seidlitz et al, 2018 and \
                                             Sebenius et al, 2022")

# Add command-line arguments to the parser
parser.add_argument("data_dir",
                    help="path of the root folder with a valid BIDS or raw NIfTI dataset")

parser.add_argument("output_dir",
                    help="path of the folder where output will be stored")

parser.add_argument("--data_dir_structure",
                    type=str,
                    choices=['bids', 'raw'],
                    required=False,
                    metavar="",
                    help="The structure of the data directory. Choices are 'bids' for a BIDS-compliant directory, 'raw' for a directory with raw NIfTI files.")

parser.add_argument("--work_dir",
                    type=str,
                    required=False,
                    metavar="",
                    help="path where intermediate results will be stored")

parser.add_argument("--reconall_dir",
                    type=str,
                    required=False,
                    metavar="",
                    help="path to directory with output from Freesurfer's recon-all")

parser.add_argument("--participant",
                    type=str,
                    required=False,
                    metavar="",
                    help="space delimited list of participant identifier(s)")

parser.add_argument("--parcellations",
                    type=str,
                    choices=['500.aparc', '100.aparc', 'HCPMMP1', '500.sym.aparc'],
                    required=False,
                    nargs='+',
                    metavar="",
                    help="Specifies the cortical parcellations to be used in the analysis. Choices include '500.aparc', '100.aparc', 'HCPMMP1', and '500.sym.aparc'. If not provided, a default scheme will be used.")

#parser.add_argument("--hemis",
#                    type=str,
#                    choices=['lh', 'rh'],
#                    required=False,
#                    nargs='+',
#                    metavar="",
#                    help="Specifies the hemisphere(s) to be used in the analysis. Choices include '500.aparc', '100.aparc', 'HCPMMP1', and '500.sym.aparc'. If not provided, a default scheme will be used.")

parser.add_argument("--n_procs",
                    type=int,
                    required=False,
                    metavar="",
                    help="maximum number of threads across all processes per task")

parser.add_argument("--mem",
                    type=int,
                    required=False,
                    metavar="",
                    help="upper bound memory limit")

# Parse command-line arguments and store them in the 'args' object
args = parser.parse_args()

# Extract the required arguments
data_dir = os.path.abspath(args.data_dir)
output_dir = os.path.abspath(args.output_dir)

# Extract optional arguments, if provided
if args.data_dir_structure is not None:
    data_dir_structure = args.data_dir_structure
else:
    data_dir_structure = 'bids'
    
if args.work_dir is not None:
    work_dir = os.path.abspath(args.work_dir)
else:
    work_dir = os.getcwd()

if args.reconall_dir is not None:
    reconall_dir = os.path.abspath(args.reconall_dir)
    
if args.participant is not None:
    participant = args.participant
    
if args.parcellations is not None:
    parcellations = args.parcellations
else:
    parcellations = ['500.aparc', '100.aparc', 'HCPMMP1', '500.sym.aparc']
    
#if args.hemis is not None:
#    hemis = args.hemis
#else:
#    hemis = ['lh', 'rh']

if args.n_procs is not None:
    n_procs = args.n_procs
else:
    n_procs = 1

if args.mem is not None:
    mem = args.mem
else:
    mem = 8

# Set default values (may change this later)
hemis = ['lh', 'rh']


"""
Set up output directory
"""
output_dir = os.path.join(output_dir, 'morphometry')
freesurfer_dir = os.path.join(output_dir,'freesurfer')

# Create output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
# Create freesurfer directory if it does not exist
if not os.path.exists(freesurfer_dir):
    os.makedirs(freesurfer_dir)


"""
Set up work directory
"""
# Create tmp directory if it does not exist
work_dir = os.path.join(work_dir,'tmp')

if not os.path.exists(work_dir):
    os.makedirs(work_dir)

# change directory
os.chdir(work_dir)

"""
Gather NIfTIs of dataset
"""
from utils.get_niftis_bids import get_niftis_bids

if data_dir_structure == 'bids':
    try:
        dataset = get_niftis_bids(data_dir,"bids")
    except Exception as e:
        raise RuntimeError(f"Error when running capture_niftis_bids for data_dir={data_dir}: {e}")
elif data_dir_structure == 'raw':
    try:
        dataset = get_niftis_bids(data_dir,"raw")
    except Exception as e:
        raise RuntimeError(f"Error when running capture_niftis_bids for data_dir={data_dir}: {e}")


"""
Gather what has been done in previous recon-all runs, if provided
"""
from utils.check_reconall import check_reconall

if 'reconall_dir' in locals():
    try: 
        dataset = check_reconall(dataset,reconall_dir)
    except Exception as e:
        raise RuntimeError(f"Error when runnning check_reconall for reconall_dir={reconall_dir}: {e}")

        
"""
Present yourself
"""
# Import necessary packages
from utils.consolidate_dataset import consolidate_dataset
from termcolor import colored
import pyfiglet

# Define the text to be printed
text1 = "Morphometry"
text2 = "                     *** ENIGMA-OCD ***"

# Create the ASCII art using pyfiglet
result = pyfiglet.figlet_format(text1)

# Add color and bold attribute to the ASCII art using termcolor
colored_result = colored(f"{result}\n{text2}", color='blue', attrs=['bold'])

# Print the result
print(colored_result)

# Explain pipeline
print("")
print(" This pipeline performs T1-weighted MRI data preprocessing for the \n morphometric similarity analyses proposed by Seidlitz et al, 2018 \n and Sebenius et al, 2022")

# Breakdown input
print("\n")
consolidate_dataset(dataset)

"""
Prepare freesurfer dir
"""
#from utils.prep_freesurfer_dir import prep_freesurfer_dir
#prep_freesurfer_dir(dataset,freesurfer_dir,reconall_dir=reconall_dir)


"""
Remove incomplete isrunning file from incomplete recon-all runs
"""
from utils.clean_reconall import clean_reconall
clean_reconall(freesurfer_dir)


"""
Recon-all workflow
"""

import subprocess

# Set the FREESURFER_HOME environment variable
freesurfer_home = '/media/leocs/leo.hd/DRIVE/enigma-ocd/imaging.transcriptomics/pipeline/v0.3/docker/freesurfer'
os.environ["FREESURFER_HOME"] = freesurfer_home
#os.environ["SUBJECTS_DIR"] = os.path.join(os.getcwd(),freesurfer_dir)
os.environ["FSFAST_HOME"] = os.path.join(freesurfer_home, 'fsfast')
os.environ["MNI_DIR"] = os.path.join(freesurfer_home, 'mni')
os.environ["FSL_DIR"] = '/usr/local/fsl'
os.environ["PATH"] = os.path.join(freesurfer_home, "bin") + os.pathsep + os.environ["PATH"]

import shutil
if not os.path.exists(os.path.join(freesurfer_dir,'fsaverage_img.trs')):
    shutil.copytree('/media/leocs/PortableSSD/DRIVE/analysis/enigma-ocd/fsaverage_img.trs', os.path.join(freesurfer_dir,'fsaverage_img.trs'))

# Source the SetUpFreeSurfer.sh script
setup_script = os.path.join(freesurfer_home, "SetUpFreeSurfer.sh")
subprocess.run(f"source {setup_script}", shell=True, executable="/bin/bash")

  
#import utils
#from nipype import Workflow


#morphometry_wf = Workflow(name='morphometry')

#input_reconall_node = utils.set_input_reconall_node(dataset)

#if input_reconall_node == None and 'reconall_dir' in locals():
    
#    input_freesurfer_dir_node = utils.set_input_freesurfer_dir_node(dataset,freesurfer_dir)
#    mri_surf2surf_reconall_dir_node = utils.set_mri_surf2surf_reconall_dir_node(reconall_dir)
#    mris_anat_stats_reconall_dir_node = utils.set_mris_anat_stats_reconall_dir_node(reconall_dir)
    
#    input_reconall_dir_node = utils.set_input_reconall_dir_node(dataset,reconall_dir,freesurfer_dir)
    
#    morphometry_wf.connect([
#                            (input_reconall_dir_node,mri_surf2surf_reconall_dir_node,[('source_annot_file_reconall_dir','source_annot_file')]),
#                            (input_reconall_dir_node,mri_surf2surf_reconall_dir_node,[('target_subject_reconall_dir','target_subject')]),
#                            (input_reconall_dir_node,mri_surf2surf_reconall_dir_node,[('out_file_mri_surf2surf_reconall_dir','out_file')]),
#                            (input_reconall_dir_node,mri_surf2surf_reconall_dir_node,[('hemi_reconall_dir','hemi')]),
#                            (input_reconall_dir_node,mris_anat_stats_reconall_dir_node,[('target_subject_reconall_dir','subject_name')]),
#                            (input_reconall_dir_node,mris_anat_stats_reconall_dir_node,[('hemi_reconall_dir','hemi')]),
#                            (mri_surf2surf_reconall_dir_node,mris_anat_stats_reconall_dir_node,[('out_file','annotation_file')]),
#                            (input_reconall_dir_node,mris_anat_stats_reconall_dir_node,[('out_file_mris_anatomical_stats_reconall_dir','table_file')])
#        ])
    
#morphometry_wf.run(plugin='MultiProc', plugin_args={'n_procs': n_procs, 'memory_gb': mem})
    
    
    


#if input_reconall_node != None:
    
#    reconall_node = utils.set_reconall_node(freesurfer_dir)
    
#morphometry_wf.write_graph('graph.png')
#    morphometry_wf.connect([
#        (input_reconall_node,reconall_node,[('T1_files','T1_files')]),
#        (input_reconall_node,reconall_node,[('subject_id','subject_id')])
#    ])
#else:
#    morphometry_wf.connect([
#        (input_reconall_dir_node,mri_surf2surf_reconall_dir_node,[('source_annot_file','source_annot_file')]),
#        (input_reconall_dir_node,mri_surf2surf_reconall_dir_node,[('target_subject','target_subject')]),
#        (input_reconall_dir_node,mri_surf2surf_reconall_dir_node,[('out_file_mri_surf2surf','out_file')]),
#        (input_reconall_dir_node,mri_surf2surf_reconall_dir_node,[('hemi','hemi')])
#        (input_reconall_dir_node,mris_anat_stats_reconall_dir_node,[('target_subject','subject_name')]),
#        (input_reconall_dir_node,mris_anat_stats_reconall_dir_node,[('hemi','hemi')]),
#        (mri_surf2surf_reconall_dir_node,mris_anat_stats_reconall_dir_node,[('out_file','annotation_file')]),
#        (input_reconall_dir_node,mris_anat_stats_reconall_dir_node,[('out_file_mris_anatomical_stats','table_file')])
#    ])
    
#    morphometry_wf.run(plugin='MultiProc', plugin_args={'n_procs': n_procs, 'memory_gb': mem})


"""
Prepare work dir
"""
import sys
sys.path.insert(0, '/media/leocs/PortableSSD/DRIVE/analysis/enigma-ocd/main')

from morphometry.utils.prep_work_dir import prep_work_dir

dataset = check_reconall(dataset, freesurfer_dir)
prep_work_dir(dataset, work_dir, parcellations,hemis)



"""
Prepare output dir
"""
#import sys
#sys.path.insert(0, '/media/leocs/PortableSSD/DRIVE/analysis/enigma-ocd/main')

from morphometry.utils.prep_output_dir import prep_output_dir

prep_output_dir(dataset,output_dir,parcellations)



"""
Morphometric stats workflow
"""
from morphometry.workflows.init_morphometry_stats_both_wf import init_morphometry_stats_both_wf

morphometry_stats_wf = init_morphometry_stats_both_wf(dataset, 
                                                      parcellations,
                                                      reconall_dir,
                                                      freesurfer_dir,
                                                      hemis,
                                                      work_dir,
                                                      output_dir)

morphometry_stats_wf.run(plugin='MultiProc', plugin_args={'n_procs': 10})

#import sys

#import nipype
#nipype.config.set('logging', 'workflow_level', 'DEBUG')

#parcellations = ['500.aparc']
#hemi = ['lh']


#morphometry_stats_wf1 = init_morphometry_stats_wf(data_dir, 
#                                       data_dir_structure, 
#                                       reconall_dir, 
#                                       parcellations, 
#                                       hemi,
#                                       work_dir,
#                                       "test1")

#morphometry_stats_wf2 = init_morphometry_stats_wf(data_dir, 
#                                       data_dir_structure, 
#                                       freesurfer_dir, 
#                                       parcellations, 
#                                       hemi,
#                                       work_dir,
#                                       "test2")

#from morphometry.workflows.init_aparcstats2table_wf import init_aparcstats2table_wf

#aparcstats2table_wf = init_aparcstats2table_wf(output_dir, 
#                                               work_dir, 
#                                               parcellations, 
#                                               hemi,
#                                               2)

#from morphometry.workflows.init_mri_seg_stats_wf import init_mri_seg_stats_wf

#mri_seg_stats_wf1 = init_mri_seg_stats_wf(data_dir, 
#                          data_dir_structure, 
#                          work_dir,
#                          parcellations, 
#                          hemi,
#                          'test3')

#from nipype import Workflow

# Create a new workflow to contain the two existing workflows
#combined_workflow = Workflow(name='combined_workflow', base_dir = work_dir)

# Add the existing workflows to the new workflow
#combined_workflow.add_nodes([morphometry_stats_wf1, 
#                             morphometry_stats_wf2,
#                             aparcstats2table_wf,
#                             mri_seg_stats_wf1])

# Run the combined workflow
#combined_workflow.connect([
#                           (morphometry_stats_wf1, aparcstats2table_wf,[('outputnode.stats_file','inputnode.list1')])#,
                           #(morphometry_stats_wf2, aparcstats2table_wf,[('outputnode.stats_file','inputnode.list2')])
#                          ])

#combined_workflow.run(plugin='MultiProc', plugin_args={'n_procs': 10})
#combined_workflow.run()


