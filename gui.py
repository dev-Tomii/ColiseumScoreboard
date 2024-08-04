import tkinter as tk
from tkinter import ttk
import sv_ttk
import functions as f

root = tk.Tk()
root.title("Coliseum Scoreboard")
root.resizable(False, False)
root.option_add("*tearOff", False)
sv_ttk.use_dark_theme()

# Vars
c1_name = tk.StringVar(value='Selecione um clã da lista')
c2_name = tk.StringVar(value='Selecione um clã da lista')
c1_p1 = tk.StringVar(value='Player 1')
c1_p2 = tk.StringVar(value='Player 2')
c1_p3 = tk.StringVar(value='Player 3')
c1_p4 = tk.StringVar(value='Player 4')
c2_p1 = tk.StringVar(value='Player 1')
c2_p2 = tk.StringVar(value='Player 2')
c2_p3 = tk.StringVar(value='Player 3')
c2_p4 = tk.StringVar(value='Player 4')
gamemode = tk.StringVar(value='3v3')

# Frames
clan1frame = ttk.LabelFrame(root, text="Clan 1", padding=(20, 10))
clan1frame.grid(rowspan=2,row=0, column=0, padx=20, pady=20, sticky="nsew")
clan2frame = ttk.LabelFrame(root, text="Clan 2", padding=(20, 10))
clan2frame.grid(rowspan=2,row=0, column=2, padx=20, pady=20, sticky="nsew")

# Clan 1
clan1box = ttk.Combobox(clan1frame, values=f.read_clans(), textvariable=c1_name, justify="center")
clan1box.grid(row=0,column=0, padx=10, pady=5, columnspan=2, sticky='ew')

c1_p1box = ttk.Combobox(clan1frame, values=[], textvariable=c1_p1)
c1_p1box.grid(row=1, column=0, padx=10, pady=5)

c1_p2box = ttk.Combobox(clan1frame, values=[], textvariable=c1_p2)
c1_p2box.grid(row=1, column=1, padx=10, pady=5)

c1_p3box = ttk.Combobox(clan1frame, values=[], textvariable=c1_p3)
c1_p3box.grid(row=2, column=0, padx=10, pady=5)

c1_p4box = ttk.Combobox(clan1frame, values=[], textvariable=c1_p4)
c1_p4box.grid(row=2, column=1, padx=10, pady=5)

# Clan 2
clan2box = ttk.Combobox(clan2frame, values=f.read_clans(), textvariable=c2_name, justify="center")
clan2box.grid(row=0,column=0, padx=10, pady=5, columnspan=2, sticky='ew')

c2_p1box = ttk.Combobox(clan2frame, values=[], textvariable=c2_p1)
c2_p1box.grid(row=1, column=0, padx=10, pady=5)

c2_p2box = ttk.Combobox(clan2frame, values=[], textvariable=c2_p2)
c2_p2box.grid(row=1, column=1, padx=10, pady=5)

c2_p3box = ttk.Combobox(clan2frame, values=[], textvariable=c2_p3)
c2_p3box.grid(row=2, column=0, padx=10, pady=5)

c2_p4box = ttk.Combobox(clan2frame, values=[], textvariable=c2_p4)
c2_p4box.grid(row=2, column=1, padx=10, pady=5)

# Save Button
save_button = ttk.Button(root, text='Salvar', style='Accent.TButton')
save_button.grid(row=1, column=1, padx=20, pady=10, ipadx=5, ipady=5)
radio_frame = ttk.LabelFrame(root, text='Gamemode', labelanchor='n')
radio_frame.grid(row=0, column=1, padx=20, pady=10)

Radio2s = ttk.Radiobutton(radio_frame, text='2v2', value='3v3', variable=gamemode)
Radio2s.grid(row=0, column=0, padx=5, pady=10)
Radio3s = ttk.Radiobutton(radio_frame, text='3v3', value='3v3', variable=gamemode)
Radio3s.grid(row=1, column=0, padx=5, pady=10)
Radio4s = ttk.Radiobutton(radio_frame, text='4v4', value='3v3', variable=gamemode)
Radio4s.grid(row=2, column=0, padx=5, pady=10)

# Commands        
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
    f.updateImage2(c2_name.get(), gamemode)
    
def save():
    c1_list = []
    c1_list.append(c1_name.get())
    c1_list.append(c1_p1.get())
    c1_list.append(c1_p2.get())
    c1_list.append(c1_p3.get())
    c1_list.append(c1_p4.get())

    c2_list = []
    c2_list.append(c2_name.get())
    c2_list.append(c2_p1.get())
    c2_list.append(c2_p2.get())
    c2_list.append(c2_p3.get())
    c2_list.append(c2_p4.get())
    f.checkDirectories()
    f.writeFiles(c1_list, c2_list)

# Adding the commands
clan1box.bind('<<ComboboxSelected>>', update_values1)
clan2box.bind('<<ComboboxSelected>>', update_values2)
save_button.configure(command=save)

root.mainloop()
