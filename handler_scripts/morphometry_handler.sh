#!/bin/bash

echo -e "\033[1;34m    ___   __   _   _   _____   _    _   _____        _____   ____   ____ "
echo -e "\033[1;34m   |  _| |  \ | | | | |  ___| | \  / | |  _  |  __  |  _  | |  __| |  _ \ "
echo -e "\033[1;34m   | \   |   \| | | | | | __  |  \/  | | |_| | |__| | | | | | |    | | \ \ "
echo -e "\033[1;34m   | /_  | |\   | | | | |_\ \ | |\/| | | | | |      | |_| | | |__  | |_/ / "
echo -e "\033[1;34m   |___| |_| \__| |_| |_____| |_|  |_| |_| |_|      |_____| |____| |____/ "
      
echo ""
echo -e "\033[1;34m                 *** Imaging Transcriptomics Project ***"
echo ""
echo -e "\033[0m    $USER, welcome and many thanks for contributing to this project!!"
echo ""
echo ""


if [ ! $(type -P docker) ] && [ ! $(type -P singularity) ]; then
    echo -e "\033[1;31mneither docker nor singularity are installed in the system"
    echo -e "\033[1;31mplease install one of them and re-run the script"
    exit 0
fi

tput sgr0

if [ ! $(type -P docker) ] && [ $(type -P singularity) ]; then

    if [ ! $(ls | grep "^morphometry\.0\.1\.\(sif\|simg\)") ]; then
        echo -e "\033[1;34m[note]\033[0m $(singularity --version) is installed in the system"
        echo -e "\033[1;34m[note]\033[0m Building pipeline image"
        echo ""

        while true; do
            if [ $(echo $(singularity --version) | grep -o "3\.[0-9]" | wc -l) -gt 0 ]; then
                singularity build morphometry.0.1.sif docker://csleo/morphometry:v0.1
            elif [ $(echo $(singularity --version) | grep -o "2\.3" | wc -l) -gt 0 ]; then
                docker run --privileged -t --rm \
                    -v /var/run/docker.sock:/var/run/docker.sock \
                    -v $(pwd):/output \
                    singularityware/docker2singularity:v2.3 \
                    --name morphometry.0.1 csleo/morphometry:v0.1
            elif [ $(echo $(singularity --version) | grep -o "2\.4" | wc -l) -gt 0 ]; then
                docker run --privileged -t --rm \
                    -v /var/run/docker.sock:/var/run/docker.sock \
                    -v $(pwd):/output \
                    singularityware/docker2singularity:v2.4 \
                    --name morphometry.0.1 csleo/morphometry:v0.1
            elif [ $(echo $(singularity --version) | grep -o "2\.5" | wc -l) -gt 0 ]; then
                docker run --privileged -t --rm \
                    -v /var/run/docker.sock:/var/run/docker.sock \
                    -v $(pwd):/output \
                    singularityware/docker2singularity:v2.5 \
                    --name morphometry.0.1 csleo/morphometry:v0.1
            elif [ $(echo $(singularity --version) | grep -o "2\.6" | wc -l) -gt 0 ]; then
                docker run --privileged -t --rm \
                    -v /var/run/docker.sock:/var/run/docker.sock \
                    -v $(pwd):/output \
                    singularityware/docker2singularity:v2.6 \
                    --name morphometry.0.1 csleo/morphometry:v0.1
            fi

            if [ $? -eq 0 ]; then
                break
            else
                echo -e "\033[1;31m[prompt] The image was not downloaded successfully. Do you want to retry? (yes/no)\033[0m"
                read answer
                if [ "$answer" != "yes" ]; then
                    echo -e "\033[1;34m[note]\033[0m Exiting the script. Please check what went wrong.\033[0m"
                    exit 1
                fi
            fi
        done
    else
        echo -e "\033[1;34m[note]\033[0m $(singularity --version) is installed in the system"
        echo -e "\033[1;34m[note]\033[0m Pipeline image already downloaded and in the current directory"
    fi

    soft=2
fi

