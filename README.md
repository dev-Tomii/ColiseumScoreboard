# Coliseum Scoreboard
This is a Scoreboard for OBS made in Python for the ColiseuDeClas Stream that [YaksaTH](https://twitch.tv/yaksath) is running.

## Guide
 - First, the program is [uncompiled](#compiling) here, just raw code. But if you want to compile it use [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/)
 - Now, run `py gui.py` to display the GUI and start working

### Compiling
I use `auto-py-to-exe` to compile this with the following settings:
- Script: ./gui.py
- One Directory
- Window Based
- add sv-ttk folder (...\site-packages\sv_ttk)
- add components folder (./components)
- Set icon (./icon.ico)
- --name set to Coliseum Scoreboard

### Walkthrough
First, select a clan. When you do it, the names of the players belonging to that clan will appear into the combobox of the clan selected. Make sure to select both clans before you continue.
Now, when you select all the players, click the 'Save' button to create the Data folder (if you didnt had it) with all the text files and images inside. Each clan has a different color of scoreboard, but name will always the same so OBS doesnt have any trouble finding the file.
Also, you will have .txt files for not only each text in the combo box, but also the player cost thats not displayed into the gui to make it faster.
