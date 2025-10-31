import logging
from core import run_powershell, fill_form

def main():
    logging.basicConfig(
        filename="run.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        encoding="utf-8"
    )

    logging.info("Inicio del examen")

    data = {
        "nombre": "Alumno Ejemplo",
        "correo": "ejemplo@correo.com",
        "equipo": "Equipo 3"
    }

    # Coordenadas obtenidas con coords_helper.py
    start_coords = (450, 320)

    logging.info("Ejecutando comando PowerShell...")
    code, out, err = run_powershell("Get-Date")

    if code == 0:
        logging.info(f"PowerShell OK: {out}")
    else:
        logging.warning(f"PowerShell error: {err}")

    logging.info("Llenando formulario...")
    fill_form(data, start_coords)

    logging.info("Fin del examen")

if __name__ == "__main__":
    main()
