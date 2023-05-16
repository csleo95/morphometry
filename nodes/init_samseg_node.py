#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 16:51:25 2023

@author: leocs
"""

def init_samseg_node(base_dir,name):
    
    from nipype.pipeline import Node
    from morphometry.interfaces.RunSamseg import RunSamseg

    samseg_node = Node(RunSamseg(), name=name)
    samseg_node.inputs.base_directory = base_dir
    
    return samseg_node