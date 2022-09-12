import os, sys
try:
    from playsound import playsound
except ModuleNotFoundError:
    os.system("py -m pip install playsound")
    from playsound import playsound
os.system("title OutroMusic-Identifier_8809431")
def path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )
playsound("/outromusic.mp3")
sys.exit
