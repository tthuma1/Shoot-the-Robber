import os
os.environ['TCL_LIBRARY'] = "C:\\Users\\Tim\\Desktop\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Tim\\Desktop\\Python36-32\\tcl\\tk8.6"

import cx_Freeze

executables = [cx_Freeze.Executable("Shoot the Robber.py")]

cx_Freeze.setup(
    name = "Shoot the Robber",
    options = {"build_exe":{"packages":["pygame"],"include_files":["C:/Users/Tim/Desktop/Shoot the Robber/Gun_Shoot.wav","C:/Users/Tim/Desktop/Shoot the Robber/Death_Yell.wav","C:/Users/Tim/Desktop/Shoot the Robber/Death_Yell2.wav","C:/Users/Tim/Desktop/Shoot the Robber/Too_Fast.wav","C:/Users/Tim/Desktop/Shoot the Robber/Clapping.wav","C:/Users/Tim/Desktop/Shoot the Robber/Game_Music.wav","C:/Users/Tim/Desktop/Shoot the Robber/background.png","C:/Users/Tim/Desktop/Shoot the Robber/background1.png","C:/Users/Tim/Desktop/Shoot the Robber/robbul.png","C:/Users/Tim/Desktop/Shoot the Robber/sherbul.png","C:/Users/Tim/Desktop/Shoot the Robber/sheriff badge.png","C:/Users/Tim/Desktop/Shoot the Robber/blood.png","C:/Users/Tim/Desktop/Shoot the Robber/game icon.png"]}},
    executables = executables
    )
