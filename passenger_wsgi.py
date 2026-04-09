import sys
import os

# 1. Garante que o Python encontre os arquivos na pasta do projeto
sys.path.insert(0, os.path.dirname(__file__))

# 2. Ponte para o Flask
try:
    # Tenta importar o objeto 'app' do seu arquivo 'main.py'
    from main import app as application
except Exception as e:
    # Se houver erro de código ou falta de biblioteca, exibe na tela
    def application(environ, start_response):
        start_response('500 Internal Server Error', [('Content-Type', 'text/plain')])
        mensagem = f"Erro de Inicializacao: {str(e)}\nLocal: {os.path.dirname(__file__)}"
        return [mensagem.encode()]

# O Passenger do DirectAdmin usará a variável 'application' acima.