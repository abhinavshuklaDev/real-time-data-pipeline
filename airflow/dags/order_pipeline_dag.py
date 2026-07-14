from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

PROJECT_ROOT = "/Users/abhinav.shukla/Projects/real-time-data-pipeline"
PYTHON = f"{PROJECT_ROOT}/.venv/bin/python"
SPARK_DIR = f"{PROJECT_ROOT}/spark"

default_args = {
    "owner": "Abhinav",
    "retries": 1,
}

with DAG(
    dag_id="real_time_order_pipeline",
    description="Real Time Order Processing Pipeline",
    start_date=datetime(2026, 7, 1),
    schedule="@hourly",
    catchup=False,
    default_args=default_args,
    tags=["spark", "etl"],
) as dag:

    silver = BashOperator(
        task_id="silver_pipeline",
        bash_command="""
        set -ex

        echo "===== START ====="
        whoami
        pwd
        env | sort
        which python || true
        python --version || true

        cd /Users/abhinav.shukla/Projects/real-time-data-pipeline/spark

        pwd
        ls -la

        /Users/abhinav.shukla/Projects/real-time-data-pipeline/.venv/bin/python run.py silver

        echo "===== DONE ====="
        """,
    )
    gold = BashOperator(
        task_id="gold_pipeline",
        bash_command=f"""
        cd {SPARK_DIR}
        {PYTHON} run.py gold
        """,
    )

    silver >> gold