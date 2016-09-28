import requests
import json
import numpy as np
import csv

r = requests.get("https://api.cartolafc.globo.com/atletas/mercado")

obj = r.json()


headers = {
	'Accept': 'application/json, text/plain, */*',
	'Accept-Encoding': 'gzip, deflate, sdch, br',
	'Accept-Language': 'en-US,en;q=0.8,pt;q=0.6',
	'Connection': 'keep-alive',
	'DNT': '1',
	'Host': 'api.cartolafc.globo.com',
	'Origin': 'https://cartolafc.globo.com',
	'Referer': 'https://cartolafc.globo.com/',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
	'X-GLB-Token': 'SEU_ACCESS_TOKEN'
}

atletas = []

scoutList = {"DD", "FS", "GS", "PE", "CV", "CA", "FC", "RB", "A", "FD", "FT", "G", "I", "SG", "DP", "GC", "FF", "PP"}

for atleta in obj['atletas']:
	if atleta['status_id'] == 7:
		#print atleta["atleta_id"]
		print atleta["apelido"]
		r = requests.get("https://api.cartolafc.globo.com/auth/mercado/atleta/{0}/pontuacao".format(atleta["atleta_id"]), headers=headers)
		pontuacaoAtleta = r.json()
		#print pontuacaoAtleta

		pontuacaoArray = []
		for pontuacao in r.json():
			if pontuacao['pontos'] != None:
				#print 'pontuacao {0}'.format(pontuacao['pontos'])
				pontuacaoArray.append(pontuacao['pontos'])

		npArray = np.array(pontuacaoArray)

		scoutArray = []

		if npArray.size != 0: #jogador ja entrou alguma vez em partidas
			atletaInfo = {"apelido": atleta["apelido"].encode("latin-1"), "atleta_id": atleta["atleta_id"], "jogos_num": atleta["jogos_num"], "posicao_id": atleta["posicao_id"], "media": np.mean(npArray, dtype=np.float64), "desvio_padrao": np.std(npArray, dtype=np.float64)}

			partida = []

			if atleta["clube_id"] == atleta["partida"]["clube_casa_id"]:
				#clube joga em casa
				atletaInfo["joga_casa"] = 1
				atletaInfo["posicao_clube"] = atleta["partida"]["clube_casa_posicao"]
				atletaInfo["posicao_adversario"] = atleta["partida"]["clube_visitante_posicao"]
			else:
				atletaInfo["joga_casa"] = 0
				atletaInfo["posicao_clube"] = atleta["partida"]["clube_visitante_posicao"]
				atletaInfo["posicao_adversario"] = atleta["partida"]["clube_casa_posicao"]

			for key,value in atleta['scout'].iteritems(): #percorre os scouts e os adiciona a lista de atletas, que sera posteriormente escrita no arquivo CSV
				atletaInfo[key.encode("latin-1")] = value

			atletas.append(atletaInfo)


#escreve CSV contendo os atletas, medias e desvios padrao

with open('cartolator.csv', 'w') as csvfile:
    fieldnames = ["apelido", "atleta_id", "jogos_num", "posicao_id", "media", "desvio_padrao"]

    for scout in scoutList:
    	fieldnames.append(scout)

    fieldnames.append("joga_casa")
    fieldnames.append("posicao_clube")
    fieldnames.append("posicao_adversario")

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    print(atletas)
    writer.writeheader()
    #writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    #writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    #writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

    for atleta in atletas:
    	writer.writerow(atleta)




