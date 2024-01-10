class Cliente:
    def __init__(self, nombre, correo,  ubicacion, telefono):
        self.nombre = nombre
        self.correo = correo
        self.ubicacion = ubicacion
        self.telefono = telefono

    def __str__(self):
        return f"El cliente {self.nombre} ha sido registrado correctamente"

    def cambiar(self):
        self.ubicacion = input("Indique su nueva ubicacion: ")
        return f"La ubicacion fue cambiada correctamente"