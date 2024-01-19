# -*- coding: utf-8 -*-
"""install_packages

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pcA4IT7Ouxu5s_9LDa4UYwz1916AxHb5
"""

# Install Apache Airflow library
!pip install apache-airflow
# Initialize the Airflow database
!airflow initdb

# Import necessary libraries
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import pandas as pd
