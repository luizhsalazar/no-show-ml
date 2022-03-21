import logging
import os
import pandas as pd

class ETLProntuariosLoad():

	def __init__(self):
		self.path_dados = os.getcwd() + '/data/'

	def merge_dados_prontuarios(self):
		logging.info('Leitura dos dados')
		prontuarios = self.get_dados_prontuarios()
		usuarios = self.get_dados_controle_usuarios()

		logging.info('Merge dos dados')
		dados = pd.merge(prontuarios, usuarios, how='left', on=['num_prontuario'])
		dados.to_csv(self.path_dados + 'processed/prontuarios.csv', index=False)

	def get_dados_prontuarios(self):
		return pd.read_csv(self.path_dados + 'raw/prontuarios-com-horarios.csv')

	def get_dados_controle_usuarios(self):
		return pd.read_csv(self.path_dados + 'raw/prontuario-controle-usuarios.csv')

	def get_processed_data(self):
		logging.info('Leitura dos dados gerados')
		prontuarios = pd.read_csv(self.path_dados + 'processed/prontuarios.csv')
		print("%d prontuários no total." % prontuarios.shape[0])
		return prontuarios

