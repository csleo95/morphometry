===========================
Running on a Slurm Server (ENIGMA-OCD)
===========================

This section provides a step-by-step guide for executing the pipeline on a slurm server. This process \
involves running a handler script that interactively collects inputs to automatically configure and initiate \
the pipeline. The script also verifies the validity of the inputs. If any inputs are found to be invalid, \
it will display error messages and prompt you to re-enter the incorrect ones.


1. Download and Execute the Handler Script
------------------------------

    - Open the terminal
    - Navigate to the directory where the handler script will be executed
    - Download the hanlder script by either:

    .. code-block:: bash

        curl -O https://raw.githubusercontent.com/csleo95/morphometry/main/handler_scripts/morphometry_handler_slurm.sh
    
    or: 

    .. code-block:: bash

        wget https://raw.githubusercontent.com/csleo95/morphometry/main/handler_scripts/morphometry_handler_slurm.sh

    - Make the handler script file executable.

    .. code-block:: bash

        chmod + x morphometry_handler_slurm.sh

    - Execute the handler script file.

    .. code-block:: bash

        ./morphometry_handler_slurm.sh


2. Provide Input for sbatch Script to Build Pipeline Image
------------------------------

    - Enter the path to the directory where the pipeline image will be built and the final image will be stored, or press enter for the current directory
    - Enter the #SBATCH flags to be append to the sbatch script, and enter "q" at the end; don't include "#SBATCH", only the flags themselves, for instance:

    .. code-block:: bash

        --partition=day
        --nodes=1
        --cpus-per-task=10
        --mem-per-cpus=5G
        --time=00-01:00:00
        q

    - The hanlder script will automatically configure the sbatch script and will run it for you


3. Enter the #SBATCH Flags for sbatch Script(s) to Run Pipeline Image
---------------------------------------------------------------------

Enter the #SBATCH flags to be append to the sbatch script, and enter "q" at the end; again: don't include "#SBATCH", only the flags themselves, for instance:

.. note::

   If the pipeline will be run as an array job, the handler script will generate two sbatch scripts to run the pipeline and will ask in turns the #SBATCH flags for each. The first script will be the array job, so don't forget to include the array flags.


4. Specifying the Directory Path for NIfTI Files
------------------------------------------------------------

During the execution of the script, you will be asked to provide the full path to the directory containing the NIfTI files of the T1 scans. Please note the following important points:

- This directory could be located in your user filesystem or on a mounted drive.
- The path provided must be the complete, absolute path. Relative paths or paths containing environment variables (such as `~/`) are not accepted.

For example, a correct full path might look like this: 

.. code-block:: bash

    /home/leocs/imgs/nifti

**Directory Structure**

The NIfTI files directory can follow one of two possible structures:

**Structure 1: Raw**
- The directory contains only the NIfTI files of the T1 scans. 

Example:

.. code-block:: bash

    ├── nifti
    │   ├── sub0001_ses-01_acq-VBM6minSENSE_rec-TOC_run-1_T1w.nii.gz
    │   ├── sub0002_ses-01_acq-VBM6minSENSE_rec-TOC_run-1_T1w.nii.gz

**Structure 2: BIDS Format**
- The directory contains the NIfTI files of the T1 scans structured in valid BIDS format (the `ses` directory is optional).

Example:

.. code-block:: bash

    ├── nifti
    │   └── sub-0001
    │       └── ses-01
    │           └── anat
    │               ├── sub-0001_ses-01_acq-VBMSENSE_rec-TOC_run-1_T1w.nii.gz
    │   └── sub-0002
    │       └── ses-01
    │           └── anat
    │               ├── sub-0002_ses-01_acq-VBMSENSE_rec-TOC_run-1_T1w.nii.gz



5. Specifying the Structure of the NIfTI Files Directory
------------------------------------------------------------------

During the execution of the script, you will be asked to specify the structure of the directory containing the NIfTI files. Please refer to the description provided in section 4 for the possible structures (i.e., raw NIfTI files or valid BIDS format).

