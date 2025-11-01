# Tercer-Parcial de Programación para Ciberseguridad
Repositorio para los programas del 3er parcial.

## Descripción del proyecto
Este proyecto automatiza el llenado de un formulario usando Python, simulando la interacción humana con el teclado y mouse.  
Además, registra toda la ejecución en un archivo de log 🪵 y guarda capturas de pantalla 📸 antes, durante y después del proceso.

---------

## Características
*Llena automáticamente un formulario con datos predefinidos  
*Genera logs detallados con fecha y hora  
*Toma capturas de pantalla en distintas etapas (`before`, `during`, `after`)  
*Permite compilarse en un ejecutable `.exe` sin mostrar consola 

---------

## Requisitos
Asegúrate de tener **Python 3.9+** instalado y luego ejecuta:
pip install pyautogui (En la terminal de tu preferencia)

---------

## Ejecución
Paso 1: Descarga o clona los scripts parcial.py y llenar_forms.py y adjuntalos en un archivo con el nombre el que desees.
Paso 2: Abre el siguiente forms:
https://forms.office.com/pages/responsepage.aspx?id=EZDKymp73kSGHwlaLKiDt4wXC_YfIWlGrUcWrbkA4-NURjFZQjdBMkJNSlkwQkVCM0c2V0cyWTVHNSQlQCNjPTEu&classId=31f16070-5361-4de8-9624-98f60a6f24ae&assignmentId=c865c317-1511-4faa-8a46-565ecf1dd392&submissionId=9a7c0fad-1f13-0b8f-cd8d-4adb955ec7f1&route=shorturl
y manten la pagina abierta.
Paso 3: Abre la terminal y cambia de directorio al de la carpeta con los scripts guardados.
Paso 4: Entra al script 'llenar_forms.py' y modifica las coordenas iniciales, para que el cursos empiece en la primer pregunta y guarda los cambios. 
Puedes consultar tus coordenadas con el script 'coords_helper.py'
Paso 5: Deja de fondo el formulario y con la venta de la terminal por un lado (que no obstruya la primer pregunta), ejecuta el comando 'python llenar_forms.py'
Paso 6: Espera unos cuantos segundo a que se llene automaticamente.

---------

## Logs y capturas
Si no se cuenta con la carpeta 'out', el script lo detectará y lo creará, en dónde se guardaran las capturas automaticamente del antes, durante y después del llenado.
De igual forma, el archivo 'run.log' se creará al terminar el forms.

---------

## Crear un ejecutable (sin ventana)
Si deseas generar un .exe que se ejecute sin mostrar consola, usa el comando:
pyinstaller --onefile --noconsole llenar_forms.py
y se creará un archivo dist.

---------

## Consejos de Uso
🚫 No muevas el mouse ni uses el teclado mientras el script está en ejecución.
🖱️ Puedes detener el programa moviendo el mouse a la esquina superior izquierda (gracias a pyautogui.FAILSAFE = True).
🧭 Ajusta las coordenadas (360, 430) en el script según tu pantalla o aplicación objetivo.

---------

## Autores
AnaLucia-cs | Automatización del formulario con pyautogui, validación de entradas
iza-0L1N    | Incorporar las capturas de pantalla y loggings, empaquetado funcional como ejecutable, ejecución sin ventana y documentación
anaslzr     | Reconstructuración en módulos
