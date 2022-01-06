class Pessoa:
    def __init__(self, nome, sexo, profissao, atuacao, data_nascimento, idade):
        self.nome = nome
        self.sexo = sexo
        self.profissao = profissao
        self.atuacao = atuacao
        self.data_nascimento = data_nascimento
        self.idade = idade



    def toString(self):
        return f'nome: {self.nome} sexo: {self.sexo} profissao: {self.profissao} atuacao: {self.atuacao} data nascimento: {self.data_nascimento}' \
               f'idade: {self.idade}'