#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 16:06:32 2023

@author: leocs
"""

def init_split_node():
    
    from nipype import MapNode
    from nipype.interfaces.utility import IdentityInterface
    
    split_node = MapNode(IdentityInterface(fields=['subs']), 
                       iterfield=['subs'], 
                       name="suplit_node")
    
    return split_node