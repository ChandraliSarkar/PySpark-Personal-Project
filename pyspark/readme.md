
# Project Title

# Table of Contents
1. [Overview](#overview)
2. [Data Ingestion Requirements](#data-ingestion-requirements)
   - [Data Lake Ingestion](#data-lake-ingestion)
   - [Schema Application](#schema-application)
   - [Audit Columns](#audit-columns)
   - [Storage Format](#storage-format)
   - [SQL Analysis](#sql-analysis)
   - [Incremental Load Handling](#incremental-load-handling)
3. [Data Transformation Requirements](#data-transformation-requirements)
   - [Creation of Reporting Table](#creation-of-reporting-table)
   - [Creation of Analysis Table](#creation-of-analysis-table)
   - [Audit Columns in Transformed Tables](#audit-columns-in-transformed-tables)
   - [SQL Analysis](#sql-analysis-1)
   - [Storage Format](#storage-format-1)
   - [Incremental Load Handling](#incremental-load-handling-1)
4. [Reporting Requirements](#reporting-requirements)
   - [Driver Standings](#driver-standings)
   - [Constructor Standings](#constructor-standings)
5. [Analytical Requirements](#analytical-requirements)
   - [Dominant Drivers](#dominant-drivers)
   - [Dominant Teams](#dominant-teams)
   - [Data Visualization](#data-visualization)
   - [Databricks Dashboards](#databricks-dashboards)
6. [Scheduling Requirements](#scheduling-requirements)
   - [Routine Scheduling](#routine-scheduling)
   - [Monitoring](#monitoring)
   - [Pipeline Rerun](#pipeline-rerun)
   - [Alerts on Failures](#alerts-on-failures)
7. [Conclusion](#conclusion)



## Overview
This document outlines the requirements for the data ingestion, transformation, and reporting processes of our project. It details the standards and methodologies to be followed for efficient data handling and analysis.

## Data Ingestion Requirements
1. **Data Lake Ingestion**
   - Ingest all 8 files into the data lake.
2. **Schema Application**
   - Ensure ingested data adheres to the predefined schema.
3. **Audit Columns**
   - Include audit columns in the ingested data.
4. **Storage Format**
   - Store ingested data in a columnar format (e.g., Parquet).
5. **SQL Analysis**
   - Enable analysis of ingested data using SQL queries.
6. **Incremental Load Handling**
   - The ingestion logic should support incremental data loads.

## Data Transformation Requirements
1. **Creation of Reporting Table**
   - Join key information needed for reporting to create a new table.
2. **Creation of Analysis Table**
   - Join key information required for analysis to create a new table.
3. **Audit Columns in Transformed Tables**
   - Include audit columns in all transformed tables.
4. **SQL Analysis**
   - Ensure transformed data is analyzable via SQL.
5. **Storage Format**
   - Store transformed data in a columnar format (Parquet).
6. **Incremental Load Handling**
   - Transformation logic should support incremental data loads.

## Reporting Requirements
1. **Driver Standings**
   - Report on driver standings.
2. **Constructor Standings**
   - Report on constructor standings.

## Analytical Requirements
1. **Dominant Drivers**
   - Analyze and report on dominant drivers.
2. **Dominant Teams**
   - Analyze and report on dominant teams.
3. **Data Visualization**
   - Visualize outputs for better understanding and analysis.
4. **Databricks Dashboards**
   - Create and manage Databricks dashboards for data visualization.

## Scheduling Requirements
1. **Routine Scheduling**
   - Schedule pipelines to run every Sunday at 10 PM.
2. **Monitoring**
   - Implement monitoring capabilities for the pipelines.
3. **Pipeline Rerun**
   - Include functionality to rerun failed pipelines.
4. **Alerts on Failures**
   - Set up alerts to notify of any pipeline failures.

## Conclusion
This document provides a comprehensive guide to the project's data processes, ensuring a structured and efficient approach to data handling, analysis, and reporting.


