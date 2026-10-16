# Timer de apagado

aplicacion de escritorio simple para programar el apagado de la computadora, hecha con python y tkinter.

este timer fue hecho como proyecto para el taller de git y github.

## Que hace

- elegis cuanto tiempo falta para el apagado en horas, minutos y segundos
- muestra una cuenta regresiva en pantalla
- se puede cancelar en cualquier momento antes de que llegue a cero
- cuando llega a 00:00:00 apaga la computadora
- funciona en windows, linux y macos

## Archivos del repo

- timer_apagado.py: el codigo del programa
- README.md: este archivo
- .gitignore: lista de cosas que git ignora (build, dist, etc)

el ejecutable (.exe) no esta en el codigo del repo, se baja desde la seccion releases.

## instalacion

en windows: descarga timer_apagado.exe desde releases y abrilo. no hace falta instalar nada, ni tener python, ni el archivo .py.

si windows muestra "windows protegio su pc", hace clic en "mas informacion" y despues en "ejecutar de todas formas". pasa con los ejecutables que no estan firmados.

en linux y macos el .exe no funciona. descarga timer_apagado.py y ejecutalo con python (esta explicado abajo).

## Requisitos para correr el codigo

- python 3
- tkinter (viene con python)

en linux, si no lo tenes:

```bash
sudo apt install python3-tk
```

## como ejecutarlo

```bash
python timer_apagado.py
```

en linux o mac puede ser `python3 timer_apagado.py`.

## como se usa

1. abri la aplicacion
2. pone el tiempo en horas, minutos y segundos
3. toca iniciar y empieza la cuenta regresiva
4. si te arrepentis, toca cancelar y se frena el apagado
5. cuando llega a 00:00:00 la compu se apaga

importante: guarda tu trabajo antes de iniciar el timer. conviene probarlo primero con 1 minuto.

## notas

- en linux el apagado usa `shutdown now`, que a veces pide permisos de administrador. si no anda, se puede cambiar por `systemctl poweroff` en el codigo.
- el .py solo hace falta para correrlo en linux o macos, o para modificarlo. para usar el .exe en windows no hace falta.

## crear el ejecutable

si modificas el codigo y queres generar un .exe nuevo:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole timer_apagado.py
```

el archivo queda en la carpeta dist/.