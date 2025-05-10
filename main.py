import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("800x600")
window.config(bg='#00FFFF')
window.resizable(width=True,height=True)
window.title('Game Library')

# Labels
lb_heading = tk.Label(window,text='The Game Library!',font=('Arial', 20), fg='black',bg='#00FFFF')
lb_heading.pack(pady=10)

# Buttons
Btn_exit = tk.Button(window,text='Exit Application!',font = ('Arial',13), command=exit)
Btn_exit.pack(side='bottom', pady=10)

# Combobox creation
n = tk.StringVar()
game_chosen = ttk.Combobox(window, textvariable=n, width=30)
game_chosen['values'] = ('Select a game...',
                        'Red Dead Redemption 1',
                        'Red Dead Redemption 2',
                        'Minecraft',
                        'Call Of Duty: Black Ops',
                        'Call Of Duty: Black Ops 2',)
game_chosen.current(0)  # Set default selection
game_chosen.pack(pady=10)

# Button for game selection
Btn_chosen_game = tk.Button(window,text='Tell Me About It!',font=('Arial',13), command=lambda: show_game_info())
Btn_chosen_game.pack(pady=10)

# Text box for game info
game_info = tk.Text(window, width=80, height=16)
game_info.pack(pady=10)

def show_game_info():
    selected = game_chosen.get()
    game_info.delete(1.0, tk.END)
    if selected == 'Red Dead Redemption 1':
        game_info.insert(tk.END, "Red Dead Redemption is an open world story from 2010 created by Rockstar Games.  It is the successor to Red Dead Revolver in 2004. It takes place in 1911 where you play as protagonist John Marston, a former outlaw who loses his wife and son to the government.\nThe story plays out with John taking justice to his enemies and the troubles and struggles he experiences on the way.")
    elif selected == 'Red Dead Redemption 2':
        game_info.insert(tk.END, "Red Dead Redemption 2 is an open world story game from 2018 created by Rockstar Games. It is set in the year 1899 and is the prequel to 2010’s\nRed Dead Redemption. Ingame, players experience the perspective of outlaw Arthur Morgan, a member of the Van Der Linde Gang.\nArthur’s story follows him trying to survive in a corrupt government while fighting off rival gangs and keeping his community safe.")
    elif selected == 'Minecraft':
        game_info.insert(tk.END, "Minecraft is a sandbox game created by Mojang Studios, led by Markus “Notch” Persson & Jens “Jeb” Bergensten. Ingame, you explore a procedurally\ngenerated 3-dimensional world filled with breakable and replaceable blocks, allowing players to create whatever they desire,\nAs you gather materials and grow stronger within the world, crafting more powerful and capable weapons and tools.")
    elif selected == 'Call Of Duty: Black Ops':
        game_info.insert(tk.END, "Call Of Duty: Black Ops is a first-person-shooter that was developed by Treyarch and published by Activision in 2010. The game is set in the 1960’s\nduring the Cold War. The main character, CIA operative, Alex Mason, attempts to locate a numbers station set to instruct soviet sleeper agents\nto spread chemicals across the US.")
    elif selected == 'Call Of Duty: Black Ops 2':
        game_info.insert(tk.END, "Call Of Duty: Black Ops II is a first-person-shooter that was developed by game company Treyarch and published by Activision in 2012.\nThe game takes place following the ending of Call Of Duty: Black Ops in between the late 1980s and 2025, swapping between Alex Mason\nand Frank Woods in the 1980’s section, while you switch perspectives to Alex Mason’s son, David, in the 2025 segment. Both time periods involve\nthe characters pursuing Raul Menendez, a Nicaraguan arms dealer and later terrorist who is responsible for kidnapping David in the 1980’s\nand starting a second Cold War during 2025.")

window.mainloop()

