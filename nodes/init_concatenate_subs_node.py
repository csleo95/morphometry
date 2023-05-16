#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 10:13:49 2023

@author: leocs
"""

def init_concatenate_subs_node(n_inputs):
    
    from nipype.interfaces.utility import Merge
    from nipype import Node
    
    # Create a Merge Node to concatenate the outputs of the two input nodes
    concatenate_subs_node = Node(Merge(10), name="concatenate_subs")
    concatenate_subs_node.inputs.ravel_inputs = True
    
    from nipype import JoinNode, IdentityInterface
    from nipype import Function, JoinNode, IdentityInterface, Workflow
    
    def concatenate_lists(list1, list2):
        return list1 + list2

    concatenate_function = Function(input_names=['list1', 'list2'],
                                output_names=['concatenated_list'],
                                function=concatenate_lists)

    concatenate_node = Node(concatenate_function, name='concatenate_node')

    joinnode = JoinNode(IdentityInterface(fields=['list1', 'list2']),
                    joinsource="inputnode",
                    joinfield=['list1', 'list2'],
                    name="joinnode")
    
    return concatenate_subs_node


