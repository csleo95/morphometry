#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 01:25:22 2023

@author: leocs
"""
from nipype.interfaces.base import CommandLine, CommandLineInputSpec, File, TraitedSpec, traits

class MRISegStatsInputSpec(CommandLineInputSpec):
    annot = traits.Str(mandatory=True, position = -3, argstr='--annot %s', desc='hemisphere')
    summ = traits.File(mandatory = True,argstr='--sum %s', desc='ASCII file in which summary statistics are saved')
    i = traits.File(mandatory = True,argstr='--i %s', desc='Input volume from which to compute more statistics')
        
class MRISegStatsOutputSpec(TraitedSpec):
    out_file = File(desc='file with computed statistics on segmented volumes')

class MRISegStats(CommandLine):
    _cmd = 'mri_segstats'
    input_spec = MRISegStatsInputSpec
    output_spec = MRISegStatsOutputSpec
    
    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['out_file'] = self.inputs.summ
        return outputs