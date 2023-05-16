#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 20:41:33 2023

@author: leocs
"""
from nipype.interfaces.base import CommandLine, CommandLineInputSpec
from nipype.interfaces.base import File, traits, TraitedSpec

class MRIsAnatStatsInputSpec(CommandLineInputSpec):
    subject_name = traits.Str(mandatory=True, argstr='%s', position=-2, desc='subject name')
    hemi = traits.Str(mandatory=True, argstr='%s', position=-1, desc='hemisphere')
    annotation_file = File(existis=True, mandatory=False, argstr='-a %s', desc='annotation file')
    table_file = File(existis=False, mandatory=False, argstr='-f %s', desc='table file')
    tabular_output = traits.Bool(argstr='-b', desc='tabular output')
        
class MRIsAnatStatsOutputSpec(TraitedSpec):
    stats_file = File(desc='file with measures of morphometric features of cortical regions')


class MRIsAnatStats(CommandLine):
    _cmd = 'mris_anatomical_stats'
    input_spec = MRIsAnatStatsInputSpec
    output_spec = MRIsAnatStatsOutputSpec
    
    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['stats_file'] = self.inputs.table_file
        return outputs