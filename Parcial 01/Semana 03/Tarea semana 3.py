# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese las temperaturas de la semana (7 días):")
    for i in range(7):
        temp = float(input(f"Día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

# Función principal
def main():
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

# Ejecutar el programa
if __name__ == "__main__":
    main()


# Clase que representa la información del clima diario
class ClimaSemanal:
    def __init__(self):
        # Atributo encapsulado para almacenar las temperaturas
        self.__temperaturas = []

    # Método para ingresar las temperaturas
    def ingresar_datos(self):
        print("Ingrese las temperaturas de la semana (7 días):")
        for i in range(7):
            temp = float(input(f"Día {i + 1}: "))
            self.__temperaturas.append(temp)

    # Método para calcular el promedio
    def calcular_promedio(self):
        if not self.__temperaturas:
            return 0
        return sum(self.__temperaturas) / len(self.__temperaturas)

    # Método para mostrar resultados
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

# Clase heredada para posibles extensiones futuras
class ClimaExtendido(ClimaSemanal):
    # Polimorfismo: sobrescribimos el método para mostrar más datos (ejemplo básico)
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"[Clima Extendido] Promedio semanal: {promedio:.2f}°C")

# Función principal
def main():
    clima = ClimaExtendido()  # Se puede cambiar a ClimaSemanal() si no se quiere herencia
    clima.ingresar_datos()
    clima.mostrar_promedio()

# Ejecutar el programa
if __name__ == "__main__":
    main()