if [ $(type -P docker) ] && [ ! $(type -P singularity) ]; then

    while true; do
        if [ $(docker images | grep "morphometry" | grep "v0.1" | wc -l) == 0 ]; then
            echo -e "\033[1;34m[note]\033[0m $(docker --version | cut -d , -f 1) is installed in the system"
            echo -e "\033[1;34m[note]\033[0m Downloading pipeline image from docker"
            echo ""
            docker pull csleo/morphometry:v0.1
        else
            echo -e "\033[1;34m[note]\033[0m $(docker --version | cut -d , -f 1) is installed in the system"
            echo -e "\033[1;34m[note]\033[0m Pipeline image already downloaded"
            break
        fi

        if [ $? -eq 0 ]; then
            break
        else
            echo -e "\033[1;31m[prompt] The image was not downloaded successfully. Do you want to retry? (yes/no)\033[0m"
            read answer
            if [ "$answer" != "yes" ]; then
                echo -e "\033[1;34m[note]\033[0m Exiting the script. Please check what went wrong.\033[0m"
                exit 1
            fi
        fi
    done

    soft=1
fi


if [ $(type -P docker) ] && [ $(type -P singularity) ]; then

    echo -e "\033[1;34m[note]\033[0m Both $(docker --version | cut -d , -f 1) and $(singularity --version) are installed in the system. Which one do you want to use?"
    echo -e "\033[1;34m[prompt]\033[0m Enter [1] for docker or [2] for singularity: \c"
    read soft

    if [ $soft == 1 ]; then
        
        while true; do
            if [ $(docker images | grep "morphometry" | grep "v0.1" | wc -l) == 0 ]; then
                echo -e "\033[1;34m[note]\033[0m Downloading pipeline image from docker"
                echo ""
                docker pull csleo/morphometry:v0.1
            else
                echo -e "\033[1;34m[note]\033[0m Pipeline image already downloaded"
                break
            fi

            if [ $? -eq 0 ]; then
                break
            else
                echo -e "\033[1;31m[prompt] The image was not downloaded successfully. Do you want to retry? (yes/no)\033[0m"
                read answer
                if [ "$answer" != "yes" ]; then
                    echo -e "\033[1;34m[note]\033[0m Exiting the script. Please check what went wrong.\033[0m"
                    exit 1
                fi
            fi
        done

        soft=1

    fi

    if [ $soft == 2 ]; then
        
        if [ ! $(ls | grep "^morphometry\.0\.1\.\(sif\|simg\)") ]; then
            echo -e "\033[1;34m[note]\033[0m Building pipeline image"
            echo ""

            while true; do
                if [ $(echo $(singularity --version) | grep -o "3\.[0-9]" | wc -l) -gt 0 ]; then
                    singularity build morphometry.0.1.sif docker://csleo/morphometry:v0.1
                elif [ $(echo $(singularity --version) | grep -o "2\.3" | wc -l) -gt 0 ]; then
                    docker run --privileged -t --rm \
                        -v /var/run/docker.sock:/var/run/docker.sock \
                        -v $(pwd):/output \
                        singularityware/docker2singularity:v2.3 \
                        --name morphometry.0.1 csleo/morphometry:v0.1
                elif [ $(echo $(singularity --version) | grep -o "2\.4" | wc -l) -gt 0 ]; then
                    docker run --privileged -t --rm \
                        -v /var/run/docker.sock:/var/run/docker.sock \
                        -v $(pwd):/output \
                        singularityware/docker2singularity:v2.4 \
                        --name morphometry.0.1 csleo/morphometry:v0.1
                elif [ $(echo $(singularity --version) | grep -o "2\.5" | wc -l) -gt 0 ]; then
                    docker run --privileged -t --rm \
                        -v /var/run/docker.sock:/var/run/docker.sock \
                        -v $(pwd):/output \
                        singularityware/docker2singularity:v2.5 \
                        --name morphometry.0.1 csleo/morphometry:v0.1
                elif [ $(echo $(singularity --version) | grep -o "2\.6" | wc -l) -gt 0 ]; then
                    docker run --privileged -t --rm \
                        -v /var/run/docker.sock:/var/run/docker.sock \
                        -v $(pwd):/output \
                        singularityware/docker2singularity:v2.6 \
                        --name morphometry.0.1 csleo/morphometry:v0.1
                fi

                if [ $? -eq 0 ]; then
                    break
                else
                    echo -e "\033[1;31m[prompt] The image was not downloaded successfully. Do you want to retry? (yes/no)\033[0m"
                    read answer
                    if [ "$answer" != "yes" ]; then
                        echo -e "\033[1;34m[note]\033[0m Exiting the script. Please check what went wrong.\033[0m"
                        exit 1
                    fi
                fi
            done
        else
            echo -e "\033[1;34m[note]\033[0m $(singularity --version) is installed in the system"
            echo -e "\033[1;34m[note]\033[0m Pipeline image already downloaded and in the current directory"
        fi

        soft=2

    fi

