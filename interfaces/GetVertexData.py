#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 22:37:11 2023

@author: leocs
"""
import os
import pandas as pd
from nipype.interfaces.base import BaseInterface, BaseInterfaceInputSpec, traits, Directory, File, TraitedSpec
from morphometry.MIND.get_vertex_df_adj import get_vertex_df

class GetVertexDataInputSpec(BaseInterfaceInputSpec):
    sub = traits.Str(desc='Subject', mandatory=True)
    subjects_dir = Directory(exists=True, desc='Subjects directory', mandatory=True)
    features = traits.List(traits.Str, desc='List of features', mandatory=True)
    parcellation = traits.Str(desc='Parcellation', mandatory=True)
    output_dir = Directory(desc='Output directory', mandatory=True)

class GetVertexDataOutputSpec(TraitedSpec):
    vertex_data_file = File(exists=True, desc='Vertex data file')
    regions_file = File(exists=True, desc='Regions file')
    features_used_file = File(exists=True, desc='Features used file')

class GetVertexData(BaseInterface):
    input_spec = GetVertexDataInputSpec
    output_spec = GetVertexDataOutputSpec

    def _run_interface(self, runtime):
        vertex_data, regions, features_used = get_vertex_df(os.path.join(self.inputs.subjects_dir, self.inputs.sub), self.inputs.features, self.inputs.parcellation)

        vertex_data.to_hdf(os.path.join(self.inputs.output_dir, self.inputs.sub +'_vertex_data.h5'), key='df', mode = 'w')
        #pd.DataFrame(regions).to_hdf(os.path.join(self.inputs.output_dir, 'regions.h5'), key='df', mode = 'w')
        #pd.DataFrame(features_used).to_hdf(os.path.join(self.inputs.output_dir, 'features_used.h5'), key='df', mode = 'w')

        return runtime

    def _list_outputs(self):
        outputs = self._outputs().get()
        outputs['vertex_data_file'] = os.path.abspath(os.path.join(self.inputs.output_dir, self.inputs.sub +'_vertex_data.h5'))
        outputs['regions_file'] = os.path.abspath(os.path.join(self.inputs.output_dir, 'regions.h5'))
        outputs['features_used_file'] = os.path.abspath(os.path.join(self.inputs.output_dir, 'features_used.h5'))
        return outputs


