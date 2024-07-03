Ativando um novo ambiente virtual

python -m venv nomedoambiente (criar ambiente virtual no vscode)
.\nomedoambiente\Scripts\activate (ativar o ambiente virtual)


Set-ExecutionPolicy Unrestricted -Force (caso der erro, escrever no powershell em admin)

deactivate (Desativar o ambiente virtual)


Bibliotecas

pip install nome_do_pacote (instalar um pacote especifico)
pip install nome_do_pacote==versão (instalar uma versao especifica do pacote)
pip install --upgrade nome_do_pacote (instalar a ultima versao do pacote)
pip uninstall nome_do_pacote (remover um pacote)
pip list (vizualizar bibliotecas instaladas)
pip show nome_do_pacote (exibir detalhes sobre o pacote)
pip freeze > requirements.txt (exibir lista de pacotes instalados)

pip install requests (instalando a biblioteca Requests)
pip install pandas  
pip install faker

