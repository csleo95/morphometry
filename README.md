# morphometry
_morphometry_ is an easy-to-use pipeline for preprocessing T1w-MRI data and computing several morphometric statistics.

## About

This is the manual for running the data processing pipeline of the ENIGMA-OCD Imaging Transcriptomics project. This pipeline performs an automated sequence of steps that include preprocessing NIfTI files with freesurfer’s recon-all (if required); computing morphometric features for subparcellations of the Desikan-Killiany (DK) atlas; using freesurfer’s run-samseg to compute morphometric statistics for subcortical structures. It should be noted that the pipeline builds upon scripts developed by Rafael Romero-Garcia et al [1]. Containerized versions of the pipeline have been developed both in the Docker and Singularity platforms for reproducibility of results and flexibility of use. 			

Overall, the running of the pipeline comprises the following steps:

1. Download a handler script.
2. Execute the handler script from terminal, which will interactively prompt the user for the following information to automatically run the pipeline:
   1. Whether Docker or Singularity will be used to run the pipeline (if just one of them is installed in the server, the handler script will automatically use it to run the pipeline);
   2. The full path to a directory containing NIfTI files;
   3. The full path to a directory containing freesurfer’s recon-all output for some / all the NIfTI files in the above directory (optional);
   4. The number of threads to be used in the pipeline.
3. Check the output files generated from the pipeline.

The instructions on this manual are divided into two main sections. The next sections have step-by-step instructions on the abovementioned steps to run the pipeline. In addition, this section has instructions on how to share the morphometric statistics generated by it. Section 3 has instructions on how to deal with potential issues that might arise when running the pipeline. We deeply appreciate your contribution to this project and hope you have a great experience running its data processing pipeline! If you have any questions, please contact leonardo.saraiva@usp.br. 

## Running the Pipeline on a Desktop Server

This section will walk you through running the pipeline step by step, which is accomplished by executing a handler script that takes minimal input from the user and uses it to automatically run the pipeline. In addition, throughout this section, you will find references to items in section 3 that have detailed instructions on how to deal with possible issues. These references are pointed out alongside the body of the text, while their specific subject and location in section 3 are at the bottom of each page.

### 1. Download the handler script ###

&nbsp;&nbsp;&nbsp;&nbsp;i. Navigate to https://github.com/csleo95/morphometry/blob/main/handler_scripts/morphometry_handler.sh <br>
&nbsp;&nbsp;&nbsp;&nbsp;ii. Click on Download raw file <br>

### 2. Execute the handler script ###

&nbsp;&nbsp;&nbsp;&nbsp;i. Open the terminal <br>
&nbsp;&nbsp;&nbsp;&nbsp;ii. Change directory to the directory where the handler script file was downloaded to. For instance, if it was downloaded to the Downloads directory, you can enter the following command: <br>
```(bash)
cd ~/Downloads
````
&nbsp;&nbsp;&nbsp;&nbsp;iii. Make the handler script file executable. To do this, enter the following command: <br>
```(bash)
chmod +x morphometry_handler.sh
````
&nbsp;&nbsp;&nbsp;&nbsp;iv. Execute the handler script file. To do this, enter the following command: <br>
```(bash)
./morphometry_handler.sh
````

### 3. Execute the handler script  <br>
The output of the handler script will depend on the container platforms installed (or not) in the server:
- _Neither Docker, nor Singularity are installed:_ the script will print a message requesting that one of these should be installed in the system and will exit. In this case, follow this instruction and execute again the handler script. 
- _Only Docker is installed:_ the script will look for the pipeline image among the local images. If it has not been downloaded yet, it will automatically download the image. The Docker image is 15.39 GB, so please make sure that there is enough room in Docker Desktop to download it. If it has already been downloaded, the handler script will proceed to the next step. 
- _Only Singularity is installed:_ the script will look for the pipeline image in the current folder. If it has not been downloaded yet, it will automatically download the image. The pipeline Singularity image is 6.5 GB, so please make sure that there is enough room in the system to download it. If it has already been downloaded, the handler script will proceed to the next step.
- _Both Docker and Singularity are installed:_ the script will prompt the user to select one of these platforms to use for executing the pipeline. If you enter 1, Docker is selected, and the handler script will follow the steps described in the Only Docker is installed item above. If you enter 2, Singularity is selected, and the handler script will follow the steps described in the Only Singularity is installed item above. 

### 4. Enter the full path to the directory containing the NIfTI files  <br>
The user will be prompted to enter the full path to the directory containing the NIfTI files of the T1 scans of the subjects. This directory can be located either in the user filesystem or in a mounted drive. In either case, it should be noted that the full path is required, without characters such as “~/’, nor environment variables. Accordingly, a full path would have a structure similar to the following: 
```(bash)
1) Full path to directory with NIfTI files: /home/leocs/imgs/nifti
```
The directory with the NIfTI files can be structured in two formats. It can contain only the NIfTI files of the T1 scans, as in the following example:
```(bash)
├── nifti
│   ├── sub0001_ses-01_acq-VBM6minSENSE_rec-TOC_run-1_T1w.nii.gz
│   ├── sub0002_ses-01_acq-VBM6minSENSE_rec-TOC_run-1_T1w.nii.gz
```
Alternatively, it can contain the NIfTI files of the T1 scans in valid BIDS format, as in the following example (the ses directory is optional):
```(bash)
├── nifti
│   └── sub-0001
│       └── ses-01
│       	 └── anat
│       	     ├── sub-0001_ses-01_acq-VBMSENSE_rec-TOC_run-1_T1w.nii.gz
│   └── sub-0002
│       └── ses-01
│       	 └── anat
│       	     ├── sub-0002_ses-01_acq-VBMSENSE_rec-TOC_run-1_T1w.nii.gz

