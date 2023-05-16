#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 04:42:48 2023

@author: leocs
"""

def init_merge_node(name):
    
    from nipype import Node
    from nipype.interfaces.utility import Merge
    
    merge_subs_node = Node(Merge(2), name = name)

    return merge_subs_node