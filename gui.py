import tkinter as tk
from tkinter import ttk
import sv_ttk
import functions as f
import json

f.verifyDB()

root = tk.Tk()
root.title("Coliseum Scoreboard")
root.resizable(False, False)
root.option_add("*tearOff", False)
sv_ttk.use_dark_theme()

from components.Vars import *

# Frames
clan1frame = ttk.LabelFrame(root, text="Clan 1")
clan1frame.grid(rowspan=2,row=1, column=0, padx=(10, 5), pady=(10,20), sticky="nsew")
stockframe = ttk.LabelFrame(root, text='Stocks')
stockframe.grid(row=1, column=2, padx=5, pady=(5, 10), sticky='ew')
clan2frame = ttk.LabelFrame(root, text="Clan 2")
clan2frame.grid(rowspan=1,row=1, column=3, padx=(5, 10), pady=(10,20), sticky="nsew")

# Clan 1
clan1box = ttk.Combobox(clan1frame, values=f.read_clans(), textvariable=c1_name, justify="center")
clan1box.grid(row=0,column=0, padx=10, pady=5, columnspan=4, sticky='ew')

c1_p1box = ttk.Combobox(clan1frame, values=[], textvariable=c1_p1, width=15)
c1_p1box.grid(row=1, column=0, padx=(10,5), pady=5)
c1_p1cost = ttk.Entry(clan1frame, textvariable=c1_c1,width=5)
c1_p1cost.grid(row=1, column=1, padx=5, pady=5)

c1_p2box = ttk.Combobox(clan1frame, values=[], textvariable=c1_p2, width=15)
c1_p2box.grid(row=1, column=2, padx=5, pady=5)
c1_p2cost = ttk.Entry(clan1frame, textvariable=c1_c2,width=5)
c1_p2cost.grid(row=1, column=3, padx=(5,10), pady=5)

c1_p3box = ttk.Combobox(clan1frame, values=[], textvariable=c1_p3, width=15)
c1_p3box.grid(row=2, column=0, padx=(10,5), pady=5)
c1_p3cost = ttk.Entry(clan1frame, textvariable=c1_c3,width=5)
c1_p3cost.grid(row=2, column=1, padx=5, pady=5)

c1_p4box = ttk.Combobox(clan1frame, values=[], textvariable=c1_p4, width=15)
c1_p4box.grid(row=2, column=2, padx=5, pady=5)
c1_p4cost = ttk.Entry(clan1frame, textvariable=c1_c4,width=5)
c1_p4cost.grid(row=2, column=3, padx=(5,10), pady=5)

# Clan 2
clan2box = ttk.Combobox(clan2frame, values=f.read_clans(), textvariable=c2_name, justify="center", width=20)
clan2box.grid(row=0,column=0, padx=10, pady=5, columnspan=4, sticky='ew')

c2_p1box = ttk.Combobox(clan2frame, values=[], textvariable=c2_p1, width=15)
c2_p1box.grid(row=1, column=0, padx=(10,5), pady=5)
c2_p1cost = ttk.Entry(clan2frame, textvariable=c2_c1,width=5)
c2_p1cost.grid(row=1, column=1, padx=5, pady=5)

c2_p2box = ttk.Combobox(clan2frame, values=[], textvariable=c2_p2, width=15)
c2_p2box.grid(row=1, column=2, padx=5, pady=5)
c2_p2cost = ttk.Entry(clan2frame, textvariable=c2_c2,width=5)
c2_p2cost.grid(row=1, column=3, padx=(5,10), pady=5)

c2_p3box = ttk.Combobox(clan2frame, values=[], textvariable=c2_p3, width=15)
c2_p3box.grid(row=2, column=0, padx=(10,5), pady=5)
c2_p3cost = ttk.Entry(clan2frame, textvariable=c2_c3,width=5)
c2_p3cost.grid(row=2, column=1, padx=5, pady=5)

c2_p4box = ttk.Combobox(clan2frame, values=[], textvariable=c2_p4, width=15)
c2_p4box.grid(row=2, column=2, padx=5, pady=5)
c2_p4cost = ttk.Entry(clan2frame, textvariable=c2_c4,width=5)
c2_p4cost.grid(row=2, column=3, padx=(5,10), pady=5)

# Stocks
c1_stocks = ttk.Spinbox(stockframe, width=3, from_=0, to=12, textvariable=c1_stock)
c1_stocks.grid(row=0, column=0, padx=(40,0), pady=10)
c1_stock.set(12)
c2_stocks = ttk.Spinbox(stockframe, width=3, from_=0, to=12, textvariable=c2_stock)
c2_stocks.grid(row=0, column=2, padx=(0,40), pady=10)
c2_stock.set(12)