```

### 5. Enter the full path to the directory containing freesurfer’s recon-all output  <br>
The user will be prompted to enter the full path to the directory containing output from the freesurfer’s recon-all command for some / all NIfTI files located in the directory with the NIfTI files. This directory can also be located in the user filesystem or in a mounted drive; and the path requirements are the same as above. In addition, it should be noted that the directories within this directory should have the same naming as their corresponding NIfTI files (without the file extensions, of course). Accordingly, considering that the provided directory with NIfTI files was any of the examples above, this directory should have the following structure and naming: 
```(bash)
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
```
If either there are no NIfTI files that have undergone recon-all, or you want to run recon-all again on them, just press ENTER when prompted to enter the path to this directory. 

### 6. Enter the number of threads to be used  <br>
The user will be prompted to enter the number of threads to be used in the pipeline. This does not affect the output of the pipeline per se. But it will make the pipeline run faster, as the number of threads corresponds to the number of NIfTI files processed simultaneously. If you are unsure on the number of cores available on your system, just enter 1. 

### 7. Pipeline starts running!  <br>
The pipeline is comprised of this two workflows:
- _Preproc workflow_
  - Runs recon-all for all the NIfTI files that were not previously processed with this command, processed with freesurfer versions < 7.1.1, or processed with errors. 
  - Runs run_samseg for all the NIfTI files. The output of this command will be stored in a directory named `samseg` inside the `enigma_ocd` directory.
  - Gathers qc statistics.
- _Morphometric stats workflow_
  - Computes area, volume, thickness, intrinsic and extrinsic curvatures, and sulcal depth statistics for cortical regions. 
  - Computes area, and volume statistics for subcortical regions. 
  - Gathers qc statistics.
  
### 8. Check and send the output  <br>
After running the pipeline, please check all the files in the directory enigma-ocd/morhometric_stats to leonardo.saraiva@usp.br.


## Running the Pipeline on a Slurm Server

This section will walk you through running the pipeline on a slurm server step by step, which is accomplished by executing a handler script that takes minimal input from the user and uses it to automatically run the pipeline. 

### 1. Download the handler script ###

&nbsp;&nbsp;&nbsp;&nbsp;i. Navigate to https://github.com/csleo95/morphometry/blob/main/handler_scripts/morphometry_handler_slurm.sh <br>
&nbsp;&nbsp;&nbsp;&nbsp;ii. Click on Download raw file <br>

### 2. Execute the handler script ###

&nbsp;&nbsp;&nbsp;&nbsp;i. Open the terminal <br>
&nbsp;&nbsp;&nbsp;&nbsp;iii. Make the handler script file executable. To do this, enter the following command: <br>
```(bash)
chmod +x morphometry_handler_slurm.sh
````
&nbsp;&nbsp;&nbsp;&nbsp;iv. Execute the handler script file. To do this, enter the following command: <br>
```(bash)
./morphometry_handler_slurm.sh
````

### 3. Enter the #SBATCH directives to build the pipeline image <br>
The handler script you ask for the #SBATCH directives (e.g., `#SBATCH --job-name=morphometry-job`) that will be appended to a sbatch script to build the Singularity / Apptainer image of the pipeline. After writing each directive, you should press enter and add the next one. After adding all directives enter `q` and press enter. At this point, the sbatch script will executed. 

