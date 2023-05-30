Running on a desktop server (ENIGMA-OCD)
============

This section will walk you through running the pipeline step by step, which is accomplished by \
executing a handler script that takes minimal input from the user and uses it to automatically \
run the pipeline. In addition, throughout this section, you will find references to items in \
section 3 that have detailed instructions on how to deal with possible issues. These references \
are pointed out alongside the body of the text, while their specific subject and location in \
section 3 are at the bottom of each page.

1. Download the handler script
-----
    i. Navigate to https://github.com/csleo95/morphometry/blob/main/handler_scripts/morphometry_handler.sh
    ii. Click on Download raw file

2. Execute the handler script
-----
    i. Open the terminal
    ii. Change directory to the directory where the handler script file was downloaded to. For instance, if it was downloaded to the Downloads directory, you can enter the following command:

cd ~/Downloads
    iii. Make the handler script file executable. To do this, enter the following command:

chmod +x morphometry_handler.sh
    iv. Execute the handler script file. To do this, enter the following command:

./morphometry_handler.sh
3. Execute the handler script
The output of the handler script will depend on the container platforms installed (or not) in the server:

Neither Docker, nor Singularity are installed: the script will print a message requesting that one of these should be installed in the system and will exit. In this case, follow this instruction and execute again the handler script.
Only Docker is installed: the script will look for the pipeline image among the local images. If it has not been downloaded yet, it will automatically download the image. The Docker image is 15.39 GB, so please make sure that there is enough room in Docker Desktop to download it. If it has already been downloaded, the handler script will proceed to the next step.
Only Singularity is installed: the script will look for the pipeline image in the current folder. If it has not been downloaded yet, it will automatically download the image. The pipeline Singularity image is 6.5 GB, so please make sure that there is enough room in the system to download it. If it has already been downloaded, the handler script will proceed to the next step.
Both Docker and Singularity are installed: the script will prompt the user to select one of these platforms to use for executing the pipeline. If you enter 1, Docker is selected, and the handler script will follow the steps described in the Only Docker is installed item above. If you enter 2, Singularity is selected, and the handler script will follow the steps described in the Only Singularity is installed item above.
4. Enter the full path to the directory containing the NIfTI files
The user will be prompted to enter the full path to the directory containing the NIfTI files of the T1 scans of the subjects. This directory can be located either in the user filesystem or in a mounted drive. In either case, it should be noted that the full path is required, without characters such as “~/’, nor environment variables. Accordingly, a full path would have a structure similar to the following:

1) Full path to directory with NIfTI files: /home/leocs/imgs/nifti
The directory with the NIfTI files can be structured in two formats. It can contain only the NIfTI files of the T1 scans, as in the following example:

├── nifti
│   ├── sub0001_ses-01_acq-VBM6minSENSE_rec-TOC_run-1_T1w.nii.gz
│   ├── sub0002_ses-01_acq-VBM6minSENSE_rec-TOC_run-1_T1w.nii.gz
Alternatively, it can contain the NIfTI files of the T1 scans in valid BIDS format, as in the following example (the ses directory is optional):

├── nifti
│   └── sub-0001
│       └── ses-01
│       	 └── anat
│       	     ├── sub-0001_ses-01_acq-VBMSENSE_rec-TOC_run-1_T1w.nii.gz
│   └── sub-0002
│       └── ses-01
│       	 └── anat
│       	     ├── sub-0002_ses-01_acq-VBMSENSE_rec-TOC_run-1_T1w.nii.gz

5. Enter the full path to the directory containing freesurfer’s recon-all output
The user will be prompted to enter the full path to the directory containing output from the freesurfer’s recon-all command for some / all NIfTI files located in the directory with the NIfTI files. This directory can also be located in the user filesystem or in a mounted drive; and the path requirements are the same as above. In addition, it should be noted that the directories within this directory should have the same naming as their corresponding NIfTI files (without the file extensions, of course). Accordingly, considering that the provided directory with NIfTI files was any of the examples above, this directory should have the following structure and naming:

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
If either there are no NIfTI files that have undergone recon-all, or you want to run recon-all again on them, just press ENTER when prompted to enter the path to this directory.

6. Enter the number of threads to be used
The user will be prompted to enter the number of threads to be used in the pipeline. This does not affect the output of the pipeline per se. But it will make the pipeline run faster, as the number of threads corresponds to the number of NIfTI files processed simultaneously. If you are unsure on the number of cores available on your system, just enter 1.

7. Pipeline starts running!
The pipeline is comprised of this two workflows:

Preproc workflow
Runs recon-all for all the NIfTI files that were not previously processed with this command, processed with freesurfer versions < 7.1.1, or processed with errors.
Runs run_samseg for all the NIfTI files. The output of this command will be stored in a directory named samseg inside the enigma_ocd directory.
Gathers qc statistics.
Morphometric stats workflow
Computes area, volume, thickness, intrinsic and extrinsic curvatures, and sulcal depth statistics for cortical regions.
Computes area, and volume statistics for subcortical regions.
Gathers qc statistics.
8. Check and send the output
After running the pipeline, please check all the files in the directory enigma-ocd/morhometric_stats to leonardo.saraiva@usp.br.