Please note that you should specify the format of your directory as either "raw" or "bids" depending on the structure of your NIfTI files directory.

For example:

.. code-block:: bash

    Enter the structure of the NIfTI files directory: raw

or 

.. code-block:: bash

    Enter the structure of the NIfTI files directory: bids


6. Specifying the Directory Path for recon-all Output
--------------------------------------------------------------

During the execution of the script, you will be asked to provide the full path to the directory containing the output from Freesurfer's `recon-all` operation. 

Please note the following:

- This directory could be located in your user filesystem or on a mounted drive.
- The path provided must be the complete, absolute path. Relative paths or paths containing environment variables (such as `~/`) are not accepted.
- The directories within this directory should be named identically to their corresponding NIfTI files, excluding file extensions.

For example, a correct full path and directory structure might look like this:

.. code-block:: bash

    /home/leocs/imgs/recon-all-output

And the corresponding directory structure:

.. code-block:: bash

    ├── reconall
    │   └── sub-0001_ses-01_acq-VBM6minSENSE_rec-TOC_run-1_T1w
    │       ├── label
    │       ├── mri
    │       ├── scripts
    │       ├── stats
    │       ├── surf
    │       ├── tmp
    │       ├── touch
    │       └── trash
    │   └── sub-0002_ses-01_acq-VBM6minSENSE_rec-TOC_run-1_T1w
    │       ├── label
    │       ├── mri
    │       ├── scripts
    │       ├── stats
    │       ├── surf
    │       ├── tmp
    │       ├── touch
    │       └── trash

In case you don't have any NIfTI files that have undergone the `recon-all` operation, or if you wish to run `recon-all` again, simply press ENTER when prompted.


7. Specifying the Number of Threads for the Pipeline
----------------------------------------------------------

During the script execution, you will be asked to specify the number of threads that the pipeline should use. This number determines how many NIfTI files can be processed concurrently. 

Keep the following in mind:

- The number of threads should ideally not exceed the number of cores available on your system.
- If you are unsure about the number of cores your system has, it's safe to specify 1.

For instance, if your system has 4 cores, you might enter:

.. code-block:: bash

    Enter the number of threads: 4

If you're unsure, you can simply enter 1:

.. code-block:: bash

    Enter the number of threads: 1


8. Launching the Pipeline
----------------------------

Upon successful configuration, the pipeline will commence its operations. It runs in two main workflows:

**1. Preprocessing Workflow**
^^^^^^^^^^^^^^^^^^^^^^

The Preprocessing Workflow performs the following tasks:

- Execution of `recon-all` command: This applies to all NIfTI files that haven't been processed with this command, those processed with FreeSurfer versions older than 7.1.1, or those that encountered errors during processing.
- Execution of `run_samseg` command: This applies to all NIfTI files. The output of this operation is stored in a `samseg` directory within the `enigma_ocd` directory.
- Quality Control (QC) Statistics: Various QC statistics are collected and stored.

**2. Morphometric Statistics Workflow**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Morphometric Statistics Workflow performs the following tasks:

- Computation of Cortical Region Statistics: Area, volume, thickness, intrinsic and extrinsic curvatures, and sulcal depth statistics are computed for cortical regions.
- Computation of Subcortical Region Statistics: Area and volume statistics are calculated for subcortical regions.


9. Reviewing and Sharing the Pipeline Output
--------------------------------------------------

Upon completion of the pipeline, an `enigma-ocd` folder will be generated in your current directory. This folder contains two key items:

- `imaging_transcriptomics.zip`: This zipped folder contains the output data from the pipeline.
- `report.html`: This HTML file presents a comprehensive report on the pipeline's operations and results.

To share these results, please send both `imaging_transcriptomics.zip` and `report.html` files to leonardo.saraiva@usp.br. You can use your preferred email client or web-based email service to do so.

