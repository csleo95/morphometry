#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 00:42:53 2023

@author: leocs
"""
from nipype.interfaces.base import CommandLine, CommandLineInputSpec, TraitedSpec, File, traits

class AparcStats2TableInputSpec(CommandLineInputSpec):
    hemi = traits.Str(mandatory=True, argstr='--hemi %s', desc='hemisphere')
    subjects = traits.List(traits.Str, mandatory=True, argstr='--subjects %s', desc='subject IDs')
    parc = traits.Str(mandatory=False, argstr='--parc %s', desc='parcellation')
    meas = traits.Str(mandatory=False, argstr='--meas %s', desc='measure')
    delimiter = traits.Str(mandatory=False, argstr='--delimiter %s', desc='delimiter between measures in the table')
    table_file = traits.Str(mandatory=False, argstr='--tablefile %s', desc='output table file',
                            default_value=traits.Undefined, usedefault=True)
        
class AparcStats2TableOutputSpec(TraitedSpec):
    table_file = File(desc='table with measures of morphometric features of cortical regions for each subject')

class AparcStats2Table(CommandLine):
    _cmd = 'aparcstats2table'
    input_spec = AparcStats2TableInputSpec
    output_spec = AparcStats2TableOutputSpec
    
