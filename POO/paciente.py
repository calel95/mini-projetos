
from pessoa import Pessoa


class Paciente(Pessoa):


    # def __init__(self, lista[]):
    #     self.nome = nome
    #     self.data_nascimento = data_nascimento
    #     self.sexo = sexo
    #     self.data_cadastro = date.today()

    def __init__(self, nome, data_nascimento, sexo):
        self.nome = nome
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.pacientes = []

    def toString(self):
        return f'''PACIENTE: {self.nome} 
    Data de nascimento: {self.data_nascimento}
    Sexo: {self.sexo}'''


