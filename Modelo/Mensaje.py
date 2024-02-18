class Mensaje:
    def __init__(self, texto):
        self.texto = texto

    def convertir_mayusculas(self):
        self.texto = self.texto.upper()