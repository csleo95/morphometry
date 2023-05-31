===========================
Usage
===========================

The `morphometry` command is a wrapper script that performs T1-weighted MRI data preprocessing for the morphometric similarity analyses proposed by Seidlitz et al, 2018 and Sebenius et al, 2022. The command takes both required and optional arguments.

Command Structure
------------------

.. code-block:: bash

    morphometry data_dir output_dir [--data-dir-structure] [--work-dir] [--recon-all-dir] [--participant-label] [--parcellations] [--preproc-only] [--group-stats-only] [--n-procs] [--mem]

Required Arguments
------------------

`data_dir`
    Path of the root folder with a valid BIDS or raw NIfTI dataset.

`output_dir`
    Path of the folder where output will be stored.

Optional Arguments
------------------

`--data-dir-structure`
    The structure of the data directory. Choices are 'bids' for a BIDS-compliant directory, 'raw' for a directory with raw NIfTI files.

`--work-dir`
    Path where intermediate results will be stored.

`--recon-all-dir`
    Path to directory with output from Freesurfer's recon-all.

`--participant-label`
    Space-delimited list of participant identifier(s).

`--parcellations`
    Specifies the cortical parcellations to be used in the analysis. Choices include '500.aparc', '100.aparc', 'HCPMMP1', and '500.sym.aparc'. If not provided, a default scheme will be used.

`--preproc-only`
    If set, only preprocessing will be performed.

`--group-stats-only`
    If set, only group statistics will be calculated.

`--n-procs`
    Maximum number of threads across all processes per task.

`--mem`
    Upper bound memory limit.

