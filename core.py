import subprocess
import logging


def run_powershell(cmd):
    """
    Ejecuta un comando de PowerShell con manejo de errores.
    Devuelve (codigo, salida, error)
    """
    try:
        result = subprocess.run(
            ["powershell", "-Command", cmd],
            capture_output=True,
            text=True,
            timeout=10
        )
        code = result.returncode
        out = result.stdout.strip()
        err = result.stderr.strip()

        if code != 0:
            logging.error(f"Error en PowerShell (código {code}): {err}")
        else:
            logging.info(f"PowerShell ejecutado correctamente: {out}")

        return code, out, err

    except subprocess.TimeoutExpired:
        logging.error("El comando de PowerShell excedió el tiempo límite.")
        return 1, "", "TimeoutExpired"

    except Exception as e:
        logging.exception("Error inesperado al ejecutar PowerShell.")
        return 1, "", str(e)
