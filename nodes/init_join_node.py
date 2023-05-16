#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 04:25:10 2023

@author: leocs
"""

def init_join_node(name,joinsource):
    
    from nipype import JoinNode
    from nipype.interfaces.utility import IdentityInterface
    
    join_subs_node = JoinNode(IdentityInterface(fields=['input']),
                                                name=name,
                                                joinsource=joinsource,
                                                joinfield='input',
                                                unique = True)
    
    return join_subs_node