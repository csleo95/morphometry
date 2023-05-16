#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 01:42:35 2023

@author: leocs
"""

def init_processed_subs_node(dataset, subjects_dir, name):
    
    from nipype import Node
    from nipype.interfaces.utility import IdentityInterface
    
    subs = []
    niftis = []
    
    for i in range(0,dataset.shape[0]):
        
        if dataset['subjects_dir'][i] != 0 and dataset['subjects_dir'][i] == subjects_dir:
            
            subs.append(dataset['subs'][i])
            niftis.append(dataset['NIfTIs'][i])
    
    # Create the identity interface node
    processed_subs_node = Node(IdentityInterface(fields=['subs','niftis']),
                            name=name)

    # Make the node iterable over the subject_ids
    processed_subs_node.iterables = [('subs', subs), ('niftis', niftis)]
    processed_subs_node.synchronize = True

    return processed_subs_node