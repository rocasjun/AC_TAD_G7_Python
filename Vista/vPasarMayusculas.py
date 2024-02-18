from tkinter import *

class VPasarMayusculas(Tk):
    def __init__(self):
        super().__init__()

        self.title("Convertir Texto a Mayúsculas")
        self.geometry("300x200")

        self.lbl_titulo = Label(self, text="Convertir el texto a mayúsculas", font=("Arial", 12))
        self.lbl_titulo.pack(pady=10)

        self.txtfa_textarea = Text(self, height=5, width=30, font=("Arial", 10))
        self.txtfa_textarea.pack(padx=10, pady=5)

        self.btn_convertir = Button(self, text="Convertir", command=self.convertir_a_mayusculas)
        self.btn_convertir.pack(pady=5)

    def convertir_a_mayusculas(self):
        texto = self.txtfa_textarea.get("1.0", "end-1c")  # Obtenemos el texto del área de texto
        texto_mayusculas = texto.upper()  # Convertimos a mayúsculas
        self.txtfa_textarea.delete("1.0", END)  # Borramos el texto actual
        self.txtfa_textarea.insert("1.0", texto_mayusculas)  # Insertamos el texto en mayúsculas

if __name__ == "__main__":
    vista = VPasarMayusculas()
    vista.mainloop()