### 4. Enter the #SBATCH directives to run the pipeline <br>
As above, the handler script you ask for the #SBATCH directives that will be appended to a sbatch script to run the image of the pipeline. After writing each directive, you should press enter and add the next one. After adding all directives enter `q` and press enter. At this point, the sbatch script will executed. 

### 5. Enter the full path to the directory containing the NIfTI files  <br>
The user will be prompted to enter the full path to the directory containing the NIfTI files of the T1 scans of the subjects; the the full path to the directory containing freesurfer’s recon-all output (if available); and the number of threads to be used by the pipeline. After entering this information, the sbatch script for running the pipeline will be automatically submitted. 

### 6. Pipeline starts running!  <br>
The pipeline is comprised of this two workflows:
- _Preproc workflow_
  - Runs recon-all for all the NIfTI files that were not previously processed with this command, processed with freesurfer versions < 7.1.1, or processed with errors. 
  - Runs run_samseg for all the NIfTI files. The output of this command will be stored in a directory named `samseg` inside the `enigma_ocd` directory.
  - Gathers qc statistics.
- _Morphometric stats workflow_
  - Computes area, volume, thickness, intrinsic and extrinsic curvatures, and sulcal depth statistics for cortical regions. 
  - Computes area, and volume statistics for subcortical regions. 
  - Gathers qc statistics.
  
### 7. Check and send the output  <br>
After running the pipeline, please check all the files in the directory enigma-ocd/morhometric_stats to leonardo.saraiva@usp.br.


## Troubleshooting

### My server does not have internet access ###
If your server does not have internet access, you can still run this pipeline by downloading its dependencies in another server (e.g., your personal computer) with internet access, and afterwards transferring them to your server. However, your server must have Docker and/or Singularity installed so you can run this pipeline. Three workarounds are outlined below depending on whether you will use Docker or Singularity in your server.

**•	Using Docker:** <br>
You will need to have Docker installed on the other server with internet access. In this case, you can follow the steps below: <br>
i. Download the handler scripts in the server with internet access. <br>
ii. Run the commands below on the server with internet access to download the pipeline image, and convert it to a tar file: <br>
```(bash)
docker pull csleo/img_trs
docker save --output img_trs.tar csleo/img_trs
```
iii. Transfer the handler script file (run_img_trs.sh) and the tar file of the pipeline (img_trs.tar) to your server without internet connection <br>
iv. In your server without internet connection, run the command below in the folder where the tar file of the pipeline (img_trs.tar) is located:
```(bash)
docker load -i img_trs.tar
```
v. In your server without internet connection, you can follow step 2.2 onwards to run the pipeline.

**•	Using Singularity (version ≥ 3.0)** <br>
You will need to have Singularity installed on the other server with internet access. In this case, you can follow the steps below: <br>
i. Download the handler scripts in the server with internet access. <br>
ii. Run the command below on the server with internet access to build the pipeline image: <br>
```(bash)
singularity build img_trs.sif docker://csleo/img_trs
```
iii. Transfer the handler script file (run_img_trs.sh) and the SIF file of the pipeline (img_trs.sif) to your server without internet connection <br>
iv. In your server without an internet connection, you can follow step 2.2 onwards to run the pipeline. Make sure the img_trs.sif file is in the directory from which you are executing the handler script.

