
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator

default_args = {
'owner': 'afctl_clone_me',
 'start_date': datetime.now()

}

dag = DAG(dag_id='new', default_args=default_args, schedule_interval='@once')
task1 = DummyOperator(task_id='task_1', dag=dag)
    
