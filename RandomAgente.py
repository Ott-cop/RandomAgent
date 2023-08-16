import random

agentes = [#Controladores
           'Astra',
           'Omen',
           'Brimstone',
           'Harbor',
           'Viper',
           
           #Sentinelas
           'Sage',
           'Cypher',
           'Killjoy',
           'Chamber',

           #Iniciadores
           'Breach',
           'Sova',
           'Fade',
           'Skye',
           'KAYO',

           #Duelistas
           'Jett',
           'Raze',
           'Reyna',
           'Yoru',
           'Phoenix',
           'Neon'
]

numAgentes = int(input('Número de Jogadores: '))

resultado = random.shuffle(agentes)
i = 0

while (i < numAgentes):
    
    print('Jogador: ', agentes[i])
    
    i = i + 1

input("")


