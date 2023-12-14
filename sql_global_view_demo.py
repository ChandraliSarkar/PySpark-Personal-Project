%run "../includes/configuration"
race_results_df=spark.read.parquet(f"{presentation_folder_path}/race_results")
race_results_df.createOrReplaceGlobalTempView("v_race_global_name")
#access view from python cell
df=spark.sql("select * from global_temp.v_race_global_name;")
#parameterizing using spark.sql
p_race_year=2019
race_df_2019=spark.sql(f"select * from global_temp.v_race_global_name where race_year={p_race_year}")
