from Persona import Persona


class Estudiante(Persona):

    def __init__(self, name, age, nota):
        super().__init__(name, age)
        self.nota = nota


p1 = Estudiante("Gabriel", 33, 9)
print(p1.age)
