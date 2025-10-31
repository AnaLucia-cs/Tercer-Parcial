# exam_script.py 
# Este código está mal estructurado. Debes modularizarlo y completarlo. 
import subprocess 
import pyautogui 
import time 
import logging 
from datetime import datetime 
from pathlib import Path 
# TODO: mover funciones a un archivo core.py y dejar solo ejecución en runner.py 
pyautogui.FAILSAFE = True 
pyautogui.PAUSE = 0.3 

def run_powershell(cmd): 
    try: 
        result = subprocess.run(["powershell", "-Command", cmd], 
        capture_output=True, text=True, timeout=10) 
        return result.returncode, result.stdout.strip(), result.stderr.strip() 
    except Exception as e: 
        return 1, "", str(e) 
    
def take_screenshot(name): 
    out = Path("out") 
    out.mkdir(exist_ok=True) 
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ") 
    path = out / f"{name}_{ts}.png" 
    img = pyautogui.screenshot() 
    img.save(path) 
    return path 

def fill_form(data, start_coords): 
    # TODO: usar coordenadas manuales para posicionar cursor 
    # Ejemplo: start_coords = (450, 320) 
    # Debes documentar resolución usada en README y aquí 
    #    take_screenshot("before") 
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

    #take_screenshot("during") 
    #time.sleep(1) 
    #take_screenshot("after") 


def main(): 
    logging.basicConfig(filename="run.log", level=logging.INFO, 
    format="%(asctime)s %(levelname)s %(message)s", encoding="utf-8") 
    logging.info("Inicio del examen") 

    print("Validando que los datos estén completos...") 
    # TODO: validar que data tenga los campos requeridos 
    data = { 
        "fecha": (datetime.now().strftime("%d/%m/%Y")), 
        "nombre": ["Ana Lucia", "Ana Laura", "Iza"], 
        "matriculas": (str(2144398+1+2)), 
        "opcion": ["Marvel"], 
        } 
    
    try:
        if not all (key in data for key in ("fecha", "nombre", "matriculas", "opcion")):
            raise KeyError
        else:
            print("Todos los campos están presentes en data.")

    except KeyError as e: 
        logging.error(f"Falta un campo en los datos: {e}") 
        exit()
    
    # TODO: permitir que el usuario defina las coordenadas manualmente 
    #Te da las coordenadas y permite que las ingreses.
    print("Mueve el cursor a la posición deseada. Para una correcta ejecución, coloque el cursor en el primer campo del formulario en 5 segundos...") 
    time.sleep(5) 
    pos = pyautogui.position() 
    print(f"Coordenadas actuales: {pos}") 
    start_coords = []  
    start_coords.append(int(input("Ingrese la coordenada X: ")))
    start_coords.append(int(input("Ingrese la coordenada Y: ")))
    start_coords = tuple(start_coords)
    print(f"Coordenadas guardadas: {start_coords}")
    #####################################################################




    code, out, err = run_powershell("Get-Date") 
    logging.info(f"PS code: {code}") 
    logging.info(f"PS output: {out}") 
    logging.info(f"PS error: {err}") 
    fill_form(data, start_coords) 
    logging.info("Fin del examen") 

if __name__ == "__main__": 
    main()