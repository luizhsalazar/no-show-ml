import airflow
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from src.models.train_model import train_model
from src.data.etl_prontuarios_load import ETLProntuariosLoad
from src.preprocessing.etl_prontuarios_preprocess import ETLProntuariosPreprocess

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(1),      # this in combination with catchup=False ensures the DAG being triggered from the current date onwards along the set interval
    'provide_context': False,                            # this is set to True as we want to pass variables on from one task to another
}

etl_load = ETLProntuariosLoad()
etl_preprocess = ETLProntuariosPreprocess(etl_load)

dag = DAG(
    dag_id='dag_prontuarios',
    default_args=args,
    schedule_interval= '@once',             # set interval
	catchup=False,                          # indicate whether or not Airflow should do any runs for intervals between the start_date and the current date that haven't been run thus far
)

task1 = PythonOperator(
    task_id='get_dados_prontuarios',
    python_callable=etl_load.merge_dados_prontuarios,        # function to be executed
    dag=dag,
)

task2 = PythonOperator(
    task_id='rename_columns',
    python_callable=etl_preprocess.rename_columns,
    dag=dag,
)

task3 = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag,
)

task1 >> task2 >> task3
