===========================
Running on a Slurm Server (ENIGMA-OCD)
===========================

This guide provides step-by-step instructions for running the pipeline in a slurm via a handler script. It requires minimal user input and automatically manages the pipeline. 

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

4. Enter the Full Path to the Directory Containing the NIfTI Files
------------------------------------------------------------------

The user needs to provide the full path to the directory containing the NIfTI files of the T1 scans. The directory can be in the user filesystem or a mounted drive. The full path is required, without characters such as "~/", nor environment variables.

    Example of full path:

    .. code-block:: bash

        /home/leocs/imgs/nifti

The NIfTI files can be structured in two ways: either only containing the T1 scans or containing the T1 scans in valid BIDS format.

    Examples:

    .. code-block:: bash

        ├── nifti
        │   ├── sub0001_ses-01_acq-VBM6minSENSE_rec-TOC_run-1_T1w.nii.gz
        │   ├── sub0002_ses-01_acq-VBM6minSENSE_rec-TOC_run-1_T1w.nii.gz

        ├── nifti
        │   └── sub-0001
        │       └── ses-01
        │       	└── anat
        │       	    ├── sub-0001_ses-01_acq-VBMSENSE_rec-TOC_run-1_T1w.nii.gz
        │   └── sub-0002
        │       └── ses-01
        │       	└── anat
        │       	    ├── sub-0002_ses-01_acq-VBMSENSE_rec-TOC_run-1_T1w.nii.gz

5. Enter the Full Path to the Directory Containing Freesurfer’s recon-all Output
-------------------------------------------------------------------------------

The user needs to provide the full path to the directory containing the output from Freesurfer’s recon-all command. The directories within this directory should have the same naming as their corresponding NIfTI files (without the file extensions).

Example:

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

If there are no NIfTI files that have undergone recon-all, or if you want to run recon-all again, just press ENTER when prompted.

6. Enter the Number of Threads to be Used
-----------------------------------------

The user will be prompted to enter the number of threads to be used in the pipeline. This number corresponds to the number of NIfTI files processed simultaneously. If unsure of the number of cores available on your system, enter 1.

7. Pipeline Starts Running!
----------------------------

The pipeline runs in two main workflows:

Preprocessing Workflow
^^^^^^^^^^^^^^^^^^^^^^

This workflow does the following:

- Runs `recon-all` for all the NIfTI files that were not previously processed with this command, processed with freesurfer versions less than 7.1.1, or processed with errors.
- Runs `run_samseg` for all the NIfTI files. The output of this command will be stored in a directory named `samseg` inside the `enigma_ocd` directory.
- Gathers quality control (QC) statistics.

Morphometric Statistics Workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This workflow does the following:

- Computes area, volume, thickness, intrinsic and extrinsic curvatures, and sulcal depth statistics for cortical regions.
- Computes area, and volume statistics for subcortical regions.
- Gathers QC statistics.

8. Check and Send the Output
----------------------------

After running the pipeline, please check all the files in the directory `enigma-ocd/morhometric_stats` and send them to leonardo.saraiva@usp.br.

