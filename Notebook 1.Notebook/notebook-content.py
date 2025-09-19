# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "80ec0a9e-39b3-4801-9adc-c635fec77e73",
# META       "default_lakehouse_name": "DemoLH",
# META       "default_lakehouse_workspace_id": "3172906b-75af-4592-8005-722f9b418b75",
# META       "known_lakehouses": [
# META         {
# META           "id": "80ec0a9e-39b3-4801-9adc-c635fec77e73"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
# My First Notebook

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Load 'publicholidays' table from the Lakehouse into a Spark DataFrame and display records
max_rows_to_read = 1000
spark_df = spark.read.table("publicholidays")
display(spark_df.limit(max_rows_to_read))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
