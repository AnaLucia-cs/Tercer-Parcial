import subprocess #ejecutar cosas de powershell
import pyautogui #mover cursor y tomar capturas
import time #pausar ejecución, epoch, 
import logging #crear wea logs
from datetime import datetime #más sofisticada
from pathlib import Path #instancias creadas representan una parte de la ruta a un archivo
from parcial import take_screenshot
# TODO: mover funciones a un archivo core.py y dejar solo ejecución en runner.py

logging.basicConfig(
    filename="run.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)
logging.info("===Inicio de ejecución===")
 
pyautogui.FAILSAFE = True 
pyautogui.PAUSE = 0.3


data = { 
        "fecha": (datetime.now().strftime("%d/%m/%Y")), 
        "nombre": ["Ana Lucia", "Ana Laura", "Iza"], 
        "matriculas": (str(2144398+2161478+2115510)), 
        "opcion": ["Marvel"], 
        } 


logging.info(f"Datos a ingresar: {data}")


try:
    logging.info("Tomando captura inicial (before)...")
    take_screenshot("before")

    start_coords = (360, 430)  # ← deben ajustar esto según su pantalla 
    logging.info(f"Coordenadas de inicio: {start_coords}")

    time.sleep(1)  # Tiempo para cambiar a la ventana del formulario
    pyautogui.click(start_coords[0], start_coords[1])
    pyautogui.click(start_coords[0], start_coords[1]) 
    pyautogui.typewrite(data["fecha"])
    logging.info("Fecha escrita correctamente.")

    pyautogui.press("tab")

    for nombre in data["nombre"]:
        pyautogui.typewrite(nombre, interval=0.1 )
        pyautogui.press("enter")
    logging.info("Nombres escritos correctamente.")

    pyautogui.press("tab")
    pyautogui.typewrite(data["matriculas"])
    pyautogui.press("tab")
    logging.info("Matrículas escritas correctamente.")

    take_screenshot("during")
    logging.info("Captura intermedia (during) tomada.")

    # Localizar una opción en pantalla
    pyautogui.press("right")
    pyautogui.press("right")

    #submit
    pyautogui.press("tab")
    pyautogui.press("enter")
    logging.info("Formulario enviado correctamente.")

    take_screenshot("after")
    logging.info("Captura final (after) tomada.")

except Exception as e:
    logging.error(f"Ocurrió un error: {e}")

finally:
    logging.info("===Fin de ejecución===")
