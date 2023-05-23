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

if [ ! $(type -P docker) ] && [ ! $(type -P singularity) ]; then
    echo -e $LIGHTRED"neither docker nor singularity are installed in the system"
    echo -e $LIGHTRED"please install one of them and re-run the script"
    exit 0
fi

tput sgr0

if [ ! $(type -P docker) ] && [ $(type -P singularity) ]; then

    if [ ! $(ls | grep "^morphometry.*") ]; then
        echo -e $NC"$(singularity --version) is installed in the system"
        echo -e $NC"Building pipeline image"
        echo ""

        if [ $(echo $(singularity --version) | grep -o "3\.[0-9]" | wc -l) -gt 0 ]; then

            singularity build morphometry.sif docker://csleo/morphometry

        elif [ $(echo $(singularity --version) | grep -o "2\.3" | wc -l) -gt 0 ]; then

            docker run --privileged -t --rm \
                -v /var/run/docker.sock:/var/run/docker.sock \
                -v $(pwd):/output \
                singularityware/docker2singularity:v2.3 \
                --name morphometry csleo/morphometry
        
        elif [ $(echo $(singularity --version) | grep -o "2\.4" | wc -l) -gt 0 ]; then

            docker run --privileged -t --rm \
                -v /var/run/docker.sock:/var/run/docker.sock \
                -v $(pwd):/output \
                singularityware/docker2singularity:v2.4 \
                --name morphometry csleo/morphometry
        
        elif [ $(echo $(singularity --version) | grep -o "2\.5" | wc -l) -gt 0 ]; then

            docker run --privileged -t --rm \
                -v /var/run/docker.sock:/var/run/docker.sock \
                -v $(pwd):/output \
                singularityware/docker2singularity:v2.5 \
                --name morphometry csleo/morphometry

        elif [ $(echo $(singularity --version) | grep -o "2\.6" | wc -l) -gt 0 ]; then

            docker run --privileged -t --rm \
                -v /var/run/docker.sock:/var/run/docker.sock \
                -v $(pwd):/output \
                singularityware/docker2singularity:v2.6 \
                --name morphometry csleo/morphometry

        fi

    else
        echo -e $NC"$(singularity --version) is installed in the system"
        echo -e $NC"Pipeline image already downloaded and in the current directory"
    fi

    soft=2

fi

if [ $(type -P docker) ] && [ ! $(type -P singularity) ]; then

    if [ $(docker images | grep "morphometry" | wc -l) == 0 ]; then
        echo -e $NC"$(docker --version | cut -d , -f 1) is installed in the system"
        echo -e $NC"Downloading pipeline image from docker"
        echo ""
        docker pull csleo/morphometry
    else
        echo -e $NC"$(docker --version | cut -d , -f 1) is installed in the system"
        echo -e $NC"Pipeline image already downloaded"
    fi

    soft=1

fi

