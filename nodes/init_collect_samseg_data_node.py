#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 23:29:02 2023

@author: leocs
"""

import os
import pandas as pd
from nipype import Node, Function

def collect_samseg_data(samseg_dir, output_file):
    # Collecting header information
    first_sub_dir = next(os.scandir(samseg_dir))
    first_file_path = os.path.join(first_sub_dir.path, 'samseg.stats')
    df = pd.read_csv(first_file_path, comment='#', header=None)
    header = df[0].apply(lambda x: x.split()[1]).tolist()
    header = ['sub'] + header + ['Intra-Cranial']

    # Initializing a dataframe with the header
    result_df = pd.DataFrame(columns=header)

    # Iterating over each subject directory
    for sub_dir in os.scandir(samseg_dir):
        samseg_stats_path = os.path.join(sub_dir.path, 'samseg.stats')
        sbtiv_stats_path = os.path.join(sub_dir.path, 'sbtiv.stats')

        # Concatenating samseg.stats and sbtiv.stats files
        with open(samseg_stats_path, 'r') as f1, open(sbtiv_stats_path, 'r') as f2:
            lines = f1.readlines() + f2.readlines()

        # Parsing the values
        values = [line.split()[2] for line in lines]
        values = [sub_dir.name] + values

        # Appending to the result dataframe
        result_df = result_df.append(pd.Series(values, index=header), ignore_index=True)

    # Saving to the output file
    result_df.to_csv(output_file, index=False)


collect_samseg_data_node = Node(Function(input_names=["samseg_dir", "output_file"],
                                         output_names=["output_file"],
                                         function=collect_samseg_data),
                                name="collect_samseg_data_node")

collect_samseg_data_node.inputs.samseg_dir = '/path/to/samseg_dir'
collect_samseg_data_node.inputs.output_file = '/path/to/output_file.csv'
