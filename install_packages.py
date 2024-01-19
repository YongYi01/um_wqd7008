# Install Apache Airflow library
!pip install apache-airflow
# Initialize the Airflow database
!airflow initdb

# Import necessary libraries
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import pandas as pd
