import tkinter as tk
import os
import platform


class TimerApagado:
    def __init__(self, root):
        self.root = root
        root.title("Timer de apagado")
        root.geometry("320x240")
        root.resizable(False, False)

        self.segundos = 0
        self.corriendo = False

        marco_entrada = tk.Frame(root)
        marco_entrada.pack(pady=(20, 5))

        self.horas = tk.Spinbox(marco_entrada, from_=0, to=23, width=3,
                                font=("Arial", 16), justify="center")
        self.minutos = tk.Spinbox(marco_entrada, from_=0, to=59, width=3,
                                  font=("Arial", 16), justify="center")
        self.segs = tk.Spinbox(marco_entrada, from_=0, to=59, width=3,
                               font=("Arial", 16), justify="center")

        self.horas.grid(row=1, column=0, padx=5)
        self.minutos.grid(row=1, column=1, padx=5)
        self.segs.grid(row=1, column=2, padx=5)

        tk.Label(marco_entrada, text="Horas").grid(row=0, column=0)
        tk.Label(marco_entrada, text="Minutos").grid(row=0, column=1)
        tk.Label(marco_entrada, text="Segundos").grid(row=0, column=2)

        # Cuenta regresiva
        self.label_tiempo = tk.Label(root, text="00:00:00", font=("Arial", 28))
        self.label_tiempo.pack(pady=15)

        # Botones
        marco_botones = tk.Frame(root)
        marco_botones.pack()
        self.btn_iniciar = tk.Button(marco_botones, text="Iniciar", width=10,
                                     command=self.iniciar)
        self.btn_iniciar.grid(row=0, column=0, padx=5)
        self.btn_cancelar = tk.Button(marco_botones, text="Cancelar", width=10,
                                      command=self.cancelar, state="disabled")
        self.btn_cancelar.grid(row=0, column=1, padx=5)

    def iniciar(self):
        try:
            h = int(self.horas.get())
            m = int(self.minutos.get())
            s = int(self.segs.get())
        except ValueError:
            self.label_tiempo.config(text="Valor inválido")
            return

        total = h * 3600 + m * 60 + s
        if total <= 0:
            self.label_tiempo.config(text="Poné un tiempo")
            return

        self.segundos = total
        self.corriendo = True
        self.btn_iniciar.config(state="disabled")
        self.btn_cancelar.config(state="normal")
        self.actualizar()

    def actualizar(self):
        if not self.corriendo:
            return

        h = self.segundos // 3600
        m = (self.segundos % 3600) // 60
        s = self.segundos % 60
        self.label_tiempo.config(text=f"{h:02d}:{m:02d}:{s:02d}")

        if self.segundos == 0:
            self.apagar()
        else:
            self.segundos -= 1
            self.root.after(1000, self.actualizar)

    def cancelar(self):
        self.corriendo = False
        self.label_tiempo.config(text="00:00:00")
        self.btn_iniciar.config(state="normal")
        self.btn_cancelar.config(state="disabled")

    def apagar(self):
        sistema = platform.system()
        if sistema == "Windows":
            os.system("shutdown /s /t 1")
        elif sistema == "Darwin":
            os.system("osascript -e 'tell app \"System Events\" to shut down'")
        else:
            os.system("shutdown now")



root = tk.Tk()
app = TimerApagado(root)
root.mainloop()