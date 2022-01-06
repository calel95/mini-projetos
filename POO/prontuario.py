from pessoa import Pessoa
from paciente import Paciente
from consulta import Consulta
from profissional import Profissional
from doenca import Doenca

lista_pacientes = []
lista_medicos = []
lista_consultas = []
#INSTANCIANDO A CLASSE CONSULTA

'''
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

quando cria um paciente, ele fica salvo na lista de pacientes, mesmo excluindo uma consulta, assim como médico também,
como se fosse um banco de dados. Se for excluir um médico ou paciente do banco de dados, precisa excluir a consulta do paciente também.
A lista_consultas é uma lista que armazena outras listas, que são as consultas de cada paciente.
Podemos atribuir uma doença no paciente.

'''
# def removeConsulta(nome, lista):
#     for i in lista:
#         if nome in x:
#             print(x)
#                 pos3 = i.index(x)
#
#                 print(pos3)



#função pra remover uma consulta
def remove(nome, l):
    for i in l:
        for x in i:
            if nome in x:
                print("Consulta abaixo excluída!")
                print(i)
                return l.remove(i)

    print(l)

def excluir(nome, lista):
    for i in lista:
        if nome in i:
            print("Excluído!")
            posicao = lista.index(i)

            print(posicao)
            return lista.pop(posicao)



def listagem(lista):
    for i in lista:
        print(i)

def adiciona(nome, variavel, sexo):
    if '/' in variavel:
        print("Paciente adicionado!")
        addPaciente = Paciente(nome, variavel, sexo)
        lista_pacientes.append(addPaciente.toString())
        print(f"Nome: {addPaciente.nome}")
        return addPaciente.toString()

    else:
        print("Profissional adicionado!")
        addMedico = Profissional(nome, variavel, sexo)
        lista_medicos.append(addMedico.toString())
        print(f"Nome: {addMedico.nome}")
        return addMedico.toString()

op = 100
while op != 0:

    print("MENU")
    print('''1 - add paciente\n2 - add medico\n3 - atribuir doenca\n4 - criar consulta\n5 - listar consultas\n6 - remover consulta
    \n7 - listar pacientes\n8 - lista medicos\n9 - remover paciente\n10 - remover medico''')
    op = int(input())

#ADICIONA PACIENTE
    if op == 1:
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento: ")
        sexo = input("Sexo: ")

        adiciona(nome,data_nascimento, sexo)
#ADICIONA MEDICO
    if op == 2:
        nome = input("Nome: ")
        especialidade = input("Especialidade: ")
        sexo = input("Sexo: ")

        adiciona(nome, especialidade, sexo)

#ADICIONA DOENCA NO PACIENTE
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
#ADICIONA CONSULTA
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
                adiciona_consulta = [addConsulta.toString()]
                lista_consultas.append(adiciona_consulta)
                print(addConsulta.toString())

        #print(lista_consultas)
        #print(addConsulta)
        # print(str(addConsulta))
        # print (repr(addConsulta))
#LISTA CONSULTAS
    if op == 5:
        listagem(lista_consultas)
#REMOVE CONSULTA
    if op == 6:
        nome_paciente = input('')
        for i in lista_consultas:
            for x in i:
                if nome_paciente in x:
                    print("achou")
                    print(i)
                    lista_consultas.remove(i)
                else:
                    print("nao tem")
        print(lista_consultas)


#LISTA PACIENTES
    if op == 7:
        listagem(lista_pacientes)

#LISTA MEDICOS
    if op == 8:
        listagem(lista_medicos)

#EXCLUI UM PACIENTE
    if op == 9:
        name = input("nome paciente:")
        excluir(name, lista_pacientes)
        print("paciente excluido!")

#EXCLUIR UM MEDICO
    if op == 10:
        name = input("nome medico:")
        excluir(name, lista_medicos)
        print("medico excluido")

    if op == 11:
        name = 'calel'
        remove(name, lista_consultas)


                #addConsulta.consultas.remove(i)

                #addConsulta.consultas.pop(x)



                # print("Achou")
                # print(i)
                    # print(Consulta)
                    # print(lista_consultas.index(i))
                    # poss = lista_consultas.index(i)
                    #
                    # print(poss)
                    # lista_consultas.pop(poss)

print("PACIENTES",lista_pacientes)
print("MEDICOS", lista_medicos)
print("CONSULTAS", lista_consultas)