if [ $(type -P docker) ] && [ $(type -P singularity) ]; then

    echo "Both docker and singularity are installed in the system. Which one do you want to use?"
    read -p "$(echo -e $LIGHTBLUE"Enter [1] for docker or [2] for singularity: ${NC}"$RESET)" soft

    if [ $soft == 1 ]; then
        
        if [ $(docker images | grep "morphometry" | wc -l) == 0 ]; then
            echo -e $NC"$(docker --version | cut -d , -f 1) is installed in the system"
            echo -e $NC"Downloading pipeline image from docker"
            echo ""
            docker pull csleo/morphometry
        else
            echo -e $NC"$(docker --version | cut -d , -f 1) is installed in the system"
            echo -e $NC"Pipeline image already downloaded"
        fi

    fi

    if [ $soft == 2 ]; then
        
        if [ ! $(ls | grep "^morphometry.*$") ]; then
            echo -e $NC"$(singularity --version) is installed in the system"
            echo -e $NC"Building pipeline image"
            echo ""

            if [ $(echo $(singularity --version) | grep -o "3\.[0-9]" | wc -l) -gt 0 ]; then

                singularity build morphometry.sif docker://csleo/morphometry

            elif [ $(echo $(singularity --version) | grep -o "2\.3" | wc -l) -gt 0 ]; then

                docker run --privileged -t --rm \
                    -v /var/run/docker.sock:/var/run/docker.sock \
                    -v $(pwd):/output \
                    singularityware/docker2singularity:v2.3 \
                    --name morphometry csleo/morphometry
        
            elif [ $(echo $(singularity --version) | grep -o "2\.4" | wc -l) -gt 0 ]; then

                docker run --privileged -t --rm \
                    -v /var/run/docker.sock:/var/run/docker.sock \
                    -v $(pwd):/output \
                    singularityware/docker2singularity:v2.4 \
                    --name morphometry csleo/morphometry
        
            elif [ $(echo $(singularity --version) | grep -o "2\.5" | wc -l) -gt 0 ]; then

                docker run --privileged -t --rm \
                    -v /var/run/docker.sock:/var/run/docker.sock \
                    -v $(pwd):/output \
                    singularityware/docker2singularity:v2.5 \
                    --name morphometry csleo/morphometry


            elif [ $(echo $(singularity --version) | grep -o "2\.6" | wc -l) -gt 0 ]; then

                docker run --privileged -t --rm \
                    -v /var/run/docker.sock:/var/run/docker.sock \
                    -v $(pwd):/output \
                    singularityware/docker2singularity:v2.6 \
                    --name morphometry csleo/morphometry

            fi

        else

            echo -e $NC"$(singularity --version) is installed in the system"
            echo -e $NC"Pipeline image already downloaded and in the current directory"

        fi
    
    fi

fi

tput sgr0

echo ""
echo "Please enter the following arguments:"
read -p "$(echo -e ${LIGHTBLUE}"1) Full path to directory with NIfTI files: ${NC}"$RESET)" niftipath
read -p "$(echo -e ${LIGHTBLUE}"2) Full path to directory with recon-all output: ${NC}"$RESET)" reconpath
read -p "$(echo -e ${LIGHTBLUE}"3) Number of cores to be used: ${NC}"$RESET)" cores

tput sgr0

if [ ! -d enigma_ocd ]; then mkdir enigma_ocd; fi

if [ $soft == 1 ]; then
    
    if [ "$reconpath" ]; then

        (docker run -ti --rm --user $(id -u):0 \
            -v $niftipath:/nifti \
            -v $reconpath:/reconall \
            -v $(pwd)/enigma_ocd:/output \
            csleo/morphometry /nifti /output --recon-all-dir /reconall --work-dir /output --n-procs $cores 2>&1 | tee enigma_ocd/stdout.log) 3>&1 1>&2 2>&3 | tee enigma_ocd/stderr.log

    else

        (docker run -ti --rm --user $(id -u):0 \
            -v $niftipath:/nifti \
            -v $(pwd)/enigma_ocd:/output \
            csleo/morphometry /nifti /output --work-dir /output --n-procs $cores 2>&1 | tee enigma_ocd/stdout.log) 3>&1 1>&2 2>&3 | tee enigma_ocd/stderr.log
            
    fi

fi

if [ $soft == 2 ]; then

    if [ "$reconpath" ]; then

        eval "(singularity run --cleanenv --bind $(pwd),$niftipath,$reconpath $(ls | grep "^morphometry.*") \
        $niftipath $(pwd)/enigma_ocd --recon-all-dir $reconpath --n-procs $cores -g 2>&1 | tee enigma_ocd/stdout.log) 3>&1 1>&2 2>&3 | tee enigma_ocd/stderr.log"

    else

        eval "(singularity run --cleanenv --bind $(pwd),$niftipath,$reconpath $(ls | grep "^morphometry.*") \
        $niftipath $(pwd)/enigma_ocd --n-procs $cores -g 2>&1 | tee enigma_ocd/stdout.log) 3>&1 1>&2 2>&3 | tee enigma_ocd/stderr.log"

    fi

fi




