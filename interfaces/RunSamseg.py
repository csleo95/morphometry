#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 23:22:13 2023

@author: leocs
"""
import os
from nipype.interfaces.base import CommandLine, CommandLineInputSpec, TraitedSpec, File, Directory, traits

class RunSamsegInputSpec(CommandLineInputSpec):
    input = File(exists=True, desc='Input NIFTI file', argstr='--input %s', mandatory=True)
    output = traits.Str(desc='Output directory', argstr='--output %s', mandatory=True)
    base_directory = Directory(exists=True, desc='Base directory for output')

class RunSamsegOutputSpec(TraitedSpec):
    output_dir = Directory(exists=True, desc='Output directory')

class RunSamseg(CommandLine):
    _cmd = 'run_samseg'
    input_spec = RunSamsegInputSpec
    output_spec = RunSamsegOutputSpec

    def _run_interface(self, runtime):
        # Make output path absolute
        self.inputs.output = os.path.join(self.inputs.base_directory, self.inputs.output)
        return super(RunSamseg, self)._run_interface(runtime)

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['output_dir'] = os.path.abspath(self.inputs.output)
        return outputs


# nipype.pipeline import Node

#run_samseg = Node(RunSamseg(), name='run_samseg')
#run_samseg.inputs.input = '/media/leocs/leo.hd/DRIVE/enigma-ocd/imaging.transcriptomics/tests_v.01/2/nifti/sub-0001/ses-C001632d20150601/anat/sub-0001_ses-C001632d20150601_acq-VBM6minSENSE_rec-TOCCHOQUE_run-1_T1w.nii.gz'
#run_samseg.inputs.output = '/media/leocs/PortableSSD/DRIVE/analysis/enigma-ocd'

#run_samseg.run()