# Save Button
save_button = ttk.Button(stockframe, text='Salvar', style='Accent.TButton')
save_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10, ipadx=5, ipady=5, sticky="ew")

Radio2s = ttk.Radiobutton(stockframe, text='2v2', value='4v4', variable=gamemode)
Radio2s.grid(row=2, column=0, padx=5, pady=5)
Radio3s = ttk.Radiobutton(stockframe, text='3v3', value='4v4', variable=gamemode)
Radio3s.grid(row=2, column=1, padx=5, pady=5)
Radio4s = ttk.Radiobutton(stockframe, text='4v4', value='4v4', variable=gamemode)
Radio4s.grid(row=2, column=2, padx=5, pady=5)

# Commands
def getCost(player):
    with open('players.json', "r") as file:
        lista = json.load(file)     
        p = 0
        for i in lista['jogadores']:
            if i['nome'] == player:
                p = i["custo"]
    file.close()
    return p

def update_costs1(self):
    c1_c1.set(getCost(c1_p1.get()))
    c1_c2.set(getCost(c1_p2.get()))
    c1_c3.set(getCost(c1_p3.get()))
    c1_c4.set(getCost(c1_p4.get()))
    
def update_costs2(self):
    c2_c1.set(getCost(c2_p1.get()))
    c2_c2.set(getCost(c2_p2.get()))
    c2_c3.set(getCost(c2_p3.get()))
    c2_c4.set(getCost(c2_p4.get()))

def update_values1(self):
    f.checkDirectories()
    c1_p1box.configure(values=f.read_players_clan(c1_name.get()))
    c1_p2box.configure(values=f.read_players_clan(c1_name.get()))
    c1_p3box.configure(values=f.read_players_clan(c1_name.get()))
    c1_p4box.configure(values=f.read_players_clan(c1_name.get()))
    c1_p1.set('')
    c1_p2.set('')
    c1_p3.set('')
    c1_p4.set('')
    c1_c1.set(0)
    c1_c2.set(0)
    c1_c3.set(0)
    c1_c4.set(0)
    f.updateImage1(c1_name.get(), gamemode)

def update_values2(self):
    f.checkDirectories()
    c2_p1box.configure(values=f.read_players_clan(c2_name.get()))
    c2_p2box.configure(values=f.read_players_clan(c2_name.get()))
    c2_p3box.configure(values=f.read_players_clan(c2_name.get()))
    c2_p4box.configure(values=f.read_players_clan(c2_name.get()))
    c2_p1.set('')
    c2_p2.set('')
    c2_p3.set('')
    c2_p4.set('')
    c2_c1.set(0)
    c2_c2.set(0)
    c2_c3.set(0)
    c2_c4.set(0)
    f.updateImage2(c2_name.get(), gamemode)
    
def save():
    cp1 = []
    cp1.append(c1_name.get())
    cp1.append(c1_p1.get())
    cp1.append(c1_p2.get())
    cp1.append(c1_p3.get())
    cp1.append(c1_p4.get())
    cc1 = []
    cc1.append(c1_c1.get())
    cc1.append(c1_c2.get())
    cc1.append(c1_c3.get())
    cc1.append(c1_c4.get())
    cp2 = []
    cp2.append(c2_name.get())
    cp2.append(c2_p1.get())
    cp2.append(c2_p2.get())
    cp2.append(c2_p3.get())
    cp2.append(c2_p4.get())
    cc2 = []
    cc2.append(c2_c1.get())
    cc2.append(c2_c2.get())
    cc2.append(c2_c3.get())
    cc2.append(c2_c4.get())
    stocks = []
    stocks.append(c1_stock.get())
    stocks.append(c2_stock.get())
    f.checkDirectories()
    f.writeFiles(cp1, cp2, cc1, cc2, stocks)

# Adding the commands
clan1box.bind('<<ComboboxSelected>>', update_values1)
clan2box.bind('<<ComboboxSelected>>', update_values2)
c1_p1box.bind('<<ComboboxSelected>>', update_costs1)
c1_p2box.bind('<<ComboboxSelected>>', update_costs1)
c1_p3box.bind('<<ComboboxSelected>>', update_costs1)
c1_p4box.bind('<<ComboboxSelected>>', update_costs1)
c2_p1box.bind('<<ComboboxSelected>>', update_costs2)
c2_p2box.bind('<<ComboboxSelected>>', update_costs2)
c2_p3box.bind('<<ComboboxSelected>>', update_costs2)
c2_p4box.bind('<<ComboboxSelected>>', update_costs2)
save_button.configure(command=save)

root.mainloop()
