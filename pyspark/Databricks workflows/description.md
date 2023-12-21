![image](https://github.com/ChandraliSarkar/PySpark-Personal-Project/assets/91789144/c36a10b1-2beb-4435-8e5d-63d0a9892f5e)

This folder contains 2 sub-folders
1.includes
2.ingestion


includes contains 2 sub-folders
1.common_functions
Python code used in the basic data ingestion code has been parameterized into Python functions
2.configuration
Contains the path of the mounted raw,processed and presentation

ingestion folder contains all the python scripts in the basic Data ingestion code
Changes are we are not specifying the path manually in the spark reader and writer apis,rather passing the parameters.
The following commands need to be run before the ingestion scripts to invoke the configuration and python common functions
1.%run '../includes/common_functions'
2.%run '../includes/configuration'
