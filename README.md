# API_Workload
Repositório com os códigos para um experimento de medição para o mestrado em Ciência da Computação.

## Setup
Execute o seguinte comando para poder executar a aplicação:

```
pip install -r requirements.txt
```

## Run
Siga os passos para testar a aplicação:
* Configure os parâmetros no client/config_experiment.json de acordo com suas necessidade.
* Você deve ter um banco de dados MySQL rodando. Configure suas credenciais criando um .json chamado db_auth_mysql com os campos necessários. 
* faça o paço anterios com também com o Postgres se preferir, mas também terá que instanciar um objeto do programa conectionBDPostGres no api.py
* Execute o programa server/api.py
* Execute em outro terminal o programa client/client.py
