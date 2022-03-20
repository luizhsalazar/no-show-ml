import logging
import os
import pandas as pd

path_dados = os.getcwd() + '/data/'

def merge_dados_prontuarios(**kwargs):

	logging.info('Leitura dos dados')
	prontuarios = pd.read_csv(path_dados + 'raw/prontuarios-com-horarios.csv')
	usuarios = pd.read_csv(path_dados + 'raw/prontuarios-com-horarios.csv')

	logging.info('Merge dos dados')
	dados = pd.merge(prontuarios, usuarios, how='left', on=['num_prontuario'])
	dados.to_csv(path_dados + 'processed/prontuarios.csv')

def get_dados_prontuarios(**kwargs):

	logging.info('Leitura dos dados gerados')
	return pd.read_csv(path_dados + 'processed/prontuarios.csv')