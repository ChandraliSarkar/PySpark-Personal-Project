This file contains information on how to process multiple csv or json files in spark.
![image](https://github.com/ChandraliSarkar/PySpark-Personal-Project/assets/91789144/395fd7f2-8bf2-41f5-b50e-195ddaeb193f)
The folder lap_times contains multiple csv files.So,we will write a spark code to read the files ,transform and write to a parquet format.

Assignment:
Step 1 - Read the CSV file using the spark dataframe reader API
Step 2 - Rename columns and add new columns
         Rename driverId and raceId
         Add ingestion_date with current timestamp
Step 3 - Write to output to processed container in parquet format
