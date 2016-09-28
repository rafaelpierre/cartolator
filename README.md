# cartolator

Script python que efetua leitura e análise de dados de jogadores do Fantasy Game CartolaFC, exportando os dados de jogadores para um arquivo .CSV.

# Utilização

- Efetue login em cartolafc.globo.com
- Busque pelo header 'X-GLB-Token' nos GET requests feitos pelo navegador
- Copie o token
- Substitua o texto "SEU_ACCESS_TOKEN" no arquivo cartolator.py pelo seu token de autenticação
- 

# Dependências

Antes de rodar o script é necessário ter as dependências abaixo instaladas.

- requests
- json
- numpy
- csv

Caso não tenha alguma delas -> pip install nome_da_dependencia

# TODO

- Login automático
- Análise de resultados históricos das equipes e cálculos de probabilidades

