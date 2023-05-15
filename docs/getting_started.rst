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

Once the application is up and running you can access the dagflow application using url **http://localhost**

You will be greated with the homepage directly where you have the option to create a new dagflow or import an existing dag to dagflow. You can also see the list of the recent dagflows.

.. image:: https://raw.githubusercontent.com/jegaths/dagflow/main/docs/images/homepage.png
   :alt: dagflow homepage

Once you opt for creating a new dagflow or importing an existing dagflow you will be taken to the editor page where you can drag and drop different operators fill the details, save the dagflow, generate the dag etc.

.. image:: https://raw.githubusercontent.com/jegaths/dagflow/main/docs/images/editor.png
   :alt: dagflow editor

Operator Lists
^^^^^^^^^^^^^^
Once you are in editor page you can see a canvas with a list of operators. You can drag and drop the operators to the canvas and start building your dagflow.

Dagflow details
^^^^^^^^^^^^^^^
As you can see there are multiple tabs at the bottom of the page which contains different information about the dagflow. The tabs are explained below.
1. General - Contains the pipeline name (dag file name) and a global field which contains the global variables,functions, codes which can be used across the dagflow or dag.

.. image:: https://raw.githubusercontent.com/jegaths/dagflow/main/docs/images/general_tab.png
   :alt: dagflow general tab

2. Node Details - Contains all the arguments for that particular node(operaotr). The arguments are different for different operators and some arguments are mandatory and some are optional. All the mandatory arguments are marked as requierd and a validation is done while saving the dagflow.

.. image:: https://raw.githubusercontent.com/jegaths/dagflow/main/docs/images/node_details_tab.png
   :alt: dagflow node details tab

3. Dag Details - Contains the dag details like dag name, schedule interval, start date, end date, catchup etc.

.. image:: https://raw.githubusercontent.com/jegaths/dagflow/main/docs/images/dag_details_tab.png
   :alt: dagflow dag details tab

4. Imports - Contains the list of imports which are required for the dagflow. The imports are automatically generated based on the operators used in the dagflow. You can also add additional imports if required.

.. image:: https://raw.githubusercontent.com/jegaths/dagflow/main/docs/images/imports_tab.png
   :alt: dagflow imports tab
