from pessoa import Pessoa
from paciente import Paciente
from consulta import Consulta
from profissional import Profissional
from doenca import Doenca
from prontuario import Prontuario

lista_pacientes = []
lista_medicos = []
lista_consultas = []
#INSTANCIANDO A CLASSE CONSULTA


#INSTANCIANDO A CLASSE PACIENTE
c1 = Paciente('calel', '19/01/1995', 'M')
c2 = Paciente('veronica', '19/01/1996', 'F')
c3 = Paciente('Fernando', '27/09/2015', 'F')

#CADASTRANDO OS MÉDICOS
p1 = Profissional('Dr Estranho','Dermato','M')
p2 = Profissional('Dr ET','otorrino','M')

#ABRINDO CONSULTAS ADICIONANDO PACIENTE, MEDICO E A DATA DA CONSULTA
# consulta.abrirConsulta(c1.toString(),p1.toString(), 'data consulta: 14/11/2021')
# consulta.abrirConsulta(c2.toString(),p1.toString(), '22/11/2021')

#LISTA AS CONSULTAS CADASTRADAS
# consulta.listarConsultas()
#consulta.buscarConsulta('veronica')

#DELETANDO UMA CONSULTA, A BUSCA FEITA PELO NOME DO PACIENTE
# consulta.deletarConsulta('veronica')
#
# consulta.listarConsultas()

#INSTANCIANDO A CLASSE DOENCA
'''
doenca = Doenca('olho vermelho', c1.toString())
doenca2 = Doenca('olho verde', c2.toString())
doenca3 = Doenca('olho azul', c3.toString())

#ATRIBUI DOENÇA NO PACIENTE
#doenca.atribuirDoenca('olho vermelho', c1.toString(), p1.toString())
#doenca.atribuirDoenca('olho verde', c2.toString(), p2.toString())
#a = doenca.atribuirDoenca('olho azul', c3.toString(), p1.toString())



prontuario = Prontuario()

prontuario.addNovo(c1.toString(), doenca.toString())
prontuario.addNovo(c3.toString(), doenca2.toString())

prontuario.listarProntuario()
'''

def math(nome, lista):
    for i in lista:
        if nome in i:
            print("achou")

def listagem(lista):
    for i in lista:
        print(i)

def adiciona(nome, variavel, sexo):
    if '/' in variavel:
        print("paciente")
    else:
        print("medico")

op = 100
while op != 0:

    print("MENU")
    print('''1 - add paciente\n2 - add medico\n3 - atribuir doenca\n4 - criar consulta\n5 - listar consultas\n6 - remover consulta
    \n7 - listar pacientes\n8 - lista medicos\n9 - remover paciente\n10 - remover medico''')
    op = int(input())

    if op == 1:
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento: ")
        sexo = input("Sexo: ")

        c10 = Paciente(nome,data_nascimento,sexo)
        lista_pacientes.append(c10.toString())

        print(c10.toString())

    if op == 2:
        nome = input("Nome: ")
        especialidade = input("Especialidade: ")
        sexo = input("Sexo: ")

        p10 = Profissional(nome,especialidade, sexo)
        lista_medicos.append(p10.toString())
        print(p10.toString())

    if op == 3:
        doenca = input("Doença: ")
        pacient = input("Paciente: ")
        for i in lista_pacientes:
            if pacient in i:
                print("achou!")
                rd = Doenca(doenca, i)
                t = lista_pacientes.index(i) #indice
                print(t)
                print(rd.toString())
                #lista_pacientes.insert(t,rd.toString())
                lista_pacientes.append(rd.toString())
                lista_pacientes.pop(t)
                break
            else:
                print("paciente nao existe")

    if op == 4:
        nome4 = input("nome paciente consulta: ")
        medico = input("nome medico consulta: ")
        data = input("Data da consulta:")
        for i in lista_pacientes:
            if nome4 in i:
                pos = lista_pacientes.index(i)  # indice
                print(pos)
        for i in lista_medicos:
            if medico in i:
                pos2 = lista_medicos.index(i)
                print(pos2)
                addConsulta = Consulta(lista_pacientes[pos], lista_medicos[pos2], data)
                lista_consultas.append(addConsulta)
        #print(lista_consultas)
        #print(addConsulta)
        # print(str(addConsulta))
        # print (repr(addConsulta))

    if op == 5:
        listagem(lista_consultas)

    if op == 6:
        nome_paciente = input("nome paciente:")
# comando novo, atraves da variavel nome_paciente, ele percorre o objeto consulta no atributo paciente do objeto consulta
# e depois faz um for(busca) na lista_consultas, forma de resumir a busca usando um for i in x e depois um if variavel in i, muito usado aqui
        if any(nome_paciente in Consulta.paciente for Consulta in lista_consultas):
            print("Achou")
            print(Consulta)
            poss = lista_consultas.index(i-1)

            print(poss)
            lista_consultas.pop(poss)
        else:
            print("nao achou")


    if op == 7:
        listagem(lista_pacientes)
    if op == 8:
        listagem(lista_medicos)
    if op == 9:
        name = input("nome paciente:")
        math(name, lista_pacientes)

print("PACIENTES",lista_pacientes)
print("MEDICOS", lista_medicos)
print("CONSULTAS", lista_consultas)

