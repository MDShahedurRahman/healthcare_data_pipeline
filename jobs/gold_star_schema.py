def build_star_schema(df, gold_path):

    dim_patient = df.select(
        "patient_id", "patient_name"
    ).distinct()

    return fact_visits
