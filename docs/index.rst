.. morphometry documentation master file, created by
   sphinx-quickstart on Sun May 28 01:05:28 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to morphometry's documentation!
=======================================

morphometry is an easy-to-use pipeline for preprocessing T1w-MRI data and computing several morphometric statistics.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage
   running_on_a_desktop_server_ENIGMA_OCD
   running_on_a_slurm_server_ENIGMA_OCD
   troubleshooting

About
-----

Welcome to the **ENIGMA-OCD Imaging Transcriptomics project** data processing pipeline manual. This user guide will walk you through each step in the process to ensure successful execution and interpretation of results.

What the Pipeline Does
----------------------

The pipeline performs an automated sequence of steps which includes:

- Preprocessing NIfTI files with freesurfer’s `recon-all` (if required)
- Computing morphometric features for subparcellations of the Desikan-Killiany (DK) atlas
- Using freesurfer’s `run-samseg` to compute morphometric statistics for subcortical structures

This pipeline builds upon scripts developed by Rafael Romero-Garcia et al [1]. To ensure reproducibility of results and flexibility of use, containerized versions of the pipeline have been developed on both the Docker and Singularity platforms.

Steps in the Pipeline
---------------------

Running the pipeline involves the following steps:

1. **Download a handler script.**
2. **Execute the handler script** from terminal, which will interactively prompt the user for the following information to automatically run the pipeline:
   - Whether Docker or Singularity will be used to run the pipeline (if just one of them is installed on the server, the handler script will automatically use it to run the pipeline)
   - The full path to a directory containing NIfTI files
   - The full path to a directory containing freesurfer’s `recon-all` output for some / all the NIfTI files in the above directory (optional)
   - The number of threads to be used in the pipeline
3. **Check the output files** generated from the pipeline


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
