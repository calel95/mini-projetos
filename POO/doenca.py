from paciente import Paciente
from consulta import Consulta
class Doenca:
    def __init__(self, doenca, paciente):
        self.doenca = doenca
        self.paciente = paciente
        print("Doenca atribuida!")
        #print(f'''\n{self.paciente}\n\033[31mDOENÇA:\033[0;0m{self.doenca}
#''')
    def addDoenca(self, d,p):
        self.doenca = d
        self.paciente = p

    def toString(self):
        return f'''\n{self.paciente}\nDOENÇA: {self.doenca}
'''