from airflow import DAG 
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from datetime import datetime


with DAG(
    'Executando-notebook-etl',
    start_date=datetime(2025, 4, 27),
    schedule="0 9 * * *"
    ) as dag_executando_notebook_extracao:

    extraindo_dados = DatabricksRunNowOperator(
        task_id='Extraindo-conversoes',
        databricks_conn_id='databricks_default',
        job_id=463489759790571,
        notebook_params={"data_execucao": '{{ data_interval_end.strftime("%Y-%m-%d") }}'}
    )

    transformando_dados = DatabricksRunNowOperator(
        task_id='transformando-dados',
        databricks_conn_id='databricks_default',
        job_id=136013615659770
    )

    enviando_dados = DatabricksRunNowOperator(
        task_id='enviando_relatorio',
        databricks_conn_id='databricks_default',
        job_id=265644665385302
    )

    extraindo_dados >> transformando_dados >> enviando_dados