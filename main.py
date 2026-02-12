from config import RAW_FILE, BRONZE_PATH, SILVER_PATH, GOLD_PATH
from utils.spark_session import get_spark_session

from jobs.bronze_ingestion import ingest_patient_visits
from jobs.silver_cleaning import clean_visit_data
from jobs.gold_star_schema import build_star_schema
from jobs.business_queries import revenue_by_department, top_diagnosis, city_wise_cost


def main():
    spark = get_spark_session()

    print("Running Bronze Layer...")
    bronze_df = ingest_patient_visits(spark, RAW_FILE, BRONZE_PATH)

    print("Running Silver Layer...")
    silver_df = clean_visit_data(bronze_df, SILVER_PATH)

    spark.stop()


if __name__ == "__main__":
    main()
