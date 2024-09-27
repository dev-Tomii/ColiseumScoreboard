import json
import os
import requests
from os.path import exists, isdir
import shutil

def verifyDB():
    if (not exists('./players.json')):
        downloadPlayers()

def downloadDB():
    downloadPlayers()

def downloadPlayers():
    data = requests.get('https://api.npoint.io/73701443fb9f9a913c0b')
    player = json.loads(data.text)
    with open('./players.json', 'w') as f:
        f.write(json.dumps(player, indent=4))
        
def downloadClans():
    raw = requests.get('https://api.npoint.io/6488fb58f82a76e31664')
    response = json.loads(raw.text)
    with open('./clans.json', 'w') as f:
        f.write(json.dumps(response, indent=4))
        
def read_clans():
    with open('clans.json', "r") as file:
        lista = json.load(file)     
        clans = []  
        for i in lista:
            clans.append(i['clan'])
    file.close()
    clans.sort()
    return clans

def read_players_clan(clan):
    with open('players.json', "r") as file:
        lista = json.load(file)     
        p = []  
        for i in lista['jogadores']:
            if i['clan'].lower() == clan.lower():
                p.append(i['nome'])
    file.close()
    p.sort()
    return p

def checkDirectories():
    if (not isdir('Data')):
        os.mkdir("Data")

def writeFiles(cp1, cp2, cc1, cc2, stocks):
    with open("./Data/clan1_name.txt", "w") as f:
        f.write(cp1[0])
        f.close()
    for i in range(1,5):
        with open(f"./Data/clan1_p{i}.txt", "w") as f:
            f.write(cp1[i])
            f.close()
    for i in range(0,4):
        with open(f"./Data/clan1_p{i+1}_cost.txt", "w") as f:
            f.write(str(cc1[i]))
            f.close()

    with open("./Data/clan2_name.txt", "w") as f:
        f.write(cp2[0])
        f.close()
    for i in range(1,5):
        with open(f"./Data/clan2_p{i}.txt", "w") as f:
            f.write(cp2[i])
            f.close()
    for i in range(0,4):
        with open(f"./Data/clan2_p{i+1}_cost.txt", "w") as f:
            f.write(str(cc2[i]))
            f.close()
            
    for i in range(0,2):
        with open(f"./Data/clan{i + 1}_stocks.txt", "w") as f:
            f.write(str(stocks[i]))
            f.close()
    
def updateImage1(clan, gamemode):
    if (os.path.isfile("./Data/clan1_img.png")):
        os.remove("./Data/clan1_img.png")
    with open('clans.json', "r") as file:
        lista = json.load(file)     
        for i in lista:
            if i['clan'].lower() == clan.lower():
                shutil.copy(f'./img/{gamemode.get()}/Left/{i['file']}', f'./Data/{i['file']}')
                os.rename(f'./Data/{i['file']}', f'./Data/clan1_img.png')
    file.close()

def updateImage2(clan, gamemode):
    if (os.path.isfile("./Data/clan2_img.png")):
        os.remove("./Data/clan2_img.png")
    with open('clans.json', "r") as file:
        lista = json.load(file)     
        for i in lista:
            if i['clan'].lower() == clan.lower():
                shutil.copy(f'./img/{gamemode.get()}/Right/{i['file']}', f'./Data/{i['file']}')
                os.rename(f'./Data/{i['file']}', f'./Data/clan2_img.png')
    file.close()
