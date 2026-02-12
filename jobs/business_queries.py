from pyspark.sql.functions import sum, count, desc


def revenue_by_department(df):
    return df.groupBy("department") \
        .agg(sum("visit_cost").alias("total_revenue")) \
        .orderBy(desc("total_revenue"))


def top_diagnosis(df):
    return df.groupBy("diagnosis") \
        .agg(count("*").alias("cases")) \
        .orderBy(desc("cases"))