**•	Using Singularity (version < 3.0)** <br>
You will need to have Docker installed on the other server with internet access. In this case, you can follow the steps below: <br>
i. Download the handler scripts in the server with internet access. <br>
ii. Run the command below on the server with internet access to download the pipeline image (note that you have to substitute the <version> by 2.3, 2.4, 2.5 or 2.6 depending on the version of Singularity that is installed on your server): <br>
```(bash)
docker run --privileged -t --rm \
           -v /var/run/docker.sock:/var/run/docker.sock \
           -v $(pwd):/output \
           singularityware/docker2singularity:v<version> \
           --name img_trs csleo/img_trs
```
iii. Transfer the handler script file (run_img_trs.sh) and the SIMG file of the pipeline (img_trs.simg)  to your server without internet connection <br>
iv. In your server without an internet connection, you can follow step 2.2 onwards to run the pipeline. Make sure the img_trs.simg file is in the directory from which you are executing the handler script.

### Neither Docker, nor Singularity are installed in the system ###
If neither container platform is installed in the system, please install one of them. You can do this by following the instructions in one of the links below (you will need root access to go through them): <br>
•	Latest Docker version on Linux:  https://docs.docker.com/desktop/install/linux-install/test <br>
•	Latest Docker version on Mac: https://docs.docker.com/desktop/install/mac-install/ <br>
•	Latest Docker version on Windows: https://docs.docker.com/desktop/install/windows-install/ <br>
•	Latest Singularity version on Linux, Mac, or Windows: https://docs.sylabs.io/guides/3.10/user-guide/quick_start.html <br>

### Docker daemon is not running ###
If the Docker daemon is not running, the handler script will output a message of this sort: <br>
```(bash)
Cannot connect to the Docker daemon at unix:///home/leocs/.docker/desktop/docker.sock. Is the docker daemon running?
```
There are two ways to fix this issue:
•	You can search Docker Desktop on the Applications menu and open it. <br>
•	Alternatively, you can run the following command on the terminal: <br>
```(bash)
systemctl –user start docker-desktop
```

### Not enough available hard disk space in Docker to download the pipeline image ###
If there is not enough available space in the hard disk allocated to Docker, the handler script will print a message of this sort: <br>
```(bash)
No space left on the device
```
There are three ways to increase the available hard disk space in Docker Desktop (you can try a combination of more than one): <br>
   
**•	Delete local images** <br>
There are two ways of doing this: <br>
&nbsp;&nbsp;&nbsp;&nbsp;-	Open Docker Desktop and delete local images by clicking on the three dots on the left of an image’s row and then clicking on remove. <br>
&nbsp;&nbsp;&nbsp;&nbsp;-	Alternatively, enter the command `docker image rm [image name]`, for instance: <br> 
```(bash)
docker image rm hello-world
```
**•	Delete unused data** <br>
&nbsp;&nbsp;&nbsp;&nbsp;-	 Enter the following command to delete unused containers, networks, images: <br>
```(bash)
docker system prune
```   
**•	Increase the available disk space allocated to Docker Desktop:** <br>
&nbsp;&nbsp;&nbsp;&nbsp;-	 Open Docker Desktop and click on the Settings button <br>
&nbsp;&nbsp;&nbsp;&nbsp;-	 Click on the Resources button <br>
&nbsp;&nbsp;&nbsp;&nbsp;-	 Increase the Disk image size of Docker Desktop <br>

### Server with Singularity version < 3.0 ###
In this case, the handler script will use the docker2singularity utility to download the pipeline image from Docker Hub and convert it to a format compatible with the Singularity version on the server. However, for this to work, Docker must be installed on the server. If it is not installed on your server, please go through the steps 3.1.2.c to 3.1.4.c to download the pipeline image from another server with Docker installed and then transfer the image to your server.

### Docker does not recognize the path of my directories ###
If are using Docker to run the pipeline and the directory with NIfTI files and/or the directory with freesurfer’s recon-all output are located in paths not shared with Docker, an error message of this sort will be print:
```(bash)
docker: Error response from daemon: Mounts denied: 
The path /media/leocs/leo.hd/DRIVE/ img_trs not shared from the host and is not known to Docker.
```   
To deal with this, go to docker desktop menu, and click on the File sharing button and add the path(s) to the directory with NIfTI files and/or the directory with freesurfer’s recon-all.
