import logging
import os

from src.data.etl_prontuarios_load import ETLProntuariosLoad

class ETLProntuariosPreprocess():

	def __init__(self, etl_load: ETLProntuariosLoad):
		self.path_dados = os.getcwd() + '/data/'
		self.etl_load = etl_load

	def rename_columns(self):
		rename = {
			'num_prontuario': 'medical_record_number',
			'especialidade': 'medical_specialty',
			'horario': 'appointment_time',
			'Genero': 'gender',
			'Data da consulta': 'appointment_date',
			'Compareceu': 'attended',
			'Justificativa': 'no_show_reason',
			'DEF.' : 'type_disability',
			'DATA DE NASCIMENTO' : 'date_of_birth',
			'DATA ENTRADA no Serviço' : 'date_entry_service',
			'PROCEDÊNCIA' : 'city',
			'CID' : 'ICD'
		}
		prontuarios_rename = self.etl_load.get_processed_data().rename(columns=rename)
		logging.info('Criação do arquivo renomeado')
		prontuarios_rename.to_csv(self.path_dados + 'processed/prontuarios-rename.csv', index=False)