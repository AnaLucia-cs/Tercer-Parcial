import subprocess #ejecutar cosas de powershell
import pyautogui #mover cursor y tomar capturas
import time #pausar ejecución, epoch, 
import logging #crear wea logs
from datetime import datetime #más sofisticada
from pathlib import Path #instancias creadas representan una parte de la ruta a un archivo
 
# TODO: mover funciones a un archivo core.py y dejar solo ejecución en runner.py
 
 
pyautogui.FAILSAFE = True 
pyautogui.PAUSE = 0.3
 
data = { 
        "fecha": (datetime.now().strftime("%d/%m/%Y")), 
        "nombre": ["Ana Lucia", "Ana Laura", "Iza"], 
        "matriculas": (str(2144398+1+2)), 
        "opcion": ["Marvel"], 
        } 

start_coords = (1243, 453)  # ← deben ajustar esto según su pantalla 

pyautogui.click(start_coords[0], start_coords[1])
pyautogui.click(start_coords[0], start_coords[1]) 
pyautogui.typewrite(data["fecha"])
pyautogui.press("tab")

for nombre in data["nombre"]:
    pyautogui.typewrite(nombre, interval=0.1 )
    pyautogui.press("enter")

pyautogui.press("tab")
pyautogui.typewrite(data["matriculas"])
pyautogui.press("tab")

# Localizar una opción en pantalla
pyautogui.press("right")
pyautogui.press("right")

#submit
pyautogui.press("tab")
pyautogui.press("enter")