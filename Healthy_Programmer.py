
#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    a=time()
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            b=time()
            break


def log_now(msg,c):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()} for {c} secs \n")

if __name__ == '__main__':
    musiconloop("International love.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs =2
    exsecs = 3
    eyessecs = 4

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            a=time()
            musiconloop('International love.mp3', 'drank')
            b=time()
            c=b-a
            init_water = time()
            log_now("Drank Water at",c)

        if time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            a = time()
            musiconloop('International love.mp3', 'doneeyes')
            b = time()
            c = b - a
            init_eyes = time()
            log_now("Eyes Relaxed at",c)

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            a = time()
            musiconloop('International love.mp3', 'donephy')
            b = time()
            c = b - a
            init_exercise = time()
            log_now("Physical Activity done at",c)




