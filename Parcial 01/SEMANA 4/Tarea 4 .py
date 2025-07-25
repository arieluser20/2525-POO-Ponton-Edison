# sistema_reservas.py

class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}"


class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo  # simple, doble, suite
        self.precio = precio
        self.disponible = True

    def reservar(self):
        self.disponible = False

    def liberar(self):
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        return f"Habitación {self.numero} - {self.tipo} - ${self.precio} - {estado}"


class Reserva:
    def __init__(self, cliente, habitacion):
        self.cliente = cliente
        self.habitacion = habitacion

    def confirmar_reserva(self):
        if self.habitacion.disponible:
            self.habitacion.reservar()
            print(f"Reserva confirmada para {self.cliente.nombre} en la habitación {self.habitacion.numero}")
        else:
            print("Lo sentimos, la habitación no está disponible.")

# --- Código de prueba ---

cliente1 = Cliente("Juan Pérez", "juanperez@example.com")
habitacion1 = Habitacion(101, "doble", 75.00)

print(habitacion1)
reserva1 = Reserva(cliente1, habitacion1)
reserva1.confirmar_reserva()
print(habitacion1)
