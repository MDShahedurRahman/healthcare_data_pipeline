from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType, IntegerType, DoubleType


def visit_schema():
    return StructType([
        StructField("visit_id", IntegerType(), True),
        StructField("patient_id", StringType(), True),
        StructField("patient_name", StringType(), True),
        StructField("doctor_id", StringType(), True),
        StructField("doctor_name", StringType(), True),
        StructField("department", StringType(), True),
        StructField("diagnosis", StringType(), True),
        StructField("cost", DoubleType(), True),
        StructField("visit_date", StringType(), True),
        StructField("hospital_city", StringType(), True)
    ])
