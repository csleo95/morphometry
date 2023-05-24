#!/bin/bash

NC='\033[0m'
LIGHTRED="\033[1;31m"
LIGHTBLUE="\033[1;34m"

echo -e $LIGHTBLUE"    ___   __   _   _   _____   _    _   _____        _____   ____   ____ "
echo -e $LIGHTBLUE"   |  _| |  \ | | | | |  ___| | \  / | |  _  |  __  |  _  | |  __| |  _ \ "
echo -e $LIGHTBLUE"   | \   |   \| | | | | | __  |  \/  | | |_| | |__| | | | | | |    | | \ \ "
echo -e $LIGHTBLUE"   | /_  | |\   | | | | |_\ \ | |\/| | | | | |      | |_| | | |__  | |_/ / "
echo -e $LIGHTBLUE"   |___| |_| \__| |_| |_____| |_|  |_| |_| |_|      |_____| |____| |____/ "
      
echo ""
echo -e $LIGHTBLUE"                 *** Imaging Transcriptomics Project ***"
echo ""
echo -e $NC"     $USER, welcome and many thanks for contributing to this project!!"
echo ""
echo ""

# Define the name of the Singularity image
image_name="morphometry.sif"

# Check if the image file exists in the current directory
if [ ! -f "$image_name" ]; then
    echo -e "Image $image_name does not exist in the current directory, so we will have to build it\n\
For this, we are going to write a build_image.sh script and run it with sbatch \n"

    script_name_build="build_image.sh"

    # Check if the build_image.sh file already exists
    if [ -f "$script_name_build" ]; then
        echo "The $script_name_build script already exists."
        read -p "Do you want to use it (y) or generate a new one (n)? " use_existing
    fi

    if [ ! -f "$script_name_build" ] || [ "$use_existing" = "N" ] || [ "$use_existing" = "n" ]; then
        # Delete the old script file
        if [ -f $script_name_build ]; then rm -f $script_name_build; fi

        # Collect sbatch flags iteratively
        echo "Enter the #SBATCH flags for building the $script_name_build script. Press 'q' when finished."
        sbatch_flags_build=()
        while true; do
            read flag
            if [ "$flag" = "q" ]; then
                break
            else
                sbatch_flags_build+=("$flag")
            fi
        done

        # Generate a sbatch script
        echo "#!/bin/bash" > $script_name_build
        for flag in "${sbatch_flags_build[@]}"; do
            echo "#SBATCH $flag" >> $script_name_build
        done
        echo "module load singularity" >> $script_name_build
        echo "singularity build $image_name docker://csleo/morphometry:latest" >> $script_name_build

    fi

    # Execute the sbatch script
    chmod +x $script_name_build
    jobid=$(sbatch $script_name_build | awk '{print $4}')

    # Define array for loading animation
    loading_anim=("." ".." "...")

    # Counter for animation state
    counter=0

    # Check job status
    squeue -j $jobid | grep -q $jobid
    job_status=$?

    # Wait for the job to complete
    while [ $job_status -eq 0 ]; do
        echo -ne "Job $jobid is not yet complete. Waiting${loading_anim[$counter]}\r"
        sleep 1
        # Reset counter if it reaches the length of loading_anim
        if [ $counter -ge ${#loading_anim[@]} ]; then
            counter=0
        fi
        let counter++
        # Recheck job status
        squeue -j $jobid | grep -q $jobid
        job_status=$?
    done

    echo -e "Job $jobid has completed.\n"

else
    echo "Image $image_name exists."
fi

# Check if the image file exists in the current directory
if [ ! -f "$image_name" ]; then
    echo "The image $image_name does not exist in the current directory."
    echo "Please inspect the slurm-$jobid.out file for any errors."
    exit 1
fi

# Define the name of the Singularity execution script
script_name_run="run_image.sh"

# Check if the run_image.sh file already exists
if [ -f "$script_name_run" ]; then
    echo "The $script_name_run script already exists."
    read -p "Do you want to use it (y) or generate a new one (n)? " use_existing
fi

if [ ! -f "$script_name_run" ] || [ "$use_existing" = "N" ] || [ "$use_existing" = "n" ]; then
    # Delete the old script file
    if [ -f $script_name_run ]; then rm -f $script_name_run; fi

    # Collect sbatch flags iteratively
    echo "Enter the #SBATCH flags for building the $script_name_run script. Press 'q' when finished."
    sbatch_flags_run=()
    while true; do
        read flag
        if [ "$flag" = "q" ]; then
            break
        else
            sbatch_flags_run+=("$flag")
        fi
    done

    # Ask for the path to the NIfTi files directory
    read -p "Enter the path to the directory containing the NIfTi files: " nifti_dir

    # Ask for the directory of previous recon-all runs, if any
    read -p "Enter the directory of previous recon-all runs (press enter if there isn't): " recon_dir

    # Ask for the number of processors to use
    read -p "Enter the number of processors to use for the analysis: " n_procs

    # Generate a sbatch script
    echo "#!/bin/bash" > $script_name_run
    for flag in "${sbatch_flags_run[@]}"; do
        echo "#SBATCH $flag" >> $script_name_run
    done
    echo "mkdir -p enigma_ocd" >> $script_name_run
    if [ -z "$recon_dir" ]; then
        echo "singularity run --cleanenv --bind $nifti_dir:/nifti_dir,$(pwd)/enigma_ocd:/enigma_ocd $image_name \
              /nifti_dir /enigma_ocd --work-dir /enigma_ocd --n-procs $n_procs" >> $script_name_run
    else
        echo "singularity run --cleanenv --bind $nifti_dir:/nifti_dir,$(pwd)/enigma_ocd:/enigma_ocd,$recon_dir:/recon_dir $image_name \
              /nifti_dir /enigma_ocd --work-dir /enigma_ocd --recon-all-dir /recon_dir --n-procs $n_procs" >> $script_name_run
    fi

fi

# Execute the sbatch script
chmod +x $script_name_run
sbatch $script_name_run


