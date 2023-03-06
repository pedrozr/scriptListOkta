import asyncio # asyncio==3.4.3
from okta.client import Client as OktaClient # okta==2.8.0
import pandas as pd # pandas==1.5.3, openpyxl==3.1.1

### Configurações
config = {
    'orgUrl': 'domino.com', # Insira o dominio que irá usar
    'token' : 'lkJa65f4sd6falkfsasd034654' # Insira o token, lembrando que o token deve ter privilegios admin
}

okta_client = OktaClient(config)

async def main(): 
    # Variaveis pré feitas
    grupoUse = []
    nome = []
    lastName = []
    email = [] 
    status = []

    # Laço para fazer a verificação dos grupos
    todosGrupos, resp, err = await okta_client.list_groups()
    for groups in todosGrupos:
        print('\nVerificando o Grupo {}'.format(groups.profile.name))
        usuariosGrupos, resp, err = await okta_client.list_group_users(groups.id)
        users = {'Grupo': grupoUse, 'Nomes': nome, 'Sobrenome': lastName, 'Email': email, 'Status': status}
        if usuariosGrupos == []:
            continue
        else:
        # Laço para verificar os dados pedidos de cada usuario de cada grupo
            for userG in usuariosGrupos: 
                print(groups.profile.name,
                    userG.profile.first_name, 
                    userG.profile.last_name, 
                    userG.profile.email, 
                    userG.status)
                
                grupoUse.append(groups.profile.name)
                nome.append(userG.profile.first_name)
                lastName.append(userG.profile.last_name)
                email.append(userG.profile.email)
                status.append(userG.status)
                users = {'Grupo': grupoUse, 'Nomes': nome, 'Sobrenome': lastName, 'Email': email, 'Status': status}
        usuariosGrupo = pd.DataFrame(users)
        #criarAba(usuariosGrupo, groups.profile.name.split()[0])
        usuariosGrupo.to_excel('dados.xlsx', sheet_name=str(groups.profile.name.split()[0]), index=False)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())