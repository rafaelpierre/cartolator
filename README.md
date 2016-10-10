# cartolator

Simples script python que efetua leitura e análise de dados e scouts de jogadores do Fantasy Game CartolaFC, exportando os dados de jogadores para um arquivo .CSV. O script efetua requests HTTP à API REST do CartolaFC (https://api.cartolafc.globo.com). Alguns dos dados obtidos a partir deste script incluem:

- Últimas 10 pontuações de todos os jogadores cujo status é "Provável" para a próxima rodada
- Pontuação média e desvio padrão destes jogadores
- Scouts básicos
- Scouts de ataque (gols, finalizações, etc)
- Scouts de defesa (roubadas de bola, defesas, etc)

O intuito é utilizar estes dados para analisar o desempenho de cada jogador e auxiliar a montar o seu time, com base em indicadores como pontuação média, desvio padrão, gols por partida, passes, assistências, etc...

# Utilização

- Efetue login em cartolafc.globo.com
- Busque pelo header 'X-GLB-Token' nos GET requests feitos pelo navegador
- Copie o token
- Substitua o texto "SEU_ACCESS_TOKEN" no arquivo cartolator.py pelo seu token de autenticação

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