fi

tput sgr0

nifti_dir=""
nifti_dir_structure=""

while true; do
    # Ask for the path to the NIfTi files directory if it's empty or needs to be reset
    if [[ -z "$nifti_dir" ]]; then
        echo -e "\033[1;34m[prompt]\033[0m Enter the absolute path to the directory containing the NIfTI files: \c"
        read nifti_dir
    fi
    
    # Check if the directory exists and the path is absolute
    if [[ "$nifti_dir" == /* ]] && [ -d "$nifti_dir" ]; then
        break
    else
        echo -e "\033[31mInvalid absolute path for the directory containing the NIfTI files. Please enter an absolute path and try again.\033[0m"
        nifti_dir=""
    fi
done

while true; do
    # Ask for the structure of the NIfTI files directory if it's empty or needs to be reset
    if [[ -z "$nifti_dir_structure" ]]; then
        echo -e "\033[1;34m[prompt]\033[0m Enter the structure of the directory containing the NIfTI files [raw or bids]: \c"
        read nifti_dir_structure
    fi

    # Check if the input is 'raw' or 'bids'
    if [[ "$nifti_dir_structure" == "raw" ]] || [[ "$nifti_dir_structure" == "bids" ]]; then
        if [[ "$nifti_dir_structure" == "bids" ]]; then
            # Check if at least one "sub-xxx" folder exists in the BIDS directory
            if ! ls -d "$nifti_dir"/sub-* >/dev/null 2>&1; then
                echo -e "\033[31mNo 'sub-xxx' folders detected in the BIDS directory.\033[0m"
                
                while true; do
                    # Ask if the user wants to proceed or set nifti_dir, nifti_dir_structure, or both
                    echo -e "\033[1;34m[prompt]\033[0m Do you want to proceed [p] or set nifti_dir [d], nifti_dir_structure [s], or both [b] again? \c"
                    read answer
                    
                    case "$answer" in
                        p|P)
                            break 2 ;;  # Break out of both inner and outer while loops
                        d|D)
                            while true; do
                                echo -e "\033[1;34m[prompt]\033[0m Enter the absolute path to the directory containing the NIfTi files: \c"
                                read nifti_dir
                            
                                # Check if the directory exists and the path is absolute
                                if [[ "$nifti_dir" == /* ]] && [ -d "$nifti_dir" ]; then
                                    break
                                else
                                    echo -e "\033[31mInvalid absolute path for the directory containing the NIfTi files. Please enter an absolute path and try again.\033[0m"
                                    nifti_dir=""
                                fi
                            done
                            break ;;  # Break out of inner while loop, restart the nifti_dir input
                        s|S)
                            while true; do
                                echo -e "\033[1;34m[prompt]\033[0m Enter the structure of the directory containing the NIfTI files [raw or bids]: \c"
                                read nifti_dir_structure
                            
                                # Check if the input is 'raw' or 'bids'
                                if [[ "$nifti_dir_structure" == "raw" ]] || [[ "$nifti_dir_structure" == "bids" ]]; then
                                    break
                                else
                                    echo -e "\033[31mInvalid input. Please enter 'raw' or 'bids'.\033[0m"
                                    nifti_dir_structure=""
                                fi
                            done
                            break ;;  # Break out of inner while loop, restart the nifti_dir_structure input
                        b|B)
                            while true; do
                                echo -e "\033[1;34m[prompt]\033[0m Enter the absolute path to the directory containing the NIfTi files: \c"
                                read nifti_dir
                            
                                # Check if the directory exists and the path is absolute
                                if [[ "$nifti_dir" == /* ]] && [ -d "$nifti_dir" ]; then
                                    break
                                else
                                    echo -e "\033[31mInvalid absolute path for the directory containing the NIfTi files. Please enter an absolute path and try again.\033[0m"
                                    nifti_dir=""
                                fi
                            done
                            
                            while true; do
                                echo -e "\033[1;34m[prompt]\033[0m Enter the structure of the directory containing the NIfTI files [raw or bids]: \c"
                                read nifti_dir_structure
                            
                                # Check if the input is 'raw' or 'bids'
                                if [[ "$nifti_dir_structure" == "raw" ]] || [[ "$nifti_dir_structure" == "bids" ]]; then
                                    break
                                else
                                    echo -e "\033[31mInvalid input. Please enter 'raw' or 'bids'.\033[0m"
                                    nifti_dir_structure=""
                                fi
                            done
                            break ;;  # Break out of inner while loop, restart both nifti_dir and nifti_dir_structure inputs
                        *)
                            echo -e "\033[31mInvalid input. Please enter 'p', 'd', 's', or 'b'.\033[0m" ;;
                    esac
                done
            else
                break
            fi
        elif [[ "$nifti_dir_structure" == "raw" ]]; then
            # Check if the directory has at least one .nii or .nii.gz file
            if ! ls "$nifti_dir"/*.nii >/dev/null 2>&1 && ! ls "$nifti_dir"/*.nii.gz >/dev/null 2>&1; then
                echo -e "\033[31mNo .nii or .nii.gz files detected in the raw directory.\033[0m"
                
                while true; do
                    # Ask if the user wants to proceed or set nifti_dir, nifti_dir_structure, or both
                    echo -e "\033[1;34m[prompt]\033[0m Do you want to proceed [p] or set nifti_dir [d], nifti_dir_structure [s], or both [b] again? \c"
                    read answer
                    
                    case "$answer" in
                        p|P)
                            break 2 ;;  # Break out of both inner and outer while loops
                        d|D)
                            while true; do
                                echo -e "\033[1;34m[prompt]\033[0m Enter the absolute path to the directory containing the NIfTi files: \c"
                                read nifti_dir
                            
                                # Check if the directory exists and the path is absolute
                                if [[ "$nifti_dir" == /* ]] && [ -d "$nifti_dir" ]; then
                                    break
                                else
                                    echo -e "\033[31mInvalid absolute path for the directory containing the NIfTi files. Please enter an absolute path and try again.\033[0m"
                                    nifti_dir=""
                                fi
                            done
                            break ;;  # Break out of inner while loop, restart the nifti_dir input
                        s|S)
                            while true; do
                                echo -e "\033[1;34m[prompt]\033[0m Enter the structure of the directory containing the NIfTI files [raw or bids]: \c"
                                read nifti_dir_structure
                            
                                # Check if the input is 'raw' or 'bids'
                                if [[ "$nifti_dir_structure" == "raw" ]] || [[ "$nifti_dir_structure" == "bids" ]]; then
                                    break
                                else
                                    echo -e "\033[31mInvalid input. Please enter 'raw' or 'bids'.\033[0m"
                                    nifti_dir_structure=""
                                fi
                            done
                            break ;;  # Break out of inner while loop, restart the nifti_dir_structure input
                        b|B)
                            while true; do
                                echo -e "\033[1;34m[prompt]\033[0m Enter the absolute path to the directory containing the NIfTi files: \c"
                                read nifti_dir
                            
                                # Check if the directory exists and the path is absolute
                                if [[ "$nifti_dir" == /* ]] && [ -d "$nifti_dir" ]; then
                                    break
                                else
                                    echo -e "\033[31mInvalid absolute path for the directory containing the NIfTi files. Please enter an absolute path and try again.\033[0m"
                                    nifti_dir=""
                                fi
                            done
                            
                            while true; do
                                echo -e "\033[1;34m[prompt]\033[0m Enter the structure of the directory containing the NIfTI files [raw or bids]: \c"
                                read nifti_dir_structure
                            
                                # Check if the input is 'raw' or 'bids'
                                if [[ "$nifti_dir_structure" == "raw" ]] || [[ "$nifti_dir_structure" == "bids" ]]; then
                                    break
                                else
                                    echo -e "\033[31mInvalid input. Please enter 'raw' or 'bids'.\033[0m"
                                    nifti_dir_structure=""
                                fi
                            done
                            break ;;  # Break out of inner while loop, restart both nifti_dir and nifti_dir_structure inputs
                        *)
                            echo -e "\033[31mInvalid input. Please enter 'p', 'd', 's', or 'b'.\033[0m" ;;
                    esac
                done
            else
                break
            fi
        fi
    else
        echo -e "\033[31mInvalid input. Please enter 'raw' or 'bids'.\033[0m"
        nifti_dir_structure=""
    fi
done


while true; do
        # Ask for the directory of previous recon-all runs, if any
        echo -e "\033[1;34m[prompt]\033[0m Enter the absolute path to the directory of previous recon-all runs [press enter if there isn't]: \c"
        read recon_dir

        # Check if the directory exists
        if [[ -z "$recon_dir" ]] || ( [ -d "$recon_dir" ] && [[ "$recon_dir" == /* ]] ); then
            break
        else
            echo -e "\033[31mInvalid absolute path for the directory of previous recon-all runs. Please try again.\033[0m"  
        fi
done

while true; do
    	# Ask for the number of processors to use
    	echo -e "\033[1;34m[prompt]\033[0m Enter the number of threads to use for the analysis: \c"
    	read n_procs
    
    	# Check if the input is a number
    	if [[ "$n_procs" =~ ^[0-9]+$ ]]; then
        	break
    	else
        	echo -e "\033[31mInvalid input. Please enter a number.\033[0m" 
    	fi
done

tput sgr0

echo -e "\033[1;34m[note]\033[0m morphometry will start now!"

if [ ! -d enigma_ocd ]; then mkdir enigma_ocd; fi

if [ $soft == 1 ]; then
    
    if [ "$recon_dir" ]; then

        docker run -ti --rm \
            -v $nifti_dir:/nifti \
            -v $recon_dir:/reconall \
            -v $(pwd)/enigma_ocd:/output \
            csleo/morphometry:v0.1 /nifti /output --recon-all-dir /reconall --work-dir /output --data-dir-structure $nifti_dir_structure --n-procs $n_procs --report --compress-results --write-dataset

    else

        docker run -ti --rm \
            -v $nifti_dir:/nifti \
            -v $(pwd)/enigma_ocd:/output \
            csleo/morphometry:v0.1 /nifti /output --work-dir /output --data-dir-structure $nifti_dir_structure --n-procs $n_procs --report --compress-results --write-dataset
            
    fi

fi

if [ $soft == 2 ]; then

    if [ "$recon_dir" ]; then

        singularity run --cleanenv --bind $(pwd),$nifti_dir,$recon_dir morphometry.0.1.sif \
        $nifti_dir $(pwd)/enigma_ocd --recon-all-dir $recon_dir --work-dir $(pwd)/enigma_ocd --data-dir-structure $nifti_dir_structure --n-procs $n_procs --report --compress-results --write-dataset 

    else

        singularity run --cleanenv --bind $(pwd),$nifti_dir,$recon_dir morphometry.0.1.sif \
        $nifti_dir $(pwd)/enigma_ocd --work-dir $(pwd)/enigma_ocd --data-dir-structure $nifti_dir_structure --n-procs $n_procs --report --compress-results --write-dataset 

    fi

fi
