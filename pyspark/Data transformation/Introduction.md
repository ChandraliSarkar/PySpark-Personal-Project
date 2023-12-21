This folder contains 2 sub-folders 1.includes 2.ingestion

includes contains 2 sub-folders 1.common_functions Python code used in the basic data ingestion code has been parameterized into Python functions 2.configuration Contains the path of the mounted raw,processed and presentation

The Data transformation folder contains the python code of the various filters,joins and transformations used on the dataset.
 The following commands need to be run before the transformation scripts to invoke the configuration and python common functions 1.%run '../includes/common_functions' 2.%run '../includes/configuration'
