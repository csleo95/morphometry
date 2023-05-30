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

