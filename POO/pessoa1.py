class Pessoa1:

    def __init__(self, nome, idade, comendo=False, falando=False): #construtor??
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo

    def comer(self, alimento):
        if self.comendo:
            print("ja esta comendo")
            return #se entrar no if, sai do if e nao executa o que estiver abaixo
        self.comendo = True
        print(f"{self.nome} está comendo {alimento}")

        if self.comendo:
            print("nao pode comer enquanto esta falando")

    def PararComer(self):
        if not self.comendo:
            print("nao esta comendo")
            return
        print("parou de comer")
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print("nao pode falar de boca cheia")
            return
        if self.falando:
            print("ja esta falando")
            return
        print("esta falando")
        self.falando = True

    def pararFalar(self):
        if not self.falando:
            print("nao esta falando")
            return
        print("parou de falar")
        self.falando = False
