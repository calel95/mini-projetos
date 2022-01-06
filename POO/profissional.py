from pessoa import Pessoa


class Profissional(Pessoa):


    def __init__(self, nome, atuacao, sexo):
        self.nome = nome
        self.atuacao = atuacao
        self.sexo = sexo

    def toString(self):
        return f'''MÉDICO: {self.nome}
    Sexo: {self.sexo}
    Especialidade: {self.atuacao}'''
