class Empresa():

    def definiEmpresa(self, nomeEmpresa, problemaEmpresa):
        self.nomeEmpresa = nomeEmpresa
        self.problemaEmpresa = problemaEmpresa

    def infoEmpresa(self):
        print(f"Empresa: {self.nomeEmpresa}")
        print(f"Problema da empresa: {self.problemaEmpresa}")


class Pessoa():
    def __init__(self, nome, curso, disciplina):
        self.nome = nome
        self.curso = curso
        self.disciplina = disciplina

    def toString(self):
        return f"nome {self.nome} curso {self.curso} disciplina: {self.disciplina}"


class Aluno(Pessoa):
    def __init__(self, nomeAluno, curso):
        self.nomeAluno = nomeAluno
        self.disciplina = curso

    def infoAluno(self):
        print(f"Aluno: {self.nomeAluno}")
        print(f"Curso: {self.disciplina}")

    def toString(self):
        return f"Aluno: {self.nomeAluno} curso: {self.curso}"


class Professor(Pessoa):
    def __init__(self, nomeProfessor, disciplina):
        self.nomeProfessor = nomeProfessor
        self.disciplina = disciplina

    def infoProfessor(self):
        print(f"Professor: {self.nomeProfessor}")
        print(f"Disciplina: {self.disciplina}")

    def toString(self):
        return f"Aluno: {self.nomeProfessor} curso: {self.disciplina}"


class Grupo():
    listagrupos = []

    def __init__(self, aluno, professor):
        self.aluno = aluno
        self.professor = professor
        addgrupo = [aluno, professor]
        self.listagrupos.append(addgrupo)
        print("grupo criado")

    def infoGrupos(self):
        return f"aluno {self.aluno} {self.grupos}"

    def listagem(self):
        for i in self.listagrupos:
            print(self.listagrupos)
            print(i)

    def __repr__(self):
        return f"{self.aluno} {self.professor}"

    def toString(self):
        return f"{self.aluno} {self.professor}"


class Projeto():
    def __init__(self, Grupo, Empresa):
        self.Grupo = Grupo
        self.Empresa = Empresa

    def listaProjetos(self):
        print("Grupo {self.Grupo}")
        print(f"Empresa: {self.Empresa}")


emp1 = Empresa()
emp2 = Empresa()

emp1.definiEmpresa("GM", "Cadastro de clientes")
emp2.definiEmpresa("ITAU", "CRM")

emp2.infoEmpresa()

a1 = Aluno('Pedrinho', 'POO')
a2 = Aluno("Ana", "Data Science")
a1.infoAluno()

p1 = Professor('Antônio', 'POO')
p2 = Professor('Maria', 'Data Science')

p2.infoProfessor()

grupo = Grupo(a1, p2)
print(grupo.toString())
grupo.listagem()
