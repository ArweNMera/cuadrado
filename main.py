class DibujadorCuadrado:
    def __init__(self, tamano):
        self.tamano = tamano

    def dibujar_cuadrado(self):
        """Dibuja un cuadrado de tamaño `tamano` utilizando asteriscos."""
        for i in range(self.tamano):
            for j in range(self.tamano):
                print('*', end=' ')
            print()  # Imprime una nueva línea después de cada fila

if __name__ == "__main__":
    try:
        tamano = int(input("Ingrese el tamaño del cuadrado: "))
        if tamano <= 0:
            raise ValueError("El tamaño debe ser un número entero positivo.")
        dibujador = DibujadorCuadrado(tamano)
        dibujador.dibujar_cuadrado()
    except ValueError as e:
        print(f"Error: {e}")
