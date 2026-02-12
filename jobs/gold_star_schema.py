def build_star_schema(df, gold_path):

    dim_patient = df.select(
        "patient_id", "patient_name"
    ).distinct()

    dim_doctor = df.select(
        "doctor_id", "doctor_name", "department"
    ).distinct()

    return fact_visits
