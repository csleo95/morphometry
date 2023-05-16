#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 16:50:10 2023

@author: leocs
"""

def consolidate_dataset(dataset):   
    
    from rich.console import Console
    from rich.table import Table
    
    version_dict = {}
    
    # Iterate through unique Freesurfer versions and count files with and without errors
    for version in list(set(dataset['FS_version'])):
        version_dict[version] = [len([error for error in dataset.loc[dataset['FS_version'] == version, 'FS_errors'] if error == "with errors"]),
                                 len([nonerror for nonerror in dataset.loc[dataset['FS_version'] == version, 'FS_errors'] if nonerror == "without errors"])]
    
    # Create a table to summarize input breakdown
    table = Table(title = "Input Breakdown", title_style="bold blue", header_style="bold")
    
    # Define table columns and their properties
    table.add_column("NIfTI Files", justify="center", style="white", no_wrap=True)
    table.add_column("Freesurfer Version", justify="center", style="white")
    table.add_column("Recon-all Errors", justify="center", style="white")
    
    # Add data to table rows
    for key in version_dict.keys():
        if key == "0":
            version = "not processed"
        else:
            version = key
        table.add_row(str(version_dict[key][0]+version_dict[key][0]) + " NIfTI files", version, str(version_dict[key][0])+" files with errors")
    
    # Print table to console
    console = Console()
    console.print(table)