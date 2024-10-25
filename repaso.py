class Auto:
    def __init__(self):
        self.color = "negro"
        self.velocidad = 0
        self.marca = "Fiat"
        self.modelo = "Cronos 1.3"

mi_auto = Auto()

print(mi_auto.marca)
print(mi_auto.modelo)
print(mi_auto.color)


# version con los valores inicializados en cero

class Auto:
    def __init__(self, color, velocidad, marca, modelo):
        self.color = color
        self.velocidad = velocidad
        self.marca = marca
        self.modelo = modelo
# creando un función que sea acelerando
    def acelerar(self):       #agregar self siempre para acceder a las propiedades de la clase
        self.velocidad += 10
        print(f"Aumentando la velocidad, el auto va ahora a {self.velocidad} km/h")

mi_auto = Auto("negro", 10, "Fiat", "Cronos 1.3")

mi_auto.acelerar()
mi_auto.acelerar()

print(mi_auto.velocidad)
