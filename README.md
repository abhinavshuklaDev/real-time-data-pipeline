# 🚀 Real-Time Data Engineering Pipeline

A production-inspired **Real-Time Data Engineering Pipeline** built using **Apache Kafka, PySpark Structured Streaming, Apache Airflow, DuckDB, and Apache Superset**.

This project demonstrates how streaming data can be ingested, processed through a Medallion Architecture (Bronze → Silver → Gold), orchestrated with Airflow, and visualized through interactive dashboards.

---

# 📌 Project Overview

The pipeline continuously generates order events, streams them through Kafka, processes them with Spark Structured Streaming, stores them in Bronze, Silver, and Gold layers, orchestrates ETL jobs using Apache Airflow, and provides business insights using Apache Superset.

---

# 🏗️ Architecture

```
                   +----------------------+
                   |  Order Generator     |
                   +----------+-----------+
                              |
                              ▼
                   +----------------------+
                   | Kafka Producer       |
                   +----------+-----------+
                              |
                              ▼
                   +----------------------+
                   |   Kafka Topic        |
                   |      orders          |
                   +----------+-----------+
                              |
                              ▼
             +-----------------------------------+
             | Spark Structured Streaming        |
             +-----------------------------------+
                              |
                              ▼
                 Bronze Layer (Raw Data)
                              |
                              ▼
              Silver Layer (Clean & Validated)
                              |
                              ▼
             Gold Layer (Business Aggregations)
                              |
                              ▼
                    DuckDB Analytics
                              |
                              ▼
                 Apache Superset Dashboard
```

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python 3.12 |
| Streaming | Apache Kafka |
| Processing | PySpark Structured Streaming |
| Workflow | Apache Airflow |
| Storage | Parquet |
| Analytics | DuckDB |
| Visualization | Apache Superset |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```
real-time-data-pipeline/
│
├── airflow/
│   ├── dags/
│   └── plugins/
│
├── producer/
│
├── consumer/
│
├── spark/
│   ├── src/
│   └── run.py
│
├── analytics/
│   ├── load_gold.py
│   └── orders.db
│
├── data/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   ├── checkpoints/
│   └── audit/
│
├── docs/
│   ├── dashboard.png
│   └── airflow_dag.png
│
├── requirements.txt
└── README.md
```

---

# 🔄 Pipeline Workflow

### 1️⃣ Order Generator

Random order events are generated with fields such as:

- Order ID
- Customer ID
- Product
- Category
- City
- Quantity
- Price
- Timestamp

---

### 2️⃣ Kafka Producer

Publishes streaming order events into the **orders** Kafka topic.

---

### 3️⃣ Spark Structured Streaming

Consumes streaming data from Kafka and processes it in three stages:

## Bronze Layer

- Raw Kafka Events
- Schema Parsing
- Data Persistence

---

## Silver Layer

- Data Cleaning
- Null Handling
- Type Conversion
- Duplicate Removal
- Business Validation

---

## Gold Layer

Business-ready aggregated datasets:

- 📈 Daily Revenue
- 🏆 Top Products
- 👥 Top Customers
- 🏙️ City Sales
- 🛍️ Category Sales

---

### 4️⃣ Apache Airflow

Automates the ETL workflow.

Current DAG:

```
Silver Pipeline
        │
        ▼
Gold Pipeline
```

---

### 5️⃣ DuckDB

Loads Gold Layer parquet files into DuckDB for fast analytical queries.

---

### 6️⃣ Apache Superset

Creates interactive dashboards directly from DuckDB.

---

# 📊 Dashboard

## Real-Time Sales Analytics Dashboard

The dashboard contains:

- 📈 Daily Revenue
- 🏆 Top Products
- 👥 Top Customers
- 🛍️ Category Sales
- 🏙️ City Sales


---

# 🌬️ Airflow DAG

The pipeline is orchestrated through Apache Airflow.

---

# ✨ Features

- Real-time Kafka Streaming
- Spark Structured Streaming
- Bronze / Silver / Gold Architecture
- Automated ETL using Airflow
- DuckDB Analytics
- Interactive Superset Dashboard
- Modular Repository Pattern
- Clean Project Structure
- Production-inspired Data Pipeline

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/abhinavshuklaDev/real-time-data-pipeline.git

cd real-time-data-pipeline
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

### macOS/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

### Start Kafka

```bash
bin/kafka-server-start.sh config/server.properties
```

---

### Start Producer

```bash
python -m producer.src.main
```

---

### Start Spark Streaming

```bash
python run.py bronze
```

---

### Trigger Airflow

```bash
airflow standalone
```

---

### Load Gold Data into DuckDB

```bash
python analytics/load_gold.py
```

---

### Start Superset

```bash
superset run -p 8088 --debug
```

---

# 📈 Business Metrics

The project provides insights such as:

- Revenue by Day
- Sales by Category
- Top Selling Products
- Top Customers
- Revenue by City

---

# 🚀 Future Improvements

- Docker Compose
- Delta Lake
- Apache Iceberg
- AWS S3
- AWS Glue
- EMR
- MWAA
- Redshift
- Great Expectations
- dbt
- GitHub Actions CI/CD
- Terraform Deployment
- Kubernetes Deployment

---

# 💡 Skills Demonstrated

- Apache Kafka
- PySpark
- Spark Structured Streaming
- Apache Airflow
- DuckDB
- Apache Superset
- Data Engineering
- ETL Development
- Data Lake Architecture
- Python
- Git
- Data Visualization

---

# 📬 Author

**Abhinav Shukla**

GitHub: https://github.com/abhinavshuklaDev

---

⭐ If you found this project helpful, consider giving it a star!