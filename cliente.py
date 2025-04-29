class Cliente: # Se crea la clase Cliente para representar a los clientes de la veterinaria
    def __init__(self, nombre, telefono): # En esta linea definimos el metodo constructor de la clase Cliente que recibe como argumentos el nombre y el telefono del cliente
        self.nombre = nombre
        self.telefono = telefono
        self.mascotas = []

    def agregar_mascota(self, mascota): # Lo que hacemos es definir un metodo para agregar una mascota al cliente
        self.mascotas.append(mascota)

    def __str__(self): # Aqui definimos el metodo str para representar al cliente como una cadena de texto
        return f"Cliente: {self.nombre}, Teléfono: {self.telefono}"