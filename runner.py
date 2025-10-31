import logging
from core import run_powershell


def main():
    logging.basicConfig(
        filename="run.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        encoding="utf-8"
    )

    logging.info("Inicio del script modularizado")

    # Comando de prueba (puedes cambiarlo por otro)
    ps_command = "Get-Date"

    code, out, err = run_powershell(ps_command)

    print("Código:", code)
    print("Salida:", out)
    print("Error:", err)

    logging.info("Fin del script")


if __name__ == "__main__":
    main()
