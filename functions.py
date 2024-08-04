import json
import os
import shutil

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
    with open('lista.json', "r") as file:
        lista = json.load(file)     
        p = []  
        for i in lista:
            if i['clan'] == clan:
                p.append(i['nome'])
    file.close()
    p.sort()
    return p

def checkDirectories():
    if (not os.path.isdir('Data')):
        os.mkdir("Data")

def getCost(player):
    with open('lista.json', "r") as file:
        lista = json.load(file)     
        p = 0
        for i in lista:
            if i['nome'] == player:
                p = i["custo"]
    file.close()
    return p

def writeFiles(c1, c2):
    with open("./Data/clan1_name.txt", "w") as f:
        f.write(c1[0])
        f.close()
    for i in range(1,5):
        with open(f"./Data/clan1_p{i}.txt", "w") as f:
            f.write(c1[i])
            f.close()
    for i in range(1,5):
        with open(f"./Data/clan1_p{i}_cost.txt", "w") as f:
            f.write(str(getCost(c1[i])))
            f.close()

    with open("./Data/clan2_name.txt", "w") as f:
        f.write(c2[0])
        f.close()
    for i in range(1,5):
        with open(f"./Data/clan2_p{i}.txt", "w") as f:
            f.write(c2[i])
            f.close()
    for i in range(1,5):
        with open(f"./Data/clan2_p{i}_cost.txt", "w") as f:
            f.write(str(getCost(c2[i])))
            f.close()
    
def updateImage1(clan, gamemode):
    if (os.path.isfile("./Data/clan1_img.png")):
        os.remove("./Data/clan1_img.png")
    with open('clans.json', "r") as file:
        lista = json.load(file)     
        for i in lista:
            if i['clan'] == clan:
                shutil.copy(f'./img/{gamemode.get()}/Left/{i['color']}.png', f'./Data/{i['color']}.png')
                os.rename(f'./Data/{i['color']}.png', f'./Data/clan1_img.png')
    file.close()

def updateImage2(clan, gamemode):
    if (os.path.isfile("./Data/clan2_img.png")):
        os.remove("./Data/clan2_img.png")
    with open('clans.json', "r") as file:
        lista = json.load(file)     
        for i in lista:
            if i['clan'] == clan:
                shutil.copy(f'./img/{gamemode.get()}/Right/{i['color']}.png', f'./Data/{i['color']}.png')
                os.rename(f'./Data/{i['color']}.png', f'./Data/clan2_img.png')
    file.close()