==================
Troubleshooting
==================

This section provides solutions to common issues that you may encounter while running the pipeline. Below is a list of problems we will address:

.. contents::
   :local:
   :depth: 2

.. _no-internet:

----------------------------------------------
My server does not have internet access
----------------------------------------------

If your server does not have internet access, you can still run this pipeline by downloading its dependencies on another server (e.g., your personal computer) with internet access, and then transferring them to your server. However, your server must have Docker and/or Singularity installed so you can run this pipeline. Three workarounds are outlined below depending on whether you will use Docker or Singularity in your server.

.. _using-docker:

Using Docker
^^^^^^^^^^^^

You will need to have Docker installed on the other server with internet access. In this case, you can follow the steps below:

1. Download the handler scripts in the server with internet access.
2. Run the commands below on the server with internet access to download the pipeline image, and convert it to a tar file::

    docker pull csleo/img_trs
    docker save --output img_trs.tar csleo/img_trs

3. Transfer the handler script file (run_img_trs.sh) and the tar file of the pipeline (img_trs.tar) to your server without internet connection
4. In your server without internet connection, run the command below in the folder where the tar file of the pipeline (img_trs.tar) is located::

    docker load -i img_trs.tar

5. In your server without internet connection, you can follow step 2.2 onwards to run the pipeline.

.. _singularity-v3:

Using Singularity (version ≥ 3.0)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You will need to have Singularity installed on the other server with internet access. In this case, you can follow the steps below:

1. Download the handler scripts in the server with internet access.
2. Run the command below on the server with internet access to build the pipeline image::

    singularity build img_trs.sif docker://csleo/img_trs

3. Transfer the handler script file (run_img_trs.sh) and the SIF file of the pipeline (img_trs.sif) to your server without internet connection
4. In your server without an internet connection, you can follow step 2.2 onwards to run the pipeline. Make sure the img_trs.sif file is in the directory from which you are executing the handler script.

.. _singularity-less-v3:

Using Singularity (version < 3.0)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You will need to have Docker installed on the other server with internet access. In this case, you can follow the steps below:

1. Download the handler scripts in the server with internet access.
2. Run the command below on the server with internet access to download the pipeline image (note that you have to substitute the `<version>` by 2.3, 2.4, 2.5 or 2.6 depending on the version of Singularity that is installed on your server)::

    docker run --privileged -t --rm \
               -v /var/run/docker.sock:/var/run/docker.sock \
               -v $(pwd):/output \
               singularityware/docker2singularity:v<version> \
               --name img_trs csleo/img_trs

3. Transfer the handler script file (run_img_trs.sh) and the SIMG file of the pipeline (img_trs.simg) to your server without internet connection


.. _no-docker-singularity:

----------------------------------------------
Neither Docker, nor Singularity are installed in the system
----------------------------------------------

If neither Docker nor Singularity are installed on the system, please install one of them. You can do this by following the instructions in one of the links below (you will need root access to go through them):

• Latest Docker version on Linux: `Docker on Linux <https://docs.docker.com/desktop/install/linux-install/test>`__
• Latest Docker version on Mac: `Docker on Mac <https://docs.docker.com/desktop/install/mac-install/>`__
• Latest Docker version on Windows: `Docker on Windows <https://docs.docker.com/desktop/install/windows-install/>`__
• Latest Singularity version on Linux, Mac, or Windows: `Singularity Quick Start Guide <https://docs.sylabs.io/guides/3.10/user-guide/quick_start.html>`__


.. _docker-daemon:

----------------------------------------------
Docker daemon is not running
----------------------------------------------

If the Docker daemon is not running, the handler script will output a message of this sort::

    Cannot connect to the Docker daemon at unix:///home/leocs/.docker/desktop/docker.sock. Is the docker daemon running?

You will need to have Docker installed on the other server with internet access. In this case, you can follow the steps below:

1. You can search Docker Desktop on the Applications menu and open it.
2. Alternatively, you can run the following command on the terminal::

    systemctl –user start docker-desktop


.. _nohard_disk:

----------------------------------------------
Not enough available hard disk space in Docker to download the pipeline image
----------------------------------------------

If there is not enough available space in the hard disk allocated to Docker, the handler script will print a message of this sort::

    No space left on the device


There are three ways to increase the available hard disk space in Docker Desktop (you can try a combination of more than one):

Delete local images
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two ways of doing this:

1. Open Docker Desktop and delete local images by clicking on the three dots on the left of an image's row and then clicking on remove.

2. Alternatively, enter the command ``docker image rm [image name]``, for instance:

.. code-block:: bash

    docker image rm hello-world

Delete unused data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enter the following command to delete unused containers, networks, images:

.. code-block:: bash

    docker system prune

Increase the available disk space allocated to Docker Desktop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Open Docker Desktop and click on the Settings button.

2. Click on the Resources button.

3. Increase the Disk image size of Docker Desktop.

Remember to save the content above in a single .rst file.


.. _lower_sing:

----------------------------------------------
Server with Singularity version < 3.0
----------------------------------------------

In this case, the handler script will use the docker2singularity utility to download the pipeline image from Docker Hub and convert it to a format compatible with the Singularity version on the server. However, for this to work, Docker must be installed on the server. If it is not installed on your server, please go through the steps 3.1.2.c to 3.1.4.c to download the pipeline image from another server with Docker installed and then transfer the image to your server.


.. _not_recog:

----------------------------------------------
Docker does not recognize the path of my directories
----------------------------------------------

If are using Docker to run the pipeline and the directory with NIfTI files and/or the directory with freesurfer’s recon-all output are located in paths not shared with Docker, an error message of this sort will be print:

.. code-block:: bash

    docker: Error response from daemon: Mounts denied: 
The path /media/leocs/leo.hd/DRIVE/ img_trs not shared from the host and is not known to Docker.

To deal with this, go to docker desktop menu, and click on the File sharing button and add the path(s) to the directory with NIfTI files and/or the directory with freesurfer’s recon-all.