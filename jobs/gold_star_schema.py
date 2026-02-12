def build_star_schema(df, gold_path):

    dim_patient = df.select(
        "patient_id", "patient_name"
    ).distinct()

    dim_doctor = df.select(
        "doctor_id", "doctor_name", "department"
    ).distinct()

    fact_visits = df.select(
        "visit_id",
        "patient_id",
        "doctor_id",
        "visit_date",
        "visit_cost",
        "diagnosis",
        "hospital_city"
    )

    return fact_visits
