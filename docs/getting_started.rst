Getting started
===============
.. _getting_started:
.. _setup:
.. _project:
.. _migration:

Setup
-----

Dagflow can be run easily using the docker. The only requirement is to have docker and docker-compose installed on the system.
The docker-compose file is already present in the repository. We just need to clone the repository and run the docker-compose.
If you already have a airflow environment you don't have to start the airflow container from here. Airflow and python versions are mentioned in the .env file, if needed you can change it and build the image.

Providers
---------
The “Core” of Apache Airflow provides core scheduler functionality which allow you to write some basic tasks, but the capabilities of Apache Airflow can be extended by installing additional packages, called providers. Installing additional providers can be done in two ways:
1. Adding the providers in the requirements.txt file and rebuilding the image.
2. Adding the provider names inside docker-airflow and ./app/Dockerfile in the airflow installation command *apache-airflow[postgres,google]*. (Adding the providers here will be limited and we recommend to add the providers in the requirements.txt file)

Execute the below commands to start dagflow application

.. code-block:: bash
   git clone git@github.com:jegaths/dagflow.git
   cd dagflow
   # If you want to run dagflow and airflow
   docker compose -f docker-compose.yml -f docker-compose-airflow.yml up -d
   #If you only want to run dagflow
    docker compose up -d

Project
-------

Once the application is up and running you can access the dagflow application using the below url

.. code-block:: bash
    http://localhost


