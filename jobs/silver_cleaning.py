from pyspark.sql.functions import col, to_date


def clean_visit_data(df, silver_path):

    cleaned_df = df.dropDuplicates() \
        .dropna() \
        .withColumn("visit_date", to_date(col("visit_date")))
