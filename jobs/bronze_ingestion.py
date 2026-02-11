from utils.schema_definitions import visit_schema


def ingest_patient_visits(spark, input_file, bronze_path):

    df = spark.read.csv(
        input_file,
        header=True,
        schema=visit_schema()
    )

    df.write.mode("overwrite").parquet(bronze_path)
    return df
