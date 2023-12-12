This file contains information on how to process multiple Json files
![image](https://github.com/ChandraliSarkar/PySpark-Personal-Project/assets/91789144/34812ec1-e316-45e7-a065-88d4c4a9ca15)
Step 1 - Read the JSON file using the spark dataframe reader API
Step 2 - Rename columns and add new columns
        1. Rename qualifyingId, driverId, constructorId and raceId
        2. Add ingestion_date with current timestamp
Step 3 - Write to output to processed container in parquet format
