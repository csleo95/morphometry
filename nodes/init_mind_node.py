#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 15:37:21 2023

@author: leocs
"""

def init_mind_node(subjects_dir,parcellations,output_dir,name):
    
    from nipype import MapNode
    from morphometry.interfaces.GetVertexData import GetVertexData
    
    mind_node = MapNode(GetVertexData(), iterfield = ['parcellation'], name=name)
    #mind_node.inputs.sub = sub
    mind_node.inputs.subjects_dir = subjects_dir
    mind_node.inputs.features = ['CT','MC','Vol','SD','SA'] 
    mind_node.inputs.parcellation = parcellations
    mind_node.inputs.output_dir = output_dir
    
    return mind_node

