from Modelo.Mensaje import Mensaje
from Vista.vPasarMayusculas import VPasarMayusculas
from tkinter import *

class CPasarMayusculas:
    def __init__(self):
        self.vista = VPasarMayusculas()

        self.vista.btn_convertir.config(command=self.pasar_mayusculas)

    def mostrar_vista(self):
        self.vista.mainloop()

    def pasar_mayusculas(self):
        texto = self.vista.txtfa_textarea.get(1.0, END)
        mensaje = Mensaje(texto)
        mensaje.convertir_mayusculas()
        self.vista.txtfa_textarea.delete(1.0, END)
        self.vista.txtfa_textarea.insert(END, mensaje.texto)

if __name__ == "__main__":
    controlador = CPasarMayusculas()
    controlador.mostrar_vista()