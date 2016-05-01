import cx_Freeze

executables = [cx_Freeze.Executable("Jumpy Bird.py")]

cx_Freeze.setup(
    name = "Jumpy Bird",
    options = {"build_exe":{"packages":["pygame"], "include_files":["bird3.png", "city.png", "grass.png", "splash.png", "land1.png", "scoreboard.png", "birds.wav", "hit.wav", "point.wav", "wing.wav", "Log.txt"]}},
    description ="Jumpy Bird",
    executables = executables
)