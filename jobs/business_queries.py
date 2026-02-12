from pyspark.sql.functions import sum, count, desc


def revenue_by_department(df):
    return df.groupBy("department") \
        .agg(sum("visit_cost").alias("total_revenue")) \
        .orderBy(desc("total_revenue"))


def top_diagnosis(df):
    return df.groupBy("diagnosis") \
        .agg(count("*").alias("cases")) \
        .orderBy(desc("cases"))


def city_wise_cost(df):
    return df.groupBy("hospital_city") \
        .agg(sum("visit_cost").alias("city_cost")) \
        .orderBy(desc("city_cost"))
