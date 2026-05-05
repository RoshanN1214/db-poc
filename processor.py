# processor.py
def run_transformation(spark_df):
    """Simple logic: Adds a 'Status' column to the data."""
    from pyspark.sql.functions import lit
    return spark_df.withColumn("Status", lit("Processed by Git POC"))