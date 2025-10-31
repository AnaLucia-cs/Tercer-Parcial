import subprocess
import pyautogui
import time
import logging
from datetime import datetime
from pathlib import Path

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3

def run_powershell(cmd):
    """Ejecuta un comando de PowerShell con manejo de errores."""
    try:
        result = subprocess.run(
            ["powershell", "-Command", cmd],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode != 0:
            logging.error(f"Error en PowerShell: {result.stderr.strip()}")
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except subprocess.TimeoutExpired:
        logging.error("Error: El comando de PowerShell excedió el tiempo límite.")
        return 1, "", "TimeoutExpired"
    except Exception as e:
        logging.error(f"Excepción al ejecutar PowerShell: {str(e)}")
        return 1, "", str(e)

def take_screenshot(name):
    """Captura pantallas y las guarda en /out."""
    out = Path("out")
    out.mkdir(exist_ok=True)
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    path = out / f"{name}_{ts}.png"
    img = pyautogui.screenshot()
    img.save(path)
    return path

def fill_form(data, start_coords):
    """Llena el formulario usando coordenadas manuales."""
    take_screenshot("before")
    pyautogui.click(start_coords[0], start_coords[1])
    pyautogui.typewrite(data["nombre"])
    pyautogui.press("tab")
    pyautogui.typewrite(data["correo"])
    pyautogui.press("tab")
    pyautogui.typewrite(data["equipo"])
    pyautogui.press("enter")
    take_screenshot("during")
    time.sleep(1)
    take_screenshot("after")
