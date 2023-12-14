%run "../includes/configuration"
race_results_df=spark.read.parquet(f"{presentation_folder_path}/race_results")
filtered_df=race_results_df.filter(race_results_df["race_year"]==2020)
#find the count of records in the df

from pyspark.sql.functions import count,countDistinct,sum
count_df=filtered_df.select(count("race_name")).show()

#count the distinct number of records in the df
count_distinct_df=filtered_df.select(countDistinct("race_name")).show()

#fine the sum of the points achieved during race
sum_df=filtered_df.select(sum("points")).show()
display(sum_df)

#find number of points for Lewis Hamilton
sum_df_Lewis=filtered_df.filter(filtered_df["driver_name"]=="Lewis Hamilton").select(sum("points")).show()

grouped_df=demo_df \
 .groupBy("race_year", "driver_name") \
.agg(sum("points").alias("total_points"),countDistinct("race_name").alias("number_of_races"))

#use rank as window_function
from pyspark.sql.window import Window
from pyspark.sql.functions import desc, rank, asc
driverRank=Window.partitionBy("race_year").orderBy(desc("total_points"))
final_df = grouped_df.withColumn("rank", rank().over(driverRank))
display(final_df)

