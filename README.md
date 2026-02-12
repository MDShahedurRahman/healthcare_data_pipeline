# Smart Healthcare Data Engineering Pipeline (PySpark)

A complete **Healthcare Analytics Data Engineering Pipeline** built using **PySpark** and the **Medallion Architecture (Bronze → Silver → Gold)**.

This project processes raw hospital patient visit records from CSV, cleans and transforms them into Parquet format, models the data into a Star Schema, and generates key healthcare business insights through Spark analytics queries.

It is designed as a **portfolio-quality Data Engineering project** demonstrating real-world ETL workflows, scalable data lake design, and analytics-ready outputs.

---

## 🚀 Project Overview

Healthcare organizations generate large volumes of patient visit data every day.  
To support reporting, analytics, and decision-making, raw transactional records must be transformed into clean, structured datasets.

This pipeline performs:

- Raw data ingestion into a Data Lake (Bronze)
- Data cleaning and enrichment (Silver)
- Star Schema modeling for analytics (Gold)
- KPI queries for hospital insights

---

## 🏗 Pipeline Architecture (Medallion Design)

```
Raw CSV Patient Visit Data
        ↓
Bronze Layer (Raw Parquet)
        ↓
Silver Layer (Clean + Standardized Parquet)
        ↓
Gold Layer (Star Schema Tables)
        ↓
Business Queries + Healthcare KPI Reports
```

---

## 📂 Project Structure

```
healthcare_data_pipeline/
│
├── main.py
├── config.py
├── requirements.txt
│
├── data/
│   └── patient_visits.csv
│
├── jobs/
│   ├── bronze_ingestion.py
│   ├── silver_cleaning.py
│   ├── gold_star_schema.py
│   └── business_queries.py
│
├── utils/
│   ├── spark_session.py
│   ├── schema_definitions.py
│   └── helpers.py
│
└── output/
    ├── bronze/
    ├── silver/
    ├── gold/
    └── reports/
```

---

## 📌 Data Source

The pipeline uses a sample dataset:

`data/patient_visits.csv`

Example:

```csv
visit_id,patient_id,patient_name,doctor_id,doctor_name,department,diagnosis,cost,visit_date,hospital_city
201,P001,John Smith,D101,Dr. Lee,Cardiology,Heart Checkup,500,2025-01-05,New York
202,P002,Amina Rahman,D102,Dr. Kim,Neurology,Migraine,300,2025-01-07,Boston
203,P003,Sarah Lee,D101,Dr. Lee,Cardiology,ECG Test,700,2025-01-10,New York
```

---

## ⚙️ Technologies Used

- **Python**
- **PySpark**
- **Parquet Storage Format**
- **Medallion Data Lake Architecture**
- **Star Schema Modeling**
- **Healthcare KPI Analytics Queries**

---

## 🚀 Pipeline Jobs

---

### 🥉 Bronze Layer: Raw Data Ingestion

**File:** `jobs/bronze_ingestion.py`

Responsibilities:

- Read raw CSV patient visit data
- Apply schema validation
- Store raw records in Parquet format

Output:

```
output/bronze/
```

---

### 🥈 Silver Layer: Data Cleaning & Transformation

**File:** `jobs/silver_cleaning.py`

Transformations applied:

- Remove duplicate visit records
- Handle missing values
- Convert visit_date into proper DateType
- Rename cost field into visit_cost for clarity

Output:

```
output/silver/
```

---

### 🥇 Gold Layer: Star Schema Modeling

**File:** `jobs/gold_star_schema.py`

Creates analytics-ready tables:

#### Dimension Tables
- `dim_patient`
- `dim_doctor`

#### Fact Table
- `fact_visits`

Output:

```
output/gold/
   ├── dim_patient/
   ├── dim_doctor/
   └── fact_visits/
```

---

### 📊 Business Queries & Healthcare KPIs

**File:** `jobs/business_queries.py`

Key business insights generated:

- Revenue by Department
- Most Common Diagnoses
- City-wise Treatment Costs

Example:

```
Cardiology → $1200
Neurology  → $300
Orthopedics → $400
```

---
