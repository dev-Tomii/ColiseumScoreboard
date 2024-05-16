import customtkinter as tk
import functions as f

tk.set_appearance_mode("dark")
tk.set_default_color_theme("blue")

# Frame Settings
app = tk.CTk()
app.geometry("1000x150")
app.title("Coliseum Scoreboard")

# Commands
def update_values1(self):
    f.checkDirectories()
    clan1_p1.configure(values=f.read_players_clan(self))
    clan1_p2.configure(values=f.read_players_clan(self))
    clan1_p3.configure(values=f.read_players_clan(self))
    clan1_p4.configure(values=f.read_players_clan(self))
    f.updateImage1(self)

def update_values2(self):
    f.checkDirectories()
    clan2_p1.configure(values=f.read_players_clan(self))
    clan2_p2.configure(values=f.read_players_clan(self))
    clan2_p3.configure(values=f.read_players_clan(self))
    clan2_p4.configure(values=f.read_players_clan(self))
    f.updateImage2(self)

# Elements Left
clan1_name = tk.CTkComboBox(app, width=400, height=32, justify="center", command=update_values1)
clan1_name.grid(row=0,column=0, padx=10, pady=5, columnspan=2)

clan1_p1 = tk.CTkComboBox(app, width=150, height=32, justify="center", values=[])
clan1_p1.grid(row=1,column=0, padx=10, pady=5, sticky="w")
clan1_p2 = tk.CTkComboBox(app, width=150, height=32, justify="center", values=[])
clan1_p2.grid(row=1,column=1, padx=10, pady=5, sticky="e")
clan1_p3 = tk.CTkComboBox(app, width=150, height=32, justify="center", values=[])
clan1_p3.grid(row=2,column=0, padx=10, pady=5, sticky="w")
clan1_p4 = tk.CTkComboBox(app, width=150, height=32, justify="center", values=[])
clan1_p4.grid(row=2,column=1, padx=10, pady=5, sticky="e")

# Elements Center
save_button = tk.CTkButton(app, text="Save", height=50)
save_button.grid(row=1, column=2, padx=10)

# Elements Right
clan2_name = tk.CTkComboBox(app, width=400, height=32, justify="center", command=update_values2)
clan2_name.grid(row=0,column=3, padx=10, pady=5, columnspan=2)

clan2_p1 = tk.CTkComboBox(app, width=150, height=32, justify="center", values=[])
clan2_p1.grid(row=1,column=3, padx=10, pady=5, sticky="w")
clan2_p2 = tk.CTkComboBox(app, width=150, height=32, justify="center", values=[])
clan2_p2.grid(row=1,column=4, padx=10, pady=5, sticky="e")
clan2_p3 = tk.CTkComboBox(app, width=150, height=32, justify="center", values=[])
clan2_p3.grid(row=2,column=3, padx=10, pady=5, sticky="w")
clan2_p4 = tk.CTkComboBox(app, width=150, height=32, justify="center", values=[])
clan2_p4.grid(row=2,column=4, padx=10, pady=5, sticky="e")

# Configure data
clan1_name.configure(values=f.read_clans())
clan1_name.set("Clan 1")
clan2_name.configure(values=f.read_clans())
clan2_name.set("Clan 2")

clan1_p1.set("Player 1")
clan1_p2.set("Player 2")
clan1_p3.set("Player 3")
clan1_p4.set("Player 4")

clan2_p1.set("Player 1")
clan2_p2.set("Player 2")
clan2_p3.set("Player 3")
clan2_p4.set("Player 4")

# Configure Button
def save():
    c1_list = []
    c1_list.append(clan1_name.get())
    c1_list.append(clan1_p1.get())
    c1_list.append(clan1_p2.get())
    c1_list.append(clan1_p3.get())
    c1_list.append(clan1_p4.get())

    c2_list = []
    c2_list.append(clan2_name.get())
    c2_list.append(clan2_p1.get())
    c2_list.append(clan2_p2.get())
    c2_list.append(clan2_p3.get())
    c2_list.append(clan2_p4.get())
    f.checkDirectories()
    f.writeFiles(c1_list, c2_list)

save_button.configure(command=save)


app.mainloop()