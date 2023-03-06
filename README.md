# scriptListOkta

## Script de listagem de grupos e membros do painel Okta.  
---
**Objetivo:** Listar a quantidade de grupos e também seus membros participantes dentro do Okta mostrando assim as seguintes informações: Grupo do participante, nome, sobrenome, email e status dentro do grupo. 
Requisitos mínimos: Ter a última versão do python instalado na sua máquina em sua última versão que pode ser baixada aqui. 

**1º Passo:** Após baixar o python e o arquivo, deve-se instalar as dependências seguindo os comandos abaixo: 
```sh
python.exe -m pip install --upgrade pip
```
-> Atualizar o gerenciador de pacotes do python para a última versão;
```sh
python -m pip install -r requirements.txt 
```
-> Instalando as dependências do código; 

**2º Passo** Dentro do Script haverá um dict com os seguintes dados      
```py
config = {
    'orgUrl': 'domino.com',
    'token' : 'lkJa65f4sd6falkfsasd034654'
}
```
Deve-se alterar o domínio e o token para o qual você irá usar.
**3º Passo:** Feito todos os passos acima com êxito, execute o script dando `python index.py`
