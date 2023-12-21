DELTA LAKE ARCHITECTURE
![image](https://github.com/ChandraliSarkar/PySpark-Personal-Project/assets/91789144/644fc1b8-c553-4bc5-be38-a33ffc3602fa)

This module focuses on incremental_load with upserts instead of overwriting.
The pyspark code to solve the assignments are present.
Certain syntax changes are there while reading and writing the files in the form of delta instead of parquet as in the previous lessons.

Contents:
1.Ingestion
This folder contains the pyspark scripts to ingest the files 
History load followed by 2 incremental(delta) files
2.demo
This folder contains materials for practice of the Azure delta lake concepts
3.includes
contains configuration and python functions
4.raw
contains DDL for creating raw tables
5.utils
contains scripts for incremental load
6.analysis
contains sql scripts to analyse the data
7.set-up
create a mount point on a new folder called delta in the storage account and use that as source path
8.trans
contains pyspark scripts used for transformations


