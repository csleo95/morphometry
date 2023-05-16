#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 16:46:38 2023

@author: leocs
"""

def get_niftis_bids(data_dir, data_dir_structure):
    
    import os 
    import pandas as pd
    from nipype.interfaces.io import BIDSDataGrabber

    # Check that the data_dir exists
    if not os.path.exists(data_dir):
        raise ValueError(f"Path does not exist: {data_dir}")

    # Initialize the BIDSDataGrabber
    bg = BIDSDataGrabber(base_dir=data_dir)
    try:
        nifti_files = bg.run().outputs.get()
    except Exception as e:
        raise RuntimeError(f"Error in BIDSDataGrabber: {e}")

    # Filter for .nii and .nii.gz files
    if data_dir_structure == "bids":
        nifti_files = [nifti for nifti in nifti_files['T1w'] if nifti.endswith(('.nii','.nii.gz'))]
    elif data_dir_structure == "raw":
        nifti_files = [nifti for nifti in os.listdir(data_dir) if nifti.endswith(('.nii','.nii.gz'))]
    
    if not nifti_files:
        raise ValueError("No .nii or .nii.gz files found in {data_dir}")
        
    # Get subs
    subs = [os.path.splitext(os.path.splitext(os.path.basename(nifti))[0])[0] for nifti in nifti_files]

    # Initialize FS_version, FS_errors, and output_dir
    fs_version = ['0'] * len(nifti_files)
    fs_error = [''] * len(nifti_files)
    subjects_dir   = [''] * len(nifti_files)

    # Create the DataFrame
    try:
        dataset = pd.DataFrame({'subs': subs, 'NIfTIs': nifti_files, 'FS_version': fs_version, 'FS_errors': fs_error, 'subjects_dir': subjects_dir  })
    except Exception as e:
        raise RuntimeError(f"Error creating DataFrame: {e}")

    return dataset
